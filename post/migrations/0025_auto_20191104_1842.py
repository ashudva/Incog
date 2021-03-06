# Generated by Django 2.2.6 on 2019-11-04 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20191104_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(blank=True, null=True, to='post.Reply'),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='post.Comment'),
        ),
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
