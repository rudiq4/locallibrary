from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import HttpResponse, Http404


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # without .all(), cause it be a default

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


class BookListView(generic.ListView):
    model = Book


#class BookListView(generic.ListView):
#    model = Book
#    context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
#    queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
#    template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения


# def book_detail_view(request, pk):
#     try:
#         book_id = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#
#     # book_id=get_object_or_404(Book, pk=pk)
#
#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book': book_id, }
#     )