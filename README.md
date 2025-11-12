

## Project Overview

This project focuses on building and deploying machine-learning models to automatically classify satellite images of buildings affected by Hurricane Harvey as either damage or no_damage. Three models were developed and evaluated: a baseline Dense ANN, a modified LeNet-5 CNN, and a deeper VGG-16 architecture. After training, the best-performing model was packaged into a Flask inference server and deployed using a Docker container, providing REST API endpoints for real-time classification. The project demonstrates the full workflow from data preparation and model development to evaluation and containerized deployment.



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

# Sample Output 
{
  "architecture": "sequential_7",
  "classes": [
    "damage",
    "no_damage"
  ],
  "description": "Binary CNN that classifies satellite images after Hurricane Harvey.",
  "input_size": [
    224,
    224,
    3
  ],
  "name": "hurricane_damage_classifier",
  "total_parameters": 25851841,
  "version": "v1"
}

# Test inference endpoint (with an image)
curl -X POST -F "image=@test_image.jpeg" http://localhost:5000/inference


# Sample Output
{
  "prediction": "damage"
}

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
