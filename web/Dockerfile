FROM python:3.10.5-buster
WORKDIR /webpage
ADD . .

ARG FLAG
ENV FLAG=$FLAG
RUN echo $FLAG > /webpage/templates/data.html

RUN apt update -y && \
    apt install -y python3-pip && \
    pip install -r requirements.txt


USER daemon
ENTRYPOINT [ "python" ]
EXPOSE 8017
CMD ["app.py"]
