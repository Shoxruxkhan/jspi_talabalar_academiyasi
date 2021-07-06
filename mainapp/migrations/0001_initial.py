# Generated by Django 2.2.10 on 2021-07-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media/event_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tanlov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media/event_images/')),
            ],
        ),
    ]
