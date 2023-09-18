from django.db import models
from django.utils.translation import gettext_lazy as gtl
import uuid


# As defined by IFC4.3
class IfcSchedulingTime:
    Name = models.CharField(max_length=255)

    class IfcDataOriginEnum(models.TextChoices):
        MEASURED = 'MD', gtl('Measured')
        PREDICTED = 'PD', gtl('Predicted')
        SIMULATED = 'SM', gtl('Simulated')
        USUERDEFINED = 'UD', gtl('User Defined')
        NOTDEFINED = 'ND', gtl('Not Defined')

    DataOrigin = models.CharField(max_length=2,
                                  choices=IfcDataOriginEnum.choices,
                                  default=IfcDataOriginEnum.NOTDEFINED)
    UserDefinedDataOrigin = models.CharField(max_length=255, null=True,
                                             blank=True)


class IfcTaskTime(IfcSchedulingTime, models.Model):
    class DurationTypeEnum(models.TextChoices):
        ELAPSEDTIME = 'ET', gtl('Elapsed Time')
        WORKTIME = 'WT', gtl('Work Time')
        NOTDEFINED = 'ND', gtl('Not Defined')
    DurationType = models.CharField(max_length=3,
                                    choices=DurationTypeEnum.choices,
                                    default=DurationTypeEnum.WORKTIME)
    ScheduleStart = models.DateTimeField(blank=True, null=True)
    ScheduleFinish = models.DateTimeField(blank=True, null=True)
    EarlyStart = models.DateTimeField(blank=True, null=True)
    EarlyFinish = models.DateTimeField(blank=True, null=True)
    LateStart = models.DateTimeField(blank=True, null=True)
    LateFinish = models.DateTimeField(blank=True, null=True)
    FreeFloat = models.DurationField(blank=True, null=True)
    TotalFloat = models.DurationField(blank=True, null=True)
    IsCritical = models.BooleanField(default=False)
    StatusTime = models.DateTimeField(blank=True, null=True)
    ActualDuration = models.DurationField(blank=True, null=True)
    ActualStart = models.DateTimeField(blank=True, null=True)
    ActualFinish = models.DateTimeField(blank=True, null=True)
    RemainingTime = models.DurationField(blank=True, null=True)
    Completition = models.FloatField(default=0.0)


class IfcProcess(models.Model):
    '''I need to create the object the higher objects as it will make
        It will make it easier to copy the data model directly. I also need to 
        follow the assignment diagram n the Process object.
    '''
    LongDescription = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class IfcTask(IfcProcess):
    # IfcRoot Attributes.
    GlobalId = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)

    # IfcObject Attributes
    ObjectType = models.CharField(max_length=255, null=True, blank=True)

    # IfcTask Attributes
    Status = models.CharField(max_length=255)
    WorkMethod = models.CharField(max_length=255, null=True, blank=True)
    IsMilestone = models.BooleanField(default=False)
    Priority = models.IntegerField(default=0)

    class IfcTaskTypeEnum(models.TextChoices):
        ADJUSTMENT = 'adj', gtl('Adjustment')
        ATTENDANCE = 'att', gtl('Attendance')
        CALIBRATION = 'cal', gtl('Calibration')
        CONSTRUCTION = 'con', gtl('Construction')
        DEMOLITION = 'dem', gtl('Demolition')
        DISMANTLE = 'dis', gtl('Dismantle')
        DISPOSAL = 'dsp', gtl('Disposal')
        EMERGENCY = 'emg', gtl('Emergency')
        INSPECTION = 'ins', gtl('Inspection'),
        INSTALLATION = 'int', gtl('Installation')
        LOGISTIC = 'log', gtl('Logistic')
        MAINTENANCE = 'man', gtl('Maintenace')
        MOVE = 'mov', gtl('Move')
        OPERATION = 'opr', gtl('Operation')
        REMOVAL = 'rem', gtl('Removal')
        RENOVATION = 'ren', gtl('Renovation')
        SAFETY = 'saf', gtl('Safety')
        SHUTDOWN = 'shu', gtl('Shutdown')
        STARTUP = 'sta', gtl('Startup')
        TESTING = 'tes', gtl('Testing')
        TROUBLESHOOTING = 'tbl', gtl('Troubleshooting')
        USERDEFINED = 'usr', gtl('User Defined')
        NOTDEFINED = 'ndf', gtl('Not Defined')
    TaskType = models.CharField(max_length=3,
                                choices=IfcTaskTypeEnum.choices,
                                default=IfcTaskTypeEnum.CONSTRUCTION)
    TaskTime = models.OneToOneField(IfcTaskTime, on_delete=models.CASCADE)


class IfcRelSequence(models.Model):
    class SequenceTypeEnum(models.TextChoices):
        FINISH_FINISH = 'FF', gtl('Finish Finish')
        FINISH_START = 'FS', gtl('Finish Start')
        START_FINISH = 'SF', gtl('Start Finish')
        START_START = 'SS', gtl('Start Start')
        USERDEFINED = 'UD', gtl('User Defined')
        NOTDEFINED = 'ND', gtl('Not Defined')
    GlobalId = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=True)
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
