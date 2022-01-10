from django.shortcuts import render
from classify.forms import ContactForm
from classify.predict import breed

def index(request):
    return render(request, 'classify/index.html', context={})
def contact(request):
    rs = "Radhe Shyam"
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        'rs': rs,
        'form': form
    }
    return render(request, 'classify/contact.html', context)

def about(request):
    return render(request, 'classify/about.html')

def works(request):
    return render(request, 'classify/works.html')

def breedify(request):
    
    hk = 'HARE KRSNA'
    if request.method == 'POST':
        pred_breed, image_path = breed(request)
        context = {
            'pred_breed': pred_breed,
            'hk':hk,
            'image_path': image_path
        }
        return render(request, 'classify/breedify.html', context)
    else:
        return render(request, 'classify/breedify.html')
