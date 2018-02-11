# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import teacherdirectory.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacherdirectory', '0002_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDoc',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=teacherdirectory.models.teacher_doc_path)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('utchrid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tchr_faculty_id', models.CharField(max_length=10)),
                ('tchr_firstname', models.CharField(max_length=50)),
                ('tchr_lastname', models.CharField(max_length=50, null=True)),
                ('tchr_fname', models.CharField(max_length=50)),
                ('tchr_gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='F', max_length=2)),
                ('tchr_nationality', models.CharField(max_length=50)),
                ('tchr_nid_pass', models.CharField(max_length=50)),
                ('tchr_religion', models.CharField(choices=[('I', 'ISLAM'), ('H', 'HINDUISM'), ('C', 'CHRISTIANITY')], default='I', max_length=2)),
                ('tchr_business_ph', models.CharField(max_length=15, null=True)),
                ('tchr_home_ph', models.CharField(max_length=15, null=True)),
                ('tchr_mobile_no', models.CharField(max_length=15)),
                ('tchr_email', models.CharField(max_length=70, null=True)),
                ('tchr_cur_add_villordist', models.CharField(max_length=50, null=True)),
                ('tchr_cur_add_province', models.CharField(max_length=50)),
                ('tchr_cur_add_country', models.CharField(max_length=50)),
                ('tchr_prmnt_add_villordist', models.CharField(max_length=50, null=True)),
                ('tchr_prmnt_add_province', models.CharField(max_length=50)),
                ('tchr_prmnt_add_country', models.CharField(max_length=50)),
                ('tchr_faculty_type', models.CharField(max_length=50)),
                ('tchr_department', models.CharField(max_length=50)),
                ('tchr_office_branch', models.CharField(max_length=70)),
                ('tchr_dob', models.DateField()),
                ('tchr_doh', models.DateField()),
                ('tchr_salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tchr_level_degree', models.CharField(max_length=100)),
                ('tchr_focus_area', models.CharField(max_length=200, null=True)),
                ('tchr_school_progname', models.CharField(max_length=100, null=True)),
                ('tchr_emg_c_name', models.CharField(max_length=50, null=True)),
                ('tchr_emg_c_phno1', models.CharField(max_length=15, null=True)),
                ('tchr_emg_c_phno2', models.CharField(max_length=15, null=True)),
                ('tchr_emg_c_relationship', models.CharField(max_length=50, null=True)),
                ('tchr_blood_group', models.CharField(max_length=3, null=True)),
                ('tchr_allergies', models.CharField(max_length=200, null=True)),
                ('tchr_resign_date', models.DateField(null=True)),
                ('tchr_resign_reason', models.CharField(max_length=200, null=True)),
                ('tchr_resign_chkliabilites', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=teacherdirectory.models.teacher_image_path)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teacherimage',
            unique_together=set([('uid', 'file')]),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacherdirectory.TeacherImage'),
        ),
        migrations.AddField(
            model_name='studentdoc',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherdirectory.Teacher'),
        ),
    ]
