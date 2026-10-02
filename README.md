def is_armstrong(num):
    num_str=str(num)
    n=len(num_str)
    sum=0
    temp=num
    while temp>0:
        digit=temp % 10
        sum+=digit**n
        temp//=10
    if num==sum:
        return True 
    else:
        return False    
num=int(input("enter the number"))        
if is_armstrong(num):
    print("armstrong number")
else:
    print("no armstrong number")    
