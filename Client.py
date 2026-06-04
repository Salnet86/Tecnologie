import socket
import subprocess

# 1. Creazione del socket (il telefono del client)
# AF_INET = usa indirizzi IP, SOCK_STREAM = usa il protocollo TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connessione al Server (bussa alla porta del server)
# Nota la doppia parentesi per passare IP e Porta come un pacchetto unico (tupla)
client.connect(("127.0.0.1", 12345))

# 3. Esecuzione del comando di sistema
# capture_output=True intercetta il risultato. .stdout prende il testo che è già in BYTE!
risultato = subprocess.run(["ls", "-l"], capture_output=True)

# 4. Invio dei dati nel tubo dello stream
# Non serve .encode() perché risultato.stdout restituisce già byte grezzi
client.sendall(risultato.stdout)

# 5. Ricezione dell'eventuale risposta dal server (massimo 1024 byte)
risposta_server = client.recv(1024)
print(f"Risposta dal server: {risposta_server.decode()}")

# 6. Chiusura del socket
client.close()
