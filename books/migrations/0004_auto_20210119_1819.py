# Generated by Django 3.1.4 on 2021-01-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='nazwisko')),
                ('about', models.TextField(blank=True, verbose_name='o autorze')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autorzy',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books.Author', verbose_name='autorzy'),
        ),
    ]