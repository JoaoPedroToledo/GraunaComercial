from django.db import models
from django import forms

class ClienteModel(models.Model):
    id_cliente=models.IntegerField(primary_key=True)
    nome_empresa=models.CharField(max_length=100)
    class Meta:
         db_table = "cliente"


class EmpresaModel(models.Model):
    id_empresa=models.IntegerField(primary_key=True)
    nome_funcionario=models.CharField(max_length=100)
    class Meta:
         db_table = "empresa"

class MaterialModel(models.Model):
    id_material=models.IntegerField(primary_key=True)
    material=models.CharField(max_length=100)
    class Meta:
         db_table = "materia_prima"


class TratamentoSuperficialModel(models.Model):
    id_superf=models.IntegerField(primary_key=True)
    nome_tratamento=models.CharField(max_length=100)
    class Meta:
         db_table = "tratamento_superficial"

class TratamentoTermicoModel(models.Model):
    id_termico=models.IntegerField(primary_key=True)
    nome_trat_termico=models.CharField(max_length=100)
    class Meta:
         db_table = "tratamento_termico"


class AnaliseCriticaModel(models.Model):
    numero_cotacao=models.CharField(max_length=100)
    cliente=models.CharField(max_length=50)
    contato=models.CharField(max_length=50)
    materia_prima=models.CharField(max_length=50)
    pn=models.CharField(max_length=50)
    rev=models.CharField(max_length=50)
    data=models.DateTimeField()
    assinatura=models.CharField(max_length=50)
    class Meta:
        db_table = "AnalisedaCotacao"