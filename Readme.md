## 简介

自动演奏原神"风物之诗琴"的软件。

项目 由 C/S 架构构成 , UDP 通信


## Server

Server 端负责 具体的动作，如原神的按键操作

目前 由 Python 驱动

运行 `main.py`


## Client

Client 端负责 发送事件，例如定时发送 midi 序列

目前由 nodejs 驱动

运行 `paly.js`
