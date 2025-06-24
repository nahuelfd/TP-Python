import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    imagen TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    alt TEXT
)
''')  # <- ¡Quitamos la coma extra en "alt TEXT"!

productos = [
    ("Camiseta titular", 125000, "tienda/camiseta_titular.jpg", 25, "camiseta_titular"),
    ("Camiseta alternativa", 115000, "tienda/camiseta_suplente.jpg", 25, "camiseta_suplente"),
    ("Short", 68000, "tienda/short.jpg", 50, "short"),
    ("Piluso", 39000, "tienda/piluso.jpg", 15, "piluso")
]

cursor.executemany('''
INSERT INTO productos (nombre, precio, imagen, cantidad, alt)
VALUES (?, ?, ?, ?, ?)
''', productos)

conn.commit()
conn.close()