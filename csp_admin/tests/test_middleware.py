# pylint: disable=protected-access

import pytest
from csp.middleware import CSPMiddleware
from csp_admin.middleware import DjangoCSPAdminMiddleware
from csp_admin.models import CSPDirective, CSPDirectiveValue
from django.http import HttpResponse
from django.test import RequestFactory

csp_mw = CSPMiddleware()
mw = DjangoCSPAdminMiddleware()
rf = RequestFactory()


@pytest.mark.django_db
def test_no_header():
    request = rf.get('/')
    response = HttpResponse()
    mw.process_response(request, response)
    csp_mw.process_response(request, response)
    assert 'content-security-policy' in response._headers
    assert response._headers['content-security-policy'] == (
        'Content-Security-Policy', '')


@pytest.mark.django_db
def test_default_src():
    d = CSPDirective.objects.create(name='default-src', enabled=True)
    CSPDirectiveValue.objects.create(directive=d, value="'self'")
    request = rf.get('/')
    response = HttpResponse()
    mw.process_response(request, response)
    csp_mw.process_response(request, response)
    assert 'content-security-policy' in response._headers
    assert response._headers['content-security-policy'] == (
        'Content-Security-Policy', "default-src 'self'")
