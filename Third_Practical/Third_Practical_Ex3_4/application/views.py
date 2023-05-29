# -*- coding: utf-8 -*-


from django.shortcuts import render
from datetime import datetime 
from django.http import HttpResponse, JsonResponse, FileResponse
import os
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotAllowed, JsonResponse, StreamingHttpResponse, FileResponse
from django.core.files import File
import random

def message(request):
    datalist = []
    # Check if the request method is POST
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        # Append the message data to the file
        with open("db.txt", 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    
    userC = request.GET.get("userC", None)
    # Check if userC is not None
    if userC is not None:
        with open("db.txt", 'r') as f:
            counter = 0
            # Iterate through each line in the file
            for line in f:
                linedata = line.strip().split('--')
                # Check if the first item in the line matches userC
                if linedata[0] == userC:
                    counter += 1
                    # Create a dictionary with message data and add it to the datalist
                    d = {"userA": linedata[1], 'msg': linedata[2], 'time': linedata[3]}
                    datalist.append(d)
                # Break the loop if the counter reaches 10
                if counter >= 10:
                    break
    print(datalist)  # Add this line to check the value of datalist
    return render(request, "temp.html", {"data": datalist})






def response_http(request):
    # Returns a HTTP response with string "Hi, I am Zeyad"
    response = HttpResponse('Hi, I am Zeyad')
    return response


def response_redirect(request):
    # returns redirect to youtube
    response = HttpResponseRedirect('https://www.youtube.com/')
    return response


def response_BR(request):
    # Returns bad request HTTP response
    response = HttpResponseBadRequest('Bad Request')
    return response


def response_Nfound(request):
    # Returns a not found response
    response = HttpResponseNotFound('not found')
    return response
       


def response_ServerErr(request):
    # Returns a server error response
    response = HttpResponseServerError('Error in server')
    return response


def response_NAll(request):
    # Returns a not allowed response
    response = HttpResponseNotAllowed(['GET', 'POST'])
    return response


def response_JSON(request):
    # Returns a JSON response with {'Z': 'Hi'}
    data = {'Z': 'Hi'}
    response = JsonResponse(data)
    return response


def response_stream(request):
    #Returns a live stream for random alphabet
    def generate_random_numbers():
        for _ in range(10):
            random_number = random.randint(1, 100)
            yield str(random_number) + '\n'
    
    return StreamingHttpResponse(generate_random_numbers(), content_type='text/plain')


def response_file(request):
    # Returns a PDF as file response
    file = File(open('Lec.pdf', 'rb'))
    response = FileResponse(file)
    return response


def response_video(request):
    video_file_path = '10 Second Timer.mp4'  #Path for the video

    # Returns a video response
    response = FileResponse(open(video_file_path, 'rb'), content_type='video/mp4')
    return response


def response_Predirect(request):
    # Returns a permenant redirect to youtube
    response = HttpResponsePermanentRedirect('https://www.youtube.com/')
    return response

