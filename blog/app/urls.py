# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('update_article/<int:pk>/', views.update_article, name='update_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
    path('add/', views.add, name='add'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
