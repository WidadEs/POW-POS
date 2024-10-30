# POW-POS
# POW (Proof Of Work )
## Structure du Code

### Classes

1. **Block**
   - Représente un bloc individuel dans la blockchain.
   - **Attributs** :
     - `index`: L'indice du bloc dans la chaîne.
     - `previous_hash`: Le hachage du bloc précédent.
     - `data`: Les données du bloc (ex. transactions).
     - `timestamp`: Le moment où le bloc a été créé.
     - `nonce`: Un nombre utilisé pour la preuve de travail.
     - `difficulty`: Le niveau de difficulté pour le minage du bloc.
     - `hash`: Le hachage du bloc.
   - **Méthodes** :
     - `compute_hash()`: Calcule le hachage SHA-256 du bloc.
     - `proof_of_work()`: Résout le problème de Proof of Work en trouvant un nonce tel que le hachage commence par un certain nombre de zéros.

2. **Blockchain**
   - Représente la chaîne de blocs.
   - **Attributs** :
     - `chain`: Une liste de blocs dans la chaîne.
   - **Méthodes** :
     - `create_genesis_block()`: Crée le bloc génésis.
     - `add_block(data, difficulty)`: Ajoute un nouveau bloc à la chaîne après avoir résolu le Proof of Work.
     - `is_chain_valid()`: Vérifie l'intégrité de la chaîne de blocs.


# POS (Proof Of Stake )
## Structure du Code

### Classes

1. **Block**
   - Représente un bloc individuel dans la blockchain.
   - **Attributs** :
     - `index`: L'indice du bloc dans la chaîne.
     - `previous_hash`: Le hachage du bloc précédent.
     - `data`: Les données du bloc (ex. transactions).
     - `timestamp`: Le moment où le bloc a été créé.
     - `validator`: Le validateur qui a validé ce bloc.
     - `hash`: Le hachage du bloc.
   - **Méthodes** :
     - `compute_hash()`: Calcule le hachage SHA-256 du bloc.

2. **Blockchain**
   - Représente la chaîne de blocs.
   - **Attributs** :
     - `chain`: Une liste de blocs dans la chaîne.
     - `validators_stakes`: Un dictionnaire contenant les validateurs et leurs mises respectives.
   - **Méthodes** :
     - `create_genesis_block()`: Crée le bloc génésis.
     - `select_validator()`: Sélectionne un validateur en fonction de sa mise.
     - `add_block(data)`: Ajoute un nouveau bloc à la chaîne avec Proof of Stake.
     - `is_chain_valid()`: Vérifie l'intégrité de la chaîne de blocs.
# Comparaison 
## Temps d'exécution des blocs
-Pour POW les temps d'exécution des blocs augmentent avec la difficulté. Par exemple, le temps pour un bloc avec une difficulté de 5 était de 4.11 secondes et a atteint jusqu'à 8.18 secondes pour d'autres blocs.
-Pour POS Les temps d'exécution sont très constants et rapides, tous autour de 0.002 à 0.003 secondes, indépendamment du nombre de blocs ajoutés.
## Difficulté
-Pour POW la difficulté a un impact significatif sur le temps d'exécution, augmentant les délais de validation avec des valeurs de difficulté plus élevées.
-Pour POS Aucune notion de difficulté variable, le processus est rapide et prévisible, ce qui permet des validations plus fréquentes.
## Scalabilité
-Pour POW Moins scalable en raison de la montée des temps d'exécution avec l'augmentation de la difficulté, ce qui peut affecter le nombre de transactions traitées par seconde.
-Pour POS très scalable grâce à des temps de validation rapides, permettant un plus grand nombre de transactions traitées.
