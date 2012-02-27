from django.conf.urls.defaults import *

urlpatterns = patterns('django_ldap_wizard',
	url(r'/?ldap_wizard/setup/?', 'views.setup', name='ldap-wizard-setup'),
)
