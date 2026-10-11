import socket


def test_ssh_port_open():
  # Indirizzo IPv4 della VM s1
  host = "192.168.200.128"

  # Porta TCP 22: servizio SSH
  port = 22

  # Crea un socket IPv4 che utilizza TCP
  # 'with' garantisce la chiusura del socket al termine
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Imposta un timeout massimo di 3 secondi
    sock.settimeout(3)

    # Tenta di stabilire una connessione TCP
    # connect_ex() restituisce 0 se la connessione riesce
    result = sock.connect_ex((host, port))

  # Verifica che la connessione sia riuscita
  # Se result è diverso da 0, pytest segnala il test come FAILED
  assert result == 0, f"Porta TCP {port} non raggiungibile su {host}"