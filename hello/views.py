from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from uuid import uuid4

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def upload_file(request):
    print('Uploading stuff')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('./' + uuid4().hex + '.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def db(request):

    if request.method == 'POST':
        eq = request.POST.get('eq', '')
        print (eq)
        # equation = Equation()
        # equation.content = eq
        # equation.save()

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
