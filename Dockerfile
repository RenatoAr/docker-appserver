FROM python:3.7-alpine
COPY . /temp
WORKDIR /temp
RUN pip install -r req.txt
CMD ["gunicorn", "-w 4", "main:app"]