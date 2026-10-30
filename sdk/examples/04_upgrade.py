"""固件升级骨架：通过网口升级控制器固件（升级文件由供货方提供）。

做什么：演示 arm.upgrade.run 的调用方式与进度回调；升级会自动让出控制权、结束后自动重连
（设备升级后会重启，连接短暂中断）。
前置条件：机械臂已上电、网络可达，且处于已失能状态；升级期间请勿断电或断网。
运行：python3 04_upgrade.py /path/to/d2_app.bin
"""

import sys

import arm_sdk

TARGET = "udp://192.168.123.2:2000"


def on_progress(progress):
    print(f"[{progress.phase}] {progress.percent:.1f}%")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("用法: python3 04_upgrade.py <固件文件路径>")
    image_path = sys.argv[1]

    answer = input("升级期间机械臂不可用，确认继续请输入 yes：")
    if answer.strip().lower() != "yes":
        raise SystemExit("已取消")

    with arm_sdk.connect(TARGET) as arm:
        arm.disable()          # 升级要求设备已失能
        # run 内部：自动让出控制权 → 升级（设备重启、连接短暂中断）→ 自动重连并重新取权。
        result = arm.upgrade.run(image_path, progress=on_progress)
        print("升级完成，协议版本:", result.hello_after.protocol_major,
              result.hello_after.protocol_minor)
        if result.device_info_after is not None:            # 未及应答 DEVICE_INFO 时可能为 None
            print("几何标识:", hex(result.device_info_after.geometry_id))
