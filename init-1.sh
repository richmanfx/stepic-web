#!/bin/sh

# Имя папки проекта
ArchDirectory=web

echo "Архивирование папки" ${ArchDirectory} "..."

# Забекапить папку проекта
/usr/bin/rar a -m5 -agYYMMDDHHMM -r $HOME/${ArchDirectory}-.rar $HOME/${ArchDirectory} && \
echo "Архив успешно создан."

# Удалить старую папку
/bin/rm -dir $HOME/${ArchDirectory}

# Создать новую структуру директорий
/bin/mkdir $HOME/${ArchDirectory} && \
/bin/mkdir $HOME/${ArchDirectory}/etc && \
/bin/mkdir $HOME/${ArchDirectory}/public && \
/bin/mkdir $HOME/${ArchDirectory}/public/css && \
/bin/mkdir $HOME/${ArchDirectory}/public/img && \
/bin/mkdir $HOME/${ArchDirectory}/public/js && \
/bin/mkdir $HOME/${ArchDirectory}/upload && \
echo "Новая структура директорий успешно создана."




