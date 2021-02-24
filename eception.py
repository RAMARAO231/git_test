try:
      a=7
      b=0
      print(a/b)
except TypeError:
       print('wrong operation') 
except ZeroDivisionError:
        print('divide by zero is infinity')
print("out of try except blocks")
