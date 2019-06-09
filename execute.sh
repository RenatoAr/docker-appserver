docker build -t docker-appserver .
docker run -d -p 5000:5000 --name docker-appserver docker-appserver