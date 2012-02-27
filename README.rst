====================
Django LDAP Wizard
====================

The Django LDAP Wizard is a tool to help you setup your LDAP connection for authentication in your application.
As a middleware component, it ensures that your LDAP configuration is setup and working, and if it's not, it helps you 
to set it up. 

Currently, this is a fairly limited library and likely only useful for internal applications as it would present 
any user with an LDAP configuration page if the LDAP server stopped working, which is probably less than desirable 
behavior in a public application.

* Note: The Django LDAP Wizard has been developed against on Django 1.2 and newer.

Installation
============

#. Add the `django_ldap_wizard` directory to your Python path.

#. Add the following middleware to your project's `settings.py` file:

	``'django_ldap_wizard.middleware.DjangoLDAPWizardMiddleware',``

   Being middleware, the LDAP connection will be tested, if it fails then the user
   is redirected to a page to test the configuration. 
   

Things to do
============

- Add a feature to only display the configuration page if you are coming from some particular IP or set of IPs
