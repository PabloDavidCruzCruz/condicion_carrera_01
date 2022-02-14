import threading
import time

class Compra():
    def __init__(self, turno = 0):
        self.locked = threading.Lock()
        self.turn_send = turno
        
    def cliente(self):
        self.locked.acquire()
        
        try:
            self.turn_send += 1
            print('Bienvenido a tienda online')
            print('Cliente: ',self.turn_send)
            print('Tiempo de espera para finalizar compra 5 minutos')
            print('Gracias')
            time.sleep(10)
        finally:
            self.locked.release()
            
def solicitar(x):
    
    for y in range(2):
        x.cliente()
        
        
if __name__ == '__main__':
    compra = Compra()
    for y in range(2):
        tstart = threading.Thread(target=solicitar, args=(compra,))
        tstart.start()