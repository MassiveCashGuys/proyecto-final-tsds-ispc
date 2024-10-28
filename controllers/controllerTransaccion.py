from backend.clasesDAO import transaccion_dao

def crear_transaccion(transaccion):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    return transaccionDao.create(transaccion)

def listar_transacciones(inversor):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    transacciones_x_inversor = transaccionDao.get_by_fk(inversor)
    
    if transacciones_x_inversor:
      
        total = -1
        index = 1 
        
        for compra in transacciones_x_inversor:
            if int(compra.get_tipo_transaccion_id_tipo_transaccion().get_id_tipo_transaccion()) == 1:
                print(f"{index}-{mostrar_transaccion(compra)}")
                print() 
                total += compra.get_precio()  
                index += 1   
                
        calculo_rendimiento(total)    
    else:
        print("El usuario no tiene historial")
    
    return transacciones_x_inversor  


def calculo_rendimiento(total):

    if total > -1:
        print(f"\nEl total de acciones compradas es de: {total}") 

        porcentajeAumento = total * 0.15 
        accionesValorActual = total + porcentajeAumento
        rendimiento = (accionesValorActual-total)/total*100
        print(f"\nTus acciones valen ahora: {accionesValorActual}") 
        print(f"\nTus acciones generaron una Ganancia Neta de: {rendimiento:.2f} %")
        print("\n")
    else:
        print(f'El usuario no tiene compras')

    return total

def mostrar_transaccion(transaccion):
    return (f'Número de transacción: {transaccion.get_id_transaccion()}, '
            f'Fecha: {transaccion.get_fecha_hora()}, '
            f'Cantidad: {transaccion.get_cantidad_acciones()}, '
            f'Precio: {transaccion.get_precio()}, '
            f'Acción de: {transaccion.get_accion_id_accion().get_nombre()}, '
            f'Transacción: {transaccion.get_tipo_transaccion_id_tipo_transaccion().get_nombre()}')



    
    


