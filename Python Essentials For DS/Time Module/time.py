import time
x=time.strftime('%I')
match x:
    case 0:
        if(x>12 and x<5):
         print("Good Morning ")
    case 1:
        if(x>=12):
           print("Good Afternoon ")
    case _:
      print("Good Evening ")       




