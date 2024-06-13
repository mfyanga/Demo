# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/localization/localization.proto

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
from common.message import geometry_pb2 as common_dot_message_dot_geometry__pb2
from common.message.simulation import simulation_obstacle_pb2 as common_dot_message_dot_simulation_dot_simulation__obstacle__pb2
from common.message.function_manage import evaluation_pb2 as common_dot_message_dot_function__manage_dot_evaluation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/localization/localization.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n.common/message/localization/localization.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\x1a\x1d\x63ommon/message/geometry.proto\x1a\x33\x63ommon/message/simulation/simulation_obstacle.proto\x1a/common/message/function_manage/evaluation.proto\"\xc8\x01\n\x0bUncertainty\x12\x39\n\x10position_std_dev\x18\x01 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12<\n\x13orientation_std_dev\x18\x02 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12@\n\x17linear_velocity_std_dev\x18\x03 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\"\x97\x05\n\x0cLocalization\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12\x32\n\x08position\x18\x02 \x01(\x0b\x32 .citibot.common.message.PointENU\x12\x38\n\x0flinear_velocity\x18\x03 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12<\n\x13linear_acceleration\x18\x04 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12\x37\n\x0borientation\x18\x05 \x01(\x0b\x32\".citibot.common.message.Quaternion\x12\x0f\n\x07heading\x18\x06 \x01(\x01\x12\x35\n\x0c\x65uler_angles\x18\x07 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12\x39\n\x10\x61ngular_velocity\x18\x08 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12\x38\n\x0buncertainty\x18\t \x01(\x0b\x32#.citibot.common.message.Uncertainty\x12\x1c\n\ris_simulation\x18\x32 \x01(\x08:\x05\x66\x61lse\x12L\n\x14simulation_obstacles\x18\x33 \x01(\x0b\x32..citibot.common.message.SimulationObstacleList\x12I\n\x17lidar_evaluation_result\x18\x64 \x01(\x0b\x32(.citibot.common.message.EvaluationResult\"\xd0\x04\n\x08Odometry\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12\x32\n\x08position\x18\x02 \x01(\x0b\x32 .citibot.common.message.PointENU\x12\x37\n\x0borientation\x18\x03 \x01(\x0b\x32\".citibot.common.message.Quaternion\x12\x38\n\x0flinear_velocity\x18\x04 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12<\n\x13linear_velocity_avg\x18\x05 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12<\n\x13linear_acceleration\x18\x06 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12@\n\x17linear_acceleration_avg\x18\x07 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12\x39\n\x10\x61ngular_velocity\x18\x08 \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12=\n\x14\x61ngular_velocity_avg\x18\t \x01(\x0b\x32\x1f.citibot.common.message.Point3D\x12\x35\n\x0c\x65uler_angles\x18\n \x01(\x0b\x32\x1f.citibot.common.message.Point3D')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,common_dot_message_dot_geometry__pb2.DESCRIPTOR,common_dot_message_dot_simulation_dot_simulation__obstacle__pb2.DESCRIPTOR,common_dot_message_dot_function__manage_dot_evaluation__pb2.DESCRIPTOR,])




_UNCERTAINTY = _descriptor.Descriptor(
  name='Uncertainty',
  full_name='citibot.common.message.Uncertainty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position_std_dev', full_name='citibot.common.message.Uncertainty.position_std_dev', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation_std_dev', full_name='citibot.common.message.Uncertainty.orientation_std_dev', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_velocity_std_dev', full_name='citibot.common.message.Uncertainty.linear_velocity_std_dev', index=2,
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
  serialized_start=237,
  serialized_end=437,
)


