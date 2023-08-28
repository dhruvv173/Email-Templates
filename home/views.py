from django.http import HttpResponse
from django.shortcuts import redirect
from .utils import sendAffiliateMail, sendPromoMail, sendNewPartnerMail, offerExpired


def affiliate(request):
    sendAffiliateMail()
    return HttpResponse()


def promo(request):
    sendPromoMail()
    return HttpResponse()


def newPartner(request):
    sendNewPartnerMail()
    return HttpResponse()


def offerExpiry(request):
    offerExpired()
    return HttpResponse()
