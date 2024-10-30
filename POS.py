import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, data, validator):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator
        self.hash = self.compute_hash()

    def compute_hash(self):
        """Retourne le hachage SHA-256 du bloc."""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.validator}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self, validators_stakes):
        self.chain = []
        self.validators_stakes = validators_stakes
        self.create_genesis_block()

    def create_genesis_block(self):
        """Crée le bloc génésis."""
        genesis_block = Block(0, "0", "Genesis Block", validator="Genesis Validator")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def select_validator(self):
        """Sélectionne un validateur en fonction de sa mise."""
        total_stake = sum(self.validators_stakes.values())
        selection_point = random.uniform(0, total_stake)
        current_sum = 0

        for validator, stake in self.validators_stakes.items():
            current_sum += stake
            if current_sum >= selection_point:
                return validator

    def add_block(self, data):
        """Ajoute un nouveau bloc à la chaîne avec Proof of Stake."""
        previous_block = self.chain[-1]
        validator = self.select_validator()
        new_block = Block(len(self.chain), previous_block.hash, data, validator)

        start_time = time.time()

        # Simuler une charge de travail pour rendre le temps d'exécution mesurable
        for _ in range(100000):  # Boucle pour simuler du travail
            pass  # Ne rien faire, juste pour le temps

        new_block.hash = new_block.compute_hash()
        end_time = time.time()

        self.chain.append(new_block)
        print(f"Bloc validé par {validator}. Temps d'exécution : {end_time - start_time:.6f} secondes.")

    def is_chain_valid(self):
        """Vérifie l'intégrité de la chaîne."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# Définition des validateurs avec leurs mises
validators_stakes = {
    'Validator1': 50,
    'Validator2': 30,
    'Validator3': 20
}

# Test de la blockchain avec Proof of Stake
blockchain = Blockchain(validators_stakes)

# Ajouter plusieurs blocs et mesurer le temps d'exécution
for i in range(1, 11):  # Ajouter 10 blocs
    blockchain.add_block(f"Transaction {i}")

# Vérifier l'intégrité de la blockchain
print(f"La chaîne est valide : {blockchain.is_chain_valid()}")
