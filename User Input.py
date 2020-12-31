Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
>>> 