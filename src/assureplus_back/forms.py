from django import forms
from .models import Users, Sinistres, Comments, files_upload

class UsersForm(forms.ModelForm):
    class Meta:     
        model = Users
        fields = ('first_name', 'last_name', 'email','street', 'zipcode',
                   'city', 'contract_number')

class SinistresForm(forms.ModelForm):
    class Meta:
        model = Sinistres
        fields = ('user', 'description',)

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('sinistre', 'comment',)
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







