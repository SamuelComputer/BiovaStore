# Generated by Django 5.0.8 on 2024-08-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biova', '0003_rename_categories_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
    ]