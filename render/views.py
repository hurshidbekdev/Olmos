from django.shortcuts import render
from .models import trenajerlar,quljangi,bodybuild,fitnes,OlmosVideo,JamoaOlmos,MashqVideo,Video3Etaj,Marosim
def home(requaest):
    data={
        'trenaj':trenajerlar.objects.all(),
        'ishchilar':JamoaOlmos.objects.all()
    }
    return render(requaest,'index.html',data)
# Create your views here.

def QULJANGI(requaest):
    part={
        'Ikkinchi':quljangi.objects.all(),
        'videolar':OlmosVideo.objects.all(),
         'mashq':MashqVideo.objects.all(),


    }
    return render(requaest,'QULJANGI.html',part)
def Bodybuild(requaest):
    part={
        'body':bodybuild.objects.all(),
        'videolar':Video3Etaj.objects.all()
    }
    return render(requaest,'bodybuild.html',part)
def Fitnes(requaest):
    dat={
        'fit':fitnes.objects.all()
    }
    return render(requaest,'Fitnes.html',dat)

def OlmosMarosimi(request):
    data={
        'OlmosMarosim':Marosim.objects.all()
    }
    return render(request,'OlmosMarosimi.html',data)

