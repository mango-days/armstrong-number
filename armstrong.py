def size(number):
  index = 0
  while number!=0:
    number = int(number/10)
    index+=1
  return index

number=int(input())
number_copy=number
ans=0
index=size(number)
while number!=0:
  temp=number%10
  ans+=pow(temp,index)
  number=int(number/10)
if ans==number_copy: print("yes")
else: print("no")
