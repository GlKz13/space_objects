# Generated by Django 4.1 on 2022-08-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_objects', '0003_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eamil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]