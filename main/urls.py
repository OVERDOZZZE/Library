from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import books, book_detail, add_book

urlpatterns = [
    path('', books, name='home'),
    path('book_detail/<int:id>/', book_detail),
    path('add_book/', add_book)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
