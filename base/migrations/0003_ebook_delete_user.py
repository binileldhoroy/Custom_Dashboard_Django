# Generated by Django 4.0.1 on 2022-01-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_baseuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=150, null=True)),
                ('author', models.CharField(max_length=150, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='', null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
