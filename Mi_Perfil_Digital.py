#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = " Valeryne Pereira García"
edad = 16
estatura = 1.50
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("valeryne_12", "Valeryne._12")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Termonuclear", "artista": "perfecto miserable", "duracion": "3:33"},
{"titulo": "Doma", "artista": "Jósean log", "duracion": "3:08"},
{"titulo": "Despierto", "artista": "Silvestre Dangond", "duracion": "4:04"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
