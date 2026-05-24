# PSUSphere Docker Setup

## For developers (build from source)
```bash
git clone https://github.com/friendsusername/psusphere-docker.git
cd psusphere-docker
docker-compose up --build
```

## For clients (pull from Docker Hub)
```bash
# 1. Copy the /for_client/docker-compose.yml to a new folder
# 2. Inside that folder, run:
docker-compose up -d

# 3. Create superuser (first time only)
docker-compose exec web python manage.py createsuperuser
```

## Access the app
Open your browser at: http://localhost:8000