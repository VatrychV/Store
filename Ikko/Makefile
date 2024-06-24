# Makefile for building and running the Docker application

# Variables
IMAGE_NAME = store-py
IMAGE_TAG = latest
CONTAINER_NAME = store-py
PORT = 8001

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

# Run the Docker container
run:
	docker run --rm -it -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME):$(IMAGE_TAG)

# Clean up the Docker environment (optional)
clean:
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: build run clean
