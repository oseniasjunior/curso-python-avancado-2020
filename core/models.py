from django.db import models


# Create your models here.

class Department(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104,
        unique=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'department'
        managed = True
