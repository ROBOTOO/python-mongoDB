import pymongo
import random
import time
import datetime
import threading 

try: 
	conn = pymongo.MongoClient() 
	print("Connected successfully!!!") 
except: 
	print("Could not connect to MongoDB") 

db = conn.innovation_demo
pattern = db.patterns 
hour=db.onehour
day=db.oneday
month=db.onemonth

def present(): 
   
    while True:
        b=random.randint(5,50)
        bi=bin(b)
        c=time.asctime()
        d=datetime.datetime.today()
        record = {
            "pattern":bi,
            "Time":c,     
        }
       
        time.sleep(1)    
        rec_id1=pattern.insert_one(record)
       
   
def one_hour(): 
   	
    while True:       
        c=time.asctime()
       
        pro_hour = {
               "Products":12,
               "time":c,
           }   
       
        time.sleep(2)      
        rec_id2=hour.insert_one(pro_hour) 
       
      
def one_day(): 	
    
    while True:       
        c=time.asctime()
        
        pro_day = {
               "Products":2,
               "time":c,
           }   
        time.sleep(3)      
        rec_id3=day.insert_one(pro_day) 
             
def one_month(): 	
    while True: 
        c=time.asctime()
        pro_month = {
               "Products":6,
               "time":c,
           }   
        time.sleep(4)      
        rec_id4=month.insert_one(pro_month)         

if __name__ == "__main__": 

	t1 = threading.Thread(target=one_hour, name='t1').start()
	t2 = threading.Thread(target=present, name='t2').start()
	t3 = threading.Thread(target=one_day, name='t3').start()
	t4 = threading.Thread(target=one_month, name='t4').start() 
	
