# Generated by Django 2.0.2 on 2018-02-01 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('target', models.URLField(max_length=2048)),
                ('status_code', models.IntegerField(blank=True, null=True)),
                ('redirects_to', models.URLField(blank=True, max_length=2048)),
                ('state', models.CharField(choices=[('new', 'New'), ('ok', 'OK'), ('broken', 'Broken'), ('acceptable', 'Acceptable')], default='new', max_length=8)),
                ('problem', models.CharField(choices=[('new', 'New'), ('ok', 'OK'), ('url', 'URL error'), ('error', 'Error response'), ('redirect', 'Redirect'), ('cert', 'Certificate error')], default='new', max_length=8)),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Object')),
            ],
        ),
    ]