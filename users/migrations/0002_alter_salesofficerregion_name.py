# Generated by Django 3.2.7 on 2021-10-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesofficerregion',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
