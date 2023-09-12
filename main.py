def factorial(x):
  if x==0 or x==1:
    return 1
  else:
    return(x*factorial(x-1)) 
#main
x=int(input("Enter number:"))
print("Factorial of given number is:",factorial(x)) 