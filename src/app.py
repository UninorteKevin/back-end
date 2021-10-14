from flask import Flask, jsonify, request;

from User import users
from Product import products
app = Flask(__name__)

#Consultar todos los usuarios
@app.route('/api/users')
def getUsers():
        return jsonify(users)

#Agregar un nuevo usuario
@app.route('/api/user/add', methods = ['POST'])
def addUser():
        try:
                newUser = {
                        'id': '00U',
                        'names': request.json['names'],
                        'surnames': request.json['surnames'],
                        'fecha_nacimiento': request.json['fecha_nacimiento'],
                        'email': request.json['email'],
                        'password': request.json['password'],
                        'estado': 'A',
                        'role': 'USER'
                        }
                users.append(newUser)
                return jsonify({
                        'status':'SUCCESS',
                        'code': 200,
                        'message': 'Usuario registrado',
                        'user': newUser
                })

        except Exception as ex:
                return jsonify({
                        'status':'ERROR',
                        'code': 404,
                        'message': 'Error al registrar un usuario',
                        'define_error': ex.args[0]
                })

#Login de un usuario
@app.route('/api/login', methods = ['POST'])
def onLogin():
        try:
                email = request.json['email']
                password = request.json['password']

                for user in users:
                        if(user['email'] == email and user['password'] == password):

                                return jsonify({
                                        'status':'SUCCESS',
                                        'code': 200,
                                        'user': user
                                })
                                

                return jsonify({
                        'status':'WARNING',
                        'code': 202,
                        'message': 'Las credenciales no son correctas.'
                })
        except Exception as ex:
                return jsonify({
                        'status':'ERROR',
                        'code': 404,
                        'message': 'Error en el servidor al enviar los datos',
                        "define_error": ex.args[0]
                })
        
#####################################
#API PARA LOS PRODUCTOS

#Agregar un nuevo producto
@app.route('/api/products/add')
def addProduct():
        try:
                newProduct = {
                        'codigo': request['codigo'],
                        'nombre': request['nombre'],
                        'descripcion': request['descripcion'],
                        'costo': request['costo'],
                        'precio_venta': request['precio_venta'],
                        'stock': request['stock'],
                        'ubicacion': request['ubicacion'],
                        'estado': request['estado'],
                        'imagenes': request['imagenes'],
                        'calificacion': request['categoria'],
                        'categoria': request['categoria']
                }

                products.append(newProduct)
                return jsonify({
                        'status':'SUCCESS',
                        'code': 200,
                        'message': 'Producto registrado.',
                        'product': newProduct
                })
        except:
                return jsonify({
                        'status':'WARNING',
                        'code': 202,
                        'message': 'No se pudo registrar el producto.'
                })


#Consultar todos los productos
@app.route('/api/products/list')
def getProducts():
        return jsonify({
                        'status':'SUCCESS',
                        'code': 200,
                        'products': products
                })

#Consultar un producto por CODIGO
@app.route('/api/products/<string:codigo>')
def getProducto(codigo):
        try:
                for product in products:
                        if(product['codigo'] == codigo):
                                return jsonify({
                                                'status':'SUCCESS',
                                                'code': 200,
                                                'product': product
                                        })

                return jsonify({
                        'status':'WARNING',
                        'code': 202,
                        'message': 'No se encontro ningun producto con esta referencia.'
                })
        except Exception as ex:
                return jsonify({
                        'status':'ERROR',
                        'code': 404,
                        'message': 'Error en el servidor al traer el producto.',
                        'define_error': ex.args[0]
                })

if __name__ == "__main__":
        app.run(debug=True)

