Drive Tracker
===================
[![Build Status](https://travis-ci.org/rohankapoorcom/drivetracker.svg?branch=master)](https://travis-ci.org/rohankapoorcom/drivetracker)
[![Coverage Status](https://coveralls.io/repos/github/rohankapoorcom/drivetracker/badge.svg?branch=master)](https://coveralls.io/github/rohankapoorcom/drivetracker?branch=master)
[![Documentation Status](https://readthedocs.org/projects/drivetracker/badge/?version=latest)](http://drivetracker.readthedocs.io/en/latest/?badge=latest)

Catalogue all of your hard drives with a beautiful web-based tool. Docker package coming soon.

### Demo
--------------
Play with Drive Tracker on it's [demo site](https://drivetracker-demo.herokuapp.com)

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

### Contributing
---------------
* Fork the project repository
* Make all of your changes in a specific branch on your fork
* Make sure your changes confirm to the [Style Guide for Python Code (PEP8)](http://python.org/dev/peps/pep-0008/)
* Open a pull request

### License
Please see [LICENSE](LICENSE)
