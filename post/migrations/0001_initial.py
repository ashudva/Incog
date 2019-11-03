# Generated by Django 2.2.6 on 2019-11-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confession', models.CharField(max_length=4000)),
                ('post_time', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
