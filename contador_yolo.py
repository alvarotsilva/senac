# pip install ultralytics opencv-python numpy

import cv2
from ultralytics import YOLO

# Carrega o modelo YOLOv8 com rastreamento ativado
model = YOLO("yolov8n.pt")

# Inicializa vídeo
cap = cv2.VideoCapture("C:/Users/alvaro.tavares/PyCharmMiscProject/contador_objetos/exemplo1.mp4")

# Linha de contagem (metade da tela)
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
linha_y = altura // 2

# Set para IDs únicos já contados
ids_contados = set()
total_contado = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Executa detecção + rastreamento (track=True ativa o ByteTrack)
    resultados = model.track(frame, persist=True, verbose=False)

    if resultados[0].boxes.id is not None:
        boxes = resultados[0].boxes.xyxy.cpu().numpy()
        ids = resultados[0].boxes.id.cpu().numpy().astype(int)
        classes = resultados[0].boxes.cls.cpu().numpy().astype(int)

        for box, obj_id, classe in zip(boxes, ids, classes):
            x1, y1, x2, y2 = map(int, box)
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            nome_classe = model.names[classe]

            # Desenha a caixa
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            cv2.putText(frame, f"{nome_classe} ID:{obj_id}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # Contagem se cruzar linha e ainda não foi contado
            if (linha_y - 10) < cy < (linha_y + 10) and obj_id not in ids_contados:
                total_contado += 1
                ids_contados.add(obj_id)

    # Desenha linha de contagem
    cv2.line(frame, (0, linha_y), (largura, linha_y), (0, 255, 0), 2)

    # Mostra total
    cv2.putText(frame, f"Total: {total_contado}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

    cv2.imshow("Contador com Rastreamento", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
