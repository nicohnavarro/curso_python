#Manupulacion de cadenas 
#En python todo es un objeto
#Manipulacion de cadenas es la actividad mas utilizada
#upper() ->Todo el string a mayusculas
#lower() ->Todo el string a minisculas
#capitalize() -> Primera letra en mayuscula
#count() -> Cantidad de caracteres que queremos repetidos
#find() isdigit() isalum() isalpha()
#split() strip() replace() rfind()

print("--------------Practica de strings---------------")
nombreUsuario=input("Introduce tu nombre de usuario:")
print("El nombre es : ",nombreUsuario)
print("upper: ",nombreUsuario.upper())
print("lower: ",nombreUsuario.lower())
print("capitalize :",nombreUsuario.capitalize())
print("Cantidad de caracteres: ",nombreUsuario.count("i"))