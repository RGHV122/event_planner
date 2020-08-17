from django.shortcuts import render,redirect
from .models import Gallery,Blogpost, ContactFormModel
# Create your views here.
def index(request):
	return render(request,'main/index.html')

def about(request):
	return render(request,'main/about.html')

def contact(request):
	return render(request,'main/contact.html')

def services(request):

	colors=['#0275d8','#5cb85c','#5bc0de','#f0ad4e','#d9534f']
	return render(request,'main/services.html',{'colors':colors})
	colors=['#024f37','#02304f','#7dc1e3','#7de395','#897de3']
	return render(request,'main/services.html',{'colors':colors})

from math import ceil
def gallery(request,page=1):
	posts = Gallery.objects.all().order_by('time').reverse()
	last_page=ceil(len(posts)/20)
	page=int(page)
	if(page<1):
		return redirect('/gallery/')
	if(len(posts)<(page-1)*20):
		#error page
		return redirect('/gallery/')
	else:
		posts=posts[20*(page-1):]
	if(len(posts)>20):
		posts=posts[:20]


	return render(request,'main/gallery.html',{'posts':posts,'last_page':last_page,'page':page,'next_page':page+1,'prev_page':page-1})

def blog(request):
	myposts = Blogpost.objects.all()
	print(myposts)
	return render(request,'main/blog.html',
				  {'myposts': myposts})

def blogpost(request, id):
	post = Blogpost.objects.filter(post_id = id)[0]
	print(post)
	return render(request, 'main/blogpost.html',{'post': post})

def handler500(request):
    return render(request, '500.html', status=500)

def contactme(request):
	if request.POST:
		pass
	else:
		return redirect('main:contact')
	first_name  = request.POST.get('firstname')
	last_name  = request.POST.get('lastname')
	email  = request.POST.get('email')
	contact_number = request.POST.get('mobile')
	event_detail  = request.POST.get('eventdetail')

	ContactFormModel.objects.create(first_name=first_name,last_name=last_name,email=email
		,contact_number=contact_number,event_detail=event_detail)
	return redirect('main:contact')
