from django.db import models

DIRECTIVES = (
    'default-src',
    'script-src',
    'object-src',
    'style-src',
    'img-src',
    'media-src',
    'frame-src',
    'font-src',
    'connect-src',
    'sandbox',
    'report-uri',
    'base-uri',
    'child-src',
    'form-action',
    'frame-ancestors',
    'manifest-src',
    'worker-src',
    'plugin-types',
    'require-sri-for',
    'upgrade-insecure-requests',
    'block-all-mixed-content',
)

DIRECTIVE_CHOICES = [(d, d) for d in DIRECTIVES]


class CSPDirective(models.Model):
    name = models.CharField(
        max_length=255, choices=DIRECTIVE_CHOICES, unique=True)

    class Meta:
        verbose_name = 'CSP Directive'
        ordering = ('name',)

    def __str__(self):
        return self.name


class CSPDirectiveValue(models.Model):
    directive = models.ForeignKey(
        CSPDirective, related_name='directive_values')
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'CSP Directive Value'
