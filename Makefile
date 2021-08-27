IMGNAME=aaaas

docker-run: docker-build
	docker run -p 8080:80 -p 1337:1337 $(IMGNAME)

docker-build:
	docker build . -t $(IMGNAME)
