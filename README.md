"# MVT-DanielCollao" 
CONSIGNA
Crear una web que permite ver los datos de algunos de tus familiares, 
    guardados en un BD.

1.- Deberá tener un template, una vista y un modelo(como minimo,
     pueden usar más)
    Template = templates/familiares.html
    Vista = def Familiares
    Modelo = Familiares (nombre, apellido, parentesco, edad, fecha nacimiento)

2.- La clase del modelo, deberá guardar mínimo un número, una cadena 
    y una fecha( puede guardar más cosas)
    nombre, apellido y parentesco = CharField
    edad = IntegerField
    fecha_nacimiento = DateField

3.- Se deberán crear como mínimo 3 familiares
    fue creado un diccionario con 5 familiares ( padre, madre, abuelo, abuela, tía )

4.- Los familiares se deben ver desde la web
    familiar.html

