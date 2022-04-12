# Generated by Django 4.0.3 on 2022-04-10 09:56

from django.db import migrations, models
import django.db.models.deletion
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product', validators=[store.validators.validate_file_size]),
        ),
    ]