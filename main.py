import random

aa=int(input("enter a number between 1 - 100 :"))

a=random.randint(1,100)
print("The judge have selected",a)

if a>aa:
  print("sorry,you have guessed a value less than the actual value")
elif a<aa:
  print("sorry,you have guessed a value more than the actual value")
else:
  print("the number selected is same as",a)
