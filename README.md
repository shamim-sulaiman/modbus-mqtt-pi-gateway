# Raspberry Pi Modbus to MQTT Gateway

This project simulates an industrial Modbus device (like a PLC) using Python on a Raspberry Pi Zero, and publishes the data to an MQTT broker.

## Features
- Modbus TCP server simulation (`modbus_slave.py`)
- MQTT publisher gateway (`modbus_to_mqtt.py`)
- Raspberry Pi Zero compatible
- Python 3 based, minimal dependencies
- Tested with public broker: `test.mosquitto.org`
- Future: Dashboard, tank simulation, and alarm logic

## Folder Structure
- `modbus_slave.py` - Modbus TCP server
- `modbus_to_mqtt.py` - Reads Modbus register, sends MQTT
