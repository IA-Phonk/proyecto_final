admin= "phonk"
clave_admin= "1234"
players={}
while True:  #bucle para el menu principal 
    print("===============================MENU PRINCIPAL==================================")
    print("\n1) registrar cuenta")
    print("2) iniciar sescion")
    print("3) salir")
    opciones= input("elige una opcion: ")
    if opciones == "1": #registro de cuenta
       usuario= input("crea un usuario: ").lower()
       clave= input("crea una clave: ")
       if usuario in players:
         print("Ese usaurio ya existe")
       else:
         players[usuario] = {"clave":clave} 
         print("cuenta creada exitosamente")
    elif opciones == "2": #login
         intentos= 0
         limite= 3
         while True:
           usuario= input("usuario: ").lower()
           clave= input("clave: ")
           if (usuario in players and players[usuario]["clave"] == clave) or (usuario == admin and clave == clave_admin):
             print("Bienvenido",usuario,"ingresando al juego...") #agregar la segunda parte
             break
           else:
             intentos += 1
             print("usuario o clave incorrectos") 
             if intentos == limite:
              print("alcanzaste el limite permitido")
              break  
    elif opciones == "3": #cerrar 
           print("juego cerrado")
           break
    else:
       print("opcion no valida")
