from rest_framework import serializers
from .models import *

class ProcessosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Processo
        fields = '__all__'

        
    
class ProvasSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Prova
        fields = '__all__'
        
class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Pessoa
        fields = '__all__'

class PessoasGETSerializer(serializers.ModelSerializer):
    
    idProcessoFK = ProcessosSerializer(read_only=True)
    provaFK = ProvasSerializer(read_only=True)
    class Meta:
        many = True
        model = Pessoa
        fields = '__all__'
        
class GabaritoIASerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = GabaritoIA
        fields = '__all__'