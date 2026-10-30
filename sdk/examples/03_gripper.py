"""夹爪控制：读取状态 → 张开 → 半开 → 闭合。

做什么：演示 arm.gripper 的位置控制；命令返回状态 dict，不抛异常。
前置条件：机械臂已上电、网络可达；夹爪为可选件且需已安装。
夹爪量程默认自动从设备读取；如需人工指定量程，见文末注释（configure）。
运行：python3 03_gripper.py
"""

import time

import arm_sdk

TARGET = "udp://192.168.123.2:2000"


if __name__ == "__main__":
    with arm_sdk.connect(TARGET) as arm:
        arm.enable()

        print("夹爪状态:", arm.gripper.state())
        print("张开:", arm.gripper.open())
        time.sleep(1.0)
        print("半开:", arm.gripper.move(50))
        time.sleep(1.0)
        print("闭合:", arm.gripper.close())

        # 需要人工覆盖量程时（默认从设备读取，一般无需）：
        #   from arm_sdk import GripperCalibration
        #   arm.gripper.configure(GripperCalibration(position_closed=0.0, position_open=0.05))
