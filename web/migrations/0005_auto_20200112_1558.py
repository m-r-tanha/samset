# Generated by Django 2.2.5 on 2020-01-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200112_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinsert',
            name='CV',
            field=models.TextField(),
        ),
    ]