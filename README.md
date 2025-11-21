Perfect! Here’s a **ready-to-copy version** you can directly paste into your `README.md` file:

````markdown
# Flask App Deployment with Docker and Self-Hosted Runner

## 1. Launch EC2
- Launch Ubuntu EC2 instance.
- SSH into instance:
```bash
ssh -i your-key.pem ubuntu@<ec2-public-ip>
````

## 2. Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
docker --version
```

## 3. Setup Self-Hosted GitHub Runner

1. Go to GitHub → Settings → Actions → Runners → Add runner.
2. On EC2, download, extract, configure, and start the runner:

```bash
./config.sh --url <repo-url> --token <token>
./run.sh
```

## 4. Build and Deploy Docker Image

```bash
# Build Docker image
docker build -t <dockerhub_username>/flask-app:latest .

# Login and push to DockerHub
docker login
docker push <dockerhub_username>/flask-app:latest

# Run container
docker stop flask-app || true
docker rm flask-app || true
docker run -d -p 5000:5000 --name flask-app <dockerhub_username>/flask-app:latest
```

```

This is **fully copy-paste ready**, minimal, and includes all steps: EC2 setup, Docker installation, runner setup, and deployment.  

If you want, I can also **add a small “GitHub Secrets setup” snippet** for DockerHub login in the README so the workflow is complete. Do you want me to add that?
```
