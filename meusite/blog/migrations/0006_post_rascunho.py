# Generated by Django 2.1.7 on 2019-05-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rascunho',
            field=models.BooleanField(default=False),
        ),
    ]
