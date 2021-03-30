# PythonMicroServices

## Description

All my previous projects have been monolithic and I wanted to gain experience in containerization and microservices. 

This is just an example site, please do not enter information you don't want to be seen in public. 

# 


# Notes to self and interested budding developers:

Docker is the same process as a fullstack app, just doing it inside a contianer which requires minimal configuration 

1. Start a project or app, `django-admin startproject projectname`. 
2. create `Dockerfile`, `docker-compose.yml`, `requirements.txt` and configure ports for Docker. 
3. `docker-compose up`: starts MySQL / app -> 
4. in another terminal, sh into what service we want, `docker-compose exec backend sh`, `backend` here.
5. `django startapp appname`
6. create models
7. `docker-compose exec backend sh` again, migrate models into db.
8. for django/backend framework, set up CRUD REST APIs //urls, views, serializer 
9. repeat per app 
10. use RabbitMQ to communicate between microservices, configure callback in the consumer.py and producer.py files and ensure data consistency between data bases.
11. 

