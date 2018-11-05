from django.contrib import admin
from .models import Author, Language, Genre, Book, BookInstance


#  @admin.register(Book) == admin.site.register(Book)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #  Поля для виведення в адмін-панелі, а їх порядок нижче
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    #  a,b,c,(d,e) -> d,e together fields / порядок виведення полей


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('genre',)
    inlines = [BooksInstanceInline]


# display it is a function(Book), because in admin panel it is can display only one genre !


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Book Instance', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Language)
admin.site.register(Genre)
