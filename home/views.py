from django.http import JsonResponse
from django.shortcuts import redirect
from email.utils import formataddr
import django
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
django.setup()


def AffiliateMail(request):
    subject = "Thank You for Joining the XIRCLS Influencer Program Waitlist!"
    name = ""
    context = {
        'name': name,
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/waitlist.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def OfferExpiryMail(request):
    subject = "Your offer is expiring in 14/7/3 days / today. Update now!"
    OfferTitle = ""
    OfferValue = ""
    OfferCode = ""
    OfferExpiryDate = ""
    context = {
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferCode': OfferCode,
        'OfferExpiryDate': OfferExpiryDate
    }

    recipient_email = "dhruv.parmar_19@sakec.ac.in"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/offer_expiry.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def OfferExpiredMail(request):
    subject = "Your offer has expired! Update now"
    OfferTitle = ""
    OfferValue = ""
    OfferCode = ""
    OfferExpiryDate = ""
    context = {
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferCode': OfferCode,
        'OfferExpiryDate': OfferExpiryDate
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/offer_expired.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def NewPartnerMail(request):
    outletName = ""
    subject = f"Request accepted. {outletName} and you are now Preferred Partners!"
    name = ""
    outletCategory = ""
    outletSubCategory = ""
    outletDescription = ""
    context = {
        'name': name,
        'outletName': outletName,
        'outletCategory': outletCategory,
        'outletSubCategory': outletSubCategory,
        'outletDescription': outletDescription
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/new_partner.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def NewOnTheNetworkMail(request):
    outletName = ""
    subject = f"{outletName} has joined the network and is looking for partners!"
    outletCategory = ""
    outletSubCategory = ""
    outletDescription = ""
    outletUrl = ""
    context = {
        'outletName': outletName,
        'outletCategory': outletCategory,
        'outletSubCategory': outletSubCategory,
        'outletDescription': outletDescription,
        'outletUrl': outletUrl
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/new_on_the_network.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def NewCustomerAcquired(request):
    subject = "You just acquired a customer from {{ outletName }}!"
    outletName = ""
    Name = ""
    Email = ""
    Mobile = ""
    OfferTitle = ""
    OfferValue = ""
    OfferCode = ""
    TransactionAmount = ""
    outletCategory = ""
    outletSubCategory = ""
    outletDescription = ""
    outletUrl = ""
    context = {
        'outletName': outletName,
        'outletCategory': outletCategory,
        'outletSubCategory': outletSubCategory,
        'outletDescription': outletDescription,
        'outletUrl': outletUrl,
        'TransactionAmount': TransactionAmount,
        'Name': Name,
        'Email': Email,
        'Mobile': Mobile,
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferCode': OfferCode,
        'outletUrl': outletUrl
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/new_customer_acquired.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def CustomerRetained(request):
    subject = "You just retained a customer!"
    Name = ""
    Email = ""
    Mobile = ""
    OfferTitle = ""
    OfferValue = ""
    OfferCode = ""
    TransactionAmount = ""
    context = {
        'TransactionAmount': TransactionAmount,
        'Name': Name,
        'Email': Email,
        'Mobile': Mobile,
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferCode': OfferCode,
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/customer_retained.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def CampaignLive(request):
    CampaignType = ""
    subject = f"Your {CampaignType} campaign is live!"
    context = {
        'CampaignType': CampaignType,
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/campaign_live.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SniperLive(request):
    subject = "Congratulations! Your Sniper campaign is live."

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Sniper/sniper-live.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SniperResumed(request):
    subject = "You’ve resumed your Sniper campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Sniper/sniper-resumed.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SniperStopped(request):
    subject = "You’ve stopped your Sniper campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Sniper/sniper-stopped.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SniperAdminResumed(request):
    OutletName = ""
    subject = f"{OutletName} has resumed its Sniper campaign!"
    context = {
        'OutletName': OutletName
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/Sniper/Admin/sniper-resumed.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SniperAdminStopped(request):
    OutletName = ""
    subject = f"{OutletName} has stopped its Sniper campaign!"
    Merchant_Contact_Details = ""
    context = {
        'Merchant_Contact_Details': Merchant_Contact_Details
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/Sniper/Admin/sniper-stopped.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SemperFiLive(request):
    subject = "Congratulations! Your Semper Fi campaign is live."

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/SemperFi/semperfi-live.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SemperFiStopped(request):
    subject = "You’ve stopped your Semper Fi campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/SemperFi/semperfi-stopped.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SemperFiResumed(request):
    subject = "You’ve resumed your Semper Fi campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/SemperFi/semperfi-resumed.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SemperFiAdminStopped(request):
    OutletName = ""
    subject = f"{OutletName} has stopped its Semper Fi campaign!"
    Merchant_Contact_Details = ""
    context = {
        'OutletName': OutletName,
        'Merchant_Contact_Details': Merchant_Contact_Details
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/SemperFi/Admin/semperfi-stopped.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def SemperFiAdminResumed(request):
    OutletName = ""
    subject = f"{OutletName} has resumed its Semper Fi campaign!"
    context = {
        'OutletName': OutletName,
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/SemperFi/Admin/semperfi-resumed.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InfinitiLive(request):
    subject = "Congratulations! Your Infiniti campaign is live."

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Infiniti/infiniti-live.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InfinitiStopped(request):
    subject = "You’ve stopped your Infiniti campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Infiniti/infiniti-stopped.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InfinitiResumed(request):
    subject = "You’ve resumed your Infiniti campaign!"

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/Infiniti/infiniti-resumed.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InfinitiAdminResumed(request):
    OutletName = ""
    subject = f"{OutletName} has resumed its Infiniti campaign."
    context = {
        'OutletName': OutletName
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/Infiniti/Admin/infiniti-resumed.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InfinitiAdminStopped(request):
    OutletName = ""
    subject = f"{OutletName} has resumed its Infiniti campaign."
    Merchant_Contact_Details = ""
    context = {
        'OutletName': OutletName,
        'Merchant_Contact_Details': Merchant_Contact_Details
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/Infiniti/Admin/infiniti-stopped.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def AddedToInnerXircl(request):
    outletName = ""
    subject = f"Your partner {outletName} has selected your offer to send to its customers!"
    name = ""
    OfferTitle = ""
    OfferValue = ""
    OfferCode = ""
    OfferExpiryDate = ""
    context = {
        'name': name,
        'outletName': outletName,
        'OfferTitle': OfferTitle,
        'OfferValue': OfferValue,
        'OfferCode': OfferCode,
        'OfferExpiryDate': OfferExpiryDate
    }

    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/InnerXIRCL/added_to_inner_xircl.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InnerXirclExpiring(request):
    subject = "Your Inner XIRCL is expiring in 14/7/3 days/ today. Update now!"
    Inner_XIRCL_name = ""
    Location = ""
    Spend = ""
    Offers_Selected = ""
    context = {
        'Inner_XIRCL_name': Inner_XIRCL_name,
        'Location': Location,
        'Spend': Spend,
        'Offers_Selected': Offers_Selected
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/InnerXIRCL/inner_xircl_expiring.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def InnerXirclExpired(request):
    Inner_XIRCL_name = ""
    Inner_XIRCL_summary = ""
    subject = f"Your Inner XIRCL {Inner_XIRCL_name} has expired. Update now!"
    context = {
        'Inner_XIRCL_name': Inner_XIRCL_name,
        'Inner_XIRCL_summary': Inner_XIRCL_summary
    }
    recipient_email = ""
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string(
        'home/InnerXIRCL/inner_xircl_expired.html', context)
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'Email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)


def MerchantSignup(request):
    subject = "Welcome to the world's first network for cross-marketing collaborations!"

    recipient_email = "tanmay.vedpathak@xircls.com"
    sender_name = "XIRCLS"
    from_email = formataddr((sender_name, settings.EMAIL_HOST_USER))
    html_message = render_to_string('home/merchant_signup.html')
    try:
        send_mail(subject, '', from_email, [
                  recipient_email], html_message=html_message)
        response_data = {
            'message': 'email sent'
        }
    except Exception as e:
        response_data = {
            'error': f'Failed due to {e}'
        }

    return JsonResponse(response_data)
