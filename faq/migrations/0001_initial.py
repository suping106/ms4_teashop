# Generated by Django 3.2.5 on 2021-08-05 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('question', models.CharField(max_length=254)),
                ('answer', models.CharField(max_length=254)),
            ],
        ),
    ]
