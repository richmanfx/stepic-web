#!/bin/sh

# Заменить конфиг на свой и перезапустить nginx 
/usr/bin/sudo /bin/rm /etc/nginx/sites-enabled/default
/usr/bin/sudo /bin/cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/usr/bin/sudo /etc/init.d/nginx restart

# Заменить конфиги на свои и перезапустить gunucorn 
/usr/bin/sudo /bin/rm /etc/gunicorn.d/*
/usr/bin/sudo /bin/cp /home/box/web/etc/gunicorn-wsgi.conf   /etc/gunicorn.d/gunicorn-wsgi.conf
# /usr/bin/sudo /bin/cp /home/box/web/etc/gunicorn-django.conf   /etc/gunicorn.d/gunicorn-django.conf
/usr/bin/sudo /etc/init.d/gunicorn stop && /usr/bin/sudo /etc/init.d/gunicorn start

# Посмотреть логи после перестартовки
/bin/echo
/bin/echo "NGINX LOG:"
/usr/bin/sudo /usr/bin/tail /var/log/nginx/error.log

/bin/echo
/bin/echo "GUNICORN LOG:"
/usr/bin/sudo /usr/bin/tail /var/log/gunicorn/gunicorn-wsgi.conf.log
#/usr/bin/sudo /usr/bin/tail /var/log/gunicorn/gunicorn-django.conf.log

/bin/echo
/bin/echo "NETSTAT"
/usr/bin/sudo /bin/netstat -nlp --ip

