inputData = str(input("enter data:"))
data = list(inputData)
flag = 's'
uflag ='l'
i = 0
urange= len(data)
while i<urange:
    if data[i] == flag:
        data.insert(i, uflag)
        i += 2
    else:
        i += 1
# staff at head
rangSize = len(data)
for i in range(rangSize):
    if i == 0:
        data.insert(i, flag)
# staff at tail
ursz= len(data)
while i <= ursz:
    if i == len(data):
        data.append(flag)
    i += 1
# printing output
x = ''.join(data)
print("output:" + x)

# test input.
# hello
# tension