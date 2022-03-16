from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic.base import TemplateView

class SvgPageView(TemplateView):
	template_name = "bombero.html"

	def get_context_data(self, **kwargs):
		context = super(SvgPageView, self).get_context_data(**kwargs)
		context['menuInicio'] = False
		context['nombre'] = 'Claudio '
		return context


class SvgPageTwoView(TemplateView):
	template_name = "empresario.html"

	def get_context_data(self, **kwargs):
		context = super(SvgPageTwoView, self).get_context_data(**kwargs)
		context['menuInicio'] = False
		context['nombre'] = 'Ronaldhino'
		return context

def svg(request):
    return render(request, 'test.html')

def render_pdf_view(request):
    template_path = 'svg.html'

    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response