# Healthcare CI/CD - actions & docker

minimal distributed healthcare (demo api) with a complete ci/cd pipeline:

    - CI: unit & integration tests + container build + e2e checks
<<<<<<< HEAD
    
    - CD: image pushed to ghcr, deploy step, health checks and logs
    
=======

    - CD: image pushed to ghcr, deploy step, health checks and logs

>>>>>>> db5e910 (test run)
    - RB: re-run workflow_dispatch with rollback_to = prior tag/sha

##run locally

docker build -t healthcare-app:local .

docker compose -f docker-compose.test.yml up -d

curl -s http://localhost:8000/health

TEST README UPDATE
- Demo change Sun Sep 28 16:31:48 CDT 2025
- Demo change Sun Sep 28 16:36:25 CDT 2025
- Demo change Sun Sep 28 16:46:09 CDT 2025
- Demo change Sun Sep 28 16:51:37 CDT 2025 - I AM GOING TO BE ANGRY >:(
- Demo Sun Sep 28 16:58:28 CDT 2025

-DEMO
- Demo Mon Sep 29 21:00:46 CDT 2025
- Demo Mon Sep 29 21:03:30 CDT 2025
- Demo Mon Sep 29 21:24:33 CDT 2025
