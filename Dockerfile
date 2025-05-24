LABEL authors="Jounaid"

FROM python:3.11-slim

WORKDIR /app

# git
RUN apt-get update && apt-get install -y git

# repo
RUN git clone https://github.com/ton-nom/openbook.git .

RUN pip install streamlit

EXPOSE 8501
# Lancement de streamlit sur le port 8501 ici
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
