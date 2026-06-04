import socket

# 1. Creazione del socket del Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind: Incolla il socket a un IP e a una Porta specifica di questa macchina
# "0.0.0.0" significa che accetta connessioni da qualsiasi scheda di rete
server.bind(("0.0.0.0", 12345))

# 3. Listen: Mette il server in modalità ascolto (linea libera)
# Il numero 5 indica la coda massima di client in attesa
server.listen(5)
print("Server in ascolto sulla porta 12345...")

# 4. Accept: Alza la cornetta quando un client bussa.
# Blocca il programma finché non si connette qualcuno e crea il canale privato 'conn'
conn, indirizzo = server.accept()
print(f"Client connesso con successo da: {indirizzo}")

# 5. Ciclo continuo per svuotare il flusso (stream) dei dati
while True:
    # Prende un blocco di massimo 1024 byte dal canale privato
    data = conn.recv(1024)
    
    # Se not data è vero (cioè se il tubo è vuoto perché il client ha chiuso)
    if not data:
        # Interrompe il ciclo e non spedisce nulla
        break
        
    # Se invece ci sono dati, li rispedisce identici al client
    conn.sendall(data)

# 6. Pulizia finale: chiude prima il canale privato e poi il server generale
conn.close()
server.close()
print("Connessione chiusa ordinatamente.")
