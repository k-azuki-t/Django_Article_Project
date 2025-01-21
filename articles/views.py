from django.shortcuts import render
from .forms import ContentForm

# Create your views here.
def test(request):
    form = ContentForm()

    return render(request, 'articles/test.html', {'form': form})
