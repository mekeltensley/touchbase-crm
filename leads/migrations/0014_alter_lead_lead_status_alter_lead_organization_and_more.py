# Generated by Django 4.0.1 on 2022-01-20 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_alter_lead_last_contacted_alter_lead_lead_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('ATTEMPTED TO CONTACT', 'ATTEMPTED TO CONTACT'), ('CONNECTED', 'CONNECTED'), ('BAD TIMING', 'BAD TIMING '), ('NEW', 'NEW'), ('UNQUALIFIED', 'UNQUALIFIED'), ('OPEN DEAL', 'OPEN DEAL'), ('IN PROGRESS', 'IN PROGRESS'), ('OPEN', 'OPEN')], max_length=100),
        ),
        migrations.AlterField(
            model_name='lead',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='source_of_lead',
            field=models.CharField(blank=True, choices=[('INSTAGRAM', 'INSTAGRAM'), ('GOOGLE SEARCH', 'GOOGLE SEARCH'), ('TWITTER', 'TWITTER'), ('REFERRAL', 'REFERRAL')], max_length=100),
        ),
    ]