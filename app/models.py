from django.db import models

# Create your models here.

class Processo(models.Model):
    titulo  =  models.CharField(max_length=55, null=False)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Prova(models.Model):
    idProcessoFK = models.ForeignKey(Processo, related_name="processo_1", on_delete=models.CASCADE)
    qtdQuestoes = models.IntegerField(null=False)
    qtdAlternativas = models.IntegerField(null=False)
    gabaritoPadrao = models.CharField(max_length=200, null=False)
    dtProva = models.DateField(null=False)
    
    def __str__(self):
        vetor = str(self.dtProva).split("-")
        return f'{vetor[2]}/{vetor[1]}/{vetor[0]}' + " | " + str(self.idProcessoFK)

class Pessoa(models.Model):
    nome = models.CharField(max_length=55, null=False)
    idProcessoFK = models.ForeignKey(Processo, related_name="processo_0", on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=False)
    provaFK = models.ForeignKey(Prova, related_name="prova", on_delete=models.CASCADE, null=True, blank=True)
    respostas = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    etnia = models.CharField(max_length=200)
    pcd = models.BooleanField(default=False)
       
    
    def __str__(self):
        return self.nome

    
        
