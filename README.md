# Sitech Django Audit Log
`sitech-django-audit_log` is a Django application and library for creates an audit history for each model operations (create, update and delete) into database, file, and many other stores automatically.

<br/>


## prerequisites
To use this library, you'll need Request Middleware from [sitech-django-middlewares](https://github.com/sitmena/sitech-django-middlewares)  and it is a Python library that allow you to access the [Request](https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects) or [User](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest.user) Object Inside the Models, Forms, Signals, ... etc.

You can do the following to install "Request Middleware":
1. Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install git+https://github.com/sitmena/sitech-django-middlewares.git@v1.0.1
```
 2. Add `sitech_middlewares.request.RequestMiddleware` to `MIDDLEWARE` in settings.py:
 
```bash
 MIDDLEWARE = (
    ...
    'sitech_middlewares.request.RequestMiddleware',
 )
```

## Installation

1. Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install git+https://github.com/sitmena/sitech-django-audit_log.git
```

2. Add `sitech_audit_log` to your `INSTALLED_APPS` in settings.py:
```bash
 INSTALLED_APPS = (
    ...
    'sitech_audit_log',
 )
```
3. Run the migration command:
```bash
 python manage.py migrate
```
<br>

## Customizing the operations being logged
By default the package will log the  `created`,  `updated`,  `deleted`  operations. You can modify this behaviour by setting the  `log_operation`  property on your model.

```python
 from django.db import models
 from sitech_audit_log import AuditLogMixin

 class Profile(models.Model, AuditLogMixin):  
	log_operation = ['updated']
	phone = models.CharField(max_length=255, verbose_name='Phone')
	address = models.TextField(max_length=512,verbose_name='Address')
```	
