FROM python:3.7

COPY . /
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8044
COPY . .

CMD [ "python", "./main/app.py" ]
