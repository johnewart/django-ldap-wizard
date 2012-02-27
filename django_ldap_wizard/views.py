from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Template, Context, loader
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group

import django.contrib.auth
import ldap

from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Context, loader
from django.db import models

def setup(request):
    t = loader.get_template('django_ldap_wizard/setup.html')
    successful_connect = False
    
    if request.GET:
        try:
            uri = request.GET.get("ldap_url", "")
            bind_dn = request.GET.get('bind_dn', "")
            bind_pw = request.GET.get('bind_pw', "")
            base_dn = request.GET.get('base_dn', "")

            con = ldap.initialize(uri)
            con.simple_bind_s( bind_dn, bind_pw )
            message = "Successfully tested your connection settings."
            successful_connect = True
        except ldap.SERVER_DOWN:
            message = "Unable to contact LDAP server -- perhaps you specified the wrong URI or the server is not accepting connections"
        except ldap.INVALID_CREDENTIALS:
            message = "Unable to authenticate using those credentials. Please double check them!"
        except ldap.LDAPError, e:
            if type(e.message) == dict and e.message.has_key('desc'):
                message = e.message['desc']
            else: 
                message = "Invalid input data, check your settings"
    else:
        uri = ""
        bind_dn = ""
        bind_pw = ""
        base_dn = ""
        message = ""
        
    ctx = {
        "uri": uri,
        "bind_dn": bind_dn, 
        "bind_pw": bind_pw,
        "base_dn": base_dn, 
        "message": message,
        "success": successful_connect
    }

    c = RequestContext(request, ctx)
    return HttpResponse(t.render(c))
    
