FROM ubuntu:latest
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN apt-get update
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]