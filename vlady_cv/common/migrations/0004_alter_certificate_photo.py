# Generated by Django 4.1.7 on 2023-03-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_certificate_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
