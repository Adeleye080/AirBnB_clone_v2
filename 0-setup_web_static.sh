#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Hlberton Coding School, Alx
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

sudo sed -i '38 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
