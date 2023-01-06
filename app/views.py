from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht
import csv
def dht11(request):
    return render(request, 'index.html')

def dht112(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index2.html', s)
# Create your views here.
def dht113(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index3.html',s)
#Jour1
def data24(request):
    #jr1=Dht.objects.filter(temp__range=(32,34)).values().all()[:5]
    jr1 = Dht.objects.all()[0:32]
    s1={'jr1':jr1}
    return render(request, 'jour1.html',s1)
def data24Graphe(request):
    tab=Dht.objects.all()[0:32]
    s1={'tab':tab}
    return render(request, 'grapheJr1.html',s1)
#Jour2
def data48(request):
    #jr1=Dht.objects.filter(temp__range=(32,34)).values().all()[:5]
    jr2 = Dht.objects.all()[32:64]
    s2={'jr2':jr2}
    return render(request, 'jour2.html',s2)
def data48Graphe(request):
    tab=Dht.objects.all()[32:64]
    s2={'tab':tab}
    return render(request, 'grapheJr2.html',s2)
#jour3
def data72(request):
    #jr1=Dht.objects.filter(temp__range=(32,34)).values().all()[:5]
    jr3 = Dht.objects.all()[144:288]
    s3={'jr3':jr3}
    return render(request, 'jour3.html',s3)
def data72Graphe(request):
    tab=Dht.objects.all()[144:288]
    s3={'tab':tab}
    return render(request, 'grapheJr3.html',s3)
#historique
def historique(request):
    return render(request, 'historique.html')


def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])

    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response



