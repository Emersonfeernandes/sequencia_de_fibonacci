def fibonacci_(var):
    var1 = 0
    var2 = 1
    sequencia = []
    i = 1
    if var == 0:
        return 'Não possivel realizar essa Operação, pois o valor foi 0'
    else:
        while i <= var:
            sequencia.append(var1)
            var1, var2 = var2, var1 + var2
            i += 1
    return sequencia
