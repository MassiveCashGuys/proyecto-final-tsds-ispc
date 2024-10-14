def validar_cuit(cuit):
    # Verificar que la longitud sea exactamente 11 y que sean solo dígitos
    return len(cuit) == 11 and cuit.isdigit()