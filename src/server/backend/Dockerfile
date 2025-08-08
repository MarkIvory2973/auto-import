FROM python:3.13-slim

WORKDIR /src/

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN playwright install chromium --with-deps

COPY . .

CMD [ "python", "./runserver.py" ]