FROM python:3.8-slim-buster
CMD pip install pandas
CMD [ "python3", "calculatorTesting.py"]