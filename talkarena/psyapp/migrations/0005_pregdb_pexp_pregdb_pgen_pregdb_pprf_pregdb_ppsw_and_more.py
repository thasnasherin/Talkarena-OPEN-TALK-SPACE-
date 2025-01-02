# Generated by Django 5.0.1 on 2024-04-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psyapp', '0004_remove_pregdb_pexp_remove_pregdb_pgen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregdb',
            name='pexp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pregdb',
            name='pgen',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pregdb',
            name='pprf',
            field=models.ImageField(default='null.jpg', upload_to='pregimgs'),
        ),
        migrations.AddField(
            model_name='pregdb',
            name='ppsw',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pregdb',
            name='pqual',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pregdb',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
