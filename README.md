# 🎯 Contador de Objetos com YOLOv8 e ByteTrack

Este projeto implementa um contador de objetos em tempo real usando **YOLOv8** com **rastreamento ByteTrack** e **OpenCV**. Ideal para aplicações como análise de fluxo de pessoas, veículos ou qualquer objeto detectável.

---

## 📦 Funcionalidades

✅ Detecção de objetos com YOLOv8  
✅ Rastreamento robusto com ByteTrack  
✅ Contagem apenas de objetos únicos (evita duplicações)  
✅ Processamento de arquivos `.mp4`  
✅ Visualização em tempo real com OpenCV  

---

## 🛠️ Requisitos

- Python 3.8+
- pip

### Instalação das dependências:

```bash
pip install ultralytics opencv-python
```

---

## 📁 Estrutura do Projeto

```
contador_objetos/
├── video.mp4            # Vídeo de entrada
├── contador_yolo.py     # Script principal
├── README.md            # Este arquivo
```

---

## ▶️ Como usar

1. Coloque seu vídeo `.mp4` no diretório.
2. Execute o script:

```bash
python contador_yolo.py
```

3. Pressione `ESC` para encerrar a execução.

---

## 🧠 Como funciona

- O YOLOv8 realiza a detecção de objetos em cada frame.
- O ByteTrack atribui um ID único a cada objeto rastreado.
- O script conta quantos IDs distintos cruzam uma **linha virtual** desenhada na tela.
- Apenas objetos que cruzam a linha uma vez são contados.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
