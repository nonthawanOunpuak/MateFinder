# Generated by Django 3.1.1 on 2020-11-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('light', models.BooleanField()),
                ('timetosleep', models.CharField(max_length=255)),
                ('pet', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DormInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name_dorm', models.CharField(max_length=255)),
                ('details_dorm', models.CharField(max_length=255)),
                ('type_dorm', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name_req', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SentRequestInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name_sent', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
