from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import IdoloList, IdoloCreate, IdoloUpdate , IdoloDelete 
urlpatterns = [
    path('listar_idolo/', IdoloList.as_view(), name="idolo_list"),
    path('crear_idolo/', IdoloCreate.as_view(), name="idolo_form"),
    path('editar_idolo/<int:pk>', IdoloUpdate.as_view(), name="idolo_update"),
    path('borrar_idolo/<int:pk>', IdoloDelete.as_view(), name="idolo_borrar"),
]


