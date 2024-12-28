
# README : Projet de Calibration et Appariement de Caractères

!

## Table des Matières
1. Description du Projet
2. Prérequis
3. Organisation des Fichiers
4. Instructions d'Utilisation
5. Auteurs
6. Licence

## Description du Projet
Ce projet implémente des techniques fondamentales de vision par ordinateur en utilisant Python et OpenCV. Il comprend trois parties principales :

1. Calibration des Caméras : Estimation des paramètres intrinsèques et extrinsèques d'une caméra à partir d'images d'un damier.
2.Correspondance des Caractères : Détection et appariement de points-clés entre deux images à l'aide de l'algorithme ORB et de Brute Force Matcher.
3. Carte de Profondeur : Génération d'une carte de profondeur à partir d'images stéréo.

---

## Prérequis

### Logiciels et Bibliothèques
- Python 3.7 ou plus récent
- OpenCV (4.5 ou plus récent)
- NumPy
- Matplotlib

### Installation des Dépendances
Pour installer les bibliothèques nécessaires, exécutez la commande suivante :

bash : 

pip install opencv-python numpy matplotlib

---

## Organisation des Fichiers

```
.
├── calibrage.py          # Script principal pour l'exécution des trois parties
├── Dataset Damier/       # Dossier contenant les images de damier pour la calibration
├──LICENCE                # Licence autorisant quiconque d'utiliser ce code
├── README.md             # Document de référence (ce fichier)
```

---

## Instructions d'Utilisation

### 1. **Calibration des Caméras**
- **Objectif** : Calculer la matrice de la caméra et les coefficients de distorsion à partir d'images d'un damier.
- **Exécution** :
  1. Placez les images de damier dans le dossier `Dataset Damier`.
  2. Spécifiez le chemin des images dans le script `calibrage.py`.
  3. Exécutez le script.
  4. Les résultats (matrice de la caméra et coefficients) seront affichés dans la console + fenetre .

- **Résultat attendu** :
  - Exemple de matrice de calibration :
    ```
    [[5.16807311e+06 0.00000000e+00 8.09526996e+02]
     [0.00000000e+00 5.59892318e+06 8.09519751e+02]
     [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
    ```

### 2. **Correspondance des Caractères**
- **Objectif** : Apparier les points-clés entre deux images à l'aide de l'algorithme ORB.
- **Exécution** :
  1. Spécifiez le chemin de deux images à comparer dans le script.
  2. Exécutez le script.
  3. Les appariements seront affichés dans une fenêtre.

- **Résultat attendu** :
  - Une image combinée montrant les 20 meilleurs appariements entre les deux images.

### 3. **Carte de Profondeur**
- **Objectif** : Générer une carte de profondeur à partir d'une paire d'images stéréo.
- **Exécution** :
  1. Spécifiez le chemin des images gauche et droite dans le script.
  2. Exécutez le script.
  3. La carte de profondeur sera affichée dans une fenêtre avec une barre de couleurs.

- **Résultat attendu** :
  - Une carte de profondeur en niveaux de gris, avec des zones claires indiquant une proximité plus grande.


---

## Auteurs
- **Nom** : AHMIM Céline
- **Contact** : celinea847@gmail.com

---

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

![Exemple Carte de Profondeur](https://via.placeholder.com/600x400?text=Carte+de+Profondeur)
