# Generated by Django 2.0.2 on 2018-05-10 12:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=0, max_length=200, verbose_name='Email')),
                ('name', models.CharField(default=0, max_length=200, verbose_name='Nom')),
                ('city', models.CharField(default=0, max_length=200, verbose_name='Ville')),
                ('quarter', models.CharField(default=0, max_length=200, verbose_name='Quartier')),
                ('street', models.CharField(default=0, max_length=200, verbose_name='Numéro de rue')),
                ('door', models.CharField(default=0, max_length=200, verbose_name='Numéro de porte')),
                ('phone', models.CharField(default=0, max_length=200, verbose_name='Téléphone')),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name="date d'envoi")),
                ('contacted', models.BooleanField(default=False, verbose_name='demande traitée')),
                ('contact', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='commerce.Contact')),
            ],
            options={
                'verbose_name_plural': 'Commandes',
                'verbose_name': 'Commande',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_photo', models.ImageField(upload_to='photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom du produit')),
                ('short_desc', models.CharField(max_length=150, verbose_name='Description courte')),
                ('long_desc', models.TextField(verbose_name='Description longue')),
                ('image', models.ImageField(null=True, upload_to='photo/', verbose_name='Miniature du produit')),
                ('price', models.CharField(max_length=200, verbose_name='Prix du produit')),
            ],
            options={
                'verbose_name_plural': 'Produits',
                'verbose_name': 'Produit',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='commerce.Product'),
        ),
    ]
