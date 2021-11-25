import logging
import os

import html2text
import htmlmin
from django.apps import apps
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger()


def html_to_text(html):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_tables = True
    return h.handle(html)


def send_welcome_email(customer_pk, extra_context=None):
    """Send an email when a visitor checks in with thier signed legal docs
    as attachments."""
    logger.info("send_welcome_email")
    # Avoid circular import - better way through re-organization?
    Customer = apps.get_model("customer", "customer")
    customer = Customer.objects.get(pk=customer_pk)
    site = Site.objects.get_current()

    to_emails = [customer.email]

    if settings.DEBUG:
        to_emails = ["admin@gmail.com"]  # For testing in sandbox
    context = {
        "customer": customer,
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "site": site,
    }
    if extra_context:
        context.update(extra_context)
    html_message = render_to_string("email/welcome.html", context)
    txt_message = html_to_text(html_message)

    html_message = htmlmin.minify(html_message, remove_empty_space=True)

    # Send to visitor with attachments (BCC the host)
    msg = EmailMultiAlternatives(
        subject="Quickly Ecommerce Registration Confirmation",
        body=txt_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_emails,
    )

    msg.attach_alternative(html_message, "text/html")
    msg.send()
    return customer_pk
