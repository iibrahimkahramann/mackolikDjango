# Generated by Django 4.2.5 on 2023-10-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mackolik', '0002_rename_skor_matches_club1_skor_matches_club2_skor'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pozition',
            field=models.CharField(max_length=20, null=True),
        ),
    ]