from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def services(request):
	colors=['#0275d8','#5cb85c','#5bc0de','#f0ad4e','#d9534f']
	return render(request,'main/services.html',{'colors':colors})

