from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from main.views import SuccessView, CancelView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/',SuccessView.as_view(), name='success'),
    # path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
   
   
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

