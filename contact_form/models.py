from django.db import models
from django.utils.translation import ugettext_lazy as _

from contact_form.conf import settings

if settings.SAVE_TO_DB:
    class ContactMessage(models.Model):
        from_email = models.CharField(_('From'), max_length=250)
        to_email   = models.CharField(_('To'), max_length=250)
        subject    = models.CharField(_('Subject'), max_length=250)
        body       = models.TextField(_('Body'))
        date_sent  = models.DateTimeField(_('Date sent'), auto_now_add=True)
        is_read    = models.BooleanField(_('Is read'), default=False)
        is_replied = models.BooleanField(_('Is replied'), default=False)

        def __unicode__(self):
            return unicode(self.subject)

        class Meta:
            verbose_name = _('Contact message')
            verbose_name_plural = _('Contact messages')
            ordering = ('-date_sent',)
