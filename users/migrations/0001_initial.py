# Generated by Django 3.0.3 on 2020-04-17 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Blood_Group', models.CharField(max_length=2)),
                ('Rh_factor', models.CharField(max_length=1)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=60)),
                ('contact_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Blood_Group', models.CharField(max_length=2)),
                ('Rh_factor', models.CharField(max_length=1)),
                ('contact_number', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]