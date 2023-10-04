#!/usr/bin/env bash
#  Sets up a web server for deployment of web_static.

#if ! command -v nginx &> /dev/null

apt-get update
apt-get -y install nginx

# make directory if it doesnt exists
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "This is a test file" > /data/web_static/releases/test/index.html

#create a symbolic link and 
#-f(if file already exists, will be removed & link be created)
ln -sf /data/web_static/releases/test/ /data/web_static/current

# changing ownership
sudo chown -R ubuntu:ubuntu /data/

location="location  /hbnb_static {\n\talias /data/web_static/current/;}"
sudo sed -i "11i \\\t$location" /etc/nginx/sites-available/default

sudo service nginx restart
