from django.http import HttpResponse
from django.shortcuts import render
from . import counter

def home(request):
	return render(request,'index.html',{'key1':'I am well python'})

def result(request):
	# name  = request.GET['user_name']
	# age  = request.GET['user_age']
	# message = f"Hi, {name} is {age} year old"
	# return render(request,'result.html',{'name':name,'age':age,'message':message})
	article = request.GET['article']
	var_dict,word_count = counter.count(article)
	return render(request,'result.html',{'article':article,'word_count':word_count,'dict_words':var_dict})