C++ = g++

CFLAGS = -O3 -std=c++11

SERIALLIBS = -lpthread -lprotobuf 

INCDIR = -I.. -I../src/proto -I../src/utils -I/space/eindra/software/install/protobuf-3/include -I/space/eindra/software/install/zmq4.2.1/include  -L/space/eindra/software/install/protobuf-3/lib -L/space/eindra/software/install/zmq4.2.1/lib

all: read-fazia-pb publish-fazia-pb

read-fazia-pb: read-fazia-pb.cpp
	$(C++) $(CFLAGS) $(INCDIR) ../src/proto/FzEventSet.pb.cpp read-fazia-pb.cpp $(SERIALLIBS) -o $@

publish-fazia-pb: publish-fazia-pb.cpp
	$(C++) $(CFLAGS) $(INCDIR) ../src/proto/FzEventSet.pb.cpp publish-fazia-pb.cpp $(SERIALLIBS) -lzmq -o $@

clean:
	rm -f *.o read-fazia-pb publish-fazia-pb
