# Generated by Django 4.0.1 on 2022-04-10 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_contact'),
        ('base', '0003_caracteristiques_images_marques_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('statut', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('caracteristiques', models.ManyToManyField(blank=True, to='base.Caracteristiques')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.images')),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_products', to='base.marques')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('sous_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_products', to='base.souscategories')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['-updated', '-created'],
            },
        ),
    ]