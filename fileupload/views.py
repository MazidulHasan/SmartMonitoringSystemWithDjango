from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings


def uploadfiles(request):
    if request.method == "POST":
        data = request.POST
        
        fileName = request.FILES.get('file_name')
        fileFrom = data.get('file_location')
        camera_number = data.get('camera_number')
        video_record_time  = data.get('video_record_time')

        print(fileName)
        print(fileFrom)
        print(camera_number)
        print(video_record_time)

        fileupload.objects.create(
            file_name = fileName,
            file_from = fileFrom,
            camera_number = camera_number,
            video_record_time = video_record_time
        )
        queryset = fileupload.objects.all()
        context = {'uploadedFiles':queryset}
        return render(request,'files/fileList.html' , context)
    return render(request,'files/uploadFiles.html')

def uploadedFileList(request):
    queryset = fileupload.objects.all()
    context = {'uploadedFiles':queryset}
    return render(request,'files/fileList.html', context)

def delete_file(id):
    queryset = fileupload.objects.get(id=id)
    # file_name = queryset.get(file_name)
    # print(file_name)
    queryset.delete()
    # file_path = os.path.join(BASE_DIR,'/media/'+file_name)
    # print("File paths are..............")
    # print(BASE_DIR)
    # print(file_path)
    # if os.path.exists(file_path):
    #     # Delete the file
    #     os.remove(file_path)
    #     print("File deleted")
    # else:
    #     print("File not found")
    return redirect('/uploadedFileList/')