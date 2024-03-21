import sqlite3

def crear(): #crear base de datos
    conection = sqlite3.connect('Notas.db')
    conection.commit()
    conection.close()
    


def crear_tabla():
    conection = sqlite3.connect('Notas.db')
    cursor = conection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seccion1 (
            nombre TEXT,
            apellido TEXT,
            numero INTEGER,
            nota INTEGER
        )
        """
    )
    conection.commit()
    conection.close()

def agregar(nombre, apellido, numero,nota):
    conection = sqlite3.connect('Notas.db')
    cursor = conection.cursor()
    cursor.execute(f"INSERT INTO seccion1 values ('{nombre}','{apellido}','{numero}','{nota}')")
    conection.commit()
    conection.close()

def agregarBulk(lista1):
    conection = sqlite3.connect('Notas.db')
    cursor = conection.cursor()
    inst = "INSERT INTO seccion1 VALUES (?,?,?,?)"
    cursor.executemany(inst, lista1)
    conection.commit()
    conection.close()

agregarBulk([('Paola', 'Arteaga', 1, 100),
             ('Luis', 'bermudez', 7, 90)])
