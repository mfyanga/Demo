import sys
import os

py_path=os.getcwd()+"/py_proto_gen"
sys.path.append(py_path)

from common.message.header_pb2 import  Header
from common.message.planning.adc_trajectory_pb2 import ADCTrajectory

adc_trajectory=ADCTrajectory()
adc_trajectory.header.timestamp=0
adc_trajectory.header.sequence_num=1
adc_trajectory.total_path_length=0
print("ADCTrajectory example")