LABEL authors="Jounaid"

FROM python:3.11-slim

WORKDIR /app

# Installer git
RUN apt-get update && apt-get install -y git

# Cloner le repo
RUN git clone https://github.com/ton-nom/openbook.git .

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]