# Generated by Django 4.0 on 2022-08-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just', '0005_remove_form_date_form_file_alter_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='file',
            field=models.ImageField(upload_to='static'),
        ),
    ]
