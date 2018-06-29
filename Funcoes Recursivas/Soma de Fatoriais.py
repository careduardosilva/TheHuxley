def fatorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*fatorial(n-1)
soma_fatorial = 0
for i in range(5):
    n = int(input())
    if(n % 3 == 0):
        soma_fatorial += fatorial(n)
print(soma_fatorial)
