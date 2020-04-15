# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource import TrackedResource


class SapMonitor(TrackedResource):
    """SAP monitor info on Azure (ARM properties and SAP monitor properties).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Network/trafficManagerProfiles.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict
    :param location: The Azure Region where the resource lives
    :type location: str
    :ivar provisioning_state: State of provisioning of the HanaInstance.
     Possible values include: 'Accepted', 'Creating', 'Updating', 'Failed',
     'Succeeded', 'Deleting', 'Migrating'
    :vartype provisioning_state: str or :class:`HanaProvisioningStatesEnum
     <azure.mgmt.saphanaonazure.models.HanaProvisioningStatesEnum>`
    :ivar managed_resource_group_name: The name of the resource group the SAP
     Monitor resources get deployed into.
    :vartype managed_resource_group_name: str
    :param log_analytics_workspace_arm_id: The ARM ID of the Log Analytics
     Workspace that is used for monitoring
    :type log_analytics_workspace_arm_id: str
    :param enable_customer_analytics: The value indicating whether to send
     analytics to Microsoft
    :type enable_customer_analytics: bool
    :param log_analytics_workspace_id: The workspace ID of the log analytics
     workspace to be used for monitoring
    :type log_analytics_workspace_id: str
    :param log_analytics_workspace_shared_key: The shared key of the log
     analytics workspace that is used for monitoring
    :type log_analytics_workspace_shared_key: str
    :ivar sap_monitor_collector_version: The version of the payload running in
     the Collector VM
    :vartype sap_monitor_collector_version: str
    :param monitor_subnet: The subnet which the SAP monitor will be deployed
     in
    :type monitor_subnet: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'managed_resource_group_name': {'readonly': True},
        'sap_monitor_collector_version': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'managed_resource_group_name': {'key': 'properties.managedResourceGroupName', 'type': 'str'},
        'log_analytics_workspace_arm_id': {'key': 'properties.logAnalyticsWorkspaceArmId', 'type': 'str'},
        'enable_customer_analytics': {'key': 'properties.enableCustomerAnalytics', 'type': 'bool'},
        'log_analytics_workspace_id': {'key': 'properties.logAnalyticsWorkspaceId', 'type': 'str'},
        'log_analytics_workspace_shared_key': {'key': 'properties.logAnalyticsWorkspaceSharedKey', 'type': 'str'},
        'sap_monitor_collector_version': {'key': 'properties.sapMonitorCollectorVersion', 'type': 'str'},
        'monitor_subnet': {'key': 'properties.monitorSubnet', 'type': 'str'},
    }

    def __init__(self, tags=None, location=None, log_analytics_workspace_arm_id=None, enable_customer_analytics=None, log_analytics_workspace_id=None, log_analytics_workspace_shared_key=None, monitor_subnet=None):
        super(SapMonitor, self).__init__(tags=tags, location=location)
        self.provisioning_state = None
        self.managed_resource_group_name = None
        self.log_analytics_workspace_arm_id = log_analytics_workspace_arm_id
        self.enable_customer_analytics = enable_customer_analytics
        self.log_analytics_workspace_id = log_analytics_workspace_id
        self.log_analytics_workspace_shared_key = log_analytics_workspace_shared_key
        self.sap_monitor_collector_version = None
        self.monitor_subnet = monitor_subnet