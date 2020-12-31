
>>> import CRD as M
>>> M.create("python",3)
>>> 
>>> M.create("India",1947)
>>> 
>>> M.create("Match",1,1000)
>>> 
>>> M.read("python")
'python:3'
>>> 
>>> M.read("india")
given key does not exist in database
>>> M.read("India")
'India:1947'
>>> 
>>> M.delete("python")
key is successfully deleted
>>> M.read("python")
given key does not exist in database
>>> 
>>> #we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
