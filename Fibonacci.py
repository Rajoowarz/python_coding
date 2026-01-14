if n <=0:
   print("Please enter a positive number")
elif n == 1:
   print(a)
else:
   print("Fibonacci series:")
   for i in range(n):
       print(a, end =" ")
       a, b = b, a + b
