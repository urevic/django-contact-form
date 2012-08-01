from django.contrib import admin
from django.utils.translation import ugettext as _

from contact_form.conf import settings


if settings.SAVE_TO_DB:
    from contact_form.models import ContactMessage


    class ContactMessageAdmin(admin.ModelAdmin):
        list_display = ('subject', 'from_email', 'to_email', 'date_sent', 'is_read', 'is_replied')
        list_filter = ('is_replied', 'is_read')
        search_fields = ('subject', 'from_email', 'to_email', 'body')
        date_hierarchy = ('date_sent')
    admin.site.register(ContactMessage, ContactMessageAdmin)
