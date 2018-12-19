# Generated by Django 2.1.3 on 2018-12-13 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('notes', models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
        migrations.AlterField(
            model_name='medicalfile',
            name='patients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicalFile', to='patients.Patient'),
        ),
        migrations.AddField(
            model_name='medicalfile',
            name='calendar',
            field=models.ManyToManyField(to='patients.Event'),
        ),
    ]