# Generated by Django 2.0.7 on 2018-07-07 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
