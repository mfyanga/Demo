# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/monitor/system_diagnosis_infomation.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/monitor/system_diagnosis_infomation.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n8common/message/monitor/system_diagnosis_infomation.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\"x\n\x0eNodeSystemInfo\x12\x12\n\x07node_id\x18\x01 \x01(\r:\x01\x30\x12\x11\n\tnode_name\x18\x02 \x01(\t\x12\x14\n\tcpu_usage\x18\x03 \x01(\r:\x01\x30\x12\x14\n\tmem_usage\x18\x04 \x01(\r:\x01\x30\x12\x13\n\x0b\x65rror_codes\x18\x05 \x03(\r\"\xb1\x02\n\x11SystemDiagInfoMsg\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12\x13\n\x0bsystem_dtcs\x18\x02 \x01(\x05\x12\x17\n\x0cmachine_temp\x18\x03 \x01(\x05:\x01\x30\x12\x14\n\tcpu_usage\x18\x04 \x01(\x05:\x01\x30\x12\x14\n\tmem_usage\x18\x05 \x01(\x05:\x01\x30\x12\x15\n\ndisk_usage\x18\x06 \x01(\x05:\x01\x30\x12\x14\n\tdisk_used\x18\x07 \x01(\x05:\x01\x30\x12\x18\n\rdisk_capacity\x18\x08 \x01(\x05:\x01\x30\x12\x39\n\tnode_info\x18\t \x03(\x0b\x32&.citibot.common.message.NodeSystemInfo\x12\x10\n\x08user_dtc\x18\n \x03(\t')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,])




_NODESYSTEMINFO = _descriptor.Descriptor(
  name='NodeSystemInfo',
  full_name='citibot.common.message.NodeSystemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='citibot.common.message.NodeSystemInfo.node_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='citibot.common.message.NodeSystemInfo.node_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_usage', full_name='citibot.common.message.NodeSystemInfo.cpu_usage', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_usage', full_name='citibot.common.message.NodeSystemInfo.mem_usage', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_codes', full_name='citibot.common.message.NodeSystemInfo.error_codes', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=113,
  serialized_end=233,
)


_SYSTEMDIAGINFOMSG = _descriptor.Descriptor(
  name='SystemDiagInfoMsg',
  full_name='citibot.common.message.SystemDiagInfoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.SystemDiagInfoMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_dtcs', full_name='citibot.common.message.SystemDiagInfoMsg.system_dtcs', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machine_temp', full_name='citibot.common.message.SystemDiagInfoMsg.machine_temp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_usage', full_name='citibot.common.message.SystemDiagInfoMsg.cpu_usage', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_usage', full_name='citibot.common.message.SystemDiagInfoMsg.mem_usage', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_usage', full_name='citibot.common.message.SystemDiagInfoMsg.disk_usage', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_used', full_name='citibot.common.message.SystemDiagInfoMsg.disk_used', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_capacity', full_name='citibot.common.message.SystemDiagInfoMsg.disk_capacity', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_info', full_name='citibot.common.message.SystemDiagInfoMsg.node_info', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_dtc', full_name='citibot.common.message.SystemDiagInfoMsg.user_dtc', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=236,
  serialized_end=541,
)

_SYSTEMDIAGINFOMSG.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_SYSTEMDIAGINFOMSG.fields_by_name['node_info'].message_type = _NODESYSTEMINFO
DESCRIPTOR.message_types_by_name['NodeSystemInfo'] = _NODESYSTEMINFO
DESCRIPTOR.message_types_by_name['SystemDiagInfoMsg'] = _SYSTEMDIAGINFOMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeSystemInfo = _reflection.GeneratedProtocolMessageType('NodeSystemInfo', (_message.Message,), dict(
  DESCRIPTOR = _NODESYSTEMINFO,
  __module__ = 'common.message.monitor.system_diagnosis_infomation_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.NodeSystemInfo)
  ))
_sym_db.RegisterMessage(NodeSystemInfo)

SystemDiagInfoMsg = _reflection.GeneratedProtocolMessageType('SystemDiagInfoMsg', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMDIAGINFOMSG,
  __module__ = 'common.message.monitor.system_diagnosis_infomation_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SystemDiagInfoMsg)
  ))
_sym_db.RegisterMessage(SystemDiagInfoMsg)


# @@protoc_insertion_point(module_scope)
