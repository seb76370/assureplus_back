import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SinistresForm, UploadFileForm, UsersForm, CommentsForm
from django.views.decorators.csrf import csrf_exempt

from .models import Comments, Sinistres, Users, files_upload
from django.contrib.auth.models import User

from .auth import create_token
from pprint import pprint


#region commons
def index(request):
    user = Users.objects.get(id=7)
    print(user)
    print(create_token(user))
    return HttpResponse("Welcome to Assureplus API")

def not_connected(request):
    return JsonResponse({'code':401,'message':"User not connected"})
#endregion

#region User
@csrf_exempt
@login_required(login_url='/not_connected/', redirect_field_name='next')
def get_user_sinistre(request,id):
    try:
            user = Users.objects.get(id=id)
            sinistres = Sinistres.objects.filter(user=id)
            comments = Comments.objects.filter(sinistre__user=id)
            files = files_upload.objects.filter(sinistre__user=id)

            # Créer un dictionnaire pour stocker les données de l'utilisateur et les données associées
            user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'street': user.street,
                'zipcode': user.zipcode,
                'city': user.city,
                'date_time': user.date_time,
                'contract_number': user.contract_number,
                'sinistres': list(sinistres.values()),
                'comments': list(comments.values()),
                'files': list(files.values()),
            }

            return JsonResponse(user_data)
    except Users.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            # user = User.objects.create_user(username='mon_utilisateur', password='mon_mot_de_passe')
            return HttpResponse('Le formulaire UsersForm a été soumis avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)
                                
@csrf_exempt
@login_required(login_url='/not_connected/', redirect_field_name='next')
def modify_user(request,id):
    try:
        user = Users.objects.get(id=id)
    except Exception:
        return HttpResponse("user unknow")

    if request.method == 'POST':
        form = UsersForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire UsersForm a été update avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)
        
@csrf_exempt
def delete_user(request,id):
    try:
        user = Users.objects.get(id=id)
    except Exception:
        return HttpResponse("user unknow")

    if request.method != 'DELETE':
        return HttpResponse("Not DELETE Request")
    
    datas:dict = get_user_sinistre(None, id)

    print(type(datas))
    files_path:str = f'./archives/user_{id}_contract_{user.contract_number}.json'
    # print(files_path)
    json_object = json.loads(datas.content)
    print(json_object)
    with open(files_path, "w",encoding='utf8') as outfile:
        json.dump(json_object, outfile, indent= 4)
    user.delete()
    return HttpResponse('Le formulaire UsersForm a été update avec succès !')
#endregion

#region sinistre
@csrf_exempt
def save_sinistre(request):
    if request.method == 'POST':
        form = SinistresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire save_sinistre a été soumis avec succès !')
        else:
            return HttpResponse("Form save_sinistre Invalide")

@csrf_exempt
def delete_sinistre(request,id):
    try:
        sinistre = Sinistres.objects.get(id=id)
    except Exception:
        return HttpResponse("Sinistre unknow")

    if request.method != 'DELETE':
        return HttpResponse("Not DELETE Request")
    sinistre.delete()
    return HttpResponse('Le formulaire Sinistre a été supprimer avec succès !')


@csrf_exempt
@login_required(login_url='/not_connected/', redirect_field_name='next')
def modify_sinistre(request,id):
    try:
        sinistre = Sinistres.objects.get(id=id)
    except Exception:
        return HttpResponse("sinistre unknow")

    if request.method == 'POST':
        form = SinistresForm(request.POST,instance=sinistre)
        if form.is_valid():
            form.save()
            return HttpResponse('Le formulaire SinistreForm a été update avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)
#endregion

#region comment
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
def delete_comment(request,id):
    try:
        sinistre = Comments.objects.get(id=id)
    except Exception:
        return HttpResponse("Comment unknow")

    if request.method != 'DELETE':
        return HttpResponse("Not DELETE Request")
    sinistre.delete()
    return HttpResponse('Le formulaire Comment a été supprimer avec succès !')


@csrf_exempt
@login_required(login_url='/not_connected/', redirect_field_name='next')
def modify_comment(request,id):
    try:

        comment = Comments.objects.get(id=id)
        print(comment.sinistre_id)
    except Exception:
        return HttpResponse("comment unknow")

    if request.method == 'POST':
        form = CommentsForm(request.POST,instance=comment)
        if form.is_valid():
            toto_value = form.cleaned_data.get('sinistre')
            print(toto_value)
            form.save()
            return HttpResponse('Le formulaire Formcomments a été update avec succès !')
        else:
            errors = form.errors.as_data()
            return HttpResponse(errors)

#endregion

#region upload
@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return HttpResponse('not a Post Request')
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        # Récupération des données du formulaire
        sinistre_id = form.cleaned_data['sinistre']
        s = Sinistres.objects.get(id=sinistre_id)
        title = form.cleaned_data['title']
        files = request.FILES.getlist('file')
        
        # Création d'un nouvel objet files_upload pour chaque fichier
        for file in files:
            new_file = files_upload(sinistre=s, title=title, file=file)
            new_file.save()
        return HttpResponse('Le formulaire upload a été soumis avec succès !')
    else:
        errors = form.errors.as_data()
        return HttpResponse(errors)
#endregion