Number = int(input("How many terms? "))

First_Value, Second_Value = 0, 1
i = 0
if Number <= 0:
   print("Please enter a positive integer")
elif Number == 1:
    print("Fibonacci sequence upto",Number,":")
    print(First_Value)
else:
   print("Fibonacci sequence:")
while i < Number:
    print(First_Value)
Next = First_Value + Second_Value

First_Value = Second_Value
Second_Value = Next
i += 1


