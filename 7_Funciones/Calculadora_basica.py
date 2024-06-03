# opcion=True
# while opcion1:
# print("\n\t..:::Calculadora Basica:::...\n 1.-Suma \n 2.-Resta \n 3.-Multiplicasion \n 4.- Division \n 5.- Sañir")
# opcion=input("\t Elige una opcion: ") .upper()


# if opcion=="1" or opcion=="+" or opcion=="SUMA":
#     n1=int(input{"Numero #1: "})
#     n2=int(input{"Numero #2: "})
#     SUMA=n1+n2
#     print(f"(n1)+(n2)=(suma)")


# if opcion=="2" or opcion=="-" or opcion=="RESTA":
#     n1=int (input{"Numero #1: "})
#     n2=int (input{"Numero #2: "})
#     RESTA=n1-n2
#     print(f"(n1)-(n2)=(Resta)")


# if opcion=="3" or opcion=="*" or opcion=="MULTIPLICASION":
#     n1=int(input{"Numero #1: "})
#     n2=int(input{"Numero #2: "})
#     MULTIPLICASION=n1*n2
#     print(f"(n1)*(n2)=(MULTIPLICASION)")


# if opcion=="4" or opcion=="/" or opcion=="DIVISION":
#     n1=int(input{"Numero #1: "})
#     n2=int(input{"Numero #2: "})
#     DIVISION=n1//n2
#     print(f"(n1)//(n2)=(DIVISION)")
# else:
#     print("Terminaste la ejecusion del SW")
# opcion1=False

# def=solicitarNUmeros():
#     n1=int(input ("Numero #1: ")
#     n2=int(input ("Numero #2: ")

# def operacionAritmetica(num1,num2,ope):
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#     return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#     return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICASION":
#     return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="RESTA":
#     return f"{n1}-{n2}={n1-n2}"

# solicitarnumeros()
# printoperacionAritmetica(n1,n2,operacion)

# opcion=True
# while opcion: 
# print("\n\t..::: CALCULADORA BASICA :::... \n 1.-Suma \n 2.-Resta \n 3.-Multiplicasion \n4.-Division \n 4.-Salir")
# opcion=input("\t Elige una opcion: ").upper()

# solicitarnumeros()
# print(operacionAritmetica(n1,n2,opcion))

def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  
    

    
opcion=True    
while opcion:
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()

 solicitarNumeros()
 print(operacionAritmetica(n1,n2,opcion))

 if opcion!="5":
    solicitarNumeros
    print(operacionAritmetica(n1,n2,opcion))
 else:  
     opcion=False    
     return "Terminaste la ejecucion del SW"