from block import Block
from blockchain import Blockchain

# Crear blockchain
blockchain = Blockchain()

# Añadir nuevos bloques con transacciones
transacciones_1 = ["Alice envía 5 a Bob", "Bob envía 3 a Charlie"]
transacciones_2 = ["Charlie envía 2 a Alice", "Alice envía 1 a Bob"]

print("--")

b1 = Block(blockchain.obtener_ultimo_bloque().hash, transacciones_1)
blockchain.agregar_bloque(b1)

b2 = Block(blockchain.obtener_ultimo_bloque().hash, transacciones_2)
blockchain.agregar_bloque(b2)

print("--")
# Verificar la validez de la cadena
print("Cadena válida:", blockchain.es_cadena_valida())

print("--")
# Mostrar la información de la cadena
for i, block in enumerate(blockchain.cadena):
    print(f"--- Bloque {i} ---")
    print(f"Hash: {block.hash}")
    print(f"Hash previo: {block.hash_previo}")
    print(f"Datos: {block.datos}")
    print(f"Nonce: {block.nonce}")
    print(f"Timestamp: {block.marca_tiempo}")
