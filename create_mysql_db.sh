#!/bin/sh

# Удалить старую базу
/bin/echo "Deleting old database"
/usr/bin/mysql -p -u root -e "drop database ask_db"

# Создать новую базу
/bin/echo "Creating new database"
/usr/bin/mysql -p -u root -e "create database ask_db"

# Создать таблицы на основе моделей
/usr/bin/python /home/box/web/ask/manage.py syncdb
