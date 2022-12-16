# Generated by Django 4.1.3 on 2022-12-16 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0012_delete_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StartTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='endtime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='roombooking.endtime'),
        ),
        migrations.AddField(
            model_name='booking',
            name='starttime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='roombooking.starttime'),
        ),
    ]
