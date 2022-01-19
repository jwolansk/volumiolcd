FROM python:3.7-buster

RUN pip install urllib3 smbus2 requests

CMD ["python", "/src/screen.py"]