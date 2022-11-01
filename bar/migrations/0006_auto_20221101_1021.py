# Generated by Django 3.2.8 on 2022-11-01 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0005_alter_barconfigs_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barconfigs',
            name='code',
            field=models.CharField(default='1z4lJU2eHz', max_length=10),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(max_length=150)),
                ('artist', models.CharField(max_length=150)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.barconfigs')),
            ],
        ),
    ]
