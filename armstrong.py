number=int(input())
number_copy=number
ans=0
while number!=0:
  temp=number%10
  ans+=temp*temp+temp
  number=int(number/10)
if ans==number_copy: print("yes")
else: print("no")