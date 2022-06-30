""" 
1. Programar una función que valide nombres de usuarios para que cumplan con los siguientes requisitos.
a. El nombre de usuario debe ser alfanumérico.
b. El nombre de usuario debe contener un mínimo de 5 caracteres y un máximo de 10
c. Si el nombre de usuario tiene más de 10 caracteres debe retornar el mensaje: 
“El nombre de usuario debe contener máximo 10 caracteres”.
d. Si el nombre de usuario tiene menos de 5 caracteres, debe retornar el
siguiente mensaje: “El nombre de usuario debe contener al menos 5
caracteres”
e. Si el nombre de usuario es alfanumérico, retornara True.

2. Programar una función que valide contraseñas para que cumplan con los siguientes
requisitos:
a. La contraseña debe tener un mínimo de 6 caracteres y un máximo de 12
caracteres.
b. La contraseña no puede contener espacios en banco.
c. Si la contraseña es válida, retorna True
d. Si la contraseña no cumple con los requisitos, retorna el siguiente mensaje:
“La contraseña ingresada no es segura”

3. Una empresa de desarrollo de software necesita un módulo que solicite a los usuario
su nombre y contraseña y valide si son correctos utilizando las funciones
programadas previamente.
"""

def vnombre(usuario):
    if not usuario.isnumeric():
        if 5 <= len(usuario) <= 10:
            return True
        else:
            if len(usuario) < 5:
                return "El nombre de usuario debe contener al menos 5 caracteres"
            if len(usuario) > 10:
                return "El nombre de usuario debe contener un máximo de 10 caracteres"
    else:
        return "El nombre de usuario debe ser alfanumérico"

def vclave(clave):
    if not clave.isnumeric():
        if 6 <= len(clave) <= 12:
            return True
        else:
            return "La contraseña ingresada no es segura"
    else:
        return "La clave debe ser alfanumerica"

def vcuenta(usuario, clave):
    rusuario = str(vnombre(usuario))
    rclave = str(vclave(clave))

    if rusuario == "True" and rclave == "True":
        return "Sesión Iniciada Correctamente"
    else:
        if rusuario != "True":
            return rusuario
        if rclave != "True":
            return rclave

def main():
    print("--------Ingrese nombre y clave para iniciar sesión-------")
    usuario = input("Ingresar Usuario: ")
    clave = input("Ingresar Clave: ")
    result = vcuenta(usuario, clave)
    print(result)
main()