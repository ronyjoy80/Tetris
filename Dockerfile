FROM python:3.9
WORKDIR /tetris
COPY . /tetris/

RUN pip install -r requirements.txt

CMD ["python", "main.py"]