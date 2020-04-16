from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from HumanCounter.settings import MEDIA_ROOT

# Create your views here.
def upload_video_yolo(request):
    context = {}
    if request.method == 'POST':
        uploaded_video = request.FILES['video']
        fs = FileSystemStorage()
        name = fs.save(uploaded_video.name, uploaded_video)
        context['upload_url'] = fs.url(name)
    return render(request, 'upload_video_yolo.html', context)