#!bin/bash

#Para container caso esteja rodando
sudo docker stop docker-appserver
#Destroi container docker-appserver se exisir
sudo docker rm docker-appserver
#Destroi imagem docker-appserver se exitir
sudo docker image rm docker-appserver
#Controi a imagem docker-appserver
sudo docker build -t docker-appserver .
#Roda container
sudo docker run -p 5000:5000 --name docker-appserver docker-appserver