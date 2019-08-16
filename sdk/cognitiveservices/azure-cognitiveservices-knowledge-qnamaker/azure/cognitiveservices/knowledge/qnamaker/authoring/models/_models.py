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
from msrest.exceptions import HttpOperationError


class ActiveLearningSettingsDTO(Model):
    """Active Learning settings of the endpoint.

    :param enable: True/False string providing Active Learning
    :type enable: str
    """

    _attribute_map = {
        'enable': {'key': 'enable', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ActiveLearningSettingsDTO, self).__init__(**kwargs)
        self.enable = kwargs.get('enable', None)


class AlterationsDTO(Model):
    """Collection of words that are synonyms.

    All required parameters must be populated in order to send to Azure.

    :param alterations: Required. Words that are synonymous with each other.
    :type alterations: list[str]
    """

    _validation = {
        'alterations': {'required': True},
    }

    _attribute_map = {
        'alterations': {'key': 'alterations', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AlterationsDTO, self).__init__(**kwargs)
        self.alterations = kwargs.get('alterations', None)


class ContextDTO(Model):
    """Context associated with Qna.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, **kwargs):
        super(ContextDTO, self).__init__(**kwargs)
        self.is_context_only = kwargs.get('is_context_only', None)
        self.prompts = kwargs.get('prompts', None)


class CreateKbDTO(Model):
    """Post body schema for CreateKb operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Friendly name for the knowledgebase.
    :type name: str
    :param qna_list: List of Q-A (QnADTO) to be added to the knowledgebase.
     Q-A Ids are assigned by the service and should be omitted.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTO]
    :param urls: List of URLs to be used for extracting Q-A.
    :type urls: list[str]
    :param files: List of files from which to Extract Q-A.
    :type files:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.FileDTO]
    """

    _validation = {
        'name': {'required': True, 'max_length': 100, 'min_length': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'qna_list': {'key': 'qnaList', 'type': '[QnADTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'files': {'key': 'files', 'type': '[FileDTO]'},
    }

    def __init__(self, **kwargs):
        super(CreateKbDTO, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.qna_list = kwargs.get('qna_list', None)
        self.urls = kwargs.get('urls', None)
        self.files = kwargs.get('files', None)


class CreateKbInputDTO(Model):
    """Input to create KB.

    :param qna_list: List of QNA to be added to the index. Ids are generated
     by the service and should be omitted.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTO]
    :param urls: List of URLs to be added to knowledgebase.
    :type urls: list[str]
    :param files: List of files to be added to knowledgebase.
    :type files:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.FileDTO]
    """

    _attribute_map = {
        'qna_list': {'key': 'qnaList', 'type': '[QnADTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'files': {'key': 'files', 'type': '[FileDTO]'},
    }

    def __init__(self, **kwargs):
        super(CreateKbInputDTO, self).__init__(**kwargs)
        self.qna_list = kwargs.get('qna_list', None)
        self.urls = kwargs.get('urls', None)
        self.files = kwargs.get('files', None)


class DeleteKbContentsDTO(Model):
    """PATCH body schema of Delete Operation in UpdateKb.

    :param ids: List of Qna Ids to be deleted
    :type ids: list[int]
    :param sources: List of sources to be deleted from knowledgebase.
    :type sources: list[str]
    """

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'sources': {'key': 'sources', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(DeleteKbContentsDTO, self).__init__(**kwargs)
        self.ids = kwargs.get('ids', None)
        self.sources = kwargs.get('sources', None)


class EndpointKeysDTO(Model):
    """Schema for EndpointKeys generate/refresh operations.

    :param primary_endpoint_key: Primary Access Key.
    :type primary_endpoint_key: str
    :param secondary_endpoint_key: Secondary Access Key.
    :type secondary_endpoint_key: str
    :param installed_version: Current version of runtime.
    :type installed_version: str
    :param last_stable_version: Latest version of runtime.
    :type last_stable_version: str
    """

    _attribute_map = {
        'primary_endpoint_key': {'key': 'primaryEndpointKey', 'type': 'str'},
        'secondary_endpoint_key': {'key': 'secondaryEndpointKey', 'type': 'str'},
        'installed_version': {'key': 'installedVersion', 'type': 'str'},
        'last_stable_version': {'key': 'lastStableVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EndpointKeysDTO, self).__init__(**kwargs)
        self.primary_endpoint_key = kwargs.get('primary_endpoint_key', None)
        self.secondary_endpoint_key = kwargs.get('secondary_endpoint_key', None)
        self.installed_version = kwargs.get('installed_version', None)
        self.last_stable_version = kwargs.get('last_stable_version', None)


class EndpointSettingsDTO(Model):
    """Endpoint settings.

    :param active_learning: Active Learning settings of the endpoint.
    :type active_learning:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.EndpointSettingsDTOActiveLearning
    """

    _attribute_map = {
        'active_learning': {'key': 'activeLearning', 'type': 'EndpointSettingsDTOActiveLearning'},
    }

    def __init__(self, **kwargs):
        super(EndpointSettingsDTO, self).__init__(**kwargs)
        self.active_learning = kwargs.get('active_learning', None)


class EndpointSettingsDTOActiveLearning(ActiveLearningSettingsDTO):
    """Active Learning settings of the endpoint.

    :param enable: True/False string providing Active Learning
    :type enable: str
    """

    _attribute_map = {
        'enable': {'key': 'enable', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EndpointSettingsDTOActiveLearning, self).__init__(**kwargs)


class Error(Model):
    """The error object. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes.
     Possible values include: 'BadArgument', 'Forbidden', 'NotFound',
     'KbNotFound', 'Unauthorized', 'Unspecified', 'EndpointKeysError',
     'QuotaExceeded', 'QnaRuntimeError', 'SKULimitExceeded',
     'OperationNotFound', 'ServiceError', 'ValidationFailure',
     'ExtractionFailure'
    :type code: str or
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.ErrorCodeType
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this
     reported error.
    :type details:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.Error]
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.inner_error = kwargs.get('inner_error', None)


