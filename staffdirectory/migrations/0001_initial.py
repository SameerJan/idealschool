# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import staffdirectory.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('ustid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('staff_id', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('fname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='F', max_length=2)),
                ('nationality', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('nid_pass', models.CharField(max_length=50)),
                ('religion', models.CharField(choices=[('I', 'ISLAM'), ('H', 'HINDUISM'), ('C', 'CHRISTIANITY')], default='I', max_length=2)),
                ('business_ph', models.CharField(max_length=15, null=True)),
                ('home_ph', models.CharField(max_length=15, null=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=70, null=True)),
                ('cur_add_villordist', models.CharField(max_length=50, null=True)),
                ('cur_add_province', models.CharField(max_length=50)),
                ('cur_add_country', models.CharField(max_length=50)),
                ('prmnt_add_villordist', models.CharField(max_length=50, null=True)),
                ('prmnt_add_province', models.CharField(max_length=50)),
                ('prmnt_add_country', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('office_branch', models.CharField(max_length=70)),
                ('doh', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('level_degree', models.CharField(max_length=100)),
                ('school_progname', models.CharField(max_length=100, null=True)),
                ('emg_c_name', models.CharField(max_length=50, null=True)),
                ('emg_c_phno1', models.CharField(max_length=15, null=True)),
                ('emg_c_phno2', models.CharField(max_length=15, null=True)),
                ('emg_c_relationship', models.CharField(max_length=50, null=True)),
                ('blood_group', models.CharField(max_length=3, null=True)),
                ('allergies', models.CharField(max_length=200, null=True)),
                ('resign_date', models.DateField(null=True)),
                ('resign_reason', models.CharField(max_length=200, null=True)),
                ('resign_chkliabilites', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffDoc',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=staffdirectory.models.staff_doc_path)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffdirectory.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=staffdirectory.models.staff_image_path)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='staffimage',
            unique_together=set([('uid', 'file')]),
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffdirectory.StaffImage'),
        ),
    ]
