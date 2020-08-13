# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2/proto/session_entity_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from dialogflow_v2.proto import (
    entity_type_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_entity__type__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dialogflow_v2/proto/session_entity_type.proto",
    package="google.cloud.dialogflow.v2",
    syntax="proto3",
    serialized_options=b"\n\036com.google.cloud.dialogflow.v2B\026SessionEntityTypeProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n:google/cloud/dialogflow_v2/proto/session_entity_type.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x32google/cloud/dialogflow_v2/proto/entity_type.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc0\x04\n\x11SessionEntityType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x63\n\x14\x65ntity_override_mode\x18\x02 \x01(\x0e\x32@.google.cloud.dialogflow.v2.SessionEntityType.EntityOverrideModeB\x03\xe0\x41\x02\x12\x44\n\x08\x65ntities\x18\x03 \x03(\x0b\x32-.google.cloud.dialogflow.v2.EntityType.EntityB\x03\xe0\x41\x02"\x82\x01\n\x12\x45ntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45NTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1f\x45NTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02:\xe7\x01\xea\x41\xe3\x01\n+dialogflow.googleapis.com/SessionEntityType\x12\x45projects/{project}/agent/sessions/{session}/entityTypes/{entity_type}\x12mprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}"\x95\x01\n\x1dListSessionEntityTypesRequest\x12\x43\n\x06parent\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\x12+dialogflow.googleapis.com/SessionEntityType\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01"\x86\x01\n\x1eListSessionEntityTypesResponse\x12K\n\x14session_entity_types\x18\x01 \x03(\x0b\x32-.google.cloud.dialogflow.v2.SessionEntityType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bGetSessionEntityTypeRequest\x12\x41\n\x04name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+dialogflow.googleapis.com/SessionEntityType"\xb6\x01\n\x1e\x43reateSessionEntityTypeRequest\x12\x43\n\x06parent\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\x12+dialogflow.googleapis.com/SessionEntityType\x12O\n\x13session_entity_type\x18\x02 \x01(\x0b\x32-.google.cloud.dialogflow.v2.SessionEntityTypeB\x03\xe0\x41\x02"\xa7\x01\n\x1eUpdateSessionEntityTypeRequest\x12O\n\x13session_entity_type\x18\x01 \x01(\x0b\x32-.google.cloud.dialogflow.v2.SessionEntityTypeB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01"c\n\x1e\x44\x65leteSessionEntityTypeRequest\x12\x41\n\x04name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+dialogflow.googleapis.com/SessionEntityType2\xd2\r\n\x12SessionEntityTypes\x12\xa7\x02\n\x16ListSessionEntityTypes\x12\x39.google.cloud.dialogflow.v2.ListSessionEntityTypesRequest\x1a:.google.cloud.dialogflow.v2.ListSessionEntityTypesResponse"\x95\x01\x82\xd3\xe4\x93\x02\x85\x01\x12\x34/v2/{parent=projects/*/agent/sessions/*}/entityTypesZM\x12K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes\xda\x41\x06parent\x12\x94\x02\n\x14GetSessionEntityType\x12\x37.google.cloud.dialogflow.v2.GetSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\x93\x01\x82\xd3\xe4\x93\x02\x85\x01\x12\x34/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM\x12K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\xda\x41\x04name\x12\xda\x02\n\x17\x43reateSessionEntityType\x12:.google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\xd3\x01\x82\xd3\xe4\x93\x02\xaf\x01"4/v2/{parent=projects/*/agent/sessions/*}/entityTypes:\x13session_entity_typeZb"K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\x13session_entity_type\xda\x41\x1aparent,session_entity_type\x12\x9d\x03\n\x17UpdateSessionEntityType\x12:.google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest\x1a-.google.cloud.dialogflow.v2.SessionEntityType"\x96\x02\x82\xd3\xe4\x93\x02\xd7\x01\x32H/v2/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\x13session_entity_typeZv2_/v2/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\x13session_entity_type\xda\x41\x13session_entity_type\xda\x41\x1fsession_entity_type,update_mask\x12\x83\x02\n\x17\x44\x65leteSessionEntityType\x12:.google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest\x1a\x16.google.protobuf.Empty"\x93\x01\x82\xd3\xe4\x93\x02\x85\x01*4/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM*K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\xda\x41\x04name\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa5\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x16SessionEntityTypeProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_entity__type__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE = _descriptor.EnumDescriptor(
    name="EntityOverrideMode",
    full_name="google.cloud.dialogflow.v2.SessionEntityType.EntityOverrideMode",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ENTITY_OVERRIDE_MODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ENTITY_OVERRIDE_MODE_OVERRIDE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ENTITY_OVERRIDE_MODE_SUPPLEMENT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=533,
    serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE)


_SESSIONENTITYTYPE = _descriptor.Descriptor(
    name="SessionEntityType",
    full_name="google.cloud.dialogflow.v2.SessionEntityType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.SessionEntityType.name",
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="entity_override_mode",
            full_name="google.cloud.dialogflow.v2.SessionEntityType.entity_override_mode",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="entities",
            full_name="google.cloud.dialogflow.v2.SessionEntityType.entities",
            index=2,
            number=3,
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE],
    serialized_options=b"\352A\343\001\n+dialogflow.googleapis.com/SessionEntityType\022Eprojects/{project}/agent/sessions/{session}/entityTypes/{entity_type}\022mprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}/entityTypes/{entity_type}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=321,
    serialized_end=897,
)


_LISTSESSIONENTITYTYPESREQUEST = _descriptor.Descriptor(
    name="ListSessionEntityTypesRequest",
    full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesRequest.parent",
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
            serialized_options=b"\340A\002\372A-\022+dialogflow.googleapis.com/SessionEntityType",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesRequest.page_token",
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
            serialized_options=b"\340A\001",
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
    serialized_start=900,
    serialized_end=1049,
)


_LISTSESSIONENTITYTYPESRESPONSE = _descriptor.Descriptor(
    name="ListSessionEntityTypesResponse",
    full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="session_entity_types",
            full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesResponse.session_entity_types",
            index=0,
            number=1,
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
            name="next_page_token",
            full_name="google.cloud.dialogflow.v2.ListSessionEntityTypesResponse.next_page_token",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1052,
    serialized_end=1186,
)


_GETSESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
    name="GetSessionEntityTypeRequest",
    full_name="google.cloud.dialogflow.v2.GetSessionEntityTypeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.GetSessionEntityTypeRequest.name",
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
            serialized_options=b"\340A\002\372A-\n+dialogflow.googleapis.com/SessionEntityType",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1188,
    serialized_end=1284,
)


_CREATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
    name="CreateSessionEntityTypeRequest",
    full_name="google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest.parent",
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
            serialized_options=b"\340A\002\372A-\022+dialogflow.googleapis.com/SessionEntityType",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="session_entity_type",
            full_name="google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest.session_entity_type",
            index=1,
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
            serialized_options=b"\340A\002",
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
    serialized_start=1287,
    serialized_end=1469,
)


_UPDATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
    name="UpdateSessionEntityTypeRequest",
    full_name="google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="session_entity_type",
            full_name="google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest.session_entity_type",
            index=0,
            number=1,
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest.update_mask",
            index=1,
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
            serialized_options=b"\340A\001",
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
    serialized_start=1472,
    serialized_end=1639,
)


_DELETESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
    name="DeleteSessionEntityTypeRequest",
    full_name="google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest.name",
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
            serialized_options=b"\340A\002\372A-\n+dialogflow.googleapis.com/SessionEntityType",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1641,
    serialized_end=1740,
)

_SESSIONENTITYTYPE.fields_by_name[
    "entity_override_mode"
].enum_type = _SESSIONENTITYTYPE_ENTITYOVERRIDEMODE
_SESSIONENTITYTYPE.fields_by_name[
    "entities"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_entity__type__pb2._ENTITYTYPE_ENTITY
)
_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE.containing_type = _SESSIONENTITYTYPE
_LISTSESSIONENTITYTYPESRESPONSE.fields_by_name[
    "session_entity_types"
].message_type = _SESSIONENTITYTYPE
_CREATESESSIONENTITYTYPEREQUEST.fields_by_name[
    "session_entity_type"
].message_type = _SESSIONENTITYTYPE
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name[
    "session_entity_type"
].message_type = _SESSIONENTITYTYPE
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name["SessionEntityType"] = _SESSIONENTITYTYPE
DESCRIPTOR.message_types_by_name[
    "ListSessionEntityTypesRequest"
] = _LISTSESSIONENTITYTYPESREQUEST
DESCRIPTOR.message_types_by_name[
    "ListSessionEntityTypesResponse"
] = _LISTSESSIONENTITYTYPESRESPONSE
DESCRIPTOR.message_types_by_name[
    "GetSessionEntityTypeRequest"
] = _GETSESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name[
    "CreateSessionEntityTypeRequest"
] = _CREATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name[
    "UpdateSessionEntityTypeRequest"
] = _UPDATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name[
    "DeleteSessionEntityTypeRequest"
] = _DELETESESSIONENTITYTYPEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionEntityType = _reflection.GeneratedProtocolMessageType(
    "SessionEntityType",
    (_message.Message,),
    {
        "DESCRIPTOR": _SESSIONENTITYTYPE,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """A session represents a conversation between a Dialogflow agent and an
  end-user. You can create special entities, called session entities,
  during a session. Session entities can extend or replace custom entity
  types and only exist during the session that they were created for.
  All session data, including session entities, is stored by Dialogflow
  for 20 minutes.  For more information, see the `session entity guide
  <https://cloud.google.com/dialogflow/docs/entities-session>`__.
  
  Attributes:
      name:
          Required. The unique identifier of this session entity type.
          Format: ``projects/<Project ID>/agent/sessions/<Session
          ID>/entityTypes/<Entity Type Display Name>``, or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity
          Type Display Name>``. If ``Environment ID`` is not specified,
          we assume default ‘draft’ environment. If ``User ID`` is not
          specified, we assume default ‘-’ user.  ``<Entity Type Display
          Name>`` must be the display name of an existing entity type in
          the same agent that will be overridden or supplemented.
      entity_override_mode:
          Required. Indicates whether the additional data should
          override or supplement the custom entity type definition.
      entities:
          Required. The collection of entities associated with this
          session entity type.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.SessionEntityType)
    },
)
_sym_db.RegisterMessage(SessionEntityType)

ListSessionEntityTypesRequest = _reflection.GeneratedProtocolMessageType(
    "ListSessionEntityTypesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTSESSIONENTITYTYPESREQUEST,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The request message for [SessionEntityTypes.ListSessionEntityTypes][go
  ogle.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes].
  
  Attributes:
      parent:
          Required. The session to list all session entity types from.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``
          or ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/ sessions/<Session ID>``. If ``Environment
          ID`` is not specified, we assume default ‘draft’ environment.
          If ``User ID`` is not specified, we assume default ‘-’ user.
      page_size:
          Optional. The maximum number of items to return in a single
          page. By default 100 and at most 1000.
      page_token:
          Optional. The next_page_token value returned from a previous
          list request.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListSessionEntityTypesRequest)
    },
)
_sym_db.RegisterMessage(ListSessionEntityTypesRequest)

ListSessionEntityTypesResponse = _reflection.GeneratedProtocolMessageType(
    "ListSessionEntityTypesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTSESSIONENTITYTYPESRESPONSE,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The response message for [SessionEntityTypes.ListSessionEntityTypes][g
  oogle.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes].
  
  Attributes:
      session_entity_types:
          The list of session entity types. There will be a maximum
          number of items returned based on the page_size field in the
          request.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListSessionEntityTypesResponse)
    },
)
_sym_db.RegisterMessage(ListSessionEntityTypesResponse)

GetSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType(
    "GetSessionEntityTypeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETSESSIONENTITYTYPEREQUEST,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The request message for [SessionEntityTypes.GetSessionEntityType][goog
  le.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityType].
  
  Attributes:
      name:
          Required. The name of the session entity type. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/entityTypes/<Entity Type Display Name>`` or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity
          Type Display Name>``. If ``Environment ID`` is not specified,
          we assume default ‘draft’ environment. If ``User ID`` is not
          specified, we assume default ‘-’ user.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.GetSessionEntityTypeRequest)
    },
)
_sym_db.RegisterMessage(GetSessionEntityTypeRequest)

CreateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType(
    "CreateSessionEntityTypeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATESESSIONENTITYTYPEREQUEST,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The request message for [SessionEntityTypes.CreateSessionEntityType][g
  oogle.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityType].
  
  Attributes:
      parent:
          Required. The session to create a session entity type for.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``
          or ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/ sessions/<Session ID>``. If ``Environment
          ID`` is not specified, we assume default ‘draft’ environment.
          If ``User ID`` is not specified, we assume default ‘-’ user.
      session_entity_type:
          Required. The session entity type to create.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest)
    },
)
_sym_db.RegisterMessage(CreateSessionEntityTypeRequest)

UpdateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateSessionEntityTypeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATESESSIONENTITYTYPEREQUEST,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The request message for [SessionEntityTypes.UpdateSessionEntityType][g
  oogle.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityType].
  
  Attributes:
      session_entity_type:
          Required. The session entity type to update.
      update_mask:
          Optional. The mask to control which fields get updated.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest)
    },
)
_sym_db.RegisterMessage(UpdateSessionEntityTypeRequest)

DeleteSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteSessionEntityTypeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETESESSIONENTITYTYPEREQUEST,
        "__module__": "google.cloud.dialogflow_v2.proto.session_entity_type_pb2",
        "__doc__": """The request message for [SessionEntityTypes.DeleteSessionEntityType][g
  oogle.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityType].
  
  Attributes:
      name:
          Required. The name of the entity type to delete. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/entityTypes/<Entity Type Display Name>`` or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity
          Type Display Name>``. If ``Environment ID`` is not specified,
          we assume default ‘draft’ environment. If ``User ID`` is not
          specified, we assume default ‘-’ user.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest)
    },
)
_sym_db.RegisterMessage(DeleteSessionEntityTypeRequest)


DESCRIPTOR._options = None
_SESSIONENTITYTYPE.fields_by_name["name"]._options = None
_SESSIONENTITYTYPE.fields_by_name["entity_override_mode"]._options = None
_SESSIONENTITYTYPE.fields_by_name["entities"]._options = None
_SESSIONENTITYTYPE._options = None
_LISTSESSIONENTITYTYPESREQUEST.fields_by_name["parent"]._options = None
_LISTSESSIONENTITYTYPESREQUEST.fields_by_name["page_size"]._options = None
_LISTSESSIONENTITYTYPESREQUEST.fields_by_name["page_token"]._options = None
_GETSESSIONENTITYTYPEREQUEST.fields_by_name["name"]._options = None
_CREATESESSIONENTITYTYPEREQUEST.fields_by_name["parent"]._options = None
_CREATESESSIONENTITYTYPEREQUEST.fields_by_name["session_entity_type"]._options = None
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name["session_entity_type"]._options = None
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name["update_mask"]._options = None
_DELETESESSIONENTITYTYPEREQUEST.fields_by_name["name"]._options = None

_SESSIONENTITYTYPES = _descriptor.ServiceDescriptor(
    name="SessionEntityTypes",
    full_name="google.cloud.dialogflow.v2.SessionEntityTypes",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow",
    create_key=_descriptor._internal_create_key,
    serialized_start=1743,
    serialized_end=3489,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListSessionEntityTypes",
            full_name="google.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes",
            index=0,
            containing_service=None,
            input_type=_LISTSESSIONENTITYTYPESREQUEST,
            output_type=_LISTSESSIONENTITYTYPESRESPONSE,
            serialized_options=b"\202\323\344\223\002\205\001\0224/v2/{parent=projects/*/agent/sessions/*}/entityTypesZM\022K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetSessionEntityType",
            full_name="google.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityType",
            index=1,
            containing_service=None,
            input_type=_GETSESSIONENTITYTYPEREQUEST,
            output_type=_SESSIONENTITYTYPE,
            serialized_options=b"\202\323\344\223\002\205\001\0224/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM\022K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CreateSessionEntityType",
            full_name="google.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityType",
            index=2,
            containing_service=None,
            input_type=_CREATESESSIONENTITYTYPEREQUEST,
            output_type=_SESSIONENTITYTYPE,
            serialized_options=b'\202\323\344\223\002\257\001"4/v2/{parent=projects/*/agent/sessions/*}/entityTypes:\023session_entity_typeZb"K/v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes:\023session_entity_type\332A\032parent,session_entity_type',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateSessionEntityType",
            full_name="google.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityType",
            index=3,
            containing_service=None,
            input_type=_UPDATESESSIONENTITYTYPEREQUEST,
            output_type=_SESSIONENTITYTYPE,
            serialized_options=b"\202\323\344\223\002\327\0012H/v2/{session_entity_type.name=projects/*/agent/sessions/*/entityTypes/*}:\023session_entity_typeZv2_/v2/{session_entity_type.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}:\023session_entity_type\332A\023session_entity_type\332A\037session_entity_type,update_mask",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteSessionEntityType",
            full_name="google.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityType",
            index=4,
            containing_service=None,
            input_type=_DELETESESSIONENTITYTYPEREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002\205\001*4/v2/{name=projects/*/agent/sessions/*/entityTypes/*}ZM*K/v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SESSIONENTITYTYPES)

DESCRIPTOR.services_by_name["SessionEntityTypes"] = _SESSIONENTITYTYPES

# @@protoc_insertion_point(module_scope)
