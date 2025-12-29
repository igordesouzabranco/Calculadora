

 
while True:
    def calc():
        n1=float(input("Digite o primeiro número: "))
        n2=float(input("Digite o segundo número: "))
        oi = n1 * n2

        return f'{n1} X {n2} = {oi}'
    print(calc())
    parar = input("Digite N para parar, ou S para continuar: ")
    if parar == "N":
        break
    else:
        continue

    

