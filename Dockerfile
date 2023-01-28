FROM python:3.10-slim-bullseye

COPY bots/main.py /bots/
COPY bots/api.py /bots/
COPY bots/twitter.py /bots/
COPY bots/setup.py /bots/
COPY bots/translate.py /bots/
COPY requirements.txt /tmp
COPY twitterbot-376108-554b24ce03a2.json /bots
COPY assets/NotoSerif-Regular.ttf /bots
RUN pip3 install -r /tmp/requirements.txt
RUN echo $HOME

WORKDIR /bots
CMD ["python3", "main.py"]