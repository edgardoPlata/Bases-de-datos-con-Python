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

def filtrar_nombre():
    con = sqlite3.connect('Notas.db')  
    cursor = con.cursor()
    inst = "SELECT nombre FROM seccion1"
    cursor.execute(inst)
    data = cursor.fetchall()
    con.commit()
    con.close()
    for row in data:
        print(row)

#filtrar_nombre()

def filtrar_nota_nombre():
    con= sqlite3.connect('Notas.db')
    cursor = con.cursor()
    instruction= "SELECT nombre, nota FROM seccion1 WHERE nombre LIKE '%a%'"
    cursor.execute(instruction)
    data = cursor.fetchall()
    con.commit()
    con.close()
    
    for row in data:
        print(row)
filtrar_nota_nombre()