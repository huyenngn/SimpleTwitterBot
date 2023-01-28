FROM python:3.10-slim-bullseye

COPY bots/api.py /bots/
COPY bots/twitter.py /bots/
COPY bots/setup.py /bots/
COPY bots/translate.py /bots/
COPY twitterbot-376108-554b24ce03a2.json /tmp/twitterbot-376108-554b24ce03a2.json
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "twitter.py"]