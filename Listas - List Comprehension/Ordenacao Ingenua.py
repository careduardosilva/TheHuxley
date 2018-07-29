n = int(input())
numeros = sorted([int(input()) for i in range(n)])
string = ''
for i in numeros:
    string += "["+str(i)+"]"
print(string)
