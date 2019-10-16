# Read/Write QR Code

This Django blog has an implementation to generate and read QR code of the given string. This made on Python 3, Django 2 and Bootstraps.
Below python libraries used to encode and decode QR code.

##### To Decode
https://pypi.org/project/pyzbar/

##### To Encode
https://pypi.org/project/PyQRCode/


### Steps to setup application
```
mkdir django
cd django
python3 -m venv myenv
. myenv/bin/activate
```

### Git Clone
```
git clone <url>
```

### Install requirements
```
cd <app directory>
pip install -r requirements.txt
```

### Run migrate
```
python manage.py migrate
```

### Start server
```
python manage.py runserver
```

### Navigate to
```
http://127.0.0.1:8000/
```

### Admin panel URL
```
http://127.0.0.1:8000/admin/
```

### Create new user command
```
python manage.py createsuperuser
```

Please refer libraries documentation if you face any package related errors
