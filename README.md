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