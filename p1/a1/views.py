from django.shortcuts import render, redirect
from pytube import *

# Create your views here.


  
# defining function
def home(request):
  
    # checking whether request.method is post or not
    if request.method == 'POST':
        
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
  
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
          
        # downloads video
        stream.download()
  
        # returning HTML page
        return render(request, 'index.html')
    return render(request, 'index.html')