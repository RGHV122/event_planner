from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    path('', views.index,name='index'),
    path("about/", views.about, name="about"),
    path('services/',views.services,name='services'),
    path('gallery/page=<page>',views.gallery,name='gallery'),
    path('gallery/',views.gallery,name='gallery'),
    path('services/',views.services,name='services'),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blog/blogpost/<int:id>", views.blogpost, name="blogpost"),
    path("add-contact-me/",views.contactme, name="contact-me")




]
