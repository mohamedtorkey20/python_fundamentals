# Generated by Django 5.0.4 on 2024-05-14 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_category_isbn_alter_book_options_book_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='test',
            new_name='isbn',
        ),
    ]