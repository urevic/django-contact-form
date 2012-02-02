from django.conf import settings

FROM_EMAIL    = getattr(settings, 'CONTACT_FORM_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
RECIPIENTS    = getattr(settings, 'CONTACT_FORM_RECIPIENTS', settings.MANAGERS)
FAIL_SILENTLY = getattr(settings, 'CONTACT_FORM_FAIL_SILENTLY', False)
