# Generated by Django 4.0.1 on 2022-01-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_alter_lead_lead_status_alter_lead_source_of_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('ATTEMPTED TO CONTACT', 'ATTEMPTED TO CONTACT'), ('BAD TIMING', 'BAD TIMING '), ('IN PROGRESS', 'IN PROGRESS'), ('OPEN DEAL', 'OPEN DEAL'), ('CONNECTED', 'CONNECTED'), ('UNQUALIFIED', 'UNQUALIFIED'), ('OPEN', 'OPEN')], max_length=100),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source_of_lead',
            field=models.CharField(blank=True, choices=[('GOOGLE SEARCH', 'GOOGLE SEARCH'), ('INSTAGRAM', 'INSTAGRAM'), ('REFERRAL', 'REFERRAL'), ('TWITTER', 'TWITTER')], max_length=100),
        ),
    ]
