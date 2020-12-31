import threading #threading for multi operation simultaneously .

from threading import*
import time #for checking time to live

d={} 


def create(key,value,timeout=0): #create function using def .
    if key in d:
        print(" key already exists try another") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Memory limit exceeded!! ")
        else:
            print(" only alphabets are allowed")


            
def read(key):
    if key not in d:
        print("given key does not exist in database") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #check live time to expiry time
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri



def delete(key):
    if key not in d:
        print("given key does not exist in database") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")

