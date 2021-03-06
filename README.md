FzDAQ
=====

- Table of contents
  * [Introduction](#introduction)
  * [Deployment](#deployment)
  * [Build](#build)
  * [Installation](#installation)
  * [Command line arguments](#command-line-arguments)
  * [Configuration](#configuration)
  * [EPICS plugin](#epics-plugin)
  * [Implementation details](#implementation-details)
    * [ZeroMQ sockets](#zeromq-sockets)
    
Introduction
------------

FzDAQ is an acquisition software for FAZIA experiment. FAZIA stands for the Four Pi A and Z Identification Array. This is a project which aims at building a new 4pi particle detector for charged particles. It operates in the domain of heavy-ion induced reactions around the Fermi energy and it groups together more than 10 institutions worldwide in Nuclear Physics. A large effort on research and development is currently made, especially on digital electronics and pulse shape analysis, in order to improve the detection capabilities of such particle detectors in different domains, such as charge and mass identification, lower energy thresholds, as well as improved energetic and angular resolutions.

FzDAQ is composed by different modules that exchange messages and events through [ZeroMQ sockets](http://zeromq.org):

- **FzReader**: it acquires by UDP socket FAZIA raw data from Regional Board that aggregates multiple detector blocks. It forwards data to FzParser thread pool.

- **FzParser**: each FzParser includes a FzFSM (Finite State Machine) able to analyze and validate each acquired event. Multiple FzParser threads can be running on multi-core machine in order to benefit from tasks parallel execution. They forward data to FzWriter module.

- **FzWriter**: this module store data in files and directories with [Google Protobuf](https://developers.google.com/protocol-buffers/) data format. It also runs a data spy in order to allow online data processing and analysis from external data visualization tools. 

- **FzNodeManager**: _local_ supervisor for FzReader/FzParser or FzWriter that run on each FzDAQ deployed machine. It sends a report on modules status to FzController and it receives run control and setup commands for modules management.

- **FzController**: _global_ supervisor for all FzNodeManager modules. It offers a global view on whole FzDAQ cluster status and accept commands for FzDAQ setup and run control.

Deployment
----------

A single FzDAQ node (=server) can run one of these combination of modules (profile):

- profile **compute** 
  - 1 FzReader thread
  - _n_ FzParser threads
  - 1 FzNodeManager thread

- profile **storage** 
  - 1 FzWriter thread
  - 1 FzNodeManager thread
  
- profile **all** 
  - 1 FzReader thread
  - _n_ FzParser threads
  - 1 FzWriter thread
  - 1 FzNodeManager thread

- FzDAQ controller
  - 1 FzController thread

Build
-----

- distribution: Debian 8.x

- install base dependencies

  ```apt-get update```
  
  ```apt-get install git screen g++ autoconf automake libprotobuf9 libprotobuf-dev protobuf-compiler libboost-thread1.55.0 libboost-thread1.55-dev liblog4cpp5 liblog4cpp5-dev libboost-system1.55.0 libboost-system1.55-dev libboost-program-options1.55.0 libboost-program-options1.55-dev libzmq3 libzmq3-dev libconfig++9 libconfig++-dev libudev1 libudev-dev```
  
- Weblog message interface dependencies

  ```apt-get install libcurl3 libcurl4-openssl-dev```

- ActiveMQ log service dependencies and build

  ```apt-get install libapr1 libapr1-dev libssl-dev```

  download ActiveMQ CPP library from http://activemq.apache.org

    ```wget http://it.apache.contactlab.it/activemq/activemq-cpp/3.9.3/activemq-cpp-library-3.9.3-src.tar.gz```
  
  compile and install ActiveMQ CPP library in /usr/local/lib

    ```tar xzf activemq-cpp-library-3.9.3-src.tar.gz ; cd activemq-cpp-library-3.9.3```
  
    ```./configure ; make ; make install ; ldconfig```
  
- clone FzDAQ GIT master branch

  ```git clone https://github.com/gtortone/FzDAQ.git```
  
- generate configure script

  ```autoreconf -ivf```

- configure parameters

  ```
  --with-boost-libdir	  directory for Boost libraries
  --enable-weblog         enable WebLog message interface
  --enable-amqlog         enable ActiveMQ log message interface
  ```

- run configure
  
  ```./configure --prefix=/opt/FzDAQ --with-boost-libdir=/usr/lib/x86_64-linux-gnu --enable-weblog --enable-amqlog```
  
- start build

  ``` make ```
  
Installation 
------------

- To install FzDAQ binaries in default directory (/opt/FzDAQ/bin) run:

  ``` make install ```
  
Command line arguments
----------------------

The main executables of FzDAQ are 'FzDAQ-mt' and 'FzController'.

FzDAQ-mt command line options:

|option|mandatory|value|default|description|
|---|---|---|---|---|
|--help|no|-|-|produce help message|
|--cfg|yes|config_file|-|configuration file|
|--profile|no|{compute, storage, all}|all|profile to start|

FzController command line options:

|option|mandatory|value|default|description|
|---|---|---|---|---|
|--help|no|-|-|produce help message|
|--cfg|yes|config_file|-|configuration file|

Configuration
-------------

FzDAQ configuration file format is based on [libconfig](http://www.hyperrealm.com/libconfig) and each module properties are defined in a separate config section. This is a sample of config section:

```
fzreader: {
      consumer: {
         url = "udp://eth0:50000";
      }; 
      producer: {
         url = "inproc://fzreader";     # push - bind
      };
 };
 ```
 
Some config file examples are available in GIT repository [config directory](config/). To explain various configuration attributes we will use the following convention: the attribute 'url' in the sample section above will be defined as

```fzreader.consumer.url```

Configuration options will be listed in related module table.

A ZeroMQ endpoint is a string composed by:

	```<transport>://<address>[:port]```

The transport specifies the underlying protocol to use. The address specifies the transport-specific address to connect to.
Address can be replaced by network interface name (e.g. eth0) when an endpoint is related to a ZeroMQ server (= receive ZeroMQ messages)

In the table below if a config attribute has a value in "linked to" field it means that it must contains the same value
of linked attribute. Each field provides a default value and, in principle, there is no need to specify these attributes.
 
### Global configuration attributes
 
### FzReader configuration attributes

|cfgfile attribute|0MQ endpoint|linked to|default|description|
|---|---|---|---|---|
|fzreader.consumer.url|udp://`<netif>`:`<port>`|-|udp://eth0:5000|UDP socket to bind for event acquisition|
|fzreader.producer.url|inproc://`<label>`|fzparser.consumer.url|inproc://fzreader|0MQ channel between FzReader and FzParser|

### FzParser configuration attributes

|cfgfile attribute|0MQ endpoint|linked to|default|description|
|---|---|---|---|---|
|fzparser.consumer.url|inproc://`<label>`|fzreader.producer.url|inproc://fzreader|0MQ channel between FzReader and FzParser|
|fzparser.producer.url|inproc://`<label>`|fzwriter.consumer.url|inproc://fzwriter|0MQ channel between FzParser and FzWriter|

|cfgfile attribute|mandatory|default|description|
|---|---|---|---|
|fzparser.nthreads|no|1|number of FzParser threads to allocate|

### FzWriter configuration attributes

|cfgfile attribute|0MQ endpoint|linked to|default|description|
|---|---|---|---|---|
|fzwriter.consumer.url|inproc://`<label>`|fzparser.producer.url|inproc://fzwriter|0MQ channel between FzParser and FzWriter|

|cfgfile attribute|mandatory|default|description|
|---|---|---|---|
|fzwriter.subdir|yes|-|base output directory|
|fzwriter.runtag|no|run|label for run directory identification (e.g. LNS, GANIL)|
|fzwriter.runid|yes|-|id for run identification (e.g. 100, 205)|
|fzwriter.esize|no|10|max size of event file in Mbytes|
|fzwriter.dsize|no|100|max size of event directory in Mbytes|
|fzwriter.spy.interface|no|*|network interface to bind for events spy|

### FzNodeManager configuration attributes

|cfgfile attribute|mandatory|default|description|
|---|---|---|---|
|fznodemanager.runcontrol_mode|yes|-|local or remote run control mode|
|fznodemanager.interface|no|eth0|network interface for run control|
|fznodemanager.stats.ip|yes|no|IP address of FzController|

### FzController configuration attributes

|cfgfile attribute|mandatory|default|description|
|---|---|---|---|
|fzcontroller.interface|no|eth0|report collector network interface|
|fzcontroller.weblog.url|no|-|Weblog url|
|fzcontroller.weblog.username|no|-|Weblog username|
|fzcontroller.weblog.interval|no|-|Weblog time interval report in seconds|

EPICS plugin
------------

Implementation details
----------------------

This section provides information about FzDAQ internal implementations.

ZeroMQ sockets
--------------

|module|type|port|description|destination|
|---|---|---|---|---|
|FzReader|ZMQ_PUSH|(cfgfile)|producer|to FzParser|
||||||
|FzParser|ZMQ_PULL|(cfgfile)|consumer|from FzReader|
|FzParser|ZMQ_PUSH|(cfgfile)|producer|to FzWriter|
||||||
|FzWriter|ZMQ_PULL|(cfgfile)|consumer|from FzParser|
|FzWriter|ZMQ_PUB|:5563|publisher|spy|
||||||
|FzNodeManager|ZMQ_PUSH|-|producer|to FzController - node report|
|FzNodeManager|ZMQ_REP|:5550|reply|from FzController - run control & setup commands - with reply|
|FzNodeManager|ZMQ_PULL|:6660|consumer|from FzController - run control & setup commands - without reply|
||||||
|FzController|ZMQ_PULL|:7000|consumer|from FzNodeManager - collector report|
|FzController|ZMQ_REP|:5555|reply|from outside - run control & setup commands|


