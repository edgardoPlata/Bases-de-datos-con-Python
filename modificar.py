import sqlite3
print("Before")
def filtrar_nombre():
    con = sqlite3.connect('Notas.db')  
    cursor = con.cursor()
    inst = "SELECT * FROM seccion1"
    cursor.execute(inst)
    data = cursor.fetchall()
    con.commit()
    con.close()
    
    for row in data:
        print(row)

filtrar_nombre()

def modificar():
    con = sqlite3.connect('Notas.db')  # Corregir el nombre de la base de datos a 'Notas.db'
    cursor = con.cursor()
    inst = "UPDATE seccion1 SET nota = 75 WHERE apellido LIKE '%jimenez'"
    cursor.execute(inst)
    data = cursor.fetchall()
    con.commit()
    con.close()
    for row in data:
        print(row)

modificar()
print("After")
filtrar_nombre()