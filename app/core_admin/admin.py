from django.contrib import admin
from core_admin.models import \
	Organization,\
	Subscription,\
	User

admin.site.register(Organization)
admin.site.register(Subscription)
admin.site.register(User)
