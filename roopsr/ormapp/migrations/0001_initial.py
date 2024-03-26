# Generated by Django 5.0.3 on 2024-03-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('publishdate', models.DateField()),
            ],
        ),
    ]