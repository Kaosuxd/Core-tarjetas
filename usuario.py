from tarjeta_credito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = []  # Lista para almacenar múltiples tarjetas de crédito

    def agregar_tarjeta(self, limite_credito, intereses=0.02):
        nueva_tarjeta = TarjetaCredito(limite_credito, intereses)
        self.tarjetas.append(nueva_tarjeta)

    def hacer_compra(self, tarjeta_index, monto):
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].compra(monto)
        else:
            print("Índice de tarjeta no válido.")

    def pagar_tarjeta(self, tarjeta_index, monto):
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].pago(monto)
        else:
            print("Índice de tarjeta no válido.")

    def mostrar_saldo_usuario(self):
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta {i+1}:")
            tarjeta.mostrar_info_tarjeta()

# Ejemplo de uso
usuario1 = Usuario("Juan", "Pérez", "juan.perez@example.com")

# Agregar tarjetas
usuario1.agregar_tarjeta(20000, intereses=0.015)
usuario1.agregar_tarjeta(15000, intereses=0.02)

# Realizar operaciones
usuario1.hacer_compra(0, 5000)
usuario1.hacer_compra(1, 3000)
usuario1.pagar_tarjeta(0, 2000)
usuario1.mostrar_saldo_usuario()
