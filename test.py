import urllib.request
import urllib.error
import time
 
date = urllib.request.urlopen('http://www.google.com').headers['Date']
print(date)
  
time = int(time.mktime(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))
print(time)