_LOCALIZATION = _descriptor.Descriptor(
  name='Localization',
  full_name='citibot.common.message.Localization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.Localization.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='citibot.common.message.Localization.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='citibot.common.message.Localization.linear_velocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='citibot.common.message.Localization.linear_acceleration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='citibot.common.message.Localization.orientation', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='citibot.common.message.Localization.heading', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='euler_angles', full_name='citibot.common.message.Localization.euler_angles', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='citibot.common.message.Localization.angular_velocity', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uncertainty', full_name='citibot.common.message.Localization.uncertainty', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_simulation', full_name='citibot.common.message.Localization.is_simulation', index=9,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simulation_obstacles', full_name='citibot.common.message.Localization.simulation_obstacles', index=10,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lidar_evaluation_result', full_name='citibot.common.message.Localization.lidar_evaluation_result', index=11,
      number=100, type=11, cpp_type=10, label=1,
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
  serialized_start=440,
  serialized_end=1103,
)


_ODOMETRY = _descriptor.Descriptor(
  name='Odometry',
  full_name='citibot.common.message.Odometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.Odometry.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='citibot.common.message.Odometry.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='citibot.common.message.Odometry.orientation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='citibot.common.message.Odometry.linear_velocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_velocity_avg', full_name='citibot.common.message.Odometry.linear_velocity_avg', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='citibot.common.message.Odometry.linear_acceleration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_acceleration_avg', full_name='citibot.common.message.Odometry.linear_acceleration_avg', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='citibot.common.message.Odometry.angular_velocity', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angular_velocity_avg', full_name='citibot.common.message.Odometry.angular_velocity_avg', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='euler_angles', full_name='citibot.common.message.Odometry.euler_angles', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=1106,
  serialized_end=1698,
)

_UNCERTAINTY.fields_by_name['position_std_dev'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_UNCERTAINTY.fields_by_name['orientation_std_dev'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_UNCERTAINTY.fields_by_name['linear_velocity_std_dev'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_LOCALIZATION.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_LOCALIZATION.fields_by_name['position'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_LOCALIZATION.fields_by_name['linear_velocity'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_LOCALIZATION.fields_by_name['linear_acceleration'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_LOCALIZATION.fields_by_name['orientation'].message_type = common_dot_message_dot_geometry__pb2._QUATERNION
_LOCALIZATION.fields_by_name['euler_angles'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_LOCALIZATION.fields_by_name['angular_velocity'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_LOCALIZATION.fields_by_name['uncertainty'].message_type = _UNCERTAINTY
_LOCALIZATION.fields_by_name['simulation_obstacles'].message_type = common_dot_message_dot_simulation_dot_simulation__obstacle__pb2._SIMULATIONOBSTACLELIST
_LOCALIZATION.fields_by_name['lidar_evaluation_result'].message_type = common_dot_message_dot_function__manage_dot_evaluation__pb2._EVALUATIONRESULT
_ODOMETRY.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_ODOMETRY.fields_by_name['position'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_ODOMETRY.fields_by_name['orientation'].message_type = common_dot_message_dot_geometry__pb2._QUATERNION
_ODOMETRY.fields_by_name['linear_velocity'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['linear_velocity_avg'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['linear_acceleration'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['linear_acceleration_avg'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['angular_velocity'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['angular_velocity_avg'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
_ODOMETRY.fields_by_name['euler_angles'].message_type = common_dot_message_dot_geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name['Uncertainty'] = _UNCERTAINTY
DESCRIPTOR.message_types_by_name['Localization'] = _LOCALIZATION
DESCRIPTOR.message_types_by_name['Odometry'] = _ODOMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Uncertainty = _reflection.GeneratedProtocolMessageType('Uncertainty', (_message.Message,), dict(
  DESCRIPTOR = _UNCERTAINTY,
  __module__ = 'common.message.localization.localization_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.Uncertainty)
  ))
_sym_db.RegisterMessage(Uncertainty)

Localization = _reflection.GeneratedProtocolMessageType('Localization', (_message.Message,), dict(
  DESCRIPTOR = _LOCALIZATION,
  __module__ = 'common.message.localization.localization_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.Localization)
  ))
_sym_db.RegisterMessage(Localization)

Odometry = _reflection.GeneratedProtocolMessageType('Odometry', (_message.Message,), dict(
  DESCRIPTOR = _ODOMETRY,
  __module__ = 'common.message.localization.localization_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.Odometry)
  ))
_sym_db.RegisterMessage(Odometry)


# @@protoc_insertion_point(module_scope)