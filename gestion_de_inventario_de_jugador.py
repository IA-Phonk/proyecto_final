
admin= "phonk"
clave_admin= "1234"
players={}
while True:   
    print("                        MENU PRINCIPAL                           ")
    opciones= input("\na) registrar cuenta / b) iniciar sescion / c) salir: ")
    if opciones == "a": #registro de cuenta
       usuario= input("crea un usuario: ")
       clave= input("crea una clave: ")
       if usuario in players:
         print("Ese usaurio ya existe")
       else:
         players[usuario] = {"clave":clave} 
         print("cuenta creada exitosamente")
    elif opciones == "b": #login
         usuario= input("usuario: ")
         clave= input("clave: ")
         if (usuario in players and players[usuario]["clave"] == clave) or (usuario == admin and clave == clave_admin):
           print("Bienvenido",usuario,"ingresando al juego...") #agregar la segunda parte
    elif opciones == "c": #cerrar 
           print("juego cerrado")
           break
    else:
       print("opcion no valida")
