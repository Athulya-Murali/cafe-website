# Generated by Django 4.2.6 on 2023-12-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]