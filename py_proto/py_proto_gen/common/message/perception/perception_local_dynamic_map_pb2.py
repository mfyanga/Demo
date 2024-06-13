# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/perception/perception_local_dynamic_map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import header_pb2 as common_dot_message_dot_header__pb2
from common.message.map import map_pb2 as common_dot_message_dot_map_dot_map__pb2
from common.message.perception import perception_obstacles_pb2 as common_dot_message_dot_perception_dot_perception__obstacles__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/perception/perception_local_dynamic_map.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n<common/message/perception/perception_local_dynamic_map.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\x1a\x1c\x63ommon/message/map/map.proto\x1a\x34\x63ommon/message/perception/perception_obstacles.proto\"\xb4\x01\n\x0fLocalDynamicMap\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12I\n\x14perception_obstacles\x18\x02 \x01(\x0b\x32+.citibot.common.message.PerceptionObstacles\x12&\n\x03map\x18\x03 \x01(\x0b\x32\x19.citibot.common.hdmap.Map')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__pb2.DESCRIPTOR,common_dot_message_dot_perception_dot_perception__obstacles__pb2.DESCRIPTOR,])




_LOCALDYNAMICMAP = _descriptor.Descriptor(
  name='LocalDynamicMap',
  full_name='citibot.common.message.LocalDynamicMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.LocalDynamicMap.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perception_obstacles', full_name='citibot.common.message.LocalDynamicMap.perception_obstacles', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='citibot.common.message.LocalDynamicMap.map', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=382,
)

_LOCALDYNAMICMAP.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_LOCALDYNAMICMAP.fields_by_name['perception_obstacles'].message_type = common_dot_message_dot_perception_dot_perception__obstacles__pb2._PERCEPTIONOBSTACLES
_LOCALDYNAMICMAP.fields_by_name['map'].message_type = common_dot_message_dot_map_dot_map__pb2._MAP
DESCRIPTOR.message_types_by_name['LocalDynamicMap'] = _LOCALDYNAMICMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocalDynamicMap = _reflection.GeneratedProtocolMessageType('LocalDynamicMap', (_message.Message,), dict(
  DESCRIPTOR = _LOCALDYNAMICMAP,
  __module__ = 'common.message.perception.perception_local_dynamic_map_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.LocalDynamicMap)
  ))
_sym_db.RegisterMessage(LocalDynamicMap)


# @@protoc_insertion_point(module_scope)
