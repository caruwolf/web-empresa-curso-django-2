# Generated by Django 4.1.2 on 2022-11-05 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-created'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