class ErrorResponse(Model):
    """Error response. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :param error: The error object.
    :type error:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ErrorResponseError(Error):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes.
     Possible values include: 'BadArgument', 'Forbidden', 'NotFound',
     'KbNotFound', 'Unauthorized', 'Unspecified', 'EndpointKeysError',
     'QuotaExceeded', 'QnaRuntimeError', 'SKULimitExceeded',
     'OperationNotFound', 'ServiceError', 'ValidationFailure',
     'ExtractionFailure'
    :type code: str or
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.ErrorCodeType
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this
     reported error.
    :type details:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.Error]
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponseError, self).__init__(**kwargs)


class FileDTO(Model):
    """DTO to hold details of uploaded files.

    All required parameters must be populated in order to send to Azure.

    :param file_name: Required. File name. Supported file types are ".tsv",
     ".pdf", ".txt", ".docx", ".xlsx".
    :type file_name: str
    :param file_uri: Required. Public URI of the file.
    :type file_uri: str
    """

    _validation = {
        'file_name': {'required': True, 'max_length': 200, 'min_length': 1},
        'file_uri': {'required': True},
    }

    _attribute_map = {
        'file_name': {'key': 'fileName', 'type': 'str'},
        'file_uri': {'key': 'fileUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FileDTO, self).__init__(**kwargs)
        self.file_name = kwargs.get('file_name', None)
        self.file_uri = kwargs.get('file_uri', None)


class InnerErrorModel(Model):
    """An object containing more specific information about the error. As per
    Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :param code: A more specific error code than was provided by the
     containing error.
    :type code: str
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.InnerErrorModel
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, **kwargs):
        super(InnerErrorModel, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.inner_error = kwargs.get('inner_error', None)


class KnowledgebaseDTO(Model):
    """Response schema for CreateKb operation.

    :param id: Unique id that identifies a knowledgebase.
    :type id: str
    :param host_name: URL host name at which the knowledgebase is hosted.
    :type host_name: str
    :param last_accessed_timestamp: Time stamp at which the knowledgebase was
     last accessed (UTC).
    :type last_accessed_timestamp: str
    :param last_changed_timestamp: Time stamp at which the knowledgebase was
     last modified (UTC).
    :type last_changed_timestamp: str
    :param last_published_timestamp: Time stamp at which the knowledgebase was
     last published (UTC).
    :type last_published_timestamp: str
    :param name: Friendly name of the knowledgebase.
    :type name: str
    :param user_id: User who created / owns the knowledgebase.
    :type user_id: str
    :param urls: URL sources from which Q-A were extracted and added to the
     knowledgebase.
    :type urls: list[str]
    :param sources: Custom sources from which Q-A were extracted or explicitly
     added to the knowledgebase.
    :type sources: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'last_accessed_timestamp': {'key': 'lastAccessedTimestamp', 'type': 'str'},
        'last_changed_timestamp': {'key': 'lastChangedTimestamp', 'type': 'str'},
        'last_published_timestamp': {'key': 'lastPublishedTimestamp', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'sources': {'key': 'sources', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(KnowledgebaseDTO, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.host_name = kwargs.get('host_name', None)
        self.last_accessed_timestamp = kwargs.get('last_accessed_timestamp', None)
        self.last_changed_timestamp = kwargs.get('last_changed_timestamp', None)
        self.last_published_timestamp = kwargs.get('last_published_timestamp', None)
        self.name = kwargs.get('name', None)
        self.user_id = kwargs.get('user_id', None)
        self.urls = kwargs.get('urls', None)
        self.sources = kwargs.get('sources', None)


class KnowledgebasesDTO(Model):
    """Collection of knowledgebases owned by a user.

    :param knowledgebases: Collection of knowledgebase records.
    :type knowledgebases:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.KnowledgebaseDTO]
    """

    _attribute_map = {
        'knowledgebases': {'key': 'knowledgebases', 'type': '[KnowledgebaseDTO]'},
    }

    def __init__(self, **kwargs):
        super(KnowledgebasesDTO, self).__init__(**kwargs)
        self.knowledgebases = kwargs.get('knowledgebases', None)


class MetadataDTO(Model):
    """Name - value pair of metadata.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Metadata name.
    :type name: str
    :param value: Required. Metadata value.
    :type value: str
    """

    _validation = {
        'name': {'required': True, 'max_length': 100, 'min_length': 1},
        'value': {'required': True, 'max_length': 500, 'min_length': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MetadataDTO, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)


class Operation(Model):
    """Record to track long running operation.

    :param operation_state: Operation state. Possible values include:
     'Failed', 'NotStarted', 'Running', 'Succeeded'
    :type operation_state: str or
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.OperationStateType
    :param created_timestamp: Timestamp when the operation was created.
    :type created_timestamp: str
    :param last_action_timestamp: Timestamp when the current state was
     entered.
    :type last_action_timestamp: str
    :param resource_location: Relative URI to the target resource location for
     completed resources.
    :type resource_location: str
    :param user_id: User Id
    :type user_id: str
    :param operation_id: Operation Id.
    :type operation_id: str
    :param error_response: Error details in case of failures.
    :type error_response:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.ErrorResponse
    """

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'str'},
        'created_timestamp': {'key': 'createdTimestamp', 'type': 'str'},
        'last_action_timestamp': {'key': 'lastActionTimestamp', 'type': 'str'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'error_response': {'key': 'errorResponse', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.operation_state = kwargs.get('operation_state', None)
        self.created_timestamp = kwargs.get('created_timestamp', None)
        self.last_action_timestamp = kwargs.get('last_action_timestamp', None)
        self.resource_location = kwargs.get('resource_location', None)
        self.user_id = kwargs.get('user_id', None)
        self.operation_id = kwargs.get('operation_id', None)
        self.error_response = kwargs.get('error_response', None)


class PromptDTO(Model):
    """Prompt for an answer.

    :param display_order: Index of the prompt - used in ordering of the
     prompts
    :type display_order: int
    :param qna_id: Qna id corresponding to the prompt - if QnaId is present,
     QnADTO object is ignored.
    :type qna_id: int
    :param qna: QnADTO - Either QnaId or QnADTO needs to be present in a
     PromptDTO object
    :type qna:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTOQna
    :param display_text: Text displayed to represent a follow up question
     prompt
    :type display_text: str
    """

    _validation = {
        'display_text': {'max_length': 200},
    }

    _attribute_map = {
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'qna_id': {'key': 'qnaId', 'type': 'int'},
        'qna': {'key': 'qna', 'type': 'PromptDTOQna'},
        'display_text': {'key': 'displayText', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PromptDTO, self).__init__(**kwargs)
        self.display_order = kwargs.get('display_order', None)
        self.qna_id = kwargs.get('qna_id', None)
        self.qna = kwargs.get('qna', None)
        self.display_text = kwargs.get('display_text', None)


class QnADTO(Model):
    """Q-A object.

    All required parameters must be populated in order to send to Azure.

    :param id: Unique id for the Q-A.
    :type id: int
    :param answer: Required. Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: Required. List of questions associated with the answer.
    :type questions: list[str]
    :param metadata: List of metadata associated with the answer.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    :param context: Context of a QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTOContext
    """

    _validation = {
        'answer': {'required': True, 'max_length': 25000, 'min_length': 1},
        'source': {'max_length': 300},
        'questions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': '[str]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnADTOContext'},
    }

    def __init__(self, **kwargs):
        super(QnADTO, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.answer = kwargs.get('answer', None)
        self.source = kwargs.get('source', None)
        self.questions = kwargs.get('questions', None)
        self.metadata = kwargs.get('metadata', None)
        self.context = kwargs.get('context', None)


class PromptDTOQna(QnADTO):
    """QnADTO - Either QnaId or QnADTO needs to be present in a PromptDTO object.

    All required parameters must be populated in order to send to Azure.

    :param id: Unique id for the Q-A.
    :type id: int
    :param answer: Required. Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: Required. List of questions associated with the answer.
    :type questions: list[str]
    :param metadata: List of metadata associated with the answer.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    :param context: Context of a QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTOContext
    """

    _validation = {
        'answer': {'required': True, 'max_length': 25000, 'min_length': 1},
        'source': {'max_length': 300},
        'questions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': '[str]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnADTOContext'},
    }

    def __init__(self, **kwargs):
        super(PromptDTOQna, self).__init__(**kwargs)


class QnADocumentsDTO(Model):
    """List of QnADTO.

    :param qna_documents: List of answers.
    :type qna_documents:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTO]
    """

    _attribute_map = {
        'qna_documents': {'key': 'qnaDocuments', 'type': '[QnADTO]'},
    }

    def __init__(self, **kwargs):
        super(QnADocumentsDTO, self).__init__(**kwargs)
        self.qna_documents = kwargs.get('qna_documents', None)


class QnADTOContext(ContextDTO):
    """Context of a QnA.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, **kwargs):
        super(QnADTOContext, self).__init__(**kwargs)


