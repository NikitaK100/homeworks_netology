from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv 


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        stations_list = []
        csv_reader = csv.DictReader(file)
        for bus_stations in csv_reader:
             stations_list.append({'Name': bus_stations.get('Name'), 'Street': bus_stations.get('Street'), 'District': bus_stations.get('District')})
        page_number = request.GET.get('page')
        paginator = Paginator(stations_list, 10)
        page = paginator.get_page(page_number)
        print(paginator.num_pages)
        context = {'bus_stations': page,
                   'page': page}
        return render(request, 'stations/index.html', context=context)
