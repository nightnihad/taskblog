# Generated by Django 4.2.4 on 2023-09-02 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_about_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='main.category'),
        ),
    ]