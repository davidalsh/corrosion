# Generated by Django 4.2.16 on 2024-11-09 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackageItemType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='package',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='package',
            name='multimedia_systems',
        ),
        migrations.RemoveField(
            model_name='package',
            name='rims',
        ),
        migrations.RemoveField(
            model_name='package',
            name='upholstery',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='MultimediaSystem',
        ),
        migrations.DeleteModel(
            name='Rims',
        ),
        migrations.DeleteModel(
            name='Upholstery',
        ),
        migrations.AddField(
            model_name='packageitem',
            name='package_item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_items', to='cars.packageitemtype'),
        ),
        migrations.AddField(
            model_name='package',
            name='package_items',
            field=models.ManyToManyField(related_name='packages', to='cars.packageitem'),
        ),
    ]
