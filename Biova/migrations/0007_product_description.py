# Generated by Django 5.0.7 on 2024-08-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biova', '0006_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='type details here'),
        ),
    ]