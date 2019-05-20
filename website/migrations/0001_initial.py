# Generated by Django 2.2.1 on 2019-05-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefones', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]