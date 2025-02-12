from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path("",views.Homeview,name="home"),
    path('create/', views.CreateView, name='create_product'),
    path('search/<int:product_id>/', views.SearchView, name='search_product'),
    path('update/<int:product_id>/', views.UpdateView, name='update_product'),
    path('delete/<int:product_id>/', views.DeleteView, name='delete_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)