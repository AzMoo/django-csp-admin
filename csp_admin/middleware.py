try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from .models import BOOL_DIRECTIVES, CSPDirective


class DjangoCSPAdminMiddleware(MiddlewareMixin):
    """
    Middleware to add the CSP configuration to the response.

    This middleware must come *after* the Django CSP middlware,
    as middlware is iterated in reverse for the response cycle
    and we need to set the config before we get to the
    Django-CSP middleware.
    """

    def process_response(self, request, response):
        """
        Django-CSP looks for its config in the _csp_config
        property on the response, so we are getting the config
        from the database and adding it to the response.
        """

        config = {}

        for d in CSPDirective.objects.filter(enabled=True):
            if d.name in BOOL_DIRECTIVES:
                config[d.name] = True
            else:
                config[d.name] = list(
                    d.directive_values.values_list('value', flat=True))

        response._csp_config = config  # pylint: disable=protected-access

        return response
