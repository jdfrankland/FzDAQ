#ifndef FSM_H_
#define FSM_H_

#include <stdint.h>
#include "FzEventSet.pb.h"
#include "FzNodeReport.pb.h"
#include "FzLogger.h"

#define WORDTYPE_NUM	18
#define TRANSITION_NUM	19
#define STATES_NUM	11

#define REGID_MASK	0x07FF
#define BLKID_MASK      0x07FF
#define EC_MASK         0x0FFF
#define TELID_MASK      0x0001
#define FEEID_MASK      0x000E
#define ADC_MASK        0x001F
#define DTYPE_MASK      0x0700  
#define DETID_MASK      0x00E0  
#define LENGTH_MASK     0x0FFF
#define CRCFE_MASK      0x0FF0
#define CRCBL_MASK      0x0FF0

#define nibble(n,word)	((word >> (n*4)) & 0x000F)
#define bit(n,word)	((word >> n) & 0x0001)

#define PARSE_OK 	1
#define PARSE_FAIL	0

// word type id
//
//	 0	DATA
//	 1	DATA
//	 2	DATA
//	 3	DATA
//	 4	DATA
//	 5	DATA
//	 6	DATA
//	 7	DATA
//	 8	EMPTY
//	 9	TELID
//	10	LENGTH
//	11	CRCFE
//	12	REGID
//	13	CRCBL
//	14	EC
//	15	EOE
//	16	DETID
//	17	BLKID

static char const* const word_names[] = { "DATA", "DATA", "DATA", "DATA", "DATA", "DATA", "DATA", "DATA", "EMPTY", "TELID", "LENGTH", "CRCFE", "REGID", "CRCBL", "EC", "EOE", "DETID", "BLKID" };

static char const* const state_names[] = { "IdleState", "State1", "State2", "State3", "State4", "State5", "State6", "State7", "State8", "State9", "State10" };

// state transitions id
// 
//	0	TRANSITION NOT VALID
//	1	idle 	->	(*)		-> idle
//	2	idle 	-> 	(EC) 		-> S1
//	3	S1 	-> 	(TELID) 	-> S2
//	4	S2 	-> 	(DATA)		-> S3
//	5	S3 	-> 	(DATA)		-> S3
//	6	S3 	-> 	(DETID)		-> S4
//	7	S4 	->	(DATA)		-> S5
//	8	S5 	-> 	(DATA)		-> S5
//	9	S5 	->	(DETID)		-> S4
//     10	S5 	->	(TELID)		-> S2
//     11	S5 	->	(LENGTH)	-> S6
//     12	S6 	->	(CRCFE)		-> S7
//     13	S7 	->	(EC)		-> S1
//     14	S1 	->	(BLKID)		-> S8
//     15	S8 	-> 	(LENGTH)	-> S9
//     16	S9 	->	(CRCBL)		-> S10
//     17	S10 	->	(EC)		-> S1
//     18	S10 	->	(REGID)		-> idle

static char const* const transition_names[] = { "not valid", "idle", "idle->S1", "S1->S2", "S2->S3", "S3->S3", "S3->S4", "S4->S5", "S5->S5", "S5->S4", "S5->S2", "S5->S6", "S6->S7", "S7->S1", "S1->S8", "S8->S9", "S9->S10", "S10->S1", "S10->idle" };

// matrix of state transition (row = current word_id, col = current state_id, ttable[row][col] = transition_id)

static const uint8_t ttable[WORDTYPE_NUM][STATES_NUM] = 

// 					idle	S1	S2	S3	S4	S5	S6	S7	S8	S9	S10  

   {	

/* id =  0 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  1 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  2 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  3 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  4 - DATA */		{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  5 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  6 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  7 - DATA */     	{	 1,	 0,	 4,	 5,	 7,	 8,	 0,	 0,	 0,	 0,	 0 	},
/* id =  8 - EMPTY */		{	 0,      0,      0,      0,      0,      0,      0,      0,      0,      0,      0      }, // case inside 'process' loop	
/* id =  9 - TELID */ 		{	 1,	 3,	 0,	 0,	 0,	10,	 0,	 0,	 0,	 0,	 0	},
/* id = 10 - LENGTH */		{	 1,	 0,	 0,	 0,	 0,	11,	 0,	 0,	15,	 0,	 0	},
/* id = 11 - CRCFE */		{	 1,	 0,	 0,	 0,	 0,	 0,	12,	 0,	 0,	 0,	 0	},
/* id = 12 - REGID */		{	 1,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	18	},
/* id = 13 - CRCBL */		{	 1,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	16,	 0	},
/* id = 14 - EC */	 	{	 2,	 0,	 0,	 0,	 0,	 0,	 0,	13,	 0, 	 0,	17	},
/* id = 15 - EOE */ 	 	{	 1,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0	}, //
/* id = 16 - DETID */		{	 1,	 0,	 0,	 6,	 0,	 9,	 0,	 0,	 0,	 0,	 0	},
/* id = 17 - BLKID */		{	 1,	14,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0,	 0	}

   };	

static char const* const FzFec_str[] = { "FEC#0", "FEC#1", "FEC#2", "FEC#3", "FEC#4", "FEC#5", "FEC#6", "FEC#7", "", "", "", "", "", "", "", "ADC", "UNK"  };
static char const* const FzDataType_str[] = { "QH1", "I1", "QL1", "Q2", "I2", "Q3", "ADC", "UNK" };
static char const* const FzTelescope_str[] = { "A", "B", "UNK" };
static char const* const FzDetector_str[] = { "Si1", "Si2", "CsI", "UNK" };

class FzFSM {

private:

   uint8_t state_id;
   uint8_t word_id;
   uint8_t trans_id;

   unsigned short int *event;
   uint32_t event_size; 
   uint32_t event_index;

   uint8_t getword_id(unsigned short int word);

   void trans00(void);
   void trans01(void);
   void trans02(void);
   void trans03(void);
   void trans04(void);
   void trans05(void);
   void trans06(void);
   void trans07(void);
   void trans08(void);
   void trans09(void);
   void trans10(void);
   void trans11(void);
   void trans12(void);
   void trans13(void);
   void trans14(void);
   void trans15(void);
   void trans16(void);
   void trans17(void);
   void trans18(void);

   // support variables

   DAQ::FzEvent *ev;
   DAQ::FzBlock *blk;
   DAQ::FzFee *fee;
   DAQ::FzHit *hit;
   DAQ::FzData *d;
   DAQ::Energy *en;
   DAQ::Waveform *wf;

   uint16_t tmp_ec;
   uint16_t tmp_rawec;

   bool energy1_done;
   bool energy2_done;
   bool pretrig_done;
   bool wflen_done;

   uint16_t rd_wflen;

   uint32_t blklen;
   uint16_t rd_blklen;
   uint32_t feelen;
   uint16_t rd_feelen;

   uint16_t blkcrc;
   uint16_t rd_blkcrc;
   uint16_t feecrc;
   uint16_t rd_feecrc;

   uint16_t save_blkcrc, save_feecrc;

   bool err_in_event;

   FzLogger *log;
   char logbuf[256];

   Report::FzFSM fsm_report;

public:

   FzFSM(void);

   bool event_is_empty;

   void init(void);
   void initlog(FzLogger *l);

   void import(unsigned short int *evraw, uint32_t size, DAQ::FzEvent *e);

   int process(void);

   Report::FzFSM get_report(void);
};

#endif
