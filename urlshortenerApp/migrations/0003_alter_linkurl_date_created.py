# Generated by Django 4.0.2 on 2022-08-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortenerApp', '0002_alter_linkurl_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkurl',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
