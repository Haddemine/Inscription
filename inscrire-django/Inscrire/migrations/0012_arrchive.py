# Generated by Django 4.0.6 on 2022-07-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inscrire', '0011_delete_arrchive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commantire', models.CharField(max_length=500)),
                ('fichiere', models.FileField(null=True, upload_to='')),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
