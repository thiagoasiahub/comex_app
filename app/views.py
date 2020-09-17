from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from app.models import Imp

# Create your views here.
def std(request):
    total_imports = Imp.objects.count()
    total_imports = f'{total_imports:,}'
    
    return render(request, 'index.html', {'total_imports' : total_imports,})

def search(request):
    query = request.GET.get('q', '')
    try:
        query = query
    except ValueError:
        query = None
        results = None
    if query:
        results = Imp.objects.filter(Q(descricao_do_produto__icontains=query) | Q(incoterm__icontains=query) | Q(cod_ncm__icontains=query)).distinct()
    else:
        return render(request, 'index.html')
    context = RequestContext(request)

    # Pagitaion
    page = request.GET.get('page', 1)
    results_paginator = Paginator(results, 50)
    
    try:
        results = results_paginator.page(page)
    except PageNotAnInteger:
        results = results_paginator.page()          
    except EmptyPage:
        results = results_paginator.page(results_paginator.num_pages)  

    context['results'] = results
    # Pagitaion END

    imports_count = int(Imp.objects.filter(Q(descricao_do_produto__icontains=query) | Q(incoterm__icontains=query) | Q(cod_ncm__icontains=query)).count())
    imports_count = f'{imports_count:,}'

    return render(request, 'search.html', {'results' : results, 
                                            'imports_count' : imports_count,
                                            })
