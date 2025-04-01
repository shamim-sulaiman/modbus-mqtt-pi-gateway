from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [50]*100),  # Register 100 has "tank level = 50"
    ir=ModbusSequentialDataBlock(0, [0]*100))
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'ShamimTest'
identity.ProductCode = 'MTQ'
identity.VendorUrl = 'http://example.com'
identity.ProductName = 'Modbus2MQTT Simulator'
identity.ModelName = 'RasPiZero'
identity.MajorMinorRevision = '1.0'

StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))
