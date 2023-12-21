d1 = 1
d10 = 10
d20 = 20
d50 = 50
c1 = c10 = c20 = c50 = 0
nv1 = nv10 = nv20 = 0
n = int(input('Digite o valor a ser sacado R$ '))
while True:
        c50 = (n // d50)
        nv20 = (n % d50)
        c20 = (nv20 // d20)
        nv10 = (nv20 % d20)
        c10 = (nv10 // d10)
        nv1 = (nv10 % d10)
        c1 = (nv1 // d1)
        break
print(f'''O valor sacado de R${n:.2f} está distribuído em:
{c50} notas de R$50,00
{c20} notas de R$20,00
{c10} notas de R$10,00
{c1} notas de R$1,00''')