# D2 机械臂交付包

本仓库是 D2 机械臂的客户交付内容：

| 目录 | 内容 |
|---|---|
| [`armecho/`](armecho/) | ArmEcho 上位机：Docker 镜像与 `armecho-compose.yml` |
| [`sdk/`](sdk/) | Python SDK：CPython 3.10 / 3.11 / 3.12 预编译 wheel 与示例 |
| [`urdf/`](urdf/) | ROS 模型包 `D2_URDF` |

## armecho/ —— 上位机

镜像 tar 体积较大，以 **Releases 附件** 形式提供（文件名 `d2arm-armecho-1.0.2.tar`）。
把它下载到 `armecho/` 目录（与仓库内的 `.sha256` 文件放一起），然后：

```bash
cd armecho
sha256sum -c d2arm-armecho-1.0.2.tar.sha256   # 输出 OK 即完好
docker load -i d2arm-armecho-1.0.2.tar
docker compose -f armecho-compose.yml up -d
docker compose -f armecho-compose.yml ps       # STATUS 应为 (healthy)
```

浏览器打开 `http://<主机地址>:8000`。机械臂连接目标在网页「系统配置 → 网络配置」中填写；
端口、网络模式等调整见 `armecho-compose.yml` 内注释。

## sdk/ —— Python SDK

`sdk/` 下有 CPython 3.10 / 3.11 / 3.12 三个版本的预编译 wheel（`manylinux2014_x86_64`）
及各自 `.sha256` 校验文件：

```bash
cd sdk
sha256sum -c arm_sdk-1.0.2-*.whl.sha256       # 输出 OK 即完好
pip install ./arm_sdk-1.0.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
```

按本机 Python 版本选择对应的 wheel。安装后可从 [`examples/`](sdk/examples/) 开始，
例如 `python 01_minimal.py`（连接、使能、小幅运动、失能）。

## urdf/ —— ROS 模型

标准 ROS（catkin）包，包名 `D2_URDF`，包含 `urdf/D2_URDF.urdf`、`meshes/`、`launch/`、
`config/` 与 `package.xml`。
可放入 ROS 工作空间的 `src/` 下编译，或直接在支持 `package://` 解析的工具中加载。
