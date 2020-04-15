# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class SapMonitorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SapMonitor <azure.mgmt.saphanaonazure.models.SapMonitor>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SapMonitor]'}
    }

    def __init__(self, *args, **kwargs):

        super(SapMonitorPaged, self).__init__(*args, **kwargs)