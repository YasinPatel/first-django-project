from __future__ import unicode_literals
from django.db import models
from django.core import urlresolvers


class BaseModel(models.Model):
    add_common_fields = True
    show_edit_icon = True
    show_view_icon = True
    show_delete_icon = True

    if add_common_fields:
        is_active = models.BooleanField(default=True)
        is_deleted = models.BooleanField(default=False)
        i_by = models.IntegerField(blank=True, null=True)
        u_by = models.IntegerField(blank=True, null=True)
        i_date = models.DateTimeField(auto_now_add=True)
        u_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

    def action_column(self):
        links = ""

        if self.show_edit_icon:
            edit_url = urlresolvers.reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
            edit_link = """
                        <a href='"""+ edit_url +"""' class="btn btn-default btn-sm btn-icon-only">
                            <i class="fa fa-pencil"></i>
                        </a>
                    """
            links += edit_link

        if self.show_view_icon:
            view_url = urlresolvers.reverse("admin:%s_%s_view" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
            view_link = """<a href='"""+view_url+"""' class='btn btn-default btn-sm btn-icon-only'>
                        <i class='fa fa-info'></i>
                    </a>"""
            links += view_link

        if self.show_delete_icon:
            delete_link = urlresolvers.reverse("admin:%s_%s_delete" %(self._meta.app_label, self._meta.model_name))
            delete_link = """
                        <a id="delete-status" data-slug-id='""" + str(self.pk) + """' data-url='""" + delete_link + """' href='javascript:void(0);' class="btn btn-default btn-sm btn-icon-only">
                                <i class="fa fa-trash"></i>
                        </a>
                      """
            links += delete_link

        return links

    action_column.allow_tags = True
    action_column.short_description = "actions"


    def status_column(self):
        data_url = urlresolvers.reverse("admin:%s_%s_changestatus" %(self._meta.app_label, self._meta.model_name))
        inactive = "<a data-slug-id='"+str(self.pk)+"' data-url='"+ data_url +"' href='javascript:void(0);' id='change-status' class='label label-danger'>Inactive</a>"
        active = "<a data-slug-id='"+str(self.pk)+"' data-url='"+ data_url +"' href='javascript:void(0);' id='change-status' class='label label-success'>Active</a>"

        if self.is_active:
            return active
        else:
            return inactive

    status_column.allow_tags = True
    status_column.short_description = "Status"
