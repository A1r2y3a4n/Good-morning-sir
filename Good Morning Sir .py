import time

current_time = time.localtime(time.time())



current_hour = int(time.strftime("%H", current_time))
current_minute = int(time.strftime("%M", current_time))
current_second = int(time.strftime("%S", current_time))
if(5<=current_hour<=12): 
  print("Good morning ")

elif(12<=current_hour<=17):
  print( "Good afternoon")
  if(17<=current_hour>=20):
    print("Good evening")
    
else:
  print("Good night")

  
