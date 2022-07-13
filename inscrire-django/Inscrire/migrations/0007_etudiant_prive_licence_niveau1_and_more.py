# Generated by Django 4.0.6 on 2022-07-08 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inscrire', '0006_etudiant_prive_licence_etudiant_prive_master_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant_Prive_Licence_Niveau1',
            fields=[
                ('etudiant_prive_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_prive_licence')),
            ],
            options={
                'verbose_name': 'Licence privé L1',
                'verbose_name_plural': 'Licence privé L1',
            },
            bases=('Inscrire.etudiant_prive_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Prive_Licence_Niveau2',
            fields=[
                ('etudiant_prive_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_prive_licence')),
            ],
            options={
                'verbose_name': 'Licence privé L2',
                'verbose_name_plural': 'Licence privé L2',
            },
            bases=('Inscrire.etudiant_prive_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Prive_Licence_Niveau3',
            fields=[
                ('etudiant_prive_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_prive_licence')),
            ],
            options={
                'verbose_name': 'Licence privé L3',
                'verbose_name_plural': 'Licence privé L3',
            },
            bases=('Inscrire.etudiant_prive_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Prive_Master_Niveau1',
            fields=[
                ('etudiant_prive_master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_prive_master')),
            ],
            options={
                'abstract': False,
            },
            bases=('Inscrire.etudiant_prive_master',),
        ),
        migrations.CreateModel(
            name='Etudiant_Prive_Master_Niveau2',
            fields=[
                ('etudiant_prive_master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_prive_master')),
            ],
            options={
                'abstract': False,
            },
            bases=('Inscrire.etudiant_prive_master',),
        ),
        migrations.CreateModel(
            name='Etudiant_Public_Licence_Niveau1',
            fields=[
                ('etudiant_public_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_public_licence')),
            ],
            options={
                'verbose_name': 'Licence public L1',
                'verbose_name_plural': 'Licence public L1',
            },
            bases=('Inscrire.etudiant_public_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Public_Licence_Niveau2',
            fields=[
                ('etudiant_public_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_public_licence')),
            ],
            options={
                'verbose_name': 'Licence public L2',
                'verbose_name_plural': 'Licence public L2',
            },
            bases=('Inscrire.etudiant_public_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Public_Licence_Niveau3',
            fields=[
                ('etudiant_public_licence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_public_licence')),
            ],
            options={
                'verbose_name': 'Licence public L3',
                'verbose_name_plural': 'Licence public L3',
            },
            bases=('Inscrire.etudiant_public_licence',),
        ),
        migrations.CreateModel(
            name='Etudiant_Public_Master_Niveau1',
            fields=[
                ('etudiant_public_master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_public_master')),
            ],
            options={
                'verbose_name': 'Master public M1',
                'verbose_name_plural': 'Master public M1',
            },
            bases=('Inscrire.etudiant_public_master',),
        ),
        migrations.CreateModel(
            name='Etudiant_Public_Master_Niveau2',
            fields=[
                ('etudiant_public_master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inscrire.etudiant_public_master')),
            ],
            options={
                'verbose_name': 'Master public M2',
                'verbose_name_plural': 'Master public M2',
            },
            bases=('Inscrire.etudiant_public_master',),
        ),
    ]
