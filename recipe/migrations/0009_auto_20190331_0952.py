# Generated by Django 2.1.7 on 2019-03-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_auto_20190319_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='unit_type',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'gram'), ('mg', 'milligram'), ('l', 'liter'), ('ml', 'milliliter'), ('oz', 'ounce'), ('floz', 'fluid oz'), ('cup', 'cup'), ('lb', 'lb'), ('tsp', 'teaspoon'), ('tbs', 'tablespoon'), ('qrt', 'quart'), ('pt', 'pint')], max_length=200),
        ),
    ]