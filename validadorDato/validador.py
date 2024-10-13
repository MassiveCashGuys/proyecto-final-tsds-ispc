       
def  is_number(numero):
     try:
        if isinstance(numero, int):
          return int(numero)
        else:
          return float(numero)   
     except ValueError :
        print(f"Error: '{numero}' no es un número válido.")
        return None