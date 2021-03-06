#ifndef FZREADER_H_
#define FZREADER_H_

#include "boost/thread.hpp"

#include "main/FzConfig.h"
#include "utils/FzTypedef.h"
#include "parser/FzParser.h"
#include "proto/FzNodeReport.pb.h"
#include "utils/zmq.hpp"
#include "utils/fossa.h"
#include "logger/FzJMS.h"
#include "logger/FzLogger.h"
#include "utils/FzTypedef.h"

#include <vector>

struct _cb_data {

   FzLogger *log_ptr;
   zmq::socket_t *reader_ptr;
   Report::FzReader *report_ptr;
   bool rec;
};

class FzReader {

private:

   std::string neturl;
   libconfig::Config cfg;

   boost::thread *thr;
   bool thread_init;
   zmq::context_t &context;
   zmq::socket_t *reader;

   RCstate rcstate;

   struct _cb_data cb_data;

   FzLogger log;
#ifdef AMQLOG_ENABLED
   std::unique_ptr<cms::Connection> AMQconn;
#endif

   struct ns_mgr udpserver;

   Report::FzReader report;

   int setupNet(void);

   int initNet(void);

   static void udp_handler(struct ns_connection *nc, int ev, void *ev_data);

   void process(void);

public:

#ifdef AMQLOG_ENABLED
   FzReader(std::string nurl, std::string cfgfile, zmq::context_t &ctx, cms::Connection *JMSconn);
#else
   FzReader(std::string nurl, std::string cfgfile, zmq::context_t &ctx);
#endif

   int setup(void);
   int init(void);
   void close(void);
   void record(bool val);

   void set_rcstate(RCstate s);

   Report::FzReader get_report(void); 
};

#endif
