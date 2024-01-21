def num_pal(num):
  #function of check id a num is palindrom
    temp = num
    val=0
    while num>0:
        q = num%10
        val=val*10+q
        num=num//10
    return val==temp
    
print(num_pal(12321))
