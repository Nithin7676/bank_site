# Generated by Django 4.1.6 on 2023-03-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_tbl_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_application',
            name='cheque',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tbl_application',
            name='credit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tbl_application',
            name='debit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_application',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_application',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tbl_application',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
