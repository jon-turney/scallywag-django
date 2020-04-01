from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from builds.models import Jobs

def index(request):
  all_rows = Jobs.objects.using('builds').all().order_by('-id')
  paginator = Paginator(all_rows, 25)

  page = request.GET.get('page')
  try:
     rows = paginator.page(page)
  except PageNotAnInteger:
     rows = paginator.page(1)
  except EmptyPage:
     rows = paginator.page(paginator.num_pages)

  return render(request, "builds/builds.html", {"rows" : rows })
