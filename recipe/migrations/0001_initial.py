# Generated by Django 2.1.7 on 2019-03-13 10:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredieantMeasurement',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('g', 'gram'), ('mg', 'milligram'), ('l', 'liter'), ('ml', 'mililiter'), ('oz', 'ounce'), ('floz', 'fluid oz'), ('cup', 'cup'), ('lb', 'lb'), ('tsp', 'teaspoon'), ('tbs', 'tablespoon'), ('qrt', 'quart'), ('pt', 'pint')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('final_product_photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredieantmeasurement',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Ingredient'),
        ),
    ]