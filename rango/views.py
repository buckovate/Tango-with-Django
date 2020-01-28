from django.shortcuts import render
from django.http import HttpResponse

def about(request):
	return HttpResponse("Rango says here is the about page. \
        <br/> <a href='/rango/'>index</a>")
	
	
	

def index(request):
	return HttpResponse("Rango says hey there partner! \
        <br/> <a href='/rango/about/'>about</a>")
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)