# CI/CD Pipeline Documentation

## Trigger

The pipeline runs automatically on every push to the `main` branch.

## Pipeline Stages

### 1. Checkout Repository
Downloads the latest source code.

### 2. Login to Docker Hub
Authenticates using GitHub Secrets.

Secrets used:
- DOCKER_USERNAME
- DOCKER_PASSWORD

### 3. Dockerfile Validation
Runs `check_dockerfile.sh` to ensure the Dockerfile does not use `:latest` as the base image.

### 4. Build Docker Image
Builds the Docker image.

### 5. Push Docker Image
Pushes the image to Docker Hub.

### 6. Run Container
Starts the container inside GitHub Actions.

### 7. Smoke Test
Checks that the application returns:

`v2 - hello from CI`

## Rollback Procedure

```bash
kubectl rollout undo deployment/ci-cd-app
```

Check rollout status:

```bash
kubectl rollout status deployment/ci-cd-app
```

Verify the application:

```bash
curl http://localhost:8080
```
