## Django CSP Admin

Admin interface for Django CSP. Provides middleware and models to store the CSP configuration. Allows modification of CSP configuration without changing ```settings.py```.
I've created this because it got frustrating having to keep adding stuff to ```settings.py``` and committing to source control every time somebody decided to add a new piece
of external javascript.

## Installation

Install with the following:

```
pip install django-csp-admin
```

Add to ```INSTALLED_APPS```:

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'csp_admin',
    ...
)
```

Add to ```MIDDLEWARE_CLASSES``` _below_ ```django-csp``` middleware:

```
MIDDLEWARE_CLASSES = (
    ...
    'csp.middleware.CSPMiddleware',
    'csp_admin.middleware.DjangoCSPAdminMiddleware',
    ...
)
```

Make sure you run migrations to initialise the database!

## Tests

To run tests, create a virtualenv, install package, run pytest:

```
pip install -e .[dev]
pytest
```

## License

MIT License. See ```LICENSE``` file.
