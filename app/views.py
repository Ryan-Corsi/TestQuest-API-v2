from turtle import width
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from reportlab.pdfbase.cidfonts import CIDFont, findCMapFile
#from cStringIO import StringIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import StringIO


from PIL import Image


import qrcode





class ProcessosAPIView(APIView):
    
    def get(self, request, pk=""):
        processos = Processo.objects.all()
        serializer = ProcessosSerializer(processos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProcessosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Processo inserido com sucesso..."})

    def put(self, request, pk=''):
        processos = Processo.objects.get(id=pk)
        serializer = ProcessosSerializer(processos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        processos = Processo.objects.get(id=pk)       
        processos.delete()
        return Response({"msg": "Processo deletada..."})

class PessoasAPIView(APIView):
    def get(self, request, pk=""):
        pessoas = Pessoa.objects.all()
        serializer = PessoasGETSerializer(pessoas, many=True)
        return Response(serializer.data)
    
    def post(self, request):      
        serializer = PessoasSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Pessoa inserida com sucesso..."})

    def put(self, request, pk=''):
        pessoas = Pessoa.objects.get(id=pk)
        serializer = PessoasSerializer(pessoas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        pessoas = Pessoa.objects.get(id=pk)       
        pessoas.delete()
        return Response({"msg": "Pessoa deletada..."})

class ProvasAPIView(APIView):
    def get(self, request, pk=""):
        provas = Prova.objects.all()
        serializer = ProvasSerializer(provas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProvasSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Prova inserida com sucesso..."})

    def put(self, request, pk=''):
        provas = Prova.objects.get(id=pk)
        serializer = ProvasSerializer(provas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        provas = Prova.objects.get(id=pk)       
        provas.delete()
        return Response({"msg": "Prova deletada..."})
    
class GabaritoGenerator(APIView):
   
    def get(self, request):
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=2,
        )
        
        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename=gabaritos.pdf'
        p = canvas.Canvas(response)
        
        # for i in range(10):
        #p.drawString(50, 815, "Processo Seletivo Smart Automation")
        #p.drawString(50, 800, "Nome:  Ryan Gabriel Silva Corsi")
        
        
        formato = Image.open(r"C:\Users\COY2CA\Desktop\YYYYY.png")
        p.drawInlineImage(formato, 0, 0) 
        p.drawString(132, 112, "Milena Fernandes da Silva")

        imagem_qrcode = qrcode.make(1)
        
        p.drawInlineImage( imagem_qrcode, 475, 37, width=int(40), height=int(40)) 
        
        p.showPage()
        p.save()
        
        return response



"""
response = HttpResponse()
response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

# Crie o objeto PDF, usando o objeto response como seu "arquivo".
p = canvas.Canvas(response)

# Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
# Veja a documentação do ReportLab para a lista completa de
# funcionalidades.
p.drawString(100, 900, "Hello world.")

# Feche o objeto PDF, e está feito.
p.showPage()
p.save()
return response
"""