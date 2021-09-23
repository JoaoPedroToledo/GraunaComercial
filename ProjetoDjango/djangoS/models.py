from django.db import models

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