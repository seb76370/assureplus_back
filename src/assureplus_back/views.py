from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from assureplus_back.models import  files_upload
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt

from pprint import pprint
def index(request):
    return HttpResponse("Welcome to Assureplsu API")

def save_sinitre(request):
    pass


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("in upload files")
            files = request.FILES.getlist('file')
            for file in files:
                _title = form.cleaned_data['title']
                print(_title)
                handle_uploaded_file(file, _title)
            return HttpResponse("OK UPLOAD FILES")
        else:
             return HttpResponse("Form invalid")

def handle_uploaded_file(file, title):
    # Lire le contenu du fichier et le stocker dans la base de données
    instance = files_upload(title=title, file=file)
    instance.save()
