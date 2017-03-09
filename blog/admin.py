from django.contrib import admin
from .models import Post
from .forms import PostAdminForm
from django.shortcuts import HttpResponse,HttpResponseRedirect,reverse,redirect,render

# Register your models here.

from helpers.admin import CommonAdmin


@admin.register(Post)
class PostAdmin(CommonAdmin):
    list_display = ['title','status_column','action_column']
    search_fields = ['title']
    list_display_links = None
    form = PostAdminForm

    def view(self,request,objectid):
        return render(request,'admin/blog/view.html',context={})

# admin.site.register(Blog,BlogAdmin)
