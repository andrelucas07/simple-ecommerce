# Generated by Django 3.1.3 on 2020-11-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20201107_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavel'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
