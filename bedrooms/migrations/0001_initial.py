# Generated by Django 4.2.6 on 2023-11-15 06:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('E', 'Economico'), ('P', 'Padrão'), ('L', 'Luxuoso')], max_length=20)),
                ('status', models.CharField(choices=[('L', 'Limpos'), ('O', 'Ocupados'), ('M', 'Em Manutenção'), ('D', 'Disponivel')], max_length=20)),
            ],
        ),
    ]
