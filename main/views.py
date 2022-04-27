from django.shortcuts import render

def main_page(rq):
    return render(rq, 'home/index.html')


