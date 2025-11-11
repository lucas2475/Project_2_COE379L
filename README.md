### 1. Build the Docker Image

Make sure your `best_model.keras` file is in the same directory as the Dockerfile.

```bash
# Build the image
docker build -t hurricane-damage-classifier:latest .
```

### 2. Run with Docker Compose

```bash
# Start the container
docker-compose up -d

# Check if it's running
docker-compose ps

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

### Full Simple Test workflow

```bash
# 1. Start container
docker-compose up -d

# 2. Test summary endpoint
curl http://localhost:5000/summary

# 3. Test inference endpoint (with an image)
curl -X POST -F "image=@test_image.jpeg" http://localhost:5000/inference

# 4. View logs if something goes wrong
docker-compose logs
```

### Test with Grader

```bash
# 1. Check that container is still running
docker ps

# 2. Run shell script
./start_grader.sh
```