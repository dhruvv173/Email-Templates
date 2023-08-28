from email.utils import formataddr
import django
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
django.setup()


def sendAffiliateMail():
    subject = "Welcome to our waitlist"
    name = "Cench"
    context = {
        'name': name,
    }

    recipient_email = "c2cc@mailinator.com"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/waitlist.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        print("Affiliate email sent")
    except Exception as e:
        print(f"failed due to {e}")


def sendPromoMail():
    subject = "Congratulations! You have won a Promo Code!"
    name = "Cench"
    promo_code = "x12badsas"
    context = {
        'name': name,
        'promo_code': promo_code
    }
    recipient_email = "c2cee@mailinator.com"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/promo.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        print("Promo email sent")
    except Exception as e:
        print(f"failed due to {e}")


def sendNewPartnerMail():
    subject = "Request accepted. <OutletName> and you are now Preferred Partners!"
    name = "Cench"
    outletName = "JP"
    outletCategory = "Finance"
    outletSubCategory = "Banking"
    outletDescription = "Lorem Ipsum"
    context = {
        'name': name,
        'outletName': outletName,
        'outletCategory': outletCategory,
        'outletSubCategory': outletSubCategory,
        'outletDescription': outletDescription,
    }
    recipient_email = "c2cc@mailinator.com"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/new_partner.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        print("New Partner email sent")
    except Exception as e:
        print(f"failed due to {e}")


def offerExpired():
    subject = "Your offer has expired! Update now."
    OfferTitle = "asda"
    OfferValue = "3000"
    OfferExpiryDate = "Today"
    context = {
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferExpiryDate': OfferExpiryDate
    }
    recipient_email = "c2cc@mailinator.com"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/offer_expired.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        print("Offer Expired email sent")
    except Exception as e:
        print(f"failed due to {e}")
