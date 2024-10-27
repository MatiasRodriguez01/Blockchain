from hashlib import sha256
from time import time

class Block:
    def __init__(self, hash_previo, datos, marca_tiempo=None):
        self.hash_previo = hash_previo  # Hash del bloque anterior
        self.datos = datos  # Información del bloque (transacciones)
        self.marca_tiempo = marca_tiempo or time()  # Marca de tiempo del bloque
        self.nonce = 0  # Número aleatorio para la minería
        self.hash = self.calcular_hash()  # Hash calculado del bloque

    def calcular_hash(self):
        """Calcula el hash del bloque."""
        informacion = f"{self.hash_previo}{self.datos}{self.marca_tiempo}{self.nonce}"
        return sha256(informacion.encode()).hexdigest()

    def minar_bloque(self, dificultad):
        """Minar el bloque ajustando el nonce hasta encontrar un hash válido."""
        while not self.hash.startswith("0" * dificultad):
            self.nonce += 1
            self.hash = self.calcular_hash()
        print(f"Bloque minado: {self.hash} con nonce {self.nonce}")
