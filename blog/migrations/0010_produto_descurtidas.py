# Generated by Django 2.2.1 on 2019-05-31 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190531_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descurtidas',
            field=models.IntegerField(default=0),
        ),
    ]
