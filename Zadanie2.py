print("Zadanie 2")
lista_5 = []
lista_sześciany = []
for x in range(1,101):
    if x % 5 == 0:
        lista_5.append(x)
        lista_sześciany.append(x**3)
print("liczby podzielne przez 5", lista_5)
print("Sześciany liczb podzielnych przez 5", lista_sześciany)
