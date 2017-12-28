from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse("Esta es la pagina principal de la app adopcion")

class SolicitudList(ListView):
    model = Solicitud
    template_name='adopcion/solicitudList.html'

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitudForm.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))
