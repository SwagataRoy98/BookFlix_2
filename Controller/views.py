from django.shortcuts import render
from .Book_Search.search_functions import search
from .forms import SearchForm
from .models import Book
# Create your views here.


def home_view(request):
    books = Book.objects.all()
    context = {
        'Books': books
    }
    return render(request, 'index.html', context=context)


def admin_dashboard_view(request, *args, **kwargs):
    context = {"searchForm": SearchForm}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query_dict = search(form.cleaned_data["search_by_title"], form.cleaned_data["search_by_author"])
            print(query_dict["edition"])
            context["search_by_title"] = form.cleaned_data["search_by_title"]
            context["search_by_author"] = form.cleaned_data["search_by_author"]
    return render(request, "adminSearchDashboard.html", context=context)
