# Generated by Django 4.0.4 on 2022-08-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0007_remove_blog_rasm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('fam', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
