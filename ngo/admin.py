from django.contrib import admin
from .models import teamMember,Donation,Review

# Register your models here.
admin.site.register(teamMember)
admin.site.register(Donation)
admin.site.register(Review)