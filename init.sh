#!/bin/sh

# Заменить конфиг на свой и перезапустить nginx 
/usr/bin/sudo /bin/rm /etc/nginx/sites-enabled/*
/usr/bin/sudo /bin/rm /etc/nginx/sites-available/*
/usr/bin/sudo /bin/cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/usr/bin/sudo /etc/init.d/nginx restart

# Заменить конфиги на свои и перезапустить gunucorn 
/usr/bin/sudo /bin/rm /etc/gunicorn.d/*
/usr/bin/sudo /bin/cp /home/box/web/etc/gunicorn-django.conf   /etc/gunicorn.d/gunicorn-django.conf
/usr/bin/sudo /etc/init.d/gunicorn stop && /usr/bin/sudo /etc/init.d/gunicorn start

# Посмотреть логи после перестартовки
/bin/echo
/bin/echo "NGINX LOG:"
/usr/bin/sudo /usr/bin/tail /var/log/nginx/error.log

/bin/echo
/bin/echo "GUNICORN LOG DJANGO:"
/usr/bin/sudo /usr/bin/tail /var/log/gunicorn/gunicorn-django.conf.log

# Перезапустить MySQL
#/etc/init.d/mysql stop && /etc/init.d/mysql start

# Смотрим сокеты
/bin/echo
/bin/echo "NETSTAT"
/usr/bin/sudo /bin/netstat -nlp --ip | grep ":80"
/usr/bin/sudo /bin/netstat -nlp --ip | grep ":33"
