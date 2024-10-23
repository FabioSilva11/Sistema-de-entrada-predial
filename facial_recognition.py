import cv2
import face_recognition

# Carrega imagens de pessoas autorizadas
authorized_image = face_recognition.load_image_file("pessoa_autorizada.jpg")
authorized_encoding = face_recognition.face_encodings(authorized_image)[0]

# Inicia a captura da câmera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Converte BGR para RGB
    
    # Localiza rostos na imagem
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding in face_encodings:
        # Compara rostos
        matches = face_recognition.compare_faces([authorized_encoding], face_encoding)
        
        if True in matches:
            print("Acesso liberado")
        else:
            print("Acesso negado")
    
    # Mostra o feed da câmera
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera
video_capture.release()
cv2.destroyAllWindows()