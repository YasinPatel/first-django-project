import json
from django.contrib import admin
from django.conf.urls import url
from django.shortcuts import HttpResponse,HttpResponseRedirect,reverse,redirect,render
from django.core import urlresolvers
from django.contrib import messages

class CommonAdmin(admin.ModelAdmin):

    class Meta:
        abstract = True

    def get_actions(self, request):
        actions = super(CommonAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    # IF IS DELETED COLUMN IS NOT THERE INHERIT THIS VIEW INTO YOUR ADMIN  ( NOTE THAT I_BY FIELD IS NAMED ON YOUR MODEL )
    def get_queryset(self, request):
        qs = super(CommonAdmin, self).get_queryset(request)
        qs = qs.filter(is_deleted=False).order_by("-pk")
        if request.user.is_superuser:
            return qs
        return qs.filter(i_by=request.user.id)

    def get_urls(self):
        urls = super(CommonAdmin, self).get_urls()
        my_urls = [
            url(r'^view/(?P<objectid>[0-9]+)/$', self.view, name="{0}_{1}_{2}".format(self.model._meta.app_label, self.model._meta.model_name,'view')),
            url(r'^delete/$', self.delete, name="{0}_{1}_{2}".format(self.model._meta.app_label, self.model._meta.model_name,'delete')),
            url(r'^change_status/$', self.change_status, name="{0}_{1}_{2}".format(self.model._meta.app_label, self.model._meta.model_name,'changestatus')),
        ]
        return my_urls + urls

    def view(self,request,objectid):
        return render(request,'admin/company/view.html',context={})

    def change_status(self, request):
        if not request.user.has_perm('{0}.change_{1}'.format(self.model._meta.app_label,self.model._meta.model_name)):
            raise PermissionDenied
        objectid = request.POST.get('data-id')
        obj = self.model.objects.filter(id=objectid).first()

        if obj.is_active:
            obj.is_active = False
        else:
            obj.is_active =  True
        obj.save()

        return_arr = {}
        return_arr['active'] = "yes" if obj.is_active else "no"
        return_arr['data-slug-id'] = obj.id
        return_arr['data-url'] = urlresolvers.reverse("admin:%s_%s_changestatus" %(self.model._meta.app_label, self.model._meta.model_name))
        return HttpResponse(json.dumps(return_arr))

    def delete(self, request):
        if not request.user.has_perm('{0}.change_{1}'.format(self.model._meta.app_label,self.model._meta.model_name)):
            raise PermissionDenied
        objectid = request.POST.get('data-id')
        obj = self.model.objects.filter(id=objectid).first()
        obj.is_deleted =  True
        obj.save()
        messages.success(request, '{0} is deleted successfully.'.format(self.model._meta.app_label))
        return HttpResponse("success")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = '{0} List'.format(str(self.model._meta.app_label).title())
        extra_context['link'] = 'add'
        extra_context['addtitle'] = 'Add new {0}'.format(self.model._meta.app_label)
        return super(CommonAdmin, self).changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('admin/appjs/common.js',)
