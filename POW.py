import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty  # Nombre de zéros requis au début du hachage
        self.hash = self.compute_hash()

    def compute_hash(self):
        """Retourne le hachage SHA-256 du bloc."""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self):
        """Résout le problème de Proof of Work en trouvant un nonce tel que le hachage ait un certain nombre de zéros."""
        target = '0' * self.difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Crée le bloc génésis (premier bloc de la chaîne)."""
        genesis_block = Block(0, "0", "Genesis Block", 1)  # Difficulté 1 pour le bloc génésis
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, data, difficulty):
        """Ajoute un nouveau bloc à la chaîne après avoir résolu le Proof of Work."""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data, difficulty)
        start_time = time.time()
        new_block.proof_of_work()
        end_time = time.time()
        self.chain.append(new_block)
        print(f"Bloc ajouté avec une difficulté de {difficulty}. Temps d'exécution : {end_time - start_time:.2f} secondes.")

    def is_chain_valid(self):
        """Vérifie l'intégrité de la chaîne."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Vérifie que le hachage du bloc est correct
            if current.hash != current.compute_hash():
                return False
            # Vérifie que le bloc précédent correspond bien
            if current.previous_hash != previous.hash:
                return False
        return True

# Test de la blockchain et de Proof of Work avec des difficultés variables
blockchain = Blockchain()

# Ajouter 10 blocs avec des difficultés croissantes
for i in range(10):  # Ajouter 10 blocs
    difficulty = min(i + 1, 5)  # On limite la difficulté à 5
    blockchain.add_block(f"Transaction {i + 1} avec difficulté {difficulty}", difficulty)

# Vérifier l'intégrité de la blockchain
print(f"La chaîne est valide : {blockchain.is_chain_valid()}")
