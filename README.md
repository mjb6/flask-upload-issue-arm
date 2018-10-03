# Minimal example to show 64kb upload limitation with flask, apache, mod_wsgi on ARM devices

I have a flask application, that supports file upload.
It runs on an ARM based debian stable server with apache wsgi.
If I upload small files, everything is fine. The problem appears, when I upload files with a file size >64kb. The famous "Bad request - The browser (or proxy) sent a request that this server could not understand." pops up.

## Steps to reproduce
- Install in an environment, as described below
- Use the web browser to go to the site
- Upload the file testfiles/1-small-file.gpx -> works
- Upload the file testfiles/3-too-big-file.gpx -> throws Bad request error

## Server Config
Server: 32bit armhf device (e.g. Odroid HC1 or Raspberry PI)
Distro: debian 9 based

Installed debian packages:
`sudo apt install python3-pip apache2 libapache2-mod-wsgi-py3`

Installed system wide python modules:
`sudo pip3 install flask peewee`

/etc/apache2/sites-available/trackdb.conf:
```
WSGIScriptAlias /trackdb /var/www/trackdb/flaskapp.wsgi

<Directory /var/www/trackdb/>
        Order allow,deny
        Allow from all
</Directory>
Alias /trackdb/static /var/www/trackdb/static
<Directory /var/www/trackdb/static/>
       Order allow,deny
       Allow from all
</Directory>
```

Copy the content of this repo to /var/www/trackdb
