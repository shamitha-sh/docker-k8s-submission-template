FROM python:alpine

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]