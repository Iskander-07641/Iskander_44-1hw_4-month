# Generated by Django 5.1.1 on 2024-09-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('non_fiction', 'Non-Fiction'), ('science', 'Science'), ('history', 'History'), ('fantasy', 'Fantasy'), ('biography', 'Biography'), ('mystery', 'Mystery'), ('romance', 'Romance')], max_length=20)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('cover_image', models.URLField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
