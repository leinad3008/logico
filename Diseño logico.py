###Progra de Diseño logico

import numpy as np
import matplotlib.pyplot as plt

#funciones definidas:

def ValidParidad():
    paridad=int(input("--->"))
    if paridad==1:
        print("Escogio paridad par")
    elif paridad==0:
        print("Escogio paridad impar")
    else:
        print("opción invalida")
        ValidParidad()
    return paridad
        

def Tabla_1(lista,par,bina):
    lista[1][3]=bina[0]
    lista[1][5]=bina[1]
    lista[1][6]=bina[2]
    lista[1][7]=bina[3]
    lista[1][9]=bina[4]
    lista[1][10]=bina[5]
    lista[1][11]=bina[6]
    lista[1][12]=bina[7]
    lista[1][13]=bina[8]
    lista[1][14]=bina[9]
    lista[1][15]=bina[10]
    lista[1][17]=bina[11]
    
    lista[7][3]=bina[0]
    lista[7][5]=bina[1]
    lista[7][6]=bina[2]
    lista[7][7]=bina[3]
    lista[7][9]=bina[4]
    lista[7][10]=bina[5]
    lista[7][11]=bina[6]
    lista[7][12]=bina[7]
    lista[7][13]=bina[8]
    lista[7][14]=bina[9]
    lista[7][15]=bina[10]
    lista[7][17]=bina[11]
    
    lista[2][3]=bina[0]
    lista[2][5]=bina[1]
    lista[2][7]=bina[3]
    lista[2][9]=bina[4]
    lista[2][11]=bina[6]
    lista[2][13]=bina[7]
    lista[2][15]=bina[9]
    lista[2][17]=bina[11]

    lista[3][3]=bina[0]
    lista[3][6]=bina[2]
    lista[3][7]=bina[3]
    lista[3][10]=bina[5]
    lista[3][11]=bina[6]
    lista[3][14]=bina[8]
    lista[3][15]=bina[9]

    lista[4][5]=bina[1]
    lista[4][6]=bina[2]
    lista[4][7]=bina[3]
    lista[4][12]=bina[6]
    lista[4][13]=bina[7]
    lista[4][14]=bina[8]

    lista[5][9]=bina[4]
    lista[5][10]=bina[5]
    lista[5][11]=bina[6]
    lista[5][12]=bina[7]

    lista[6][17]=bina[11]

    #if paridad==1:    La idea de esto es empezar aqui a sacar los bits de paridad
     #   i=

    #else:
        
    
    for valor in lista:
        print(valor)

def Tabla_2(lista,par,bina):
    lista[1][3]=bina[0]
    lista[1][5]=bina[1]
    lista[1][6]=bina[2]
    lista[1][7]=bina[3]
    lista[1][9]=bina[4]
    lista[1][10]=bina[5]
    lista[1][11]=bina[6]
    lista[1][12]=bina[7]
    lista[1][13]=bina[8]
    lista[1][14]=bina[9]
    lista[1][15]=bina[10]
    lista[1][17]=bina[11]

    lista[2][3]=bina[0]
    lista[2][5]=bina[1]
    lista[2][7]=bina[3]
    lista[2][9]=bina[4]
    lista[2][11]=bina[6]
    lista[2][13]=bina[7]
    lista[2][15]=bina[9]
    lista[2][17]=bina[11]

    lista[3][3]=bina[0]
    lista[3][6]=bina[2]
    lista[3][7]=bina[3]
    lista[3][10]=bina[5]
    lista[3][11]=bina[6]
    lista[3][14]=bina[8]
    lista[3][15]=bina[9]

    lista[4][5]=bina[1]
    lista[4][6]=bina[2]
    lista[4][7]=bina[3]
    lista[4][12]=bina[6]
    lista[4][13]=bina[7]
    lista[4][14]=bina[8]

    lista[5][9]=bina[4]
    lista[5][10]=bina[5]
    lista[5][11]=bina[6]
    lista[5][12]=bina[7]

    lista[6][17]=bina[11]


    for valor in lista:
        print(valor)


def ToBin(num, let): #pasa el numero octal a binario
    q=len(let)
    i=q-1
    x=""
    while i>=0:
        p=int(let[i])
        if p==0:
            x="000"+x
        elif p==1:
            x="001"+x
        elif p==2:
            x="010"+x
        elif p==3:
            x="011"+x
        elif p==4:
            x="100"+x
        elif p==5:
            x="101"+x
        elif p==6:
            x="110"+x
        else:
            x="111"+x
        i=i-1
    return x
        
