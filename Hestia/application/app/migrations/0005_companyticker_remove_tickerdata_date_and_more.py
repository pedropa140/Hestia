# Generated by Django 5.0.4 on 2024-04-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_tickerdata_date_alter_tickerdata_ticker'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyTicker',
            fields=[
                ('company_name', models.CharField(default='Unknown', max_length=100)),
                ('ticker', models.CharField(default='TICK', max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='tickerdata',
            name='date',
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='book_to_share_value',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='book_value',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='company_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='current_ratio',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='debt_ratio',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='dividend_yield',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='earnings_per_share',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='end_close',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='end_date',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='end_high',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='end_low',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='tickerdata',
            name='end_open',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='start_close',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='start_date',
            field=models.DateField(default='1900-01-01', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='start_high',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='start_low',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='start_open',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='ticker',
            field=models.CharField(default='TICK', max_length=4),
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='volume',
            field=models.FloatField(default=-1.0),
        ),
    ]
