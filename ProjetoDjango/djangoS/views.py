from django.shortcuts import render             
from djangoS.models import ClienteModel, EmpresaModel, MaterialModel

def djangoSCliente(request):
    clienteobj=ClienteModel.objects.all()
    empresaobj=EmpresaModel.objects.all()
    materialobj=MaterialModel.objects.all()    
    return render(request, 'index.html', {"Clientedata": clienteobj, "Empresadata": empresaobj, "Materialdata":materialobj})