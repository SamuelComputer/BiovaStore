from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,  ProductDetailView, BlogDetailView

app_name = 'Biova'

namespace ='Biova'

urlpatterns = [
    path('', index, name="index"),
  
    path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)