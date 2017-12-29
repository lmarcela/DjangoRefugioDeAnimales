from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Views

def listado(request):
	lista = serializers.serialize('json', Mascota.objects.all().order_by('id'))
	return HttpResponse(lista, content_type='application/json')

def index(request):
    return render(request,'mascota/index.html')

def mascota_view(request):
    if request.method=='POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    else:
        form = MascotaForm()
    return render(request,'mascota/mascotaForm.html',{'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request,'mascota/mascotaList.html',contexto)

def mascota_edit(request,id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method=='GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST,instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request,'mascota/mascotaForm.html',{'form':form})

def mascota_delete(request,id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method=='POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(request,'mascota/mascotaDelete.html',{'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascotaList2.html'
    paginate_by = 5    
    ordering = ['id']

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascotaForm.html'
    success_url = reverse_lazy('mascota_listar2')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascotaForm.html'
    success_url = reverse_lazy('mascota_listar2')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascotaDelete2.html'
    success_url = reverse_lazy('mascota_listar2')

