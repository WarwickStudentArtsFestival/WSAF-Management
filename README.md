# WSAF Management

This was an MVP of a schedule management tool for WSAF 2024, using Django admin for making updates, and serving the updated schedule to digital signage and website. For later events, we switched to Pretalx, but this might be useful for *something* in the future (particularly the db models).

Copy `template.env` to `.env`

Run `docker compose up`

## Making Migrations
```bash
docker compose exec -it web /bin/bash
python manage.py makemigrations
python manage.py migrate
```

```
python manage.py createsuperuser
```

## Setting up without Docker
```bash
python -m venv .venv

.venv\Scripts\activate
.venv/bin/activate

pip install -U setuptools wheel pip uv
pip install -r .\config\requirements\dev_lock.txt
```

Note - on Windows, you may need to install [Cygwin](https://stackoverflow.com/questions/68616000/pip-install-uwsgi-gives-error-attributeerror-module-os-has-no-attribute-un) for uwsgi to install. Or use WSL.
