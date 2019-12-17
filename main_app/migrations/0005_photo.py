# Generated by Django 2.2.6 on 2019-12-17 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rescue_adopters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('rescue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Rescue')),
            ],
        ),
    ]
