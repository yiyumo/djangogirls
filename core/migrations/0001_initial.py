# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 21:24
from __future__ import unicode_literals

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_date_extensions.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('sponsor', '0001_initial'),
        ('coach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', django_date_extensions.fields.ApproximateDateField(blank=True, validators=[core.validators.validate_approximatedate])),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('latlng', models.CharField(blank=True, max_length=30, null=True, verbose_name='latitude and longitude')),
                ('photo', models.ImageField(blank=True, help_text='The best would be 356 x 210px', null=True, upload_to='event/cities/')),
                ('photo_credit', models.CharField(blank=True, help_text="Only use pictures with a <a href='https://creativecommons.org/licenses/'>Creative Commons license</a>.", max_length=200, null=True)),
                ('photo_link', models.URLField(blank=True, null=True, verbose_name='photo URL')),
                ('email', models.EmailField(blank=True, max_length=75, null=True, verbose_name='event email')),
                ('is_on_homepage', models.BooleanField(default=True, verbose_name='visible on homepage?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='deleted?')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('page_title', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('page_description', models.TextField(blank=True, default='Django Girls is a one-day workshop about programming in Python and Django tailored for women.', verbose_name='description')),
                ('page_main_color', models.CharField(blank=True, default='FF9400', help_text='Main color of the chapter in HEX', max_length=6, verbose_name='main color')),
                ('page_custom_css', models.TextField(blank=True, verbose_name='custom CSS rules')),
                ('page_url', models.CharField(blank=True, help_text='Will be used as part of the event URL (djangogirls.org/______/)', max_length=200, verbose_name='URL slug')),
                ('is_page_live', models.BooleanField(default=False, verbose_name='Website is ready')),
                ('attendees_count', models.IntegerField(blank=True, null=True, verbose_name='Number of attendees')),
                ('applicants_count', models.IntegerField(blank=True, null=True, verbose_name='Number of applicants')),
                ('thank_you_email_sent', models.DateTimeField(blank=True, null=True)),
                ('submit_information_email_sent', models.DateTimeField(blank=True, null=True)),
                ('offer_help_email_sent', models.DateTimeField(blank=True, null=True)),
                ('main_organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_organizer', to=settings.AUTH_USER_MODEL)),
                ('team', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'List of events',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='EventPageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(help_text='HTML allowed')),
                ('background', models.ImageField(blank=True, help_text='Optional background photo', null=True, upload_to='event/backgrounds/')),
                ('position', models.PositiveIntegerField(help_text='Position of the block on the website')),
                ('is_public', models.BooleanField(default=False)),
                ('coaches', models.ManyToManyField(to='coach.Coach', verbose_name='Coaches')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='core.Event')),
                ('sponsors', models.ManyToManyField(to='sponsor.Sponsor', verbose_name='Sponsors')),
            ],
            options={
                'verbose_name': 'Website Content',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='EventPageMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(help_text='http://djangogirls.org/city/<the value you enter here>', max_length=255)),
                ('position', models.PositiveIntegerField(help_text='Order of menu')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='core.Event')),
            ],
            options={
                'verbose_name': 'Website Menu',
                'ordering': ('position',),
            },
        ),
    ]
