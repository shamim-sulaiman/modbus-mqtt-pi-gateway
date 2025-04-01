from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification
from threading import Thread
import time
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Initial tank level
tank_level = 0

# Create the Modbus data store
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),  # Holding registers
    ir=ModbusSequentialDataBlock(0, [0]*100)
)
context = ModbusServerContext(slaves=store, single=True)

# Function to simulate tank filling
def simulate_tank():
    global tank_level
    while True:
        if tank_level < 100:
            tank_level += 5
        else:
            tank_level = 0  # Reset when full

        # Write tank_level to holding register 0
        context[0].setValues(3, 0, [tank_level])
        print(f"Simulated tank level: {tank_level}")
        time.sleep(5)  # update every 5 seconds

# Start tank simulation in a separate thread
sim_thread = Thread(target=simulate_tank)
sim_thread.daemon = True
sim_thread.start()

# Modbus server identity info
identity = ModbusDeviceIdentification()
identity.VendorName = 'ShamimTech'
identity.ProductCode = 'TANKSIM'
identity.VendorUrl = 'http://shamimsulaiman.com'
identity.ProductName = 'Tank Level Simulator'
identity.ModelName = 'PiZero'
identity.MajorMinorRevision = '1.0'

StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))
