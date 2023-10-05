# installing nginx

package {'nginx':
  ensure => 'installed',
}

file {['/data/', '/data/web_static/', '/data/web_static/releases/',
  '/data/web_static/shared/', '/data/web_static/releases/test/']:
  ensure => 'directory',
}

# create a file

file {'/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => ' Test file content',
}

# executinga commmad
exec {'creating symlink':
  command => '/usr/bin/ln -sf /data/web_static/releases/test/ /data/web_static/current',
 # path    => '/usr/bin/ln'
}

exec {'change ownership':
        command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
        # path    => '/usr/bin/chown'
}

# update ngnix
file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}',
}

exec {'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
  path        => '/usr/sbin/service',
}
