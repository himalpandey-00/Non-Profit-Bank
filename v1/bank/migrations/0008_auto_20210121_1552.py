# Generated by Django 3.1.4 on 2021-01-21 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20210120_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bank.banktype'),
        ),
    ]