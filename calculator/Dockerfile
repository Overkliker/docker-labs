FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    x11-apps \
    openjdk-17-jre \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /app

COPY calc.jar .

ENV DISPLAY=host.docker.internal:0

CMD ["java", "-jar", "calc.jar"]
