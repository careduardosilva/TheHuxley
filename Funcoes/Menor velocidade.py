def velkmh(v0,a,t):
    return (v0 + a*t)
v = 0
maiorab = 0
for i in range(0,3):
    vaux = v
    v0 = float(input())
    a = float(input())
    t = float(input())
    convertvms = 3.6 * v0
    v = velkmh(convertvms,a,t)
    menorab = (vaux+v-abs(vaux-v))/2 #Podemos obter os menores valores, pela formula do exercicio anterior
print(maiorab)
