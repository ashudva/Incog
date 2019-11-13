# Generated by Django 2.2.7 on 2019-11-13 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0042_auto_20191113_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mod_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='mod_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='mod_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Comment'),
        ),
    ]