from django.db import models


class Book(models.Model):
    objects = None
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


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.author}"
