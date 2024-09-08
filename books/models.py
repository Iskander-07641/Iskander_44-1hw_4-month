from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('science_fiction', 'Science Fiction'),
        ('biography', 'Biography'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    ]

    title = models.CharField(max_length=255, verbose_name='Title', blank=False)
    author = models.CharField(max_length=100, verbose_name='Author', blank=False)
    published_date = models.DateField(verbose_name='Published Date', blank=False)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='fiction', verbose_name='Genre', blank=False)
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN', blank=False)
    summary = models.TextField(verbose_name='Summary', blank=False)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Cover Image')
    pages = models.IntegerField(verbose_name='Number of Pages', blank=False)
    language = models.CharField(max_length=30, verbose_name='Language', blank=False)

    def __str__(self):
        return f'{self.title} by {self.author}'
