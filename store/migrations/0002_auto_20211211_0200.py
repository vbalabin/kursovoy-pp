# Generated by Django 3.0.3 on 2021-12-10 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availibility',
            new_name='availability',
        ),
    ]