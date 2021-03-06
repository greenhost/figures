# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-09 14:17
from __future__ import unicode_literals

from django import VERSION as DJANGO_VERSION
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    if DJANGO_VERSION[0:2] == (1,8):
        dependencies = [
            migrations.swappable_dependency(settings.AUTH_USER_MODEL),
            ('sites', '0001_initial'),
            ('figures', '0014_add_indexes_to_daily_metrics'),
        ]
    else:  # Assuming 1.11+
        dependencies = [
            migrations.swappable_dependency(settings.AUTH_USER_MODEL),
            ('sites', '0002_alter_domain_unique'),
            ('figures', '0014_add_indexes_to_daily_metrics'),
        ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('course_id', models.CharField(db_index=True, max_length=255)),
                ('date_for', models.DateField(db_index=True)),
                ('date_enrolled', models.DateField(db_index=True)),
                ('is_enrolled', models.BooleanField()),
                ('is_completed', models.BooleanField()),
                ('progress_percent', models.FloatField(default=0.0)),
                ('points_possible', models.FloatField()),
                ('points_earned', models.FloatField()),
                ('sections_worked', models.IntegerField()),
                ('sections_possible', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='enrollmentdata',
            unique_together=set([('site', 'user', 'course_id')]),
        ),
    ]
