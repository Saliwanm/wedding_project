# Generated by Django 4.1.4 on 2022-12-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_forum_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='comment',
            field=models.CharField(max_length=250, null=True, verbose_name='Comment'),
        ),
    ]
