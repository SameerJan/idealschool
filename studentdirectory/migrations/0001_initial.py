# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import studentdirectory.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('f_name', models.CharField(max_length=50)),
                ('gf_name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=2)),
                ('dob', models.DateField()),
                ('nid_no', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('religion', models.CharField(choices=[('I', 'ISLAM'), ('H', 'HINDUISM'), ('C', 'CHRISTIANITY')], default='I', max_length=2)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('current_add', models.TextField()),
                ('permanent_add', models.TextField()),
                ('emg_contact1_name', models.CharField(max_length=50)),
                ('emg_contact1_phone_1', models.CharField(max_length=12)),
                ('emg_contact1_phone_2', models.CharField(max_length=12)),
                ('emg_contact1_relation', models.CharField(max_length=50)),
                ('emg_contact2_name', models.CharField(max_length=50, null=True)),
                ('emg_contact2_phone_1', models.CharField(max_length=12, null=True)),
                ('emg_contact2_phone_2', models.CharField(max_length=12, null=True)),
                ('emg_contact2_relation', models.CharField(max_length=50, null=True)),
                ('blood_group', models.CharField(max_length=5)),
                ('alergies', models.TextField()),
                ('medications', models.TextField()),
                ('medical_conditions', models.TextField()),
                ('transfered_in_date', models.DateField(null=True)),
                ('transfered_in_from_school', models.CharField(max_length=50, null=True)),
                ('transfered_in_reason', models.TextField(null=True)),
                ('transfered_out_date', models.DateField(null=True)),
                ('transfered_out_to_school', models.CharField(max_length=50, null=True)),
                ('transfered_out_reason', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDoc',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=studentdirectory.models.student_doc_path)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentdirectory.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=studentdirectory.models.student_image_path)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='studentimage',
            unique_together=set([('uid', 'file')]),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentdirectory.StudentImage'),
        ),
    ]
