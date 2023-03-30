from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from assureplus_back.models import  files_upload
from .forms import SinitresForm, UploadFileForm, UsersForm, CommentsForm
from django.views.decorators.csrf import csrf_exempt

from .models import Comments, Sinitres, Users

from pprint import pprint
def index(request):
    return HttpResponse("Welcome to Assureplus API")


@csrf_exempt
def get_user_sinitre(request):
    user_id = 6
    try:
            user = Users.objects.get(id=6)
            sinitres = Sinitres.objects.filter(user=user_id)
            comments = Comments.objects.filter(sinitre__user=user_id)
            files = files_upload.objects.filter(sinitre__user=user_id)

            # Créer un dictionnaire pour stocker les données de l'utilisateur et les données associées
            user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'street': user.street,
                'zipcode': user.zipcode,
                'city': user.city,
                'contract_number': user.contract_number,
                'sinitres': list(sinitres.values()),
                'comments': list(comments.values()),
                'files': list(files.values()),
            }

            return JsonResponse(user_data)
    except Users.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    return HttpResponse(sinistres)

@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire UsersForm a été soumis avec succès !')
        else:
            return HttpResponse("Form UsersForm Invalide")

@csrf_exempt
def save_sinistre(request):
    if request.method == 'POST':
        form = SinitresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire save_sinistre a été soumis avec succès !')
        else:
            return HttpResponse("Form save_sinistre Invalide")
    
@csrf_exempt
def save_comment(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire CommentsForm a été soumis avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Récupération des données du formulaire
            sinitre_id = form.cleaned_data['sinistre']
            print(sinitre_id)
            s = Sinitres.objects.get(id=sinitre_id)
            title = form.cleaned_data['title']
            files = request.FILES.getlist('file')
            
            # Création d'un nouvel objet files_upload pour chaque fichier
            for file in files:
                new_file = files_upload(sinitre=s, title=title, file=file)
                new_file.save()
            return HttpResponse('Le formulaire upload a été soumis avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)

def handle_uploaded_file(file, title):
    # Lire le contenu du fichier et le stocker dans la base de données
    instance = files_upload(title=title, file=file)
    instance.save()
