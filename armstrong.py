number=int(input())
number_copy=number
ans=0
index=len(str(number))
while number!=0:
  temp=number%10
  ans+=pow(temp,index)
  number=int(number/10)
if ans==number_copy: print("yes")
else: print("no")
