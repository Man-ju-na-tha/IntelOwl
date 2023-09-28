# Generated by Django 4.1.10 on 2023-09-14 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "api_app",
            "0046_remove_pluginconfig_plugin_config_no_config_all_null_and_more",
        ),
        ("connectors_manager", "0021_alter_connectorconfig_python_module"),
    ]

    operations = [
        migrations.AlterField(
            model_name="connectorconfig",
            name="python_module",
            field=models.ForeignKey(
                limit_choices_to={"base_path": "api_app.connectors_manager.connectors"},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)ss",
                to="api_app.pythonmodule",
            ),
        ),
    ]
