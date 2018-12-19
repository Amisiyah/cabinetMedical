# Generated by Django 2.1.3 on 2018-12-05 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('comments', models.TextField()),
                ('prescription', models.TextField()),
                ('price_for_consultation', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('consultation_date', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('doctors', models.ManyToManyField(to='patients.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('pin', models.CharField(max_length=13)),
                ('age', models.IntegerField(choices=[(0, ' < 14 '), (1, ' 14-18 '), (2, ' > 18 ')], default=2)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='medicalfile',
            name='patients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
        ),
    ]