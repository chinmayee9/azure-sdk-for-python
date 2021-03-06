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

from .format_write_settings_py3 import FormatWriteSettings


class DelimitedTextWriteSettings(FormatWriteSettings):
    """Delimited text write settings.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Required. The write setting type.
    :type type: str
    :param quote_all_text: Indicates whether string values should always be
     enclosed with quotes. Type: boolean (or Expression with resultType
     boolean).
    :type quote_all_text: object
    :param file_extension: Required. The file extension used to create the
     files. Type: string (or Expression with resultType string).
    :type file_extension: object
    """

    _validation = {
        'type': {'required': True},
        'file_extension': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'quote_all_text': {'key': 'quoteAllText', 'type': 'object'},
        'file_extension': {'key': 'fileExtension', 'type': 'object'},
    }

    def __init__(self, *, type: str, file_extension, additional_properties=None, quote_all_text=None, **kwargs) -> None:
        super(DelimitedTextWriteSettings, self).__init__(additional_properties=additional_properties, type=type, **kwargs)
        self.quote_all_text = quote_all_text
        self.file_extension = file_extension
