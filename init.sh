#!/bin/sh

/bin/rm /etc/nginx/sites-enabled/default
/usr/bin/sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/usr/bin/sudo /etc/init.d/nginx restart


#/usr/bin/sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#/usr/bin/sudo /etc/init.d/gunicorn restart