## How to Run Classifier

Make sure `best_model.keras` file is in the same directory as the Dockerfile.

### Run using docker run
```bash
# Pull image from Docker Hub
docker pull etmch5341/hurricane-damage-classifier:latest

# Run it
docker run -d -p 5000:5000 etmch5341/hurricane-damage-classifier:latest
# or
docker run -it --rm -p 5000:5000 etmch5341/hurricane-damage-classifier:latest

# Test summary endpoint
curl http://localhost:5000/summary

# Test inference endpoint (with an image)
curl -X POST -F "image=@test_image.jpeg" http://localhost:5000/inference

# Stop it
docker stop <container_id>
```

### Run using docker-compose
```bash
# other option is docker compose (currently setup to use the pulled image)
# since docker-compose file setup to use the docker hub image

# Start the container
docker-compose up -d

# Check if it's running
docker-compose ps

# View logs
docker-compose logs -f

# Test summary endpoint
curl http://localhost:5000/summary

# Test inference endpoint (with an image)
curl -X POST -F "image=@test_image.jpeg" http://localhost:5000/inference

# Stop the container
docker-compose down
```

### Building Image
```bash
# Build the image if needed
docker build -t hurricane-damage-classifier:latest .
```

### Checking image list
```bash
# Check list of docker images
docker images
```

### Test with Grader

```bash
# 1. Check that container is still running
docker ps

# 2. Run shell script
./start_grader.sh
```