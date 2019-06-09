FROM python:3.7-alpine
ADD ./src/req.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD ./src /opt/src/
WORKDIR /opt/src
EXPOSE 5000
CMD ["python", "appserver.py"]