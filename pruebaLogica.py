import pedirDatos

def validaNota(nota1,nota2,nota3,nota4,nota5):
    listaDeNotas = []

    if nota1.isdigit() and nota2.isdigit() and nota3.isdigit() and nota4.isdigit() and nota5.isdigit():
        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        nota4 = int(nota4)
        nota5 = int(nota5)
        if nota1 > 20 or nota2>20 or nota3>20 or nota4>20 or nota5>20:
            print("Has Ingresado valores incorrectos, intenta de nuevo")
            pedirDatos.ingresarNota()
        else:
            print("Notas agregadas...")
            listaDeNotas.append(nota1)
            listaDeNotas.append(nota2)
            listaDeNotas.append(nota3)
            listaDeNotas.append(nota4)
            listaDeNotas.append(nota5)
            print(listaDeNotas)
    else:
        print()
        print("Intenta de nuevo")
        pedirDatos.ingresarNota()
    
    suma = 0
    prom = 0
    mayor = 0
    menor = 0
    
    for i in listaDeNotas:
        suma = suma +i
        prom = suma/5

    mayor = max(listaDeNotas)
    menor = min(listaDeNotas)   
    
    print(f"La suma: {suma}")
    print(f"El promedio de notas: {prom}")
    print(f"El menor: {menor}")
    print(f"El mayor: {mayor}")