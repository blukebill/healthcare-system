# Healthcare CI/CD - actions & docker

minimal distributed healthcare (demo api) with a complete ci/cd pipeline:
    - CI: unit & integration tests + container build + e2e checks
    - CD: image pushed to ghcr, deploy step, health checks and logs
    - RB: re-run workflow_dispatch with rollback_to = prior tag/sha

##run locally

docker build -t healthcare-app:local .
docker compose -f docker-compose.test.yml up -d
curl -s http://localhost:8000/health
