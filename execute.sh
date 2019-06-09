docker build -t docker-appserver .
docker run -p 5000:5000 -it --name docker-appserver docker-appserver