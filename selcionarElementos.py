import sqlite3

def agregarBulk(lista1):
    conection = sqlite3.connect('Notas.db')
    cursor = conection.cursor()
    inst = "INSERT INTO seccion1 VALUES (?,?,?,?)"
    cursor.executemany(inst, lista1)
    conection.commit()
    conection.close()


#agregarBulk([('Paola', 'Arteaga', 1, 100),
  #           ('Luis', 'bermudez', 7, 90)])

def leer():
    con = sqlite3.connect('Notas.db')  # Corregir el nombre de la base de datos a 'Notas.db'
    cursor = con.cursor()
    inst = "SELECT * FROM seccion1"
    cursor.execute(inst)
    data = cursor.fetchall()
    con.commit()
    con.close()
    for row in data:
        print(row)

leer()
