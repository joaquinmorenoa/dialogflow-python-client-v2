# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/webhook.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dialogflow_v2beta1.proto import (
    context_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2,
)
from dialogflow_v2beta1.proto import (
    intent_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2,
)
from dialogflow_v2beta1.proto import (
    session_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2,
)
from dialogflow_v2beta1.proto import (
    session_entity_type_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2,
)
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dialogflow_v2beta1/proto/webhook.proto",
    package="google.cloud.dialogflow.v2beta1",
    syntax="proto3",
    serialized_options=b"\n#com.google.cloud.dialogflow.v2beta1B\014WebhookProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n3google/cloud/dialogflow_v2beta1/proto/webhook.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x33google/cloud/dialogflow_v2beta1/proto/context.proto\x1a\x32google/cloud/dialogflow_v2beta1/proto/intent.proto\x1a\x33google/cloud/dialogflow_v2beta1/proto/session.proto\x1a?google/cloud/dialogflow_v2beta1/proto/session_entity_type.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"\xb1\x02\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12\x42\n\x0cquery_result\x18\x02 \x01(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResult\x12O\n\x19\x61lternative_query_results\x18\x05 \x03(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResult\x12\x64\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b\x32<.google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest"\xad\x03\n\x0fWebhookResponse\x12\x18\n\x10\x66ulfillment_text\x18\x01 \x01(\t\x12M\n\x14\x66ulfillment_messages\x18\x02 \x03(\x0b\x32/.google.cloud.dialogflow.v2beta1.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x41\n\x0foutput_contexts\x18\x05 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.Context\x12I\n\x14\x66ollowup_event_input\x18\x06 \x01(\x0b\x32+.google.cloud.dialogflow.v2beta1.EventInput\x12\x17\n\x0f\x65nd_interaction\x18\x08 \x01(\x08\x12P\n\x14session_entity_types\x18\n \x03(\x0b\x32\x32.google.cloud.dialogflow.v2beta1.SessionEntityType"h\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructB\xaa\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cWebhookProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_WEBHOOKREQUEST = _descriptor.Descriptor(
    name="WebhookRequest",
    full_name="google.cloud.dialogflow.v2beta1.WebhookRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="session",
            full_name="google.cloud.dialogflow.v2beta1.WebhookRequest.session",
            index=0,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="response_id",
            full_name="google.cloud.dialogflow.v2beta1.WebhookRequest.response_id",
            index=1,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="query_result",
            full_name="google.cloud.dialogflow.v2beta1.WebhookRequest.query_result",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="alternative_query_results",
            full_name="google.cloud.dialogflow.v2beta1.WebhookRequest.alternative_query_results",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="original_detect_intent_request",
            full_name="google.cloud.dialogflow.v2beta1.WebhookRequest.original_detect_intent_request",
            index=4,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=677,
)


_WEBHOOKRESPONSE = _descriptor.Descriptor(
    name="WebhookResponse",
    full_name="google.cloud.dialogflow.v2beta1.WebhookResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="fulfillment_text",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.fulfillment_text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fulfillment_messages",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.fulfillment_messages",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.source",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.payload",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="output_contexts",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.output_contexts",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="followup_event_input",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.followup_event_input",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="end_interaction",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.end_interaction",
            index=6,
            number=8,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="session_entity_types",
            full_name="google.cloud.dialogflow.v2beta1.WebhookResponse.session_entity_types",
            index=7,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=680,
    serialized_end=1109,
)


_ORIGINALDETECTINTENTREQUEST = _descriptor.Descriptor(
    name="OriginalDetectIntentRequest",
    full_name="google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="source",
            full_name="google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest.source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest.payload",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1111,
    serialized_end=1215,
)

_WEBHOOKREQUEST.fields_by_name[
    "query_result"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2._QUERYRESULT
)
_WEBHOOKREQUEST.fields_by_name[
    "alternative_query_results"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2._QUERYRESULT
)
_WEBHOOKREQUEST.fields_by_name[
    "original_detect_intent_request"
].message_type = _ORIGINALDETECTINTENTREQUEST
_WEBHOOKRESPONSE.fields_by_name[
    "fulfillment_messages"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2._INTENT_MESSAGE
)
_WEBHOOKRESPONSE.fields_by_name[
    "payload"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WEBHOOKRESPONSE.fields_by_name[
    "output_contexts"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2._CONTEXT
)
_WEBHOOKRESPONSE.fields_by_name[
    "followup_event_input"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2._EVENTINPUT
)
_WEBHOOKRESPONSE.fields_by_name[
    "session_entity_types"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2._SESSIONENTITYTYPE
)
_ORIGINALDETECTINTENTREQUEST.fields_by_name[
    "payload"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name["WebhookRequest"] = _WEBHOOKREQUEST
DESCRIPTOR.message_types_by_name["WebhookResponse"] = _WEBHOOKRESPONSE
DESCRIPTOR.message_types_by_name[
    "OriginalDetectIntentRequest"
] = _ORIGINALDETECTINTENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebhookRequest = _reflection.GeneratedProtocolMessageType(
    "WebhookRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _WEBHOOKREQUEST,
        "__module__": "google.cloud.dialogflow_v2beta1.proto.webhook_pb2",
        "__doc__": """The request message for a webhook call.
  
  Attributes:
      session:
          The unique identifier of detectIntent request session. Can be
          used to identify end-user inside webhook implementation.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``,
          or ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>``.
      response_id:
          The unique identifier of the response. Contains the same value
          as ``[Streaming]DetectIntentResponse.response_id``.
      query_result:
          The result of the conversational query or event processing.
          Contains the same value as
          ``[Streaming]DetectIntentResponse.query_result``.
      alternative_query_results:
          Alternative query results from KnowledgeService.
      original_detect_intent_request:
          Optional. The contents of the original request that was passed
          to ``[Streaming]DetectIntent`` call.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.WebhookRequest)
    },
)
_sym_db.RegisterMessage(WebhookRequest)

WebhookResponse = _reflection.GeneratedProtocolMessageType(
    "WebhookResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _WEBHOOKRESPONSE,
        "__module__": "google.cloud.dialogflow_v2beta1.proto.webhook_pb2",
        "__doc__": """The response message for a webhook call.  This response is validated
  by the Dialogflow server. If validation fails, an error will be
  returned in the [QueryResult.diagnostic_info][google.cloud.dialogflow.
  v2beta1.QueryResult.diagnostic_info] field. Setting JSON fields to an
  empty value with the wrong type is a common error. To avoid this
  error:  -  Use ``""`` for empty strings -  Use ``{}`` or ``null`` for
  empty objects -  Use ``[]`` or ``null`` for empty arrays  For more
  information, see the `Protocol Buffers Language Guide
  <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.
  
  Attributes:
      fulfillment_text:
          Optional. The text response message intended for the end-user.
          It is recommended to use ``fulfillment_messages.text.text[0]``
          instead. When provided, Dialogflow uses this field to populate
          [QueryResult.fulfillment_text][google.cloud.dialogflow.v2beta1
          .QueryResult.fulfillment_text] sent to the integration or API
          caller.
      fulfillment_messages:
          Optional. The rich response messages intended for the end-
          user. When provided, Dialogflow uses this field to populate [Q
          ueryResult.fulfillment_messages][google.cloud.dialogflow.v2bet
          a1.QueryResult.fulfillment_messages] sent to the integration
          or API caller.
      source:
          Optional. A custom field used to identify the webhook source.
          Arbitrary strings are supported. When provided, Dialogflow
          uses this field to populate [QueryResult.webhook_source][googl
          e.cloud.dialogflow.v2beta1.QueryResult.webhook_source] sent to
          the integration or API caller.
      payload:
          Optional. This field can be used to pass custom data from your
          webhook to the integration or API caller. Arbitrary JSON
          objects are supported. When provided, Dialogflow uses this
          field to populate [QueryResult.webhook_payload][google.cloud.d
          ialogflow.v2beta1.QueryResult.webhook_payload] sent to the
          integration or API caller. This field is also used by the
          `Google Assistant integration
          <https://cloud.google.com/dialogflow/docs/integrations/aog>`__
          for rich response messages. See the format definition at
          `Google Assistant Dialogflow webhook format <https://developer
          s.google.com/assistant/actions/build/json/dialogflow-webhook-
          json>`__
      output_contexts:
          Optional. The collection of output contexts that will
          overwrite currently active contexts for the session and reset
          their lifespans. When provided, Dialogflow uses this field to
          populate [QueryResult.output_contexts][google.cloud.dialogflow
          .v2beta1.QueryResult.output_contexts] sent to the integration
          or API caller.
      followup_event_input:
          Optional. Invokes the supplied events. When this field is set,
          Dialogflow ignores the ``fulfillment_text``,
          ``fulfillment_messages``, and ``payload`` fields.
      end_interaction:
          Optional. Indicates that this intent ends an interaction. Some
          integrations (e.g., Actions on Google or Dialogflow phone
          gateway) use this information to close interaction with an end
          user. Default is false.
      session_entity_types:
          Optional. Additional session entity types to replace or extend
          developer entity types with. The entity synonyms apply to all
          languages and persist for the session. Setting this data from
          a webhook overwrites the session entity types that have been
          set using ``detectIntent``, ``streamingDetectIntent`` or [Sess
          ionEntityType][google.cloud.dialogflow.v2beta1.SessionEntityTy
          pe] management methods.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.WebhookResponse)
    },
)
_sym_db.RegisterMessage(WebhookResponse)

OriginalDetectIntentRequest = _reflection.GeneratedProtocolMessageType(
    "OriginalDetectIntentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ORIGINALDETECTINTENTREQUEST,
        "__module__": "google.cloud.dialogflow_v2beta1.proto.webhook_pb2",
        "__doc__": """Represents the contents of the original request that was passed to the
  ``[Streaming]DetectIntent`` call.
  
  Attributes:
      source:
          The source of this request, e.g., ``google``, ``facebook``,
          ``slack``. It is set by Dialogflow-owned servers.
      version:
          Optional. The version of the protocol used for this request.
          This field is AoG-specific.
      payload:
          Optional. This field is set to the value of the
          ``QueryParameters.payload`` field passed in the request. Some
          integrations that query a Dialogflow agent may provide
          additional information in the payload.  In particular, for the
          Dialogflow Phone Gateway integration, this field has the form:
          .. raw:: html     <pre>{     "telephony": {       "caller_id":
          "+18558363987"     }    }</pre>  Note: The caller ID field
          (``caller_id``) will be redacted for Standard Edition agents
          and populated with the caller ID in `E.164 format
          <https://en.wikipedia.org/wiki/E.164>`__ for Enterprise
          Edition agents.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest)
    },
)
_sym_db.RegisterMessage(OriginalDetectIntentRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
