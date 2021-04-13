# Generated by Django 3.0.5 on 2020-04-14 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='num_sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_code', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField(default=0)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookApp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookApp.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookApp.Book')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookApp.Book'),
        ),
    ]
