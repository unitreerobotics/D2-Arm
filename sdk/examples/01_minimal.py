"""最小可用客户端：连接机械臂 → 使能 → J1 依次运动到 1 rad → -1 rad → 回到 0 → 退出。

做什么：演示 SDK 的最短用法（J1 依次 1 rad → -1 rad → 0，其余关节保持 0）；
退出 with 时自动失能并断开。
前置条件：机械臂已上电，上位机与机械臂网络可达（见《D2 机械臂使用手册》§4）。
运行：python3 01_minimal.py
"""

import arm_sdk

if __name__ == "__main__":
    with arm_sdk.connect("udp://192.168.123.2:2000") as arm:
        arm.enable()
        arm.motion.movej([1.0, 0, 0, 0, 0, 0, 0], speed=1.0).wait(10.0)
        arm.motion.movej([-1.0, 0, 0, 0, 0, 0, 0], speed=1.0).wait(10.0)
        arm.motion.movej([0, 0, 0, 0, 0, 0, 0], speed=1.0).wait(10.0)
