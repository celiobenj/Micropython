from machine import Pin
import network

# Configurações iniciais do WIFI
ssid = 'celio'
password = '12345678'

# Conectando no WIFI
station = network.WLAN(network.STA_IF) # Station Interface
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

# Conectado!
print('Conectado com sucesso!', station.ifconfig())
led = Pin(2, Pin.OUT)
led.on()
