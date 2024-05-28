class TarjetaCredito:
    instances = []  # Lista para rastrear las instancias creadas

    def __init__(self, limite_credito, intereses=0.02, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar
        TarjetaCredito.instances.append(self)  # Añadir la instancia a la lista de instancias
    
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
    
    def pago(self, monto):
        self.saldo_pagar -= monto
    
    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
    
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses

    @classmethod
    def imprimir_todas_las_tarjetas(cls):
        print("Información de todas las tarjetas:")
        for instance in cls.instances:
            print(f"Tarjeta - Límite de Crédito: ${instance.limite_credito}, Intereses: {instance.intereses}, Saldo a Pagar: ${instance.saldo_pagar}")

# Creación de las instancias de TarjetaCredito
tarjeta1 = TarjetaCredito(500)
tarjeta2 = TarjetaCredito(1000)
tarjeta3 = TarjetaCredito(300, intereses=0.03)

# Acciones para la primera tarjeta
tarjeta1.compra(200)
tarjeta1.compra(300)
tarjeta1.pago(100)
tarjeta1.cobrar_interes()
tarjeta1.mostrar_info_tarjeta()

# Acciones para la segunda tarjeta
tarjeta2.compra(150)
tarjeta2.compra(200)
tarjeta2.compra(300)
tarjeta2.pago(200)
tarjeta2.pago(150)
tarjeta2.cobrar_interes()
tarjeta2.mostrar_info_tarjeta()

# Acciones para la tercera tarjeta
tarjeta3.compra(100)
tarjeta3.compra(150)
tarjeta3.compra(200)
tarjeta3.compra(300)
tarjeta3.compra(100)
tarjeta3.mostrar_info_tarjeta()

# Impresión de la información de todas las tarjetas
TarjetaCredito.imprimir_todas_las_tarjetas()
