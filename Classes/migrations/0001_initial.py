# Generated by Django 3.0.6 on 2020-05-28 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_names', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_names', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ClassContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('video_url', models.URLField()),
                ('notes_url', models.URLField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.Classrooms')),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.Subjects')),
            ],
        ),
    ]
