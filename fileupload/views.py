from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def upload_via_api(request):
    if request.method == "POST":
        data = request.POST
        uploaded_file = request.FILES.get('file_name')
        file_from = data.get('file_location')
        camera_number = data.get('camera_number')
        video_record_time = data.get('video_record_time')
        
        file_path = None  # Define file_path with a default value
        
        # Save the uploaded file to your local directory
        if uploaded_file:
            additional_directories = ['public', 'static','videos']
            file_path = os.path.join(settings.BASE_DIR, *additional_directories, uploaded_file.name)
            # file_path = os.path.join('D:/DjangoProjects/SmartMonitoringSystem/core/public/static/videos/', uploaded_file.name)
            with open(file_path, 'wb') as file:
                for chunk in uploaded_file.chunks():
                    file.write(chunk)
        newFileName = 'videos/'+ uploaded_file.name
        # Save the file details to the database
        fileupload.objects.create(
            file_name=newFileName if newFileName else "",  # Save the file path to the database
            file_from=file_from,
            camera_number=camera_number,
            video_record_time=video_record_time
        )

        # Return a success response
        return JsonResponse({'message': 'File uploaded successfully'})

    return JsonResponse({'message': 'Invalid request method'}, status=405)