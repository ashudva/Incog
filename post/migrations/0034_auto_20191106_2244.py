# Generated by Django 2.2.6 on 2019-11-06 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_auto_20191106_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Comment'),
        ),
    ]
