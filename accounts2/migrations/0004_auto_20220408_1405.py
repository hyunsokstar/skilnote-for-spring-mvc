# Generated by Django 3.2.11 on 2022-04-08 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skilnote1', '0003_allowlistforskilnote_commonsubject_lecturebookmark_myplan'),
        ('accounts2', '0003_profile_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='common_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skilnote1.commonsubject'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_category',
            field=models.CharField(default='ca1', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_category',
            field=models.CharField(default='ca1', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github1',
            field=models.CharField(blank=True, default='www.github.com', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github2',
            field=models.CharField(blank=True, default='www.github.com', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github3',
            field=models.CharField(blank=True, default='www.github.com', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github4',
            field=models.CharField(default='www.github.com', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_original',
            field=models.CharField(blank=True, default='www.github.com', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_updated_category',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='selected_category_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subject_of_memo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]