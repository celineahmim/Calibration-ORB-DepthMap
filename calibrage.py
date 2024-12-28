import cv2
import numpy as np
import os

# Chemin vers le dossier contenant les images de damier
image_folder = "C:/Users/ProBook/Desktop/AA Calibrage/Dataset Damier"

# Vérifiez si le dossier existe
if not os.path.exists(image_folder):
    print(f"Dossier introuvable : {image_folder}")
    exit()

# Liste des fichiers d'image dans le dossier
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Vérifiez que des images sont disponibles
if not image_files:
    print(f"Aucune image trouvée dans le dossier : {image_folder}")
    exit()

print(f"Images trouvées : {image_files}")

# Paramètres de calibration
CHECKERBOARD = (6, 9)  # Taille du damier (adapter selon votre damier réel)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Points 3D dans le monde réel (z=0 pour un damier plat)
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# Listes pour stocker les points 3D et 2D
objpoints = []  # Points 3D
imgpoints = []  # Points 2D

# Dimensions de la fenêtre redimensionnée
window_width = 300
window_height = 300

# Parcourir toutes les images
for img_file in image_files:
    # Charger l'image
    img = cv2.imread(img_file)
    if img is None:
        print(f"Impossible de lire l'image : {img_file}")
        continue

    # Convertir en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Trouver les coins du damier
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objpoints.append(objp)
        refined_corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(refined_corners)

        # Afficher les coins détectés
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, refined_corners, ret)

        # Redimensionner l'image
        img_resized = cv2.resize(img, (window_width, window_height))

        # Centrer la fenêtre sur l'écran
        cv2.namedWindow("Coins détectés", cv2.WINDOW_NORMAL)
        screen_width = cv2.getWindowImageRect("Coins détectés")[2]
        screen_height = cv2.getWindowImageRect("Coins détectés")[3]
        cv2.moveWindow("Coins détectés", (screen_width - window_width) // 2, (screen_height - window_height) // 2)

        # Afficher l'image
        cv2.imshow("Coins détectés", img_resized)
        cv2.waitKey(500)
    else:
        print(f"Coins non détectés pour l'image : {img_file}")

cv2.destroyAllWindows()

# Calibration de la caméra
if objpoints and imgpoints:
    ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # Affichage des résultats
    print("Calibration réussie !")
    print("Matrice de la caméra :\n", camera_matrix)
    print("Coefficients de distorsion :\n", dist_coeffs)
else:
    print("Calibration échouée : pas assez de données pour calibrer la caméra.")


#Partie 2 

import cv2
import numpy as np

# Chemin des deux images à comparer
image1_path = "C:/Users/ProBook/Desktop/AA Calibrage/Dataset Damier/damier 1.png"
image2_path = "C:/Users/ProBook/Desktop/AA Calibrage/Dataset Damier/damier 2.png"

# Charger les images
img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
    print("Impossible de charger l'une des images.")
    exit()

# Détecteur ORB
orb = cv2.ORB_create()

# Détection des points clés et calcul des descripteurs
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Vérification de la détection
if descriptors1 is None or descriptors2 is None:
    print("Pas assez de descripteurs détectés.")
    exit()

# Brute Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Apparier les descripteurs
matches = bf.match(descriptors1, descriptors2)

# Trier les appariements par distance (plus petit = meilleur)
matches = sorted(matches, key=lambda x: x.distance)

# Dessiner les 20 meilleurs appariements
matched_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Redimensionner l'image pour un meilleur affichage
matched_img_resized = cv2.resize(matched_img, (800, 600))

# Afficher les appariements
cv2.imshow("Appariements des caractéristiques (20 meilleurs)", matched_img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Partie 3 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chemin des images stéréo (gauche et droite)
left_image_path = "C:/Users/ProBook/Desktop/AA Calibrage/Dataset Damier/damier 1.png"
right_image_path = "C:/Users/ProBook/Desktop/AA Calibrage/Dataset Damier/damier 2.png"

# Charger les images gauche et droite
img_left = cv2.imread(left_image_path, cv2.IMREAD_GRAYSCALE)
img_right = cv2.imread(right_image_path, cv2.IMREAD_GRAYSCALE)

if img_left is None or img_right is None:
    print("Impossible de charger les images stéréo.")
    exit()

# Assurez-vous que les deux images ont la même taille
height, width = img_left.shape[:2]
img_right = cv2.resize(img_right, (width, height))

# Configurer l'algorithme StereoBM
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# Calculer la disparité
disparity = stereo.compute(img_left, img_right)

# Normaliser les valeurs de la disparité pour une meilleure visualisation
disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Afficher la carte de profondeur
plt.imshow(disparity_normalized, cmap='gray')
plt.colorbar()
plt.title("Carte de Profondeur")
plt.show()
