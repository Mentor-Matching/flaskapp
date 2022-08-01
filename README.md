# Mentor Matching Recommendation Engine

Note: We decided to separate out the recomendation engine from our static asset serving app. Please inquire @GoKooma for any questions regarding frontend.

## Table of contents

1. [Setup](#setup)
  - [virtualenv](#virtualenv)
  - [install packages](#install-package)
  - [environment variable](#environment-variable)
  - [run server](#run-server)

## Setup
This set up guide is dedicated for our recommendation engine developers.

### virtualenv
Please follow this [handy guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to install, create and activate virtual environment.

tl;dr.

See below to see the examples from the [handy guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to create and activate virtual environment. I skipped the installation part because, hey, you ought to put in some effort to at least install, nay? :)

Here is an example of creating virtual environment after installing virtualenv on mac:
```
python3 -m venv env
```

On Windows:
```
py -m venv env
```

Here is an example of activating virtual enviroment.
On mac:
```
source env/bin/activate
```
On Windows:
```
.\env\Scripts\activate
```

At the **END** of development, exit virtual environment using the following command
```
deactivate
```

### install packages
After virtualenv is activated, install all the necessary packages following the command below (not sure if this is the same in Windows):
```
pip install -r requirements.txt
```

### environment variable
Once all the packages are installed, set enviroment variable like below to avoid import error - Again, I am not sure how this is done in Windows. Sorry Windows users :(
```
export set FLASK_APP=flaskapp
```

### run server
After all those inital set ups are done, move into **```backend``` directory,** and then run ```flask run``` in terminal (for mac users). Now you are all set! Happy hacking :D
