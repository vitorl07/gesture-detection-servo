# gesture-detection-servo
Detecção de gestos para mover um Servo Motor

Esse projeto é apenas um teste para mover um Servo Motor com um Arduino e usando metodos da Visão Computacional.

Para usar esse projeto será necessário um Servo Motor conectado ao Arduino Uno, dessa maneira:
<img width="1366" height="564" alt="stunning_borwo-elzing_1AxSYIVIKv" src="https://github.com/user-attachments/assets/f9cd622c-77d1-46e1-a8fe-428af33a61f0" />

OBS: Utilizei o pino digital 2 para esse projeto!

Após ser conectado será necessário a instalação das bibliotecas Pyfirmata, Mediapipe e OpenCV. Para instalar o Pyfirmata e o Mediapipe se utiliza o comando:

pip install pyfirmata
pip install mediapipe

Para o OpenCV recomendo a instalação pelo site: https://opencv.org/releases/

Após a Instalação das 3 bibliotecas e na conexão do circuito você pode inicializar o main.py. Os gestos para controlar o Servo Motor é a Mão Fechada e a Mão Aberta, aonde cada gesto consegue mover até 180° graus.

Fique a vontade para utilizar o codigo nesse projeto.

Referências:
https://www.instructables.com/Control-Your-Arduino-With-Pythons-Pyfirmata-Librar/
https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/
https://docs.arduino.cc/libraries/servo/
https://pypi.org/project/pyFirmata/
https://ai.google.dev/edge/mediapipe/solutions/guide?hl=pt-br
