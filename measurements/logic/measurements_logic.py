from variables.logic.variables_logic import get_variable
from ..models import Measurement
from datetime import datetime

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mar_pk):
    measurements = Measurement.objects.get(pk=mar_pk)
    return measurements

def create_measurement(mar):
    measurement = Measurement(variable=get_variable(mar["var_pk"]), value=mar["value"], unit=mar["unit"], place=mar["place"])
    measurement.save()
    return measurement

def update_measurement(mar_pk, new_mar):
    measurement = get_measurement(mar_pk)
    measurement.variable = get_variable(new_mar["var_pk"])
    measurement.value = new_mar["value"]
    measurement.unit = new_mar["unit"]
    measurement.place = new_mar["place"]
    measurement.dateTime = datetime.strptime(new_mar["dateTime"], '%Y-%m-%d %H:%M:%S')
    measurement.save()
    return measurement

def delete_measurement(mar_pk):
    measurement = get_measurement(mar_pk)
    measurement.delete()
    return measurement