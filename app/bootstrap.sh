#!/bin/bash
python /workspace/app/mikado_line_bot_site/manage.py collectstatic --noinput --clear
while ! python /workspace/app/mikado_line_bot_site/manage.py migrate --noinput; do
    sleep 1
done
pass=$(openssl rand -base64 8)
export DJANGO_SUPERUSER_PASSWORD=$pass
echo ==============================
echo ${DJANGO_SUPERUSER_PASSWORD}
echo ==============================
python /workspace/app/mikado_line_bot_site/manage.py createsuperuser --noinput --username Administrator --email admin@example.com
cp /workspace/app/mikado_line_bot_site/media/NoImage.png /var/www/media/NoImage.png
gunicorn mikado_line_bot_site.wsgi --bind=unix:/var/run/gunicorn/gunicorn.sock --chdir=/workspace/app/mikado_line_bot_site
# sleep infinity
