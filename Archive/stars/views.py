from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from stars.models import Star, RA, DEC
from django.shortcuts import render_to_response, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from stars.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def index(request):
    return HttpResponse("This is the first view for the app Stars!")
    
class StarList(ListView):
	model = Star
	context_object_name = 'these_are_stars'
	template_name = 'star_list.html'

def homepage(request):
	return render_to_response('stars/Trial.html')
	
def catalog(request):
	entry_list = Star.objects.all()
	paginator= Paginator(entry_list, 50) #50 entries allowed per page
	page = request.GET.get('page')	
	
	try: 
		entries = paginator.page(page)
	except PageNotAnInteger:
		entries = paginator.page(1)
	except EmptyPage:
		entries = paginator.page(paginator.num_pages)
	#the pagination execution in order to have page numbers appear in the website
		
	return render(request, 'stars/catalog.html', {"entries": entries, "entry_list": entry_list})
	
class Detail(DetailView):
	model = Star
	template_name = 'stars/stardetails.html' 

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['enter_email_here']) #contact email should be entered.
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "stars/email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')
    

