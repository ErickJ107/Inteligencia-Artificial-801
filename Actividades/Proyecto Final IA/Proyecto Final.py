import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
import time

etiquetas_espanol = {
    "person": "Humano",
    "chair": "silla",
    "desk": "escritorio",
    "table": "mesa",
    "board": "pizarrón",
    "blackboard": "pizarrón negro",
    "whiteboard": "pizarrón blanco",
    "marker": "marcador",
    "pen": "pluma",
    "pencil": "lápiz",
    "eraser": "borrador",
    "notebook": "cuaderno",
    "book": "libro",
    "backpack": "mochila",
    "laptop": "laptop",
    "computer": "computadora",
    "mouse": "Ratón",
    "keyboard": "teclado",
    "projector": "proyector",
    "screen": "pantalla",
    "clock": "reloj",
    "ruler": "regla",
    "calculator": "calculadora",
    "scissors": "tijeras",
    "stapler": "engrapadora",
    "paper": "hoja de papel",
    "folder": "carpeta",
    "glue": "pegamento",
    "highlighter": "resaltador",
    "speaker": "bocina",
    "microphone": "micrófono",
    "fan": "ventilador",
    "trash bin": "bote de basura",
    "door": "puerta",
    "window": "ventana",
    "curtain": "cortina",
    "lamp": "lámpara",
    "air conditioner": "aire acondicionado",
    "heater": "calefactor",
    "student": "estudiante",
    "teacher": "maestro",
    "schoolbag": "bolsa escolar",
    "remote": "Control remoto",
    "dog": "Perro",
    "cat": "Gato",
    "cell phone": "Celular pedorro",
    "tv": "Pantalla",
    "frisbee": "Platillo volador no identificado",
    "teddy bear": "Oso de peluche",
    "sports ball": "Pelota",
    "traffic light": "Semaforo",
    "umbrella": "Sombrilla",
    "train": "Tren",
    "surfboard": "Tabla de surf",
    "bird": "Pajaro"
}

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

detections_list = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]
            label_es = etiquetas_espanol.get(label, label)

            detections_list.append([label_es, conf, x1, y1, x2, y2, time.time()])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label_es}: {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detección de Objetos", frame)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

df = pd.DataFrame(detections_list, columns=["Objeto", "Confianza", "X1", "Y1", "X2", "Y2", "Tiempo"])

df.to_csv("Objetos detectados.csv", index=False)

print("\nResumen de detecciones:")
print(df.groupby("Objeto").agg({"Confianza": ["count", "mean"]}))

cap.release()
cv2.destroyAllWindows()
