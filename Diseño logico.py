###Progra de Diseño logico

#funciones definidas:
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
        
def ToHex(bi):    #pasa el numero binario a Hexa
    
    
    

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

    if len(Largo)<= 4:
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


#programa principal 


def menu():
    
    try:
        
        Octal= int(input("Ingrese un número en base octal de 4 digitos: ")) #carga el octal
        
        Largo= str(Octal) #pasa el numero a string
        
        valid(Octal, Largo) #función valid

        NumBin= int(ToBin(Octal, Largo)) #funcion ineficiente para pasar a binario y lo guarda en la una variable tipo int 

        NumHexa= ToHex(NumBin)
        
        print(NumBin)
        print(NumHexa)
        submenu()
        
    except ValueError:
        print("El valor no es valido")
        menu()
        
    
    

menu()
