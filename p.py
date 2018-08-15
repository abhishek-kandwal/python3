def mul(a,b):
    return a*b
def add(a,b):
    return a+b
def div(a,b):
    return a/b
def sub(a,b):
    return abs(a-b)
a = input('input the values for calculations \n a =')
b = input('\n b= ')
while True:
      opt=input('\n select any 1 function \n 1.MULTIPLY  2.ADD  3.DIVIDE  4.SUBTRACT 5.ALL 6.exit \n')
      if opt == 1:
         print ('multiplied a and b =' + str(mul(a,b)))
      elif opt == 2:
         print ( 'added a and b =' + str(add(a,b)))
      elif opt == 3:
         print ( 'divided a and b =' + str(div(a,b)))
      elif opt == 4:
         print ( 'subtracted a and b =' + str(sub(a,b)))
      elif opt == 5:
         print ( ' multiplied a and b =' + str(mul(a,b)) + '\n added a and b =' + str(add(a,b))  + '\n divided a and b =' + str(div(a,b)) + '\n subtracted a and b =' + str(sub(a,b)) + '\n')
      elif opt == 6:
         break 
exit()
