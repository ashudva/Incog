# Generated by Django 2.2.7 on 2019-11-12 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0040_auto_20191111_0502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='appreciations',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='appreciations',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='appreciations',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='n_replies',
        ),
        migrations.AlterField(
            model_name='comment',
            name='mod_date',
            field=models.DateField(blank=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='confession',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='heading',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='mod_date',
            field=models.DateField(blank=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='mod_date',
            field=models.DateField(blank=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
