from django.db import models
from django.utils.translation import gettext_lazy as gtl
import uuid


class IfcTask(models.Model):
    # IfcRoot Attributes.
    Status = models.CharField(max_length=255)
    GlobalId = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=False)
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)

    # IfcObject Attributes
    ObjectType = models.CharField(max_length=255, null=True, blank=True)


class IfcRelSequence(models.Model):
    class SequenceTypeEnum(models.TextChoices):
        FINISH_FINISH = 'FF', gtl('Finish Finish')
        FINISH_START = 'FS', gtl('Finish Start')
        START_FINISH = 'SF', gtl('Start Finish')
        START_START = 'SS', gtl('Start Start')
        USERDEFINED = 'UD', gtl('User Defined')
        NOTDEFINED = 'ND', gtl('Not Defined')
    RelatingProcess = models.ForeignKey(IfcTask,
                                        related_name='RelatingProcess',
                                        on_delete=models.CASCADE)
    RelatedProcess = models.ForeignKey(IfcTask,
                                       related_name='RelatedProcess',
                                       on_delete=models.CASCADE)
    TimeLag = models.DurationField(blank=True, null=True)
    SequenceType = models.CharField(max_length=2,
                                    choices=SequenceTypeEnum.choices,
                                    default=SequenceTypeEnum.FINISH_START)
    UserDefinedSequenceType = models.CharField(max_length=255,
                                               null=True, blank=True)
