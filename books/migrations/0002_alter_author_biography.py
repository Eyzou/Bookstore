# Generated by Django 5.1.2 on 2024-10-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(null=True),
        ),
    ]
