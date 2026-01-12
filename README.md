# URL Shortener

Simple web app for shortening URLs. Built with Flask and designed for educational purposes.  
Uses `sqlite3` as the database and `md5` hashing algorithm for generating short URLs.

## Tech Stack

- Python 3.12+ with Flask
- SQLite3
- Docker & Kubernetes
- GitHub Actions (CI/CD)

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation & Usage

**Local Development:**
```bash
git clone https://github.com/vitos-exe/url-shortener.git
cd url-shortener
uv sync
source .venv/bin/activate  # On Linux/macOS
flask run
```
Access at `http://127.0.0.1:5000`

**Docker:**
```bash
docker build -t url-shortener .
docker run -p 5000:5000 url-shortener
```
Or use pre-built image: `ghcr.io/vitos-exe/url-shortener:master`

**Kubernetes:**
```bash
kubectl apply -f manifests/
```
Service exposes port 9090 (LoadBalancer).

## CI/CD

GitHub Actions workflow (`.github/workflows/docker-publish.yml`) automatically:
- Builds multi-arch Docker images (amd64/arm64) on push to `master`
- Pushes to GitHub Container Registry
- Deploys to Kubernetes cluster via rolling restart

## Project Structure

```
├── .github/workflows/docker-publish.yml  # CI/CD workflow
├── app/                                  # Flask application
├── manifests/                            # Kubernetes configs
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
└── pyproject.toml
```
