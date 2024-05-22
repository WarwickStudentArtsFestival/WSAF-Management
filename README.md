# WSAF Management

Copy `template.env` to `.env`

Run `docker compose up`

## Making Migrations
```bash
docker compose exec -it web /bin/bash
python migrate.py makemigrations
```
