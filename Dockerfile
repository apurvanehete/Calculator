FROM python:3.8-slim-buster
WORKDIR /src
COPY . .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python3", "calculatorTesting.py"]