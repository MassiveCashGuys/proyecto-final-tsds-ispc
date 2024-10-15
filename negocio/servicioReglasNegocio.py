import bcrypt


def crear_encriptacion_password(password):
    salt = bcrypt.gensalt()
    print(salt)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed)
    return hashed


def validar_password(password_has, pas):
    return bcrypt.checkpw(pas.encode('utf-8'), password_has)


def asignar_saldo_inicial(self, idporfolio):
    if connection:
        try:
            cursor = connection.cursor()

            sql = "update portafolio set saldo_actual = %s where id_portafolio= %s"
            values = (1000000, self.__id_portafolio)
            cursor.execute(sql, valores)

            connection.commit()

            cursor.close()
            connection.close()
            return True

        except Exception as e:
            # print(f"Error:{e}")
            return False
    else:
        return "No se pudo conectar a la db"
