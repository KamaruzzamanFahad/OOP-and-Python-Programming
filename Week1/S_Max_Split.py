string = input()

balance = 0
current = ""
array = []
cnt =0

for s in string:
    current += s

    if s == 'L':
        balance += 1
    else:
        balance -= 1

    if balance == 0:
        array.append(current)
        current = ""
        cnt += 1

print(cnt)

for a in array:
    print(a)