n=int(input("Enter number:"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print("Number is not a prime:",n)
            break
    else:
             print("Number is  prime:",n)
else:
    print("Number is not prime",n)
             
