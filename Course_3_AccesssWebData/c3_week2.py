import re
file_name = input("Enter file name:")
fp = open(file_name)
sum = 0
for line in fp:
    num = re.findall('([0-9]+)', line)
    if len(num) == 0:
        continue
    for number in num:
        sum = sum + int(number)
print(sum)


