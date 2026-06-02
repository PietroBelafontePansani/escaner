# 🔍 Scanner com YOLOv8 e Streamlit

Uma aplicação web leve e otimizada desenvolvida em Python que utiliza o modelo **YOLOv8 (Nano)** para realizar a detecção de objetos em tempo real através da câmera do dispositivo. O projeto foi estruturado especificamente para rodar de forma eficiente em ambientes de nuvem com recursos limitados, como o plano gratuito do **Render**.

## 🚀 Funcionalidades

* **Detecção em Tempo Real:** Interface interativa utilizando o componente nativo de câmera do Streamlit.
* **Modelo Otimizado:** Uso do YOLOv8n (apenas ~6MB), garantindo velocidade e baixo consumo de memória.
* **Pronto para Nuvem:** Configurações ajustadas para evitar estouro de memória RAM (limite de 512MB do Render).

---

## 🛠️ Pré-requisitos e Instalação Local

Se quiser rodar o projeto localmente na sua máquina, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO

   Crie um ambiente virtual (opcional, mas recomendado):
   python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
