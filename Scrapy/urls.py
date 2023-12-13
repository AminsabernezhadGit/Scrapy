
from django.contrib import admin
from django.urls import path

from app.views import TriggerSpiderView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('trigger-spider/', TriggerSpiderView.as_view(), name='trigger_spider'),

]
