# Generated by Django 5.0.1 on 2024-03-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pregdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pmail', models.EmailField(max_length=254)),
                ('pprf', models.ImageField(default='null.jpg', upload_to='pregimgs')),
                ('ppsw', models.TextField()),
            ],
        ),
    ]
