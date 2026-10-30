"""订阅实时状态：连接后持续打印各关节角，运行若干秒后自动退出。

做什么：演示 arm.state.subscribe 回调式读取遥测（回调内只打印，不做耗时/阻塞操作）。
前置条件：机械臂已上电，上位机与机械臂网络可达；本脚本只读状态、不做运动。
运行：python3 02_state_subscribe.py
"""

import time

import arm_sdk

TARGET = "udp://192.168.123.2:2000"
RUN_SECONDS = 5.0


def on_telemetry(snap):
    joints = " ".join(f"{snap.motors[i].q:+.3f}" for i in range(7))
    print("关节角(rad):", joints)


if __name__ == "__main__":
    with arm_sdk.connect(TARGET) as arm:
        arm.state.subscribe(on_telemetry)   # 回调在接收线程内联调用，勿阻塞
        time.sleep(RUN_SECONDS)
        arm.state.unsubscribe(on_telemetry)
