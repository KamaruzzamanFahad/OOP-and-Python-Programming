lenth = input()
numbers = list(map(int, input().split()))
good_seq = []

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

minimum_remove =0

for f in freq:
    if int(f) == int(freq[f]):
        continue
    if(int(f) < int(freq[f]) ):
        minimum_remove +=  int(freq[f])  -int(f)
    else:
        minimum_remove += int(freq[f])
    
print(minimum_remove)
