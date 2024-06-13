# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/dispatch/working_pose.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import geometry_pb2 as common_dot_message_dot_geometry__pb2
from common.message.map import map_id_pb2 as common_dot_message_dot_map_dot_map__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/dispatch/working_pose.proto',
  package='citibot.common.dispatch',
  syntax='proto2',
  serialized_pb=_b('\n*common/message/dispatch/working_pose.proto\x12\x17\x63itibot.common.dispatch\x1a\x1d\x63ommon/message/geometry.proto\x1a\x1f\x63ommon/message/map/map_id.proto\"\x98\x02\n\x0bWorkingPose\x12\x32\n\x08position\x18\x01 \x01(\x0b\x32 .citibot.common.message.PointENU\x12\x0f\n\x07heading\x18\x02 \x01(\x01\x12,\n\noverlap_id\x18\x03 \x03(\x0b\x32\x18.citibot.common.hdmap.Id\x12\x34\n\tpose_flag\x18\x04 \x01(\x0e\x32!.citibot.common.dispatch.PoseFlag\x12\x34\n\tpose_type\x18\x05 \x01(\x0e\x32!.citibot.common.dispatch.PoseType\x12*\n\x08match_id\x18\x06 \x01(\x0b\x32\x18.citibot.common.hdmap.Id*7\n\x08PoseFlag\x12\r\n\tkFlagNone\x10\x00\x12\r\n\tkFlagLoad\x10\x01\x12\r\n\tkFlagDump\x10\x02*9\n\x08PoseType\x12\x0c\n\x08kUnknown\x10\x00\x12\r\n\tkOriginal\x10\x01\x12\x10\n\x0ckDestination\x10\x02')
  ,
  dependencies=[common_dot_message_dot_geometry__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__id__pb2.DESCRIPTOR,])

_POSEFLAG = _descriptor.EnumDescriptor(
  name='PoseFlag',
  full_name='citibot.common.dispatch.PoseFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kFlagNone', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kFlagLoad', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kFlagDump', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=418,
  serialized_end=473,
)
_sym_db.RegisterEnumDescriptor(_POSEFLAG)

PoseFlag = enum_type_wrapper.EnumTypeWrapper(_POSEFLAG)
_POSETYPE = _descriptor.EnumDescriptor(
  name='PoseType',
  full_name='citibot.common.dispatch.PoseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kOriginal', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDestination', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=475,
  serialized_end=532,
)
_sym_db.RegisterEnumDescriptor(_POSETYPE)

PoseType = enum_type_wrapper.EnumTypeWrapper(_POSETYPE)
kFlagNone = 0
kFlagLoad = 1
kFlagDump = 2
kUnknown = 0
kOriginal = 1
kDestination = 2



_WORKINGPOSE = _descriptor.Descriptor(
  name='WorkingPose',
  full_name='citibot.common.dispatch.WorkingPose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='citibot.common.dispatch.WorkingPose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='citibot.common.dispatch.WorkingPose.heading', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='citibot.common.dispatch.WorkingPose.overlap_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose_flag', full_name='citibot.common.dispatch.WorkingPose.pose_flag', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose_type', full_name='citibot.common.dispatch.WorkingPose.pose_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_id', full_name='citibot.common.dispatch.WorkingPose.match_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=136,
  serialized_end=416,
)

_WORKINGPOSE.fields_by_name['position'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_WORKINGPOSE.fields_by_name['overlap_id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_WORKINGPOSE.fields_by_name['pose_flag'].enum_type = _POSEFLAG
_WORKINGPOSE.fields_by_name['pose_type'].enum_type = _POSETYPE
_WORKINGPOSE.fields_by_name['match_id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
DESCRIPTOR.message_types_by_name['WorkingPose'] = _WORKINGPOSE
DESCRIPTOR.enum_types_by_name['PoseFlag'] = _POSEFLAG
DESCRIPTOR.enum_types_by_name['PoseType'] = _POSETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkingPose = _reflection.GeneratedProtocolMessageType('WorkingPose', (_message.Message,), dict(
  DESCRIPTOR = _WORKINGPOSE,
  __module__ = 'common.message.dispatch.working_pose_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.dispatch.WorkingPose)
  ))
_sym_db.RegisterMessage(WorkingPose)


# @@protoc_insertion_point(module_scope)
