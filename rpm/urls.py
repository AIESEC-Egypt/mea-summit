from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('registration.html/', views.registration, name='registration'),
    path('thankyou.html/', views.thankyou, name='thankyou'),
    path('cart.html/', views.cart, name='cart'),
    path('why.html/', views.egypt, name='egypt'),



]

if settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)