# Generated by Django 3.2.8 on 2022-10-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_music', '0001_initial'),
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_1', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_10', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_2', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_3', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_4', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_5', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_6', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_7', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_8', to='request_music.gender'),
        ),
        migrations.AlterField(
            model_name='gender_bar',
            name='gender_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_9', to='request_music.gender'),
        ),
    ]
