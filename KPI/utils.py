from statistics_page.models import Statistics
from statistics_page.utils import __remove_commas, __not_empty
from .models import KPI
from statistics_page import utils


# Updates a statistic field by the litigation field
def __update_field(statistic, field):
    if __not_empty(field):
        return statistic + float(__remove_commas(field))
    return statistic

# Update statistic object
# def __update_kpi(statistik_page, id):
#     try:
#         statistic = Statistics.objects.get(id=id)
#         statistic.contenziosi_in_gestione = __update_field(statistic.)