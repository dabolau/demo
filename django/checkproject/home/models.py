from django.db import models
from django import forms
from django.contrib.auth.models import User

################
#步骤
################


# 数据库模型（步骤）
class Bjs_base_step(models.Model):
    '''
    步骤
    '''
    bjs_base_dual_power_switching = models.OneToOneField(
        verbose_name='双电源切换柜',
        blank=True,
        null=True,
        to='Bjs_base_dual_power_switching',
        on_delete=models.CASCADE,
    )
    bjs_base_battery_power_mainframe = models.OneToOneField(
        verbose_name='蓄电池电源主机柜',
        blank=True,
        null=True,
        to='Bjs_base_battery_power_mainframe',
        on_delete=models.CASCADE,
    )
    bjs_base_power_off_mainframe = models.OneToOneField(
        verbose_name='分时下电柜',
        blank=True,
        null=True,
        to='Bjs_base_power_off_mainframe',
        on_delete=models.CASCADE,
    )
    bjs_base_battery_mainframe = models.OneToOneField(
        verbose_name='电池柜',
        blank=True,
        null=True,
        to='Bjs_base_battery_mainframe',
        on_delete=models.CASCADE,
    )
    bjs_base_other_situation = models.OneToOneField(
        verbose_name='巡检记事',
        blank=True,
        null=True,
        to='Bjs_base_other_situation',
        on_delete=models.CASCADE,
    )

    check_man = models.ForeignKey(
        verbose_name='巡检人员',
        to=User,
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField(
        verbose_name='开始时间',
        auto_now_add=True,
    )
    end_time = models.DateTimeField(
        verbose_name='结束时间',
        auto_now=True,
    )


############
#双电源切换柜
############


# 数据库模型（双电源切换柜）
class Bjs_base_dual_power_switching(models.Model):
    '''
    双电源切换柜
    '''
    choices = (
        (11, '白灯'),
        (12, '红灯'),
        (13, '绿灯'),
        (14, '橙灯'),
        (21, '白闪'),
        (22, '红闪'),
        (23, '绿闪'),
        (24, '橙闪'),
        (99, '灭'),
    )

    vab = models.CharField(
        verbose_name='1-2',
        max_length=32,
    )
    vbc = models.CharField(
        verbose_name='2-3',
        max_length=32,
    )
    vca = models.CharField(
        verbose_name='3-1',
        max_length=32,
    )
    van = models.CharField(
        verbose_name='1-N',
        max_length=32,
    )
    vbn = models.CharField(
        verbose_name='2-N',
        max_length=32,
    )
    vcn = models.CharField(
        verbose_name='3-N',
        max_length=32,
    )
    la = models.CharField(
        verbose_name='L1',
        max_length=32,
    )
    lb = models.CharField(
        verbose_name='L2',
        max_length=32,
    )
    lc = models.CharField(
        verbose_name='L3',
        max_length=32,
    )
    ln = models.CharField(
        verbose_name='N',
        max_length=32,
    )
    voltage = models.CharField(
        verbose_name='电压',
        max_length=32,
    )
    current = models.CharField(
        verbose_name='电流',
        max_length=32,
    )
    powerful = models.CharField(
        verbose_name='功率',
        max_length=32,
    )
    city1 = models.SmallIntegerField(
        verbose_name='市电1指示灯',
        choices=choices,
    )
    city2 = models.SmallIntegerField(
        verbose_name='市电2指示灯',
        choices=choices,
    )
    cityout = models.SmallIntegerField(
        verbose_name='市电输出指示灯',
        choices=choices,
    )


################
#蓄电池电源主机柜
################


# 数据库模型（蓄电池电源主机柜）
class Bjs_base_battery_power_mainframe(models.Model):
    '''
    蓄电池电源主机柜
    '''
    normal = (
        (1, '正常'),
        (0, '不正常'),
    )

    choices = (
        (11, '白灯'),
        (12, '红灯'),
        (13, '绿灯'),
        (14, '橙灯'),
        (21, '白闪'),
        (22, '红闪'),
        (23, '绿闪'),
        (24, '橙闪'),
        (99, '灭'),
    )

    load_powered = models.SmallIntegerField(
        verbose_name='LOAD POWERED',
        choices=choices,
    )
    check_log = models.SmallIntegerField(
        verbose_name='CHECK LOG',
        choices=choices,
    )
    warning = models.SmallIntegerField(
        verbose_name='WARNING',
        choices=choices,
    )
    critical = models.SmallIntegerField(
        verbose_name='CRITICAL',
        choices=choices,
    )
    warning_number = models.CharField(
        verbose_name='告警条数',
        max_length=3,
    )
    warning_content = models.CharField(
        verbose_name='警告内容',
        max_length=32,
    )
    time_calibration = models.SmallIntegerField(
        verbose_name='时间校准',
        choices=normal,
    )
    ups_state = models.CharField(
        verbose_name='UPS STATE',
        max_length=32,
    )
    volts_in1 = models.CharField(
        verbose_name='VOLTS IN1',
        max_length=32,
    )
    volts_in2 = models.CharField(
        verbose_name='VOLTS IN2',
        max_length=32,
    )
    volts_in3 = models.CharField(
        verbose_name='VOLTS IN3',
        max_length=32,
    )
    volts_out1 = models.CharField(
        verbose_name='VOLTS OUT1',
        max_length=32,
    )
    volts_out2 = models.CharField(
        verbose_name='VOLTS OUT2',
        max_length=32,
    )
    volts_out3 = models.CharField(
        verbose_name='VOLTS OUT3',
        max_length=32,
    )
    amps1 = models.CharField(
        verbose_name='AMPS1',
        max_length=32,
    )
    amps2 = models.CharField(
        verbose_name='AMPS2',
        max_length=32,
    )
    amps3 = models.CharField(
        verbose_name='AMPS3',
        max_length=32,
    )
    load_power1 = models.CharField(
        verbose_name='负载功率1',
        max_length=32,
    )
    load_power2 = models.CharField(
        verbose_name='负载功率2',
        max_length=32,
    )
    load_power3 = models.CharField(
        verbose_name='负载功率3',
        max_length=32,
    )
    battery_output_power1 = models.CharField(
        verbose_name='蓄电池输出功率1',
        max_length=32,
    )
    battery_output_power2 = models.CharField(
        verbose_name='蓄电池输出功率2',
        max_length=32,
    )
    battery_output_power3 = models.CharField(
        verbose_name='蓄电池输出功率3',
        max_length=32,
    )
    ups_load = models.CharField(
        verbose_name='UPS LOAD(%)',
        max_length=32,
    )
    power_modules_total = models.CharField(
        verbose_name='POWER MODULES TOTAL',
        max_length=32,
    )
    power_modules_bad = models.CharField(
        verbose_name='POWER MODULES BAD',
        max_length=32,
    )
    power_modules_capacity = models.CharField(
        verbose_name='POWER MODULES CAPACITY(%VA)',
        max_length=32,
    )
    power_modules_redundancy = models.CharField(
        verbose_name='POWER MODULES REDUNDANCY',
        max_length=32,
    )
    battery_modules_runtime = models.CharField(
        verbose_name='BATTERY MODULES RUNTIME',
        max_length=32,
    )
    battery_modules_capacity = models.CharField(
        verbose_name='BATTERY MODULES CAPACITY(%)',
        max_length=32,
    )


################
#分时下电柜
################


# 数据库模型（分时下电柜）
class Bjs_base_power_off_mainframe(models.Model):
    '''
    分时下电柜
    '''
    choices = (
        (11, '白灯'),
        (12, '红灯'),
        (13, '绿灯'),
        (14, '橙灯'),
        (21, '白闪'),
        (22, '红闪'),
        (23, '绿闪'),
        (24, '橙闪'),
        (99, '灭'),
    )

    hour_05 = models.SmallIntegerField(
        verbose_name='0.5小时供电指示灯',
        choices=choices,
    )
    hour_10 = models.SmallIntegerField(
        verbose_name='1小时供电指示灯',
        choices=choices,
    )
    bypass_supply = models.SmallIntegerField(
        verbose_name='旁路供电指示灯',
        choices=choices,
    )
    timing_start = models.SmallIntegerField(
        verbose_name='计时启动指示灯',
        choices=choices,
    )
    ups_output_switch = models.SmallIntegerField(
        verbose_name='蓄电池输出指示灯',
        choices=choices,
    )


################
#电池柜
################


# 数据库模型（电池柜）
class Bjs_base_battery_mainframe(models.Model):
    '''
    电池柜
    '''
    normal = (
        (1, '正常'),
        (0, '不正常'),
    )

    battery_appearance = models.SmallIntegerField(
        verbose_name='电池外观检查（有无鼓包、起泡、漏夜）',
        choices=normal,
    )
    battery_connection_line = models.SmallIntegerField(
        verbose_name='电池连接线检查（是否牢固）',
        choices=normal,
    )
    battery_temperature = models.CharField(
        verbose_name='电池表面温度（摄氏度）',
        max_length=3,
    )
    battery_number = models.CharField(
        verbose_name='目前电池使用组数',
        max_length=3,
    )


################
#巡检记事
################


# 数据库模型（巡检记事）
class Bjs_base_other_situation(models.Model):
    '''
    巡检记事
    '''
    normal = (
        (1, '正常'),
        (0, '不正常'),
    )

    temperature = models.CharField(
        verbose_name='环境温度（摄氏度）',
        max_length=3,
    )
    smell = models.SmallIntegerField(
        verbose_name='设备室有无异味',
        choices=normal,
    )
    fire_equipment = models.SmallIntegerField(
        verbose_name='消防设施设备外观检查',
        choices=normal,
    )
    epilog = models.CharField(
        verbose_name='巡检结论',
        max_length=64,
    )
