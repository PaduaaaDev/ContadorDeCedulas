a = input()
lista_notas = [100, 50, 20, 10, 5, 2, 1]
lista_cont = [0, 0, 0, 0, 0, 0, 0]

n1 = int(a)
numero = n1

while n1 != 0:
    novo_valor = n1
    if n1 >= lista_notas[0]:
        n1 -= lista_notas[0] 
        lista_cont[0] += 1
    elif n1 >= lista_notas[1]:
        n1 -= lista_notas[1]
        lista_cont[1] += 1
    elif n1 >= lista_notas[2]:
        n1 -= lista_notas[2]
        lista_cont[2] += 1
    elif n1 >= lista_notas[3]:
        n1 -= lista_notas[3]
        lista_cont[3] += 1
    elif n1 >= lista_notas[4]:
        n1 -= lista_notas[4]
        lista_cont[4] += 1
    elif n1 >= lista_notas[5]:
        n1 -= lista_notas[5]
        lista_cont[5] += 1
    elif n1 >= lista_notas[6]:
        n1 -= lista_notas[6]
        lista_cont[6] += 1    
    else:
        print("Não era para chegar aqui")

print("Dinheiro recebido: R$", numero)
print(f"Foi dado {lista_cont[0]} nota(s) de R$ 100,00")
print(f"Foi dado {lista_cont[1]} nota(s) de R$ 50,00")
print(f"Foi dado {lista_cont[2]} nota(s) de R$ 20,00")
print(f"Foi dado {lista_cont[3]} nota(s) de R$ 10,00")
print(f"Foi dado {lista_cont[4]} nota(s) de R$ 5,00")
print(f"Foi dado {lista_cont[5]} nota(s) de R$ 2,00")
print(f"Foi dado {lista_cont[6]} nota(s) de R$ 1,00")