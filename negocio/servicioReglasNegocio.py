import bcrypt
def crear_encriptacion_password(password):
    salt = bcrypt.gensalt()
    print(salt)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed)
    return hashed

def validar_password(password_has,pas):
    return bcrypt.checkpw(pas.encode('utf-8'),password_has)