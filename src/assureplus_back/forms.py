from django import forms
from .models import Users, Sinitres, Comments, files_upload

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'street', 'zipcode',
                   'city', 'contract_number')

class SinitresForm(forms.ModelForm):
    class Meta:
        model = Sinitres
        fields = ('user', 'description',)

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('sinitre', 'comment','date',)
from django import forms

class MultiFileField(forms.FileField):
    widget = forms.ClearableFileInput(attrs={'multiple': True})

class UploadFileForm(forms.Form):
    sinistre = forms.IntegerField()
    title = forms.CharField(max_length=50)
    file = MultiFileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sinistre'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control-file'

# class MultiFileField(forms.FileField):
#     widget = forms.ClearableFileInput(attrs={'multiple': True})

# class UploadFileForm(forms.Form):
#     Sinitre = forms.IntegerField()
#     title = forms.CharField(max_length=50)
#     file = MultiFileField()





