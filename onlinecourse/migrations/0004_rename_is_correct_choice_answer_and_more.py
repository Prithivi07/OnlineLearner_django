# Generated by Django 4.2.3 on 2024-10-25 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_rename_option_choice_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='is_correct',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='content',
            new_name='option',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='grade',
            new_name='mark',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='ques',
        ),
    ]