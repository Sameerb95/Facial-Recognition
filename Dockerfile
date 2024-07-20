FROM python:3.9.6
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt .
COPY src src/
WORKDIR .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR src/
ENTRYPOINT ["streamlit","run", "start.py"]