# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RoleAssignment(Model):
    """Role Assignments.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The role assignment ID.
    :vartype id: str
    :ivar name: The role assignment name.
    :vartype name: str
    :ivar type: The role assignment type.
    :vartype type: str
    :param properties: Role assignment properties.
    :type properties:
     ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentPropertiesWithScope
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'RoleAssignmentPropertiesWithScope'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(RoleAssignment, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties