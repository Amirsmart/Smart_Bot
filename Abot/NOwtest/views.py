from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
import telebot
import time


def index(request):
    template = loader.get_template('NOwtest/index.html')
    return HttpResponse(template.render())
def send(request):
        post = request.POST['NewPost']
        bot_token='519054224:AAGVqYdFI8KdEny-oUIP956xNLeujJNIvS0'
        bot = telebot.TeleBot(token=bot_token)
        bot.send_message("@testsmart1", post)
        return HttpResponse("Your Post Has Been Sent")
    
