# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_model', models.CharField(choices=[('2345\u7f51\u5740\u5bfc\u822a', '2345\u7f51\u5740\u5bfc\u822a'), ('2345\u8f6f\u4ef6', '2345\u8f6f\u4ef6'), ('\u5176\u5b83', '\u5176\u5b83')], max_length=64, verbose_name='\u9879\u76ee\u6a21\u5757')),
                ('project_name', models.CharField(max_length=32, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('project_type', models.CharField(choices=[('\u9700\u6c42\u5f00\u53d1', '\u9700\u6c42\u5f00\u53d1'), ('\u7248\u672c\u5347\u7ea7', '\u7248\u672c\u5347\u7ea7'), ('\u884c\u653f\u4e8b\u52a1', '\u884c\u653f\u4e8b\u52a1'), ('\u4eba\u4e8b', '\u4eba\u4e8b')], max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b')),
                ('project_priority', models.CharField(choices=[('\u7d27\u6025', '\u7d27\u6025'), ('\u91cd\u8981', '\u91cd\u8981'), ('\u4e00\u822c', '\u4e00\u822c')], max_length=10)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('project_promoter', models.CharField(max_length=32, verbose_name='\u9879\u76ee\u53d1\u8d77\u4eba')),
                ('product_leader', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4ea7\u54c1\u8d1f\u8d23\u4eba')),
                ('design_leader', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bbe\u8ba1\u8d1f\u8d23\u4eba')),
                ('frontend_leader', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u524d\u7aef\u8d1f\u8d23\u4eba')),
                ('backend_leader', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u540e\u7aef\u8d1f\u8d23\u4eba')),
                ('test_leader', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u6d4b\u8bd5\u8d1f\u8d23\u4eba')),
                ('project_participants', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u9879\u76ee\u53c2\u4e0e\u8005')),
                ('default_cc', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u9879\u76ee\u6284\u9001\u4eba')),
                ('project_description', models.TextField(verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('project_attachment', models.FileField(blank=True, null=True, upload_to='./uploads/')),
                ('project_status', models.CharField(default='\u5f85\u521b\u5efa', max_length=10, verbose_name='\u9879\u76ee\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u8868',
                'verbose_name_plural': '\u9879\u76ee\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=10, unique=True)),
                ('project_model', models.CharField(choices=[('2345\u7f51\u5740\u5bfc\u822a', '2345\u7f51\u5740\u5bfc\u822a'), ('2345\u8f6f\u4ef6', '2345\u8f6f\u4ef6'), ('\u5176\u5b83', '\u5176\u5b83')], max_length=64, verbose_name='\u9879\u76ee\u6a21\u5757')),
                ('task_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6807\u9898')),
                ('related_task', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u5173\u8054\u4efb\u52a1')),
                ('task_type', models.CharField(choices=[('\u9700\u6c42\u5f00\u53d1', '\u9700\u6c42\u5f00\u53d1'), ('\u7248\u672c\u5347\u7ea7', '\u7248\u672c\u5347\u7ea7'), ('\u884c\u653f\u4e8b\u52a1', '\u884c\u653f\u4e8b\u52a1'), ('\u4eba\u4e8b', '\u4eba\u4e8b')], max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b')),
                ('task_priority', models.CharField(choices=[('\u7d27\u6025', '\u7d27\u6025'), ('\u91cd\u8981', '\u91cd\u8981'), ('\u4e00\u822c', '\u4e00\u822c')], max_length=10)),
                ('task_promoter', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u53d1\u8d77\u4eba')),
                ('task_assign', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6307\u6d3e\u4eba')),
                ('task_cc', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6284\u9001\u4eba')),
                ('is_test', models.CharField(choices=[('0', '\u5426'), ('1', '\u662f')], max_length=5)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('task_target', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4efb\u52a1\u76ee\u6807')),
                ('task_description', models.TextField(verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('task_status', models.CharField(default='\u5f85\u521b\u5efa', max_length=20, verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('task_attachment', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('task_history', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('task_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Projects')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u521b\u5efa\u8868',
                'verbose_name_plural': '\u4efb\u52a1\u521b\u5efa\u8868',
            },
        ),
        migrations.CreateModel(
            name='TasksHandle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=10, unique=True)),
                ('task_assign', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6307\u6d3e\u4eba')),
                ('task_transfer', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u8f6c\u63a5\u4eba')),
                ('task_cc', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6284\u9001\u4eba')),
                ('task_status', models.CharField(default='\u5f85\u63a5\u53d7', max_length=20, verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_accept', models.BooleanField(default=0)),
                ('is_reject', models.BooleanField(default=0)),
                ('is_transfer', models.BooleanField(default=0)),
                ('is_delay', models.BooleanField(default=0)),
                ('task_history', models.TextField(blank=True, null=True)),
                ('task_remark', models.TextField(blank=True, null=True)),
                ('task_attachment', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('task_handle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Tasks')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u5904\u7406\u8868',
                'verbose_name_plural': '\u4efb\u52a1\u5904\u7406\u8868',
            },
        ),
        migrations.CreateModel(
            name='TaskTalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk_name', models.CharField(max_length=32, verbose_name='\u8ba8\u8bba\u8005')),
                ('talk_content', models.TextField(verbose_name='\u8ba8\u8bba\u5185\u5bb9')),
                ('talk_time', models.DateTimeField(auto_now_add=True)),
                ('task_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Tasks')),
            ],
            options={
                'verbose_name': '\u8ba8\u8bba\u533a',
                'verbose_name_plural': '\u8ba8\u8bba\u533a',
            },
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=32)),
                ('project_model', models.CharField(max_length=64, verbose_name='\u9879\u76ee\u6a21\u5757')),
                ('task_name', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('task_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6807\u9898')),
                ('related_task', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u5173\u8054\u4efb\u52a1')),
                ('task_type', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b')),
                ('task_priority', models.CharField(max_length=10)),
                ('task_promoter', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u53d1\u8d77\u4eba')),
                ('task_assign', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6307\u6d3e\u4eba')),
                ('task_cc', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4efb\u52a1\u6284\u9001\u4eba')),
                ('is_test', models.CharField(max_length=5)),
                ('task_target', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4efb\u52a1\u76ee\u6807')),
                ('task_description', models.TextField(verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('task_attachment', models.FileField(blank=True, null=True, upload_to='uploads')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u6a21\u677f\u8868',
                'verbose_name_plural': '\u4efb\u52a1\u6a21\u677f\u8868',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8d26\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u8d26\u6237\u4fe1\u606f',
            },
        ),
    ]
