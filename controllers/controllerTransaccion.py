from backend.clasesDAO import transaccion_dao

def crear_transaccion(transaccion):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    return transaccionDao.create(transaccion)

def listar_transacciones(inversor):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    transacciones_x_inversor = transaccionDao.get_by_fk(inversor)
    if transacciones_x_inversor:
        for x in transacciones_x_inversor:
            print(x)
            print("\n")
    else:
        print("El usuario no tiene historial")
    return inversor

def listar_transacciones(inversor):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    transacciones_x_inversor = transaccionDao.get_by_fk(inversor)
    
    if transacciones_x_inversor:
        for x in transacciones_x_inversor:
            print(x)
            print("\n")
    else:
        print("El usuario no tiene historial")
    
    return transacciones_x_inversor  # Retornar la lista de transacciones

def listar_compras(inversor):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    transacciones_x_inversor = transaccionDao.get_by_fk(inversor)
    
    if transacciones_x_inversor:
        # Imprimir cada transacción y extraer precios
        total = -1
        
        for compra in transacciones_x_inversor:
            if int(compra.get_tipo_transaccion_id_tipo_transaccion()) == 1:
                print(mostrar_compras(compra))  # Usar mostrar_compras para cada compra
                print("\n")
                total += compra.get_precio()  # Sumar el precio de las compras    
                
    calculo_rendimiento(total)    
    return transacciones_x_inversor  # Retorna solo las compras

def calculo_rendimiento(total):

    if total > -1:
        print(f"\nEl total de acciones compradas es de: {total}") 

        porcentajeAumento = total * 0.15 # Aumento del 15% de las transacciones
        accionesValorActual = total + porcentajeAumento
        rendimiento = (accionesValorActual-total)/total*100
        print(f"\nTus acciones valen ahora: {accionesValorActual}") 
        print(f"\nTus acciones generaron una Ganancia Neta de: {rendimiento:.2f} %")
        print("\n")
    else:
        print("El usuario no tiene compras")

    return total

def mostrar_compras(compra):
    return (f'Número de transacción: {compra.get_id_transaccion()}, '
            f'Fecha: {compra.get_fecha_hora()}, '
            f'Cantidad: {compra.get_cantidad_acciones()}, '
            f'Precio: {compra.get_precio()}, '
            f'Acción: {compra.get_accion_id_accion().get_simbolo()}, '
            f'ID Transacción: {compra.get_tipo_transaccion_id_tipo_transaccion()}')



    
    


