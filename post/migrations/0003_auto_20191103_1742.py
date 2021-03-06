# Generated by Django 2.2.6 on 2019-11-03 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20191103_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='post_likes',
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('comment_time', models.DateTimeField(verbose_name='Time of comment')),
                ('replies', models.IntegerField(default=0)),
                ('comment_likes', models.IntegerField(default=0)),
                ('parent_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
