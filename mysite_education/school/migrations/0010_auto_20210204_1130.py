# Generated by Django 3.0.7 on 2021-02-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20210203_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_category',
            field=models.CharField(choices=[('N&P', 'Nursery & Primary'), ('JSS', 'Junior'), ('SSS', 'Senior')], default='Nursery & Primary', help_text='Please click on this to select the category the subject falls under', max_length=20),
        ),
    ]
