# Generated by Django 5.0.6 on 2024-05-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('username',)},
        ),
    ]
