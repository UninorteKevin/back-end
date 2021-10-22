from config import obtener_conexion

def Register (
        codigo,
        usuario,
        correo,
        contraseña,
        estado,
        rol,
        create_at,
        update_at):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(CODIGO, USUARIO, CORREO, CONTRASENA, ESTADO, ROL, CREATED_AT, UPDATE_AT) "
                        + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (codigo,usuario,correo,contraseña,estado,rol,create_at,update_at))
    conexion.commit()
    conexion.close()

def GetUsers():
    users = []
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT CODIGO, USUARIO, CORREO, CREATED_AT, ESTADO, ROL FROM USUARIOS")
        users = cursor.fetchall()
    conexion.commit()
    conexion.close()

    return users

def UpdateUser(codigo,
        usuario,
        correo,
        contraseña,
        update_at):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            
            cursor.execute("UPDATE usuarios SET USUARIO = %s, CORREO = %s, CONTRASEÑA = %s, UPDATE_AT = %s WHERE CODIGO = %s",
                        (usuario,correo,contraseña,update_at,codigo))
        conexion.commit()
        conexion.close()

def DeleteUser(codigo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET ESTADO = 'X' WHERE CODIGO = %s",
                    (codigo))
    conexion.commit()
    conexion.close()