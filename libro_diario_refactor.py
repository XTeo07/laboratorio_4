class LibroDiario:
    ''' Agrega transacciones y calcula el total de ingresos y egresos'''

    def __init__(self):
        ''' Constructor de la clase'''
        self.transacciones = []

    def agregar(self, fecha, descripcion, monto, tipo):
        ''' Función para registrar los datos de la transacción'''

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def resumen(self):
        ''' Calcula total ingreso y egresos'''
        ingresos = 0
        egresos = 0
        for t in self.transacciones:
            if t["tipo"] == "ingreso":
                ingresos += t["monto"]
            else:
                egresos += t["monto"]
        return "Total ingresos: " + str(ingresos) + " Total egresos: " + str(egresos)
