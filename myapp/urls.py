from django.urls import path
from myapp.views import index, product, about, blog, round_neck, polo, jersey, hoodie, cap, screen, sublimation, embroidery, dtf, quoteform, quotedata

urlpatterns = [
    path('', index),
    path('product/', product),
    path('about/', about),
    path('blog/', blog),
    path('round_neck/', round_neck),
    path('polo/', polo),
    path('jersey/', jersey),
    path('hoodie/', hoodie),
    path('cap/', cap),
    path('screen', screen),
    path('sublimation/', sublimation),
    path('embroidery/', embroidery),
    path('dtf/', dtf),
    path('quote/', quoteform, name='quote_form'),
    path('quotedata/', quotedata)
]

