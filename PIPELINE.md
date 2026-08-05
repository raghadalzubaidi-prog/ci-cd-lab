# CI/CD Pipeline

## Trigger
- Runs on every push to the main branch.

## Pipeline Stages
1. Checkout repository
2. Login to Docker Hub
3. Validate Dockerfile
4. Build Docker image
5. Push Docker image
6. Run container
7. Smoke test

## Secrets Used
- DOCKER_USERNAME
- DOCKER_PASSWORD

## Rollback Procedure
If a deployment fails:

```bash
kubectl rollout undo deployment/ci-cd-app
kubectl rollout status deployment/ci-cd-app
```
