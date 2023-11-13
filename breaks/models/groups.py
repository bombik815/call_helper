from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Group(models.Model):
    organisation = models.ForeignKey(to='breaks.Organisation', on_delete=models.CASCADE, related_name='groups',
                                     verbose_name='Организация', )
    name = models.CharField('Название', max_length=255)
    manager = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='group_managers',
                                verbose_name='Менеджер', )
    employees = models.ManyToManyField(User, related_name='group_employees', verbose_name='Сотрудники',
                                       blank=True, )
    min_activ = models.PositiveSmallIntegerField(verbose_name='Минимальное количество активных сотрудников', null=True, blank=True,)
    break_start = models.TimeField(verbose_name='Начало обеда', null=True, blank=True,)
    break_end = models.TimeField(verbose_name='Конец обеда', null=True, blank=True,)
    break_max_duration = models.PositiveSmallIntegerField(verbose_name='Максимальная длительность обеда', null=True, blank=True,)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'