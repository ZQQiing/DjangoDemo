# Generated by Django 4.1.3 on 2022-11-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tibmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.CharField(max_length=1023)),
                ('entity1', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=64)),
                ('entity2', models.CharField(max_length=255)),
            ],
        ),
    ]
