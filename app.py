import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO

# 1. Configuração da página do Streamlit
st.set_page_config(
    page_title="Scanner com Yolo",
    layout="centered"
)

st.title("Scanner com YOLO")
st.write("Abra a câmera para iniciar a detecção de objetos em tempo real.")

# 2. Carregamento do modelo YOLO (utilizando cache para otimizar o desempenho)
@st.cache_resource
def load_yolo_model():
    # Carrega o modelo YOLOv8 inicial (pesos leves adequados para deploy)
    return YOLO("yolov8n.pt")

model = load_yolo_model()

# 4. Botão para ativar/abrir o fluxo da câmera
# O Streamlit utiliza o componente camera_input para acessar o hardware nativamente
img_file_buffer = st.camera_input("Clique no botão abaixo para tirar uma foto ou iniciar a câmera")

# 3. Processamento da imagem capturada e detecção de objetos
if img_file_buffer is not None:
    # Converte o buffer de imagem do Streamlit em um formato legível pelo OpenCV/YOLO
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Executa a inferência do YOLO na imagem capturada
    results = model(cv2_img)
    
    # Renderiza os resultados (caixas delimitadoras e rótulos) na imagem
    annotated_frame = results[0].plot()
    
    # Converte o canal de cores de BGR (OpenCV) para RGB (Streamlit)
    annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    
    # Exibe o resultado final com as detecções na tela
    st.image(annotated_frame_rgb, caption="Objetos Detectados", use_container_width=True)