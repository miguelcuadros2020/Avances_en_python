puerto = input("\nIngrese el numero del puerto:")
nombre_baseDatos = input("\nIngrese el nombre de la base de datos: ")
nombre_usuario = input("\ningrese el nombre del usuario: ")
contrasena = input("\nIngresa la contraseña de la base de datos: ")
# tomamos los datos del cliente para validar el ingreso

# tomamos los datos de la maquina para crear la url

servidor = "www.riwi.com/BD"
puerto_maquina = 3080
usuario_maquina = "miguelcuadro20"
nom_baseDatos_maquina = "prueba1"
contrasena_maquina = "ingreso20*"

# Validamos los datos ingresados por el cliente
url = f"{servidor}/{puerto_maquina}/{nom_baseDatos_maquina}/{nombre_usuario}/{contrasena_maquina}"
url_usuario = f"{servidor}/{puerto}/{nombre_baseDatos}/{nombre_usuario}/{contrasena}"
if url_usuario == url:
    print("\nbienvenido a la base de datos!!")
else:
    print(f"\nDatos invalidos verifica la infotmacion y escribela de nuevo:\n\n{url_usuario}")