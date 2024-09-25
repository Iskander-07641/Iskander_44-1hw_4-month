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

    title = models.CharField(max_length=255, verbose_name='Title', blank=False, db_index=True)
    author = models.CharField(max_length=100, verbose_name='Author', blank=False, db_index=True)
    published_date = models.DateField(verbose_name='Published Date', blank=False, db_index=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='fiction', verbose_name='Genre', blank=False, db_index=True)
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN', blank=False, db_index=True)
    summary = models.TextField(verbose_name='Summary', blank=False, db_index=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Cover Image', db_index=True)
    pages = models.IntegerField(verbose_name='Number of Pages', blank=False, db_index=True)
    language = models.CharField(max_length=30, verbose_name='Language', blank=False, db_index=True)

    def __str__(self):
        return f'{self.title} by {self.author}'


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE, db_index=True)
    author = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.author}"