class ReplaceKbDTO(Model):
    """Post body schema for Replace KB operation.

    All required parameters must be populated in order to send to Azure.

    :param qn_alist: Required. List of Q-A (QnADTO) to be added to the
     knowledgebase. Q-A Ids are assigned by the service and should be omitted.
    :type qn_alist:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTO]
    """

    _validation = {
        'qn_alist': {'required': True},
    }

    _attribute_map = {
        'qn_alist': {'key': 'qnAList', 'type': '[QnADTO]'},
    }

    def __init__(self, **kwargs):
        super(ReplaceKbDTO, self).__init__(**kwargs)
        self.qn_alist = kwargs.get('qn_alist', None)


class UpdateContextDTO(Model):
    """Update Body schema to represent context to be updated.

    :param prompts_to_delete: List of prompts associated with qna to be
     deleted
    :type prompts_to_delete: list[int]
    :param prompts_to_add: List of prompts to be added to the qna.
    :type prompts_to_add:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTO]
    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    """

    _attribute_map = {
        'prompts_to_delete': {'key': 'promptsToDelete', 'type': '[int]'},
        'prompts_to_add': {'key': 'promptsToAdd', 'type': '[PromptDTO]'},
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(UpdateContextDTO, self).__init__(**kwargs)
        self.prompts_to_delete = kwargs.get('prompts_to_delete', None)
        self.prompts_to_add = kwargs.get('prompts_to_add', None)
        self.is_context_only = kwargs.get('is_context_only', None)


class UpdateKbContentsDTO(Model):
    """PATCH body schema for Update operation in Update Kb.

    :param name: Friendly name for the knowledgebase.
    :type name: str
    :param qna_list: List of Q-A (UpdateQnaDTO) to be added to the
     knowledgebase.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateQnaDTO]
    :param urls: List of existing URLs to be refreshed. The content will be
     extracted again and re-indexed.
    :type urls: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'qna_list': {'key': 'qnaList', 'type': '[UpdateQnaDTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbContentsDTO, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.qna_list = kwargs.get('qna_list', None)
        self.urls = kwargs.get('urls', None)


class UpdateKbOperationDTO(Model):
    """Contains list of QnAs to be updated.

    :param add: An instance of CreateKbInputDTO for add operation
    :type add:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateKbOperationDTOAdd
    :param delete: An instance of DeleteKbContentsDTO for delete Operation
    :type delete:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateKbOperationDTODelete
    :param update: An instance of UpdateKbContentsDTO for Update Operation
    :type update:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateKbOperationDTOUpdate
    """

    _attribute_map = {
        'add': {'key': 'add', 'type': 'UpdateKbOperationDTOAdd'},
        'delete': {'key': 'delete', 'type': 'UpdateKbOperationDTODelete'},
        'update': {'key': 'update', 'type': 'UpdateKbOperationDTOUpdate'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTO, self).__init__(**kwargs)
        self.add = kwargs.get('add', None)
        self.delete = kwargs.get('delete', None)
        self.update = kwargs.get('update', None)


class UpdateKbOperationDTOAdd(CreateKbInputDTO):
    """An instance of CreateKbInputDTO for add operation.

    :param qna_list: List of QNA to be added to the index. Ids are generated
     by the service and should be omitted.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.QnADTO]
    :param urls: List of URLs to be added to knowledgebase.
    :type urls: list[str]
    :param files: List of files to be added to knowledgebase.
    :type files:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.FileDTO]
    """

    _attribute_map = {
        'qna_list': {'key': 'qnaList', 'type': '[QnADTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'files': {'key': 'files', 'type': '[FileDTO]'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTOAdd, self).__init__(**kwargs)


class UpdateKbOperationDTODelete(DeleteKbContentsDTO):
    """An instance of DeleteKbContentsDTO for delete Operation.

    :param ids: List of Qna Ids to be deleted
    :type ids: list[int]
    :param sources: List of sources to be deleted from knowledgebase.
    :type sources: list[str]
    """

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[int]'},
        'sources': {'key': 'sources', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTODelete, self).__init__(**kwargs)


class UpdateKbOperationDTOUpdate(UpdateKbContentsDTO):
    """An instance of UpdateKbContentsDTO for Update Operation.

    :param name: Friendly name for the knowledgebase.
    :type name: str
    :param qna_list: List of Q-A (UpdateQnaDTO) to be added to the
     knowledgebase.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateQnaDTO]
    :param urls: List of existing URLs to be refreshed. The content will be
     extracted again and re-indexed.
    :type urls: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'qna_list': {'key': 'qnaList', 'type': '[UpdateQnaDTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTOUpdate, self).__init__(**kwargs)


class UpdateMetadataDTO(Model):
    """PATCH Body schema to represent list of Metadata to be updated.

    :param delete: List of Metadata associated with answer to be deleted
    :type delete:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    :param add: List of metadata associated with answer to be added
    :type add:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    """

    _attribute_map = {
        'delete': {'key': 'delete', 'type': '[MetadataDTO]'},
        'add': {'key': 'add', 'type': '[MetadataDTO]'},
    }

    def __init__(self, **kwargs):
        super(UpdateMetadataDTO, self).__init__(**kwargs)
        self.delete = kwargs.get('delete', None)
        self.add = kwargs.get('add', None)


class UpdateQnaDTO(Model):
    """PATCH Body schema for Update Qna List.

    :param id: Unique id for the Q-A
    :type id: int
    :param answer: Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: List of questions associated with the answer.
    :type questions:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateQnaDTOQuestions
    :param metadata: List of metadata associated with the answer to be updated
    :type metadata:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateQnaDTOMetadata
    :param context: Context associated with Qna to be updated.
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.UpdateQnaDTOContext
    """

    _validation = {
        'id': {'maximum': 2147483647, 'minimum': 0},
        'source': {'max_length': 300},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': 'UpdateQnaDTOQuestions'},
        'metadata': {'key': 'metadata', 'type': 'UpdateQnaDTOMetadata'},
        'context': {'key': 'context', 'type': 'UpdateQnaDTOContext'},
    }

    def __init__(self, **kwargs):
        super(UpdateQnaDTO, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.answer = kwargs.get('answer', None)
        self.source = kwargs.get('source', None)
        self.questions = kwargs.get('questions', None)
        self.metadata = kwargs.get('metadata', None)
        self.context = kwargs.get('context', None)


class UpdateQnaDTOContext(UpdateContextDTO):
    """Context associated with Qna to be updated.

    :param prompts_to_delete: List of prompts associated with qna to be
     deleted
    :type prompts_to_delete: list[int]
    :param prompts_to_add: List of prompts to be added to the qna.
    :type prompts_to_add:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTO]
    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    """

    _attribute_map = {
        'prompts_to_delete': {'key': 'promptsToDelete', 'type': '[int]'},
        'prompts_to_add': {'key': 'promptsToAdd', 'type': '[PromptDTO]'},
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(UpdateQnaDTOContext, self).__init__(**kwargs)


class UpdateQnaDTOMetadata(UpdateMetadataDTO):
    """List of metadata associated with the answer to be updated.

    :param delete: List of Metadata associated with answer to be deleted
    :type delete:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    :param add: List of metadata associated with answer to be added
    :type add:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.MetadataDTO]
    """

    _attribute_map = {
        'delete': {'key': 'delete', 'type': '[MetadataDTO]'},
        'add': {'key': 'add', 'type': '[MetadataDTO]'},
    }

    def __init__(self, **kwargs):
        super(UpdateQnaDTOMetadata, self).__init__(**kwargs)


class UpdateQuestionsDTO(Model):
    """PATCH Body schema for Update Kb which contains list of questions to be
    added and deleted.

    :param add: List of questions to be added
    :type add: list[str]
    :param delete: List of questions to be deleted.
    :type delete: list[str]
    """

    _attribute_map = {
        'add': {'key': 'add', 'type': '[str]'},
        'delete': {'key': 'delete', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateQuestionsDTO, self).__init__(**kwargs)
        self.add = kwargs.get('add', None)
        self.delete = kwargs.get('delete', None)


class UpdateQnaDTOQuestions(UpdateQuestionsDTO):
    """List of questions associated with the answer.

    :param add: List of questions to be added
    :type add: list[str]
    :param delete: List of questions to be deleted.
    :type delete: list[str]
    """

    _attribute_map = {
        'add': {'key': 'add', 'type': '[str]'},
        'delete': {'key': 'delete', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateQnaDTOQuestions, self).__init__(**kwargs)


class WordAlterationsDTO(Model):
    """Collection of word alterations.

    All required parameters must be populated in order to send to Azure.

    :param word_alterations: Required. Collection of word alterations.
    :type word_alterations:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.AlterationsDTO]
    """

    _validation = {
        'word_alterations': {'required': True},
    }

    _attribute_map = {
        'word_alterations': {'key': 'wordAlterations', 'type': '[AlterationsDTO]'},
    }

    def __init__(self, **kwargs):
        super(WordAlterationsDTO, self).__init__(**kwargs)
        self.word_alterations = kwargs.get('word_alterations', None)
