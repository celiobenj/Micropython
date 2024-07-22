import socket
import ujson
from Led import Led
from html import html

# Instancia o objeto led
led = Led(33, 25, 26)
led.off()
r, g, b = (0, 0, 0)

# Inicia o servidor WEB - TCP/IP Protocol (IPv4)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print('Aguardando conexões...')

# Página HTML no arquivo html.py
html = html.page()

# Loop infinito
while (True):
    # "conn" is a new socket object usable to send and receive data on the connection, and "address" is the address bound to the socket on the other end of the connection
    conn, address = s.accept() # Handshake
    print('Cliente conectado de', address)
    
    # Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize. A returned empty bytes object indicates that the client has disconnected
    request = str(conn.recv(2**10))
    
    if 'GET / ' in request:
        # Send data (no caso, o próprio html) to the socket. The socket must be connected to a remote socket (no caso, "conn")
        conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        conn.send(html)
        
    elif 'POST /result' in request:
        body = str("{"+request.split('{')[-1]).split('\'')[0]
        data = ujson.loads(body) # Cria um dicionário JSON
        type = data['type'] # Qual dos dados foi enviado (update_color, cicle, transition)
            
        if type == 'update_color':
            r = int(data['r']) * 4
            g = int(data['g']) * 4
            b = int(data['b']) * 4
            led.rgb(r, g, b)
        
        elif type == 'cicle':
            preset = int(data['preset'])
            if preset in {1, 2, 3}: 
                led.cicle(preset)
                led.off()
                continue
            delay = int(data['delay'])
            loop = 1
            hex_list = data['hex_list'].split(chr(0x5C)+'n')
            led.cicle(preset, delay, loop, hex_list)
            led.off()
            
        
        elif type == 'transition':
            delay = int(data['delay'])
            led.transition(delay)
            led.off()
            
        
        conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n')
        conn.send(ujson.dumps({'status': 'success'}))

    # Mark the socket closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).
    conn.close()
