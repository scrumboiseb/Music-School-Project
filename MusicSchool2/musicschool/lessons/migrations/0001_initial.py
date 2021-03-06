# Generated by Django 2.0.2 on 2018-04-04 22:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equiptment',
            fields=[
                ('instrumentID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('instrument', models.CharField(help_text='Enter a name for the instrument', max_length=20)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Instrument availability', max_length=1)),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('firstName', models.CharField(help_text='Enter your First Name Only', max_length=30)),
                ('lastName', models.CharField(help_text='Enter your Last Name Only', max_length=30)),
                ('DOB', models.DateField(help_text='Enter your Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('firstName', models.CharField(help_text='Enter your First Name Only', max_length=30)),
                ('lastName', models.CharField(help_text='Enter your Last Name Only', max_length=30)),
                ('skillsSummary', models.TextField(help_text='Provide a brief summary of your teaching skills and history', max_length=1000)),
                ('studentID', models.ManyToManyField(help_text='Select your students', null=True, to='lessons.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacherID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.Teacher'),
        ),
    ]
