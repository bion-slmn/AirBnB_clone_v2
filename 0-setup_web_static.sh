#!/usr/bin/env bash
#  Bash script that sets up your web servers for the deployment of web_static

# install nginx if not installed
if ! command -v nginx &> /dev/null
then
	apt-get -y update
	apt-get -y install nginx
fi

# make directory if it doesnt exists
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

#create a symbolic link 
if [ -L "/data/web_static/current" ] && [ -e "/data/web_static/current" ]
then
	unlink /data/web_static/current
	ln -s /data/web_static/releases/test/ /data/web_static/current
else
	ln -s /data/web_static/releases/test/ /data/web_static/current
fi
# changing ownership
sudo chown -R ubuntu:ubuntu /data/

location="location ^~ /hbnb_static {\n\talias /data/web_static/current/;}"
sudo sed -i "11i \\\t$location" /etc/nginx/sites-available/default

sudo service nginx restart
