# Sitech Django Audit Log
`sitech-django-audit_log` is a Django application and library for  creates an audit history for each model events (create, update and delete)  automatically.

<br/>


## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install git+https://github.com/sitmena/sitech-django-audit_log.git
```

Add `sitech_audit_log` to your `INSTALLED_APPS` in settings.py:
```bash
 INSTALLED_APPS = (
    ...
    'sitech_audit_log',
 )
```
Run the migration command:
```bash
 python manage.py migrate
```
