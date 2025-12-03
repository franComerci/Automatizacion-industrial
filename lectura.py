#importar 
from pymodbus.client import ModbusTcpClient
import time
PLC = ModbusTcpClient('192.168.30.10')
PLC.connect()


try:
    while True:
        valorLeido = PLC.read_holding_registers(0)
        lectura = valorLeido[0]
        print(lectura)
        time.sleep(0.5)
except:
    PLC.close

