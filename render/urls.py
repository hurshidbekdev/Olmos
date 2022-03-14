from django .urls import path
from .views import home
from .views import QULJANGI
from .views import Bodybuild
from .views import Fitnes
from .views import OlmosMarosimi


urlpatterns = [
    path('',home,name='home'),
    path('QULJANGI',QULJANGI, name='QULJANGI'),
    path('Fitnes',Fitnes, name='Fitnes'),
    path('Bodybuild',Bodybuild, name='Bodybuild'),
    path('OlmosMarosimi',OlmosMarosimi,name='OlmosMarosimi')
]

