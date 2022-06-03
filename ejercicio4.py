import pandas as pd
#Formato de numeros de telefonos
#Codigo de pais: +57
#Extensiòn M: 11
#Extensiòn F: 10
listNames = []
listSexo = []
listTels = []
op = True
while( op != False):
    nombre = str(input('Nombre: '))
    sexo = str(input('Sexo(M/F): '))
    telefono = str(input('Teléfono (+57): '))
    if( sexo == "M" or sexo == "m"):
        updateTelefono = "+57-" + telefono + "-" + "11"
    else: 
        updateTelefono = "+57-" + telefono + "-" + "10"
    listNames.append(nombre)
    listSexo.append(sexo)
    listTels.append(updateTelefono)

    opcion = str(input("Desea continuar agregando (s/n): "))
    if( opcion == "S" or opcion == "s" ):
        op = True
    else:
        op = False

data = {
    "Nombres": listNames,
    "Sexo": listSexo,
    "Telefono": listTels
}

df = pd.DataFrame(data)

print(df)