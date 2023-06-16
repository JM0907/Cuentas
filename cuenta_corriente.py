#Murillo Santos Joseph Loenardo

from Cuentas import Cuentas

class CuentaCorriente(Cuentas):
    def __init__(self, numero, nombre_propietario, saldo, tiene_chequera):
        super().__init__(numero, nombre_propietario, saldo)
        self.tiene_chequera = tiene_chequera

    @property
    def tiene_chequera(self):
        return self._tiene_chequera

    @tiene_chequera.setter
    def tiene_chequera(self, tiene_chequera):
        self._tiene_chequera = tiene_chequera

    def pagar_cheque(self, valor):
        if self.tiene_chequera:
            self.debito(valor)
        else:
            print("No se puede pagar el cheque. Cuenta sin chequera.")

    def mostrar_cuenta(self):
        print("Cuenta Corriente:")
        print("Número de cuenta:", self.numero)
        print("Propietario:", self.nombre_propietario)
        self.mostrar_saldo()
print("_______________________________________")
cuenta_corriente = CuentaCorriente("1524875678", "Maria Murillo", 250.0, True)
cuenta_corriente.mostrar_cuenta()
cuenta_corriente.credito(20.0)
cuenta_corriente.debito(40.0)
cuenta_corriente.mostrar_cuenta()
cuenta_corriente.pagar_cheque(18.0)
cuenta_corriente.mostrar_cuenta()
print("_______________________________________")

