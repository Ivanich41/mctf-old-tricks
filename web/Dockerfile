FROM python:3.10.5-buster

WORKDIR /webpage
ADD . .

RUN apt-get update & apt-get upgrade & apt-get install python & apt-get install pip & pip install -r requirements.txt

ENTRYPOINT [ "python" ]
EXPOSE 8017

CMD ["app.py"]
