# Reconhecimento básico de gestos com controle de servo

import cv2
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyfirmata

# Configuração do Arduino e servo
board = pyfirmata.Arduino('COM19')
servo_pin = board.get_pin('d:2:s')
angulo = 90  # Ângulo inicial
incremento = 5  # Quanto aumentar/diminuir por gesto
servo_pin.write(angulo)

# Função para mover o servo
def mover_servo(novo_angulo):
    global angulo
    if 0 <= novo_angulo <= 180:
        angulo = novo_angulo
        servo_pin.write(angulo)
        print(f"Servo movido para {angulo}°")

# Configuração do reconhecedor de gestos
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')

def resultado_gesto(result, output_image, timestamp_ms):
    global angulo
    if result.gestures:
        gesto = result.gestures[0][0].category_name
        print(f"Gesto: {gesto}")
        
        if gesto == "Closed_Fist" and angulo + incremento <= 180:
            mover_servo(angulo + incremento)
        elif gesto == "Open_Palm" and angulo - incremento >= 0:
            mover_servo(angulo - incremento)

options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.LIVE_STREAM,
    result_callback=resultado_gesto
)

# Inicialização da câmera e reconhecedor
cam = cv2.VideoCapture(0)
reconhecedor = vision.GestureRecognizer.create_from_options(options)

print("Pressione 'q' para sair...")

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Espelho
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    timestamp = int(time.time() * 1000)
    reconhecedor.recognize_async(mp_image, timestamp)
    
    cv2.imshow('Controle de Servo por Gestos', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpeza
cam.release()
cv2.destroyAllWindows()
reconhecedor.close()