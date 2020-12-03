def box ():
  for row in range (1,11):
    digit = row
    for col in range (1,11):
      print(digit % 10, end = "")
      digit += 1
    
    print()
def withwhile():
  for i in range(9):
    fact = i + 2
    print("{}!=".format(fact),end = "")

    digits = 1
    while digits < fact:
      print("{}*".format(digits), end ="")
      digits +=1

    print("{}=".format(fact),end = "")

    result = 1
    count = 1

    while count <= fact:
      result*= count
      count +=1

    print('{}'.format(result))
def triangle():
  num = int(input())
  count = 1

  for row in range (1, num + 1):
    for spaces in range (num - row):
      print(" ", end = "")

    for digits in range (1,row + 1):
      print(count%10, end = ' ')
      count +=1
    
    print()
def fact():
  for count in range (2,11):
    print("{}!=".format(count),end ="")

    for digit in range (1,count):
      print("{}*".format(digit),end = "")
    
    result = 1
    for i in range (1,count + 1):
      result *= i
      
    print("{}={}".format(count,result))
def threecount():
  num = int(input())
  count = 0

  for i in range (1, num +1):
    target = i
    while target:
      if target % 10 == 3:
        count += 1
      target //= 10
    
  print(count)