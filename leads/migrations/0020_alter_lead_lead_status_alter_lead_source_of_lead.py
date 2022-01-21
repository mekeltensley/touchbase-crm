# Generated by Django 4.0.1 on 2022-01-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_alter_lead_lead_status_alter_lead_source_of_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('CONNECTED', 'CONNECTED'), ('OPEN', 'OPEN'), ('ATTEMPTED TO CONTACT', 'ATTEMPTED TO CONTACT'), ('NEW', 'NEW'), ('OPEN DEAL', 'OPEN DEAL'), ('UNQUALIFIED', 'UNQUALIFIED'), ('IN PROGRESS', 'IN PROGRESS'), ('BAD TIMING', 'BAD TIMING ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source_of_lead',
            field=models.CharField(blank=True, choices=[('INSTAGRAM', 'INSTAGRAM'), ('GOOGLE SEARCH', 'GOOGLE SEARCH'), ('TWITTER', 'TWITTER'), ('REFERRAL', 'REFERRAL')], max_length=100),
        ),
    ]