# Generated by Django 4.0.4 on 2022-05-12 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id_cidade', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id_conta', models.BigAutoField(primary_key=True, serialize=False)),
                ('tp_conta', models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente')], max_length=30, verbose_name='Tipo da conta')),
                ('id_banco', models.IntegerField()),
                ('banco', models.CharField(choices=[('Banco 1', 'Banco 1'), ('Banco 2', 'Banco 2'), ('Banco 3', 'Banco 3'), ('Banco 4', 'Banco 4')], max_length=50)),
                ('conta', models.IntegerField()),
                ('agencia', models.IntegerField(verbose_name='Agência')),
                ('operacao', models.IntegerField(verbose_name='Operação')),
            ],
            options={
                'db_table': 'contas',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id_endereco', models.BigAutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=8, verbose_name='Número')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('bairro', models.CharField(max_length=80)),
                ('complemento', models.CharField(max_length=60)),
                ('observacoes', models.TextField(verbose_name='Observações')),
                ('id_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.cidade')),
            ],
            options={
                'verbose_name': 'Endereço',
                'db_table': 'enderecos',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id_uf', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'ufs',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.BigAutoField(primary_key=True, serialize=False)),
                ('vinculo', models.CharField(choices=[('Vinculo 1', 'Vinculo 1'), ('Vinculo 2', 'Vinculo 2')], max_length=20)),
                ('cpf', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('id_conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.conta')),
                ('id_endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.endereco')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id_ocorrencia', models.BigAutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('realizada', models.BooleanField()),
                ('ocorrencia', models.TextField(verbose_name='Ocorrência')),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.pessoa')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'db_table': 'ocorrencias',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='id_uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.uf'),
        ),
    ]