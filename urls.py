from django.urls import path
from . import views
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',PostListView.as_view(),name='home-home'),
    path('about/',views.about,name='home-about'),
    path('contact/',views.contact,name='home-contact'),
    path('product/',views.product,name='home-product'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)