from django.shortcuts import render, redirect
import os 
from pathlib import Path
import json
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from wordListHub.settings import MEDIA_ROOT
from .forms import *
import io
import zipfile


def sanitize(path):
    requested_path = Path(MEDIA_ROOT) / path
    resolved_path = requested_path.resolve()

    if not resolved_path.is_relative_to(MEDIA_ROOT):
        return None

    if not resolved_path.exists():
        return None

    return resolved_path

def get_file_dir(path):
    path = os.path.join(MEDIA_ROOT, path)

    if os.path.exists(path):
        all_items = [os.path.join(path, x) for x in os.listdir(path)]

        files = []
        dirs = []

        for x in all_items:            
            if os.path.isdir(x):
                dirs.append(x.split(MEDIA_ROOT)[1])
            elif os.path.isfile(x):
                files.append(x.split(MEDIA_ROOT)[1])


        return files, dirs
    else:
        return [], []
    

def view_dir(r):
    path = r.GET.get("path") if r.GET.get("path") else ""
    if path:
        path = path if path != "/" else ""
        path = sanitize(path)

        if path and os.path.isdir(path):
            files, dirs = get_file_dir(path)

            path = r.GET.get("path")
            splited_path = path.split("/")


            if path == "/":
                back_dir = ""
            elif len(splited_path) == 1:
                back_dir = "/"
            else:
                back_dir = "/".join(splited_path[:-1])

            return render(r, "view_dir.html",{"dirs": dirs, "files": files, "back_dir": back_dir, "path":path} )      
        else:
            return HttpResponse("directory is not found", content_type="text/plain")
    else:
        return redirect("/?path=/")
def show_file(r):
    if r.GET.get("file"):
        file = r.GET.get("file")
        file_path = os.path.join(MEDIA_ROOT, file)
        file_path = sanitize(file_path)


        if file_path and os.path.isfile(file_path):

            with open(file_path, "rb") as f :
                return HttpResponse(f.read(), content_type="text/plain")
        else:
            return HttpResponse("file is not found", content_type="text/plain")
    else:
        return redirect("/")
    

def uploadWordlist(r):
    if r.user.is_authenticated and r.user.is_staff:
        if r.method == "POST":
            form = uploadwordlistform(r.POST, r.FILES)

            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                return HttpResponse("invalid file")
        return render(r, "upload.html")
    else:
        return redirect("/")
    

def get_dirs_api(r):
    if r.user.is_authenticated and r.user.is_staff:
        
        data = {}
        dirs = []
        for d in Path(MEDIA_ROOT).rglob("*"):
            if d.is_dir():
                dirs.append(str(d).split(MEDIA_ROOT)[-1]+"/")
        
        data["dirs"] = dirs
        print(data)

        return JsonResponse(data)
    else:
        return HttpResponseForbidden("access denied")
    

def DownloadWordList(request):
    folder_path = MEDIA_ROOT
    zip_filename = "myWordList.zip"

    # Create in-memory buffer
    buffer = io.BytesIO()

    # Create zip file in memory
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Keep folder structure inside zip
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)

    buffer.seek(0)

    # Create HTTP response
    response = HttpResponse(buffer.getvalue(), content_type="application/zip")
    response["Content-Disposition"] = f'attachment; filename="{zip_filename}"'

    return response