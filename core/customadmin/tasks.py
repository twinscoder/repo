from celery.decorators import task
from .helpers import email, twilio


@task
def send_welcome_email(invite_pk):
    """Wrapper around method so we can use it as a celery task."""
    return email.send_welcome_email(invite_pk)


@task
def send_sms(to, body):
    """Wrapper around method so we can use it as a celery task."""
    return twilio.send_sms(to=to, body=body)
