# Generated by Django 3.2.7 on 2021-10-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_doctorcategory_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorcategory',
            name='qr_code',
        ),
        migrations.AddField(
            model_name='doctor',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='media/qr_codes'),
        ),
    ]
