from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("processos/", ProcessosAPIView.as_view(), name="processos"),
    path("processos/<int:pk>/", ProcessosAPIView.as_view(), name="uprocessosParametros"),
    path("pessoas/", PessoasAPIView.as_view(), name="pessoas"),
    path("pessoas/<int:pk>/", PessoasAPIView.as_view(), name="pessoasParametros"),
    path("provas/", ProvasAPIView.as_view(), name="provas"),
    path("provas/<int:pk>/", ProvasAPIView.as_view(), name="provasParametros"),
    path("gabaritos", GabaritoGenerator.as_view(), name="gabaritos") 
]