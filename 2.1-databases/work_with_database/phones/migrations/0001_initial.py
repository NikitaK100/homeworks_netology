# Generated by Django 4.2.3 on 2023-08-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('image', models.CharField(max_length=255)),
                ('release_date', models.CharField(max_length=20)),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
