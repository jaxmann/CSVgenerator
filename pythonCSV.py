import csv
import random
import datetime
from datetime import datetime
from datetime import timedelta
from random import randint
import sys

# args are 0: numLines, 1: output file

user_id = [
    1,
    2,
    3
]

acct_num = [
    '123',
    '456',
    '789'
]

card_number = [
    '1111-2222-3333-4444',
    '5555-6666-7777-8888',
]

transaction_type = [
   1,
   2,
   3
]

channel_type = [
    100,
    200,
    300
]

txn_location = [
    'Texas',
    'Idaho',
    'Ohio',
    'Alabama',
]     

if (len(sys.argv) < 3): print 'invalid num of arguments: arg1: num lines, arg2; output file'


# yyyy/mm/dd
start_date= datetime(2010,10,10) #lower limit for random datetime
end_date= datetime(2015,01,04) #upper limit for random datetime

def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

ctr = '00000'
g=open(sys.argv[2],"w")
w=csv.writer(g, lineterminator='\n')
w.writerow(('User_ID','Account_Number','Card_Number','Transaction_Category','Transaction_Type','Channel_Type', 'Channel_Id','Transaction_Date','Transaction_Time','Transaction_Time_Hour_of_Day','Transaction_Time_Minute_of_Hour','Credit_Debit_Indicator','Account_Balance','Transaction_Amount','Transaction_Currency','Transaction_Location','Transaction_ID'))
for i in xrange(int(sys.argv[1])):

    randUser = random.randrange(1,40,1)
    randDate = random_date(start_date, end_date)
    txn_date = str(randDate.month) + "/" + str(randDate.day) + "/" + str(randDate.year)
    txn_hour = str(random.randrange(0,24,1))
    txn_minute = str(random.randrange(0,60,1))
    txn_time = txn_hour + ":" + txn_minute
    ctr = str(int(ctr) + 1).zfill(len(ctr))

    w.writerow((
        user_id[randUser], 
        acct_num[randUser], 
        card_number[randUser],
        '1',
        random.choice(transaction_type),
        random.choice(channel_type),
        random.randrange(1,100,1),
        txn_date,
        txn_date + " "+  txn_time,
        txn_hour,
        txn_minute,
        random.choice(["CR", "DB"]),
        random.randrange(500,40000,1),
        random.randrange(40,4000,1),
        "USD",
        random.choice(txn_location),
        "TXN" + ctr
    ))

   

