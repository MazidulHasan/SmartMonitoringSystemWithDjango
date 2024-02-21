from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings
from pathlib import Path

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

def delete_file(request,id):
    queryset = fileupload.objects.get(id=id)
    file_name = os.path.normpath(queryset.file_name.name)  # Normalize the file path
    print("File name is ::::::::::::::::::::::::::::::::::::")
    print(file_name)
    queryset.delete()
    print("settings.BASE_DIR")
    print(settings.BASE_DIR)

    # Additional directories to append to the file path
    additional_directories = ['public', 'static',]

    # Construct the full file path by joining all directories
    file_path = os.path.join(settings.BASE_DIR, *additional_directories, file_name)

    print(file_path)
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print("File deleted")
    else:
        print("File not found")
    return redirect('/uploadedFileList/')