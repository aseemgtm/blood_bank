# Generated by Django 3.0.3 on 2020-05-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200427_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='city',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='seeker',
            name='city',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(default=' ', help_text='eg : #112 Sector 40C', max_length=100),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='address',
            field=models.CharField(default=' ', help_text='eg : #112 Sector 40C', max_length=100),
        ),
    ]
