# Generated by Django 2.0.3 on 2019-03-28 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20190328_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipes',
            new_name='recipe',
        ),
    ]
