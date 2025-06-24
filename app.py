from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


# Funciones para interactuar con SQLite
def obtener_productos():
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, imagen, cantidad, alt FROM productos")
    filas = cursor.fetchall()
    conn.close()
    productos = []
    for fila in filas:
        productos.append({
            "nombre": fila[0],
            "precio": fila[1],
            "imagen": fila[2],
            "cantidad": fila[3],
            "alt": fila[4],
            
        })
    return productos

def obtener_producto(nombre):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, imagen, cantidad, alt FROM productos WHERE nombre = ?", (nombre,))
    fila = cursor.fetchone()
    conn.close()
    if fila:
        return {
            "nombre": fila[0],
            "precio": fila[1],
            "imagen": fila[2],
            "cantidad": fila[3],
            "alt": fila[4]
        }
    return None

def insertar_producto(data):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, precio, imagen, cantidad, alt)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['nombre'], data['precio'], data['imagen'], data['cantidad'], data.get('alt', '')))
    conn.commit()
    conn.close()

def actualizar_producto(nombre, data):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE productos SET nombre=?, precio=?, imagen=?, cantidad=?, alt=?
        WHERE nombre=?
    ''', (data['nombre'], data['precio'], data['imagen'], data['cantidad'], data.get('alt', ''), nombre))
    conn.commit()
    conn.close()

def eliminar_producto(nombre):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()

# Rutas
@app.route('/tienda')
def tienda():
    productos = obtener_productos()
    return render_template('tienda.html', productos=productos)

@app.route('/products')
def get_products():
    productos = obtener_productos()
    return render_template('tienda.html', productos=productos)

@app.route('/products/<string:product_name>')
def get_product(product_name):
    producto = obtener_producto(product_name)
    if producto:
        return jsonify({"product": producto})
    return jsonify({"message": "Producto no encontrado"})

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    insertar_producto(data)
    return jsonify({"message": "Producto AÃ±adido", "productos": obtener_productos()})

@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    data = request.json
    actualizar_producto(product_name, data)
    return jsonify({"message": "Producto Actualizado", "product": obtener_producto(data['nombre'])})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    eliminar_producto(product_name)
    return jsonify({"message": "Producto Eliminado", "productos": obtener_productos()})


@app.route('/sedes')
def sedes():
    return render_template('sedes.html')

@app.route('/plantel')
def plantel():
    return render_template('plantel.html')

@app.route('/palmares')
def palmares():
    return render_template('palmares.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Opcionalmente agregá otras rutas si las tenés
@app.route('/')
def inicio():
    return render_template('index.html')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)