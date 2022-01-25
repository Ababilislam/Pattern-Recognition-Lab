inputData = str(input("enter data:"))
data = list(inputData)
flag = 's'
uFlag = 'l'
i = 0
rmHT = data[1:-1]
# print(rmHT)

while i < len(rmHT):
    if rmHT[i] == uFlag and rmHT[i + 1] == flag:
        rmHT.pop(i)
    i += 1

x = ''.join(rmHT)
print("output:" + x)

#  input>> shelslos
# Output should be >>  heslo
