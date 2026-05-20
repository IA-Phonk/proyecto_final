usuario_correcto= "phonk"
usuario= ""
clave_correcta= "jugador00156"
clave= ""
while clave != clave_correcta or usuario != usuario_correcto:
    usuario= input("ingrese usuario: ")
    clave= input("ingrese clave: ")
    if clave != clave_correcta or usuario != usuario_correcto:
        print("clave o usuario incorrecta intente nuevamente")
print("vereficacion correcta. Ingresando al inventario...")        