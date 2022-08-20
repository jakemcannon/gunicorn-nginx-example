FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

ENV FLASK_APP=main

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "main:app"]
#CMD ["flask", "run", "--host=0.0.0.0"]
