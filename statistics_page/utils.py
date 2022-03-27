from litigations.models import Litigation
from .models import Statistics
from decimal import Decimal


# Removes commas from litigation fields
def __remove_commas(field):
    return Decimal("".join(field.split(",")))


# Checks if a variable is empty or not
def __not_empty(field):
    return field and field != ""


# Updates a statistic field by the litigation field
def __update_field(statistic, field):
    if __not_empty(field):
        return statistic + float(__remove_commas(field))
    return statistic


# Update statistic object
def __update_statistic(litigation, id):
    try:
        statistic = Statistics.objects.get(id=id)
        statistic.initial_value = __update_field(statistic.initial_value, litigation.initial_estimation_value)
        statistic.objective_value = __update_field(statistic.objective_value, litigation.target_value)
        statistic.final_value = __update_field(statistic.final_value, litigation.final_value)
        statistic.revue_value = __update_field(statistic.revue_value, litigation.revenue)
        statistic.total_cost_value = __update_field(statistic.total_cost_value, litigation.total_cost)
        statistic.ebit = __update_field(statistic.ebit, litigation.EBIT)
        statistic.number = statistic.number + 1
        objective_or_final_value = 0
        if statistic.id == 4 or statistic.id == 2:
            objective_or_final_value = statistic.objective_value
        elif statistic.id == 3:
            objective_or_final_value = statistic.final_value

        if statistic.initial_value != 0:
            statistic.total_value = round((objective_or_final_value * 100) / statistic.initial_value, 2)
        else:
            statistic.total_value = 0

        if litigation.EBIt_percent:
            statistic.ebit_percent = statistic.ebit_percent + float(litigation.EBIt_percent)

        statistic.save()
    except Statistics.DoesNotExist:
        __create_statistic(id)


# Check if litigation is closed, with contract or not
def __make_litigation_decision(litigation):
    litigation_is_closed = litigation.closed
    litigation_is_opened = not litigation_is_closed
    contract_uploaded = litigation.upload_pdf != ""
    contract_not_uploaded = not contract_uploaded

    __update_statistic(litigation, 4)
    if litigation_is_closed and contract_uploaded:
        __update_statistic(litigation, 3)
    elif litigation_is_opened and contract_uploaded:
        __update_statistic(litigation, 2)
    elif litigation_is_opened and contract_not_uploaded:
        __update_statistic(litigation, 1)


# Clear the statistics database and recreate the values based on the litigations
def __reset_statistic_values():
    for i in range(1, 5):
        try:
            statistic = Statistics.objects.get(id=i)
            statistic.number = 0
            statistic.initial_value = 0
            statistic.objective_value = 0
            statistic.final_value = 0
            statistic.total_value = 0
            statistic.revue_value = 0
            statistic.total_cost_value = 0
            statistic.ebit = 0
            statistic.ebit_percent = 0
            statistic.save()
        except Statistics.DoesNotExist:
            __create_statistic(i)


# If a statistic does not exist by id create it
def __create_statistic(id):
    statistic = Statistics()
    statistic.id = id
    statistic.number = 0
    statistic.initial_value = 0
    statistic.objective_value = 0
    statistic.final_value = 0
    statistic.total_value = 0
    statistic.revue_value = 0
    statistic.total_cost_value = 0
    statistic.ebit = 0
    statistic.ebit_percent = 0
    if id == 1:
        statistic.title = "Contenzioni in trativa senza contratto"
    elif id == 2:
        statistic.title = "Contenzioni aperti (not chiusa) con contratto"
    elif id == 3:
        statistic.title = "Contenzioni chiusi con contratto"
    elif id == 4:
        statistic.title = "Contenzioni in gestione"
    statistic.save()


def __make_post_processing():
    for i in range(1, 5):
        statistic = Statistics.objects.get(id=i)
        if statistic.number != 0:
            statistic.ebit_percent = round(statistic.ebit_percent / statistic.number, 2)
        else:
            statistic.ebit_percent = 0
        statistic.save()


# Start the statistic objects
def build_statistics_objects():
    litigation_list = Litigation.objects.all()
    __reset_statistic_values()
    for litigation in litigation_list:
        __make_litigation_decision(litigation)
    __make_post_processing()
