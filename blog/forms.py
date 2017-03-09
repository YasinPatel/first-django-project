from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].widget.attrs['class'] = 'form-control'
    class Meta:
        model=Post
        fields=('title','text')


class PostAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].widget.attrs['class'] = 'form-control'

    class Meta:
        model=Post
        # fields=('title','text')
        exclude = ['i_by','u_by','is_active','is_deleted','author']
