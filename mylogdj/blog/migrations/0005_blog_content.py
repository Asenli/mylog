# Generated by Django 2.0.7 on 2018-07-20 04:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容'),
        ),
    ]
