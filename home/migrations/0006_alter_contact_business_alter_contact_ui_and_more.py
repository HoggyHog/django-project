# Generated by Django 4.0.4 on 2022-05-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_business_alter_contact_ui_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='business',
            field=models.CharField(default='false', max_length=100, null='true'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ui',
            field=models.CharField(default='false', max_length=100, null='true'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='web',
            field=models.CharField(default='false', max_length=100, null='true'),
        ),
    ]
