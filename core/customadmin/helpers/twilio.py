import logging

from django.conf import settings
from twilio.rest import Client

logger = logging.getLogger()


def send_sms(to, body):
    """Send SMS message."""
    logger.info("send_sms")
    client = Client(settings.TWILIO_API_KEY, settings.TWILIO_TOKEN)
    if settings.DEBUG:
        to = "+13212970255"  # Override for testing
    message = client.messages.create(to=to, from_=settings.TWILIO_FROM, body=body)
    print(message.sid)
