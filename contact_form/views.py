
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView

from contact_form.conf import settings


class CompletedPage(TemplateView):
    template_name = "contact_form/contact_completed.html"


class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        if settings.SAVE_TO_DB:
            from contact_form.models import ContactMessage
            f = form.get_message_dict()
            c = ContactMessage()
            c.from_email = f['from_email']
            c.to_email = f['to']
            c.subject = f['subject'] 
            c.body = f['body']
            c.save()
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("contact_form:completed")

class ContactFormView(ContactFormMixin, FormView):
    template_name="contact_form/contact.html"

class ContactModelFormView(ContactFormMixin, CreateView):
    template_name="contact_form/contact.html"
