# URL Shortener

A simple and efficient web application for shortening URLs. Built with Flask and designed for educational purposes, this project demonstrates modern web development practices with containerization and Kubernetes deployment.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Local Development](#local-development)
  - [Docker](#docker)
  - [Kubernetes](#kubernetes)
- [CI/CD](#cicd)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **URL Shortening**: Convert long URLs into short, manageable links
- **Persistent Storage**: Uses SQLite database for storing URL mappings
- **MD5 Hashing**: Generates short URL fragments using MD5 algorithm
- **Redirect Service**: Automatically redirects short URLs to original destinations
- **Web Interface**: Simple and intuitive HTML interface
- **Containerized**: Ready-to-deploy Docker image
- **Kubernetes Ready**: Includes Kubernetes manifests for production deployment

## 🛠️ Tech Stack

- **Backend Framework**: Flask 3.1.0+
- **Language**: Python 3.12+
- **Database**: SQLite3
- **Package Manager**: uv
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Container Registry**: GitHub Container Registry (GHCR)

## 📦 Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- (Optional) Docker for containerized deployment
- (Optional) Kubernetes cluster for production deployment

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vitos-exe/url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

## 💻 Usage

### Local Development

1. **Run the application**
   ```bash
   flask run
   ```

2. **Access the application**
   
   Open your browser and navigate to `http://127.0.0.1:5000`

3. **Shorten a URL**
   - Enter your long URL in the input field
   - Click submit to get a shortened version
   - Use the shortened URL to redirect to the original destination

### Docker

The project includes a Dockerfile for containerized deployment.

1. **Build the Docker image**
   ```bash
   docker build -t url-shortener .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 url-shortener
   ```

3. **Access the application**
   
   Navigate to `http://localhost:5000`

**Pre-built images** are available on GitHub Container Registry:
```bash
docker pull ghcr.io/vitos-exe/url-shortener:master
docker run -p 5000:5000 ghcr.io/vitos-exe/url-shortener:master
```

### Kubernetes

Kubernetes manifests are provided in the `manifests/` directory for production deployment.

1. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f manifests/deployment.yaml
   kubectl apply -f manifests/service.yaml
   ```

2. **Check deployment status**
   ```bash
   kubectl get deployments
   kubectl get services
   ```

3. **Access the application**
   
   The service is configured as LoadBalancer on port 9090:
   ```bash
   kubectl get service url-shortener-service
   ```

The deployment configuration includes:
- **Deployment**: Single replica with automatic image pull
- **Service**: LoadBalancer type exposing port 9090 (maps to container port 5000)
- **Image**: Uses the latest master branch image from GHCR

## 🔄 CI/CD

This project uses **GitHub Actions** for continuous integration and deployment:

### Workflow: Build and Push Docker Image

Located in `.github/workflows/docker-publish.yml`, the workflow:

1. **Triggers**: Automatically runs on push to the `master` branch
2. **Build Process**:
   - Sets up QEMU and Docker Buildx for multi-architecture builds
   - Builds Docker images for `linux/amd64` and `linux/arm64` platforms
   - Pushes images to GitHub Container Registry (GHCR)
3. **Deployment**:
   - Automatically deploys to Kubernetes cluster
   - Performs rolling restart of the `url-shortener` deployment
   - Uses Kubernetes config from repository secrets

### Container Registry

Docker images are automatically published to:
```
ghcr.io/vitos-exe/url-shortener:master
```

## 📁 Project Structure

```
url-shortener/
├── .github/
│   └── workflows/
│       └── docker-publish.yml    # GitHub Actions CI/CD workflow
├── app/
│   ├── __init__.py               # Flask application initialization
│   ├── db.py                     # Database operations
│   ├── schema.sql                # Database schema
│   ├── utils.py                  # Utility functions (URL validation, hashing)
│   └── templates/
│       └── index.html            # Web interface
├── manifests/
│   ├── deployment.yaml           # Kubernetes deployment configuration
│   └── service.yaml              # Kubernetes service configuration
├── Dockerfile                    # Docker image definition
├── pyproject.toml                # Python project configuration
└── README.md                     # Project documentation
```

## 🤝 Contributing

Contributions are welcome! This is an educational project, and improvements are always appreciated.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**vitos-exe**

- GitHub: [@vitos-exe](https://github.com/vitos-exe)

---

**Note**: This project was created for educational purposes to demonstrate web application development, containerization, and deployment practices.
