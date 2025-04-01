from pymodbus.client.sync import ModbusTcpClient
import paho.mqtt.client as mqtt
import time
import json

MODBUS_HOST = "localhost"
MODBUS_PORT = 5020

MQTT_BROKER = "test.mosquitto.org"  # Use your broker if self-hosted
MQTT_TOPIC = "shamim/factory/tank"

client_modbus = ModbusTcpClient(MODBUS_HOST, port=MODBUS_PORT)
client_mqtt = mqtt.Client()
client_mqtt.connect(MQTT_BROKER, 1883, 60)

while True:
    rr = client_modbus.read_holding_registers(0, 1, unit=0)

    if rr.isError():
        print("Modbus read error:", rr)
    else:
        tank_level = rr.registers[0]
        payload = {
            "tank_level": tank_level,
            "timestamp": time.time()
        }
        client_mqtt.publish(MQTT_TOPIC, json.dumps(payload))
        print("Published:", payload)

    time.sleep(5)
