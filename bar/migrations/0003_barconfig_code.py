# Generated by Django 3.2.8 on 2022-10-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_auto_20221029_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='barconfig',
            name='code',
            field=models.CharField(default='ziltUqIih1', max_length=10),
        ),
    ]