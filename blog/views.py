from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Code
from .forms import CodeForm
from .utils import generate_qr, decode_now

class CodeList(generic.ListView):
  queryset = Code.objects.order_by('-created_on')
  template_name = 'index.html'

class CodeDetail(generic.DetailView):
  model = Code
  template_name = 'code_detail.html'

def code_new(request):
  if request.method == "POST":
    form = CodeForm(request.POST)
    if form.is_valid():
      code = form.save(commit=False)
      code.save()
      generate_qr(code)
      return redirect('code_detail', pk=code.pk)
  else:
    form = CodeForm()
  return render(request, 'code_edit.html', {'form': form})

def code_edit(request, pk):
  code = get_object_or_404(Code, pk=pk)
  if request.method == "POST":
    form = CodeForm(request.POST, instance=code)
    if form.is_valid():
        code = form.save(commit=False)
        code.save()
        generate_qr(code)
        return redirect('code_detail', pk=code.pk)
  else:
    form = CodeForm(instance=code)
  return render(request, 'code_edit.html', {'form': form})

def decode_qr(request, pk):
  code = get_object_or_404(Code, pk=pk)
  result = decode_now(pk)
  return render(request, 'decode_qr.html', {'data': result[0][0], 'pk': pk})
