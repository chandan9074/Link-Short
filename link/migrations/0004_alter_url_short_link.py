# Generated by Django 3.2 on 2021-04-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_alter_url_short_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_link',
            field=models.CharField(blank=True, max_length=500, unique=True),
        ),
    ]
