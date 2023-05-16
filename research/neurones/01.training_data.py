import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
from PIL import Image

# Chargement des données d'entraînement (à adapter en fonction de votre cas)
train_image_paths = ["image.jpg", "image2.jpg"]
train_images = [] # Vos images d'entraînement
for image_path in train_image_paths:
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Redimensionner les images si nécessaire
    image = np.array(image)
    train_images.append(image)
train_images = np.array(train_images)

# Chargement des étiquettes (mesures d'asymétrie)
train_labels = np.array([0.8, 0.2])  # Exemple de valeurs d'asymétrie correspondantes



test_image_path = "image2.jpg"  # Chemin vers votre image de test
image = Image.open(test_image_path)
image = image.resize((224, 224))  # Redimensionner l'image si nécessaire
test_image = np.array(image)
test_image = np.expand_dims(test_image, axis=0)  # Ajouter une dimension de lot (batch dimension)


 
# Création du modèle
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilation du modèle
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Entraînement du modèle
model.fit(train_images, train_labels, epochs=10, batch_size=32)



test_image_path = "image2.jpg"  # Chemin vers votre image de test
image = Image.open(test_image_path)
image = image.resize((224, 224))  # Redimensionner l'image si nécessaire
test_image = np.array(image)
test_image = np.expand_dims(test_image, axis=0)  # Ajouter une dimension de lot (batch dimension)
# Prédiction sur une image de test
predicted_asymmetry = model.predict(test_image)

# Affichage du résultat
print("Asymmetry score:", predicted_asymmetry)