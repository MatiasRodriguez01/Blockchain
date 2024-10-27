from block import Block

class Blockchain:
    def __init__(self, dificultad=4):
        self.cadena = [self.crear_bloque_genesis()]  # Crear el primer bloque (génesis)
        self.dificultad = dificultad  # Dificultad de la minería

    def crear_bloque_genesis(self):
        """Crea el bloque génesis (primer bloque de la cadena)."""
        return Block("0" * 64, "Bloque génesis")

    def obtener_ultimo_bloque(self):
        """Devuelve el último bloque de la cadena."""
        return self.cadena[-1]

    def agregar_bloque(self, nuevo_bloque):
        """Añade un nuevo bloque a la cadena después de minarlo."""
        nuevo_bloque.hash_previo = self.obtener_ultimo_bloque().hash
        nuevo_bloque.minar_bloque(self.dificultad)
        self.cadena.append(nuevo_bloque)

    def es_cadena_valida(self):
        """Verifica si la cadena de bloques es válida."""
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]

            # Verificar si el hash del bloque actual es correcto
            if bloque_actual.hash != bloque_actual.calcular_hash():
                print(f"Hash inválido en el bloque {i}")
                return False
            
            # Verificar si el hash previo es correcto
            if bloque_actual.hash_previo != bloque_anterior.hash:
                print(f"Hash previo incorrecto en el bloque {i}")
                return False
        
        return True
