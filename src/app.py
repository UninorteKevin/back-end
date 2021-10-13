from flask import Flask, jsonify, request;

from User import users

app = Flask(__name__)

@app.route('/api/users')
def getUsers():
        return jsonify(users)

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
                                        'message': 'Logeado correctamente',
                                        'identity': user
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
        


if __name__ == "__main__":
        app.run(debug=True)

