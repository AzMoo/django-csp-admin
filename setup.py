from setuptools import find_packages, setup

setup(
    name='django_csp_admin',
    description='Admin interface for Django CSP',
    url='http://gitlab/websites/django-csp-admin',
    author='Matt Magin',
    author_email='matt.magin@cmv.com.au',
    license='Proprietary',
    setup_requires=["setuptools_scm>=1.11.1"],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-csp==3.3',
        'Django==1.11',
    ],
    extras_require={
        'dev': [
            'pre-commit',
            'prospector',
            's3pypi',
            'pytest',
            'pytest-django'
        ]
    }
)
