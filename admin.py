from django.contrib import admin
from .models import Blog, Tag
from django.contrib.auth.models import User, Group
class BlogAdmin(admin.AdminSite):
    site_header = 'Blogger Admin'

admin_site = BlogAdmin(name='BlogAdmin')
admin_site.register(Blog),
admin_site.register(Tag),
admin_site.register(User),
admin_site.register(Group),