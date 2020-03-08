from typing import Dict, Any

from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
#from Linkedin_Webscrapping import *

@csrf_exempt
#@require_POST
def UserInput(request):
    if request.method == 'POST':
        if request.POST.get( 'Email' ) and request.POST.get( 'Keyword' ):
            post = UserInsert()
            post.Email= request.POST.get( 'Email' )
            post.Keyword = request.POST.get( 'Keyword' )
            post.Location = request.POST.get( 'Location' )
            post.CV = request.POST.get( 'CV' )
            post.save()
            return render( request, 'UserInput.html' )
    else:
        return render( request, 'UserInput.html' )
