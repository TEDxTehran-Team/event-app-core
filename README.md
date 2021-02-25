# Deploy
1. Clone the repo
2. Copy .env.example to .env
3. Copy .env.local.example - or .env.production.example depending on where you are deploying - to .env.local
4. Add secret key and other data to the env files
5. Run these commands:
```shell script
docker-compose up
docker-compose exec app python manage.py migrate
```