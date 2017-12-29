## Django CSP Admin

Admin interface for Django CSP. Provides middleware and models to store the CSP configuration. Allows modification of CSP configuration without changing ```settings.py```.

## Code Example

## Installation

Install with the following:

```
pip install django-csp-admin --extra-index-url=http://cmv-pkg-shed.s3-website-ap-southeast-2.amazonaws.com/ --trusted-host=cmv-pkg-shed.s3-website-ap-southeast-2.amazonaws.com
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

Describe and show how to run the tests with code examples.

## License

Proprietry CMV. Will probably open source this in the future.