def hexa(bina):
    largo=len(bina)
   
    if largo%4==0:
        lista1=[]
        cont=0
        contf=0
        
        while cont<largo:
            aux=""
            while (contf<4):
                aux=aux+(bina[cont])
                contf+=1
                cont+=1
            
            lista1.append(aux)
            contf=0
        global aux1
        aux1=[]
        for n in range(0,len(lista1)):
            if lista1[n]=="0000":
                aux1.append("0")
            elif lista1[n]=="0001":
                aux1.append("1")
            elif lista1[n]=="0010":
                aux1.append("2")
            elif lista1[n]=="0011":
                aux1.append("3")
            elif lista1[n]=="0100":
                aux1.append("4")
            elif lista1[n]=="0101":
                aux1.append("5")
            elif lista1[n]=="0110":
                aux1.append("6")
            elif lista1[n]=="0111":
                aux1.append("7")
            elif lista1[n]=="1000":
                aux1.append("8")
            elif lista1[n]=="1001":
                aux1.append("9")
            elif lista1[n]=="1010":
                aux1.append("A")
            elif lista1[n]=="1011":
                aux1.append("B")
            elif lista1[n]=="1100":
                aux1.append("C")
            elif lista1[n]=="1101":
                aux1.append("D")
            elif lista1[n]=="1110":
                aux1.append("E")
            elif lista1[n]=="1111":
                aux1.append("F")
            else:
                print("Numero invalido")
       
        
    else: #Correcion en caso de que el numero binario no tenga todos los ceros
        nuevo="0"
        nuevo=nuevo+bina
        
        largo=len(nuevo)
        hexa(nuevo)
    Hexa=""
    for ele in range(0,len(aux1)):
        Hexa=Hexa+(aux1[ele])
    
    return Hexa
    
    
    
    
def Nrz(bina):
    lista=["0"]
    Datos_Nrz=""
    contl=1
    cont=0
    while cont<len(bina):
        
        if bina[cont]=='0':
            lista.append(lista[contl-1])
        else:
            if lista[contl-1]=="0":
                lista.append("1")
            else:
                lista.append("0")
        cont+=1
        contl+=1
        
    for ele in range(1,len(lista)):
        Datos_Nrz=Datos_Nrz+lista[ele]
    return lista



def submenu(): #submenu final que permite terminar el programa o continuar 
    print("1- digitar un nuevo número")
    print("2- salir")
    opcion=int(input("ocpión: "))
    if opcion ==1:
            menu()
    elif opcion==2:
            print("Adios")
    else :
            print ("opcion invalida")
            submenu()


    
def valid(ent, Largo): #valida que sea de 4 digitos, que este dentro del rango y que sea octal

    if len(Largo)== 4:
        if ent < 0 or ent > 7777:
            print("El numero no es valido")
            menu()
            
        else:
            i=0
            y=len(Largo)-1
            while i<=y:
                x=int(Largo[i])
                if x>7:
                    print("El número no es valido")
                    menu()
                i=i+1
            return 1
            
    else:
            print("El número no es valido")
            menu()

def Nrzi(data):
    xs = np.repeat(range(len(data)), 2)
    ys = np.repeat(data, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.plot(xs, ys)
    plt.ylim(-0.5, 1.5)
    plt.show()

#programa principal 


def menu():
    
    try:
        
        Largo= str(input("Ingrese un número en base octal de 4 digitos: ")) #carga el octal
        
        Octal= int(Largo) #lo pasa a int
        
        valid(Octal, Largo) #función valid
        
        Tabla1=[["","p1","p2","d1","p3","d2","d3","d4","p4","d5","d6","d7","d8","d9","d10","d11","p5","d12"],["Palabras de datos recibida(sin paridad):","","","","","","","","","","","","","","","","",""],["p1","","","","","","","","","","","","","","","","",""],["p2","","","","","","","","","","","","","","","","",""],["p3","","","","","","","","","","","","","","","","","",""],["p4","","","","","","","","","","","","","","","","",""],["p5","","","","","","","","","","","","","","","","",""],["Palabras de datos recibida(con paridad):","","","","","","","","","","","","","","","","",""]]
        Tabla2=[["","p1","p2","d1","p3","d2","d3","d4","p4","d5","d6","d7","d8","d9","d10","d11","p5","d12","Prueba de paridad","Bit de paridad"],["Palabras de datos recibida:","","","","","","","","","","","","","","","","","","",""],["p1","","","","","","","","","","","","","","","","","","",""],["p2","","","","","","","","","","","","","","","","","","",""],["p3","","","","","","","","","","","","","","","","","","",""],["p4","","","","","","","","","","","","","","","","","","",""],["p5","","","","","","","","","","","","","","","","","","",""]]

        NumBin= str(ToBin(Octal, Largo)) #funcion ineficiente para pasar a binario y lo guarda en la una variable tipo int 

        NumHexa= hexa(NumBin)
        
        print("El número",Octal,"en binario es:",NumBin)
        print("El número",Octal,"en hexadecimal es:",NumHexa)
        print("Qué tipo de paridad desea:")
        print("0. impar")
        print("1. par")
        Paridad=ValidParidad()##escoge el tipo de paridad
        dato=Nrz(NumBin)
        print("Dato en Nrz:",dato)
    
        print("Tabla 1:")
        Tabla_1(Tabla1,Paridad,NumBin)
        print("Tabla 2:")
        Tabla_2(Tabla2,Paridad,NumBin)
        ###Nrzi(dato)
        
        submenu()
        
    except ValueError:
        print("El valor no es valido")
        menu()
        
    
    

menu()
