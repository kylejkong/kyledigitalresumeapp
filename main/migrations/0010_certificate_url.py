# Generated by Django 4.1.7 on 2023-03-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_certificate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
