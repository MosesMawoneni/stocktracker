# Generated by Django 4.2.4 on 2023-10-17 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0007_alter_storepersonnelprofile_user_worker_issue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="quantity_issued",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="present_quantity",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="recent_purchase_quantity",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="shelf_number",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
