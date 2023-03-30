from django import forms


class MultiFileField(forms.FileField):
    widget = forms.ClearableFileInput(attrs={'multiple': True})

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = MultiFileField()

