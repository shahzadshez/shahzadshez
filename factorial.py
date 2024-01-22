# write a program to find factorial of a number
def fact(num):
  result=1
  for i in range(2,num+1):
    result=result*i
  return result

def fact1(num):
  if num=1:
    return  1
  else:
    return num*fact(num-1)

print(fact(5))
print(fact1(5))
