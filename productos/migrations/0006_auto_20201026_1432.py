# Generated by Django 3.1 on 2020-10-26 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20201019_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='quienesSomos',
            field=ckeditor.fields.RichTextField(verbose_name='quienesSomos'),
        ),
    ]
