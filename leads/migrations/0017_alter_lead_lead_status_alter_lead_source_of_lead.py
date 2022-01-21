# Generated by Django 4.0.1 on 2022-01-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_alter_lead_lead_status_alter_lead_source_of_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('IN PROGRESS', 'IN PROGRESS'), ('NEW', 'NEW'), ('ATTEMPTED TO CONTACT', 'ATTEMPTED TO CONTACT'), ('OPEN', 'OPEN'), ('OPEN DEAL', 'OPEN DEAL'), ('UNQUALIFIED', 'UNQUALIFIED'), ('BAD TIMING', 'BAD TIMING '), ('CONNECTED', 'CONNECTED')], max_length=100),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source_of_lead',
            field=models.CharField(blank=True, choices=[('REFERRAL', 'REFERRAL'), ('INSTAGRAM', 'INSTAGRAM'), ('GOOGLE SEARCH', 'GOOGLE SEARCH'), ('TWITTER', 'TWITTER')], max_length=100),
        ),
    ]