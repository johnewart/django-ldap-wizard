from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

class DjangoLDAPWizardMiddleware(object):
    def __init__(self):
        'Constructor for DjangoLDAPWizardMiddleware'
        try:
            ldap_url = settings.AUTH_LDAP_SERVER_URI
            self.process_response = self.check_ldap_settings
        except AttributeError:
            self.process_response = self.redirect_to_setup

    def check_ldap_settings(self, request, response):
        return response

    def redirect_to_setup(self, request, response):
        if request.path == "/ldap_wizard/setup/":
            return response
        elif request.path == "/ldap_wizard/setup":
            return response
        else:
            return HttpResponseRedirect("/ldap_wizard/setup/")
		