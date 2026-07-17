FROM ubuntu
COPY main.py /main.py
COPY requirements.txt /requirements.txt
COPY README.md /README.md
RUN apt -y update && apt -y upgrade && apt install -y python3-pip && apt install -y uvicorn python3-fastapi
CMD ["uvicorn main:app --host 0.0.0.0 --port 8000"]
