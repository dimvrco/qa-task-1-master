from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponseRedirect

urlpatterns = [
	path('', lambda r: HttpResponseRedirect('admin/')),
	path('admin/', admin.site.urls),
]
