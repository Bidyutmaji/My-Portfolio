from django.urls import path
from classify.views import breedify, index, contact, about, works
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name='index' ),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('works/breedify', breedify, name='breedify'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)