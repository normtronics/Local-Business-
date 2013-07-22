from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout 
from forms import *
from django.core.context_processors import csrf

def main_page(request):
	#template = get_template('main_page.html')
	#variables = Context({
	#	'head_title' : u'Django Bookmarks',
	#	'page_title' : u'Welcome to Django Bookmarks',
	#	'page_body' : u'Where you can store and share bookmarks!'
#	})

	#variables = Context({'user' : request.user})

	#output = template.render(variables)
	#return HttpResponse(output)

	return render_to_response(

		'main_page.html', RequestContext(request)
	)

def user_page(request, username):
	try:
		user = User.objects.get(username = username)
	except User.DoesNotExist:
		raise Http404(u'Requested user not found.')
	bookmarks = user.bookmark_set.all()

	#template = get_template('user_page.html')
	variables = RequestContext(request, {
		'username' : username,
		'bookmarks' : bookmarks
	})

	#output = template.render(variables)
	return render_to_response('user_page.html', variables)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')


def register_page(request):
	if request.method == 'POST':
		form = ResgistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
					username = form.cleaned_data['username'],
					password = form.cleaned_data['password1'],
					email = form.cleaned_data['email']
			)
			return HttpResponseRedirect('/')
	else:
	  form = ResgistrationForm()
	variables = RequestContext(request, {
		'form' : form
	})
	return render_to_response(
		'registration/register.html',
				variables		
	)

