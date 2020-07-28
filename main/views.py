from django.shortcuts import render,redirect
from .models import Gallery
# Create your views here.
def index(request):
	return render(request,'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def services(request):
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