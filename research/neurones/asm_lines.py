from lib.dlibcv import cv2, get_detected_faces


image = cv2.imread('faces/lena.jpg')
faces = get_detected_faces(image)

# Vérifier si un visage a été détecté
if len(faces) > 0:
    # Sélectionner le premier visage détecté
    face = faces[0]
    
    # Calcul des coordonnées du milieu du visage
    x_mid = (face.left() + face.right()) // 2
    y_mid = (face.top() + face.bottom()) // 2
    print("left", face.left())
    print("right", face.right())
    
    print("y_mid", y_mid)
    print("y_mid", y_mid)
    
    # Tracer une ligne verticale
    cv2.line(image, (x_mid, face.top()), (x_mid, face.bottom()), (5, 5, 5), 5)
    
    # Tracer une ligne horizontale
    cv2.line(image, (face.left(), y_mid), (face.right(), y_mid), (5, 5, 5), 5)
    
    
         
    # Save image
    cv2.imwrite("outputs/result6.jpg", image)

else:
    print("Aucun visage détecté dans l'image.")

