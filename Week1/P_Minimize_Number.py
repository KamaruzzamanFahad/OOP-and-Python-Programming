lenth = input()

numbers = list(map(int,input().split()))

count =0
def alleven(arr):
    for num in arr:
        if num % 2 !=0:
            return False
    return True

while alleven(numbers):
    for  i in range(len(numbers)):
        numbers[i] = numbers[i] //2
    
    count +=1
print(count)
        
