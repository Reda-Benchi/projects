@author: Reda Benhci (https://github.com/Reda-Benchi/projects/tree/main/algorithmicTrading)

# IBKR connection
1. IBKR uses a TCP WebSocket connection.
2. Once the connection is established, the IBKR server pushes data to the client as soon as it becomes available.
3. Note: Although HTTP is generally recommended for logging due to security reasons, IBKR does not use it; all interactions occur over the TCP WebSocket connection.
4. The system can handle up to 36 indicators, keep this limitation in mind.

# HTTP arcitechture: 
client pushes data and pulls data from server, therafter the connection is closed.
# Websocket architecture: 
client opens a connection, server pushes data to client, and the connection remains open for further communication.