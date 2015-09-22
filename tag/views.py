from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView
from .models import Tag
from .models import Callbacks
from .forms import regTagForm
from datetime import datetime
import json
import urllib2

HARDCODED_PASS = 'password'

def index(request):
	return HttpResponse("")


def callback(request):
	if request.GET.get('a'):
		akey = request.GET.get('a','')
		#return HttpResponse("{}".format(akey))
		try:
			atag = Tag.objects.get(key = akey)
			#return HttpResponse("{}".format(tag.title))
			atime = datetime.now()
			aip = request.META.get('REMOTE_ADDR')
			auser_agent = request.META['HTTP_USER_AGENT']
			#return HttpResponse("{0}, {1}, {2}".format(atime, aip, auser_agent))
			call = Callbacks(tag=atag, date=atime, ip=aip, ua=auser_agent)
			call.save()
			# For Debugging
			#return HttpResponse("Item: {0}, phoned home at: {1}. From {2}, with the user_agent: {3}".format(atag.title, atime, aip, auser_agent))
			return HttpResponse("")
		except:
			# For Debugging
			#return HttpResponse("Not a legit key")
			return index(request)
	else:
		return index(request)


def dump(request):
	if request.GET.get('pwd','') == HARDCODED_PASS:
		response = []
		for event in Callbacks.objects.all():
			log = "Item: {0}, phoned home at: {1}, from {2}, with the user_agent: {3} <br>".format(event.tag.title, event.date, event.ip, event.ua)
			response.append(log)
		return HttpResponse(response)
	else: return index(request)

def regTag(request):
	if request.POST:
		campaign = request.POST.get('campaign','')
		title = request.POST.get('title','')
		key = request.POST.get('key','')
		tag_type = request.POST.get('type','')
		time =  datetime.now()		
		tag = Tag(campaign=campaign, title=title, key=key, type=tag_type, pub_date=time)
		tag.save()
		if tag_type == "html":
			src_ip = urllib2.urlopen("http://icanhazip.com").read()
			src_ip = ''.join(src_ip.split())
			html_payload = "&ltimg src='http://{0}/s?a={1}'&gt".format(src_ip, key)
			return HttpResponse("Use this for your html payload: {}".format(html_payload))
		elif tag_type == "php":
			src_ip = urllib2.urlopen("http://icanhazip.com").read()
			src_ip = ''.join(src_ip.split())
			php_payload = "$r = new HttpRequest('http://{0}/s?a={1}', HttpRequest::METH_GET); $r->send();".format(src_ip, key)
			return HttpResponse("Use this for your php payload: {}".format(php_payload))
		else: return HttpResponse("Tag added, please construct a callback using {}".format(key))
	else:
		if request.GET.get('pwd','') == HARDCODED_PASS:
			form = regTagForm()
			return HttpResponse(render(request, 'tag/regTagForm.html', {'form':form}))
		else: return index(request)
		



