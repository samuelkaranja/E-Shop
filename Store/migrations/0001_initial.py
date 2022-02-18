# Generated by Django 4.0.2 on 2022-02-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='Product-Images')),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Kitchen', 'Kitchen'), ('Shoes', 'Shoes'), ('Fashion', 'Fashion'), ('Phone & Accessories', 'Phone & Accessories')], max_length=200)),
            ],
        ),
    ]
