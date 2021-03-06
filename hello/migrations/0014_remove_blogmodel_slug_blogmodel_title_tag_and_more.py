# Generated by Django 4.0.2 on 2022-05-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0013_blogmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='slug',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_tag',
            field=models.CharField(default='SDU BLOG', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
