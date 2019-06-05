docker build -t docker-flask ./
docker run -p 5000:5000 -it --name docker-flask docker-flask