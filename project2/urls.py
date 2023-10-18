from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.addItem, name="Add Item"),
    path("home_sort/", views.home_sort),
    path("update/<title>/", views.update, name="update"),
    path("<title>/", views.detail),
    path("delete/<title>/", views.delete, name="update"),
    path("home_sort/", views.home_sort)


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
