# Generated by Django 4.0.4 on 2022-05-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='business',
            field=models.CharField(default='false', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='comments',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='dept',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='ui',
            field=models.CharField(default='false', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='web',
            field=models.CharField(default='false', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='roll',
            field=models.CharField(default='', max_length=100),
        ),
    ]
