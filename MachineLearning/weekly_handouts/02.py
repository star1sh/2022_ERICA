num = 0
sum = 0

while num <= 20:
    num += 1
    if (num%2) == 0:
        sum += num
    else:
        continue

print(sum)
