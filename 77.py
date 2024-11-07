def findFirstEven(numbers):
    for num in numbers:
        if num%2==0:
            return num
    return None 
list1=[1,5,9,7,3,6,8]
result=findFirstEven(list1)
print(result)

print("Code written and executed by Kunsh Dhawan") 