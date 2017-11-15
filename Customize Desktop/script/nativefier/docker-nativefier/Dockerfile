FROM resin/rpi-raspbian:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y  \
	npm
RUN npm cache clean -f 
RUN	npm install -g n 
RUN	n stable 
RUN	npm install nativefier -g

ENTRYPOINT ["nativefier"]
CMD ["--help"]
