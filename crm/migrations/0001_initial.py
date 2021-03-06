# Generated by Django 4.0.1 on 2022-01-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=64)),
                ('takes_to', models.CharField(max_length=64)),
                ('icon', models.CharField(default='None', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='crm.NavbarItem')),
            ],
        ),
    ]
