from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        try:
            n = int(num, from_base)
        except:
            return "Проверьте данные"
    else:
        n = int(num)
    alphabet = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


class MainView(TemplateView):
    template_name = 'numtrans/main.html'


class AboutView(TemplateView):
    template_name = 'numtrans/aboutpr.html'


class TranslView(TemplateView):
    template_name = 'numtrans/transl.html'


class InstrView(TemplateView):
    template_name = 'numtrans/instruction.html'


def translatenum(request):
    if request.method == "POST":
        num = request.POST['number']
        translate_from = request.POST['from']
        translate_to = request.POST['to']

        result = convert_base(num, to_base=int(translate_to), from_base=int(translate_from))
        mydict = {
            "number": result,
        }
        return render(request, 'numtrans/transl.html', context = mydict)
