Drive Tracker
===================

Catalogue all of your hard drives with a beautiful web-based tool. Docker package coming soon.

### Features
---------------
* Responsive web design - for use on desktop and mobile browsers
* Designed using [Bootstrap 3](http://getbootstrap.com/)
* Built with [Django](http://www.djangoproject.com/)
* Runs wherever Python does
* Search by any field
* Input and store all the data you have about each of your harddrives
* All fields are optional

### Requirements
---------------
* Python 2.7
* SQL Server (PostgreSQL recommended)

### Optional
---------------
* Nginx (or other reverse proxy running in front of gunicorn)

### Installation
---------------
1. Open a terminal and go to the folder where you want to install (```cd /opt/dt```)
2. Download and unzip the [latest build](https://github.com/rohankapoorcom/drivetracker/archive/master.zip) to that directory (```/opt/dt/```)
3. Create a virtualenvironment and use pip to install all of the required packages

  ```
  virtualenv venv
  source venv/bin/activate
  sudo apt-get install libpq-dev python-dev (ubuntu only)
  pip install -r requirements.txt
  ```
4. Copy drivetracker/settings/example.py to drivetracker/settings/local.py and fill in your configuration details
  * Make sure to disable debug by setting ```DEBUG = False``` in local.py
  * Make sure to provide correct database settings or the app won't start
5. Migrate the database ```python manage.py migrate```
6. Start Drive Tracker by executing ```gunicorn -b 0.0.0.0:8000 drivetracker.wsgi```
7. You can access Drive Tracker from a web browser at ```yourip:8000```
8. [Configure Gunicorn to start automatically](http://docs.gunicorn.org/en/stable/deploy.html)

### License
Please see [LICENSE](LICENSE)