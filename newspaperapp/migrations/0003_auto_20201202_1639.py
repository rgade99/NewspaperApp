# Generated by Django 3.1.1 on 2020-12-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaperapp', '0002_auto_20201202_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to='newspaperapp.newsCategory'),
        ),
    ]
