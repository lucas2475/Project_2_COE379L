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

### Full Test workflow

```bash
# 1. Start container
docker-compose up -d

# 2. Wait a few seconds for startup
sleep 5

# 3. Test summary endpoint
curl http://localhost:5000/summary

# 4. Test inference endpoint (with an image)
curl -X POST -F "image=@test_image.png" http://localhost:5000/inference

# 5. View logs if something goes wrong
docker-compose logs
```