from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT

# Create your views here.
def upload_image_yolo(request):
    context = {}
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['upload_url'] = fs.url(name)
    return render(request, 'upload_image_yolo.html', context)