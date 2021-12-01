import msg91_sms as msgsms
import logging

from django.conf import settings

msg = msgsms.Cspd_msg91(apikey="YOUR MSG91 API KEY")


logger = logging.getLogger()


def send_sms(to, body):
    """Send SMS message."""
    logger.info("send_sms")
    sms_txt = "This is a text SMS from MSG91"
    send_sms_resp = msg.send(4, "TXTIN", "919999999999", sms_txt)
