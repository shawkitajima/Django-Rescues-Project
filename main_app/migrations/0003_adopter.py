# Generated by Django 2.2.6 on 2019-12-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
