Okapi
=====

This is the web front end for the stockwalk program

Server setup
------------
Setup a virtual environment with python3

Run `sudo pip3 install -r requirements/production.txt`

Copy the `server/okapi_production_settings.ini.example` to
`/etc/okapi_production_settings.ini` and change the settings therein. If you
are on aws, change the `ALLOWED_HOSTS` variable to the public ip which can be
found on the AWS console. If you are on a local machine set this to
`127.0.0.1`
