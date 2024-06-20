# 情感驱动会话AI

这是一个基于Flask的聊天应用程序，结合了情感分析和智能对话模型，实现了情感丰富的自动回复功能。用户可以通过Web界面与聊天机器人进行互动。

## 目录

- [情感驱动会话AI](#情感驱动会话ai)
  - [目录](#目录)
  - [功能简介](#功能简介)
  - [安装步骤](#安装步骤)
  - [使用说明](#使用说明)
  - [项目结构](#项目结构)
  - [依赖项](#依赖项)
  - [注意事项](#注意事项)
  - [许可证](#许可证)

## 功能简介

- **用户登录**：用户可以通过输入用户名登录聊天页面。
- **情感分析**：应用集成了情感分析模型，能够识别用户输入的情感并进行分类。
- **智能对话**：基于GLM模型的智能回复系统，能够根据用户输入生成情感丰富的回复。
- **实时互动**：使用WebSocket实现用户与机器人的实时聊天互动。

## 安装步骤

1. **克隆项目**：
    ```bash
    git clone https://github.com/AuroraEchos/EmoChat.git
    cd EmoChat
    ```

2. **创建虚拟环境**（可选）：
    ```bash
    python -m venv venv
    source venv/bin/activate  # 对于Windows，使用 venv\Scripts\activate
    ```

3. **安装依赖项**：
    ```bash
    pip install -r requirements.txt
    ```

4. **模型和数据准备**：
    - 确保已下载并放置情感分析模型在适当位置（如 `models/` 目录下）。
    - 我们提供完整的文本情感分类训练源码，详细内容[ SetimentAnalysis ](https://github.com/AuroraEchos/SetimentAnalysis)。
    - 我们提供一份完整的模型，[ 点此下载 ](https://pan.baidu.com/s/1dmiGQAtYaXShyxl44pMOvw?pwd=9o8m)。
    - 更新 `models/service.py` 文件中的模型路径。
  
## 使用说明

1. **启动服务器**：
    ```bash
    python app.py
    ```

2. **访问应用**：
    打开浏览器，访问 `http://127.0.0.1:5000/` 进行用户登录和聊天互动。

3. **与聊天机器人互动**：
    - 输入消息并按下Enter键发送消息。
    - 可以使用语音输入功能，通过点击麦克风图标进行语音输入。

## 项目结构
```
EmoChat/
├── app.py                   # Flask应用主文件
├── models/
│   ├── service.py           # 模型API文件，包含情感分析和聊天模型逻辑
│   └── ...                  # 其他模型相关文件
├── static/
│   ├── css/
│   │   └── chat.css         # 样式文件
│   ├── images/
│   │   └── ...              # 图标和图片文件
│   ├── js/
│   │   └── ...              # 前端JS文件
│   └── favicon.ico          # 网站图标
├── templates/
│   ├── index.html           # 登录页面
│   └── chat.html            # 聊天页面
├── requirements.txt         # Python依赖项列表
└── README.md                # 项目说明文件
```

## 依赖项

- Flask
- Flask-SocketIO
- gevent
- torch
- transformers
- 其他依赖项详见 `requirements.txt` 文件

## 注意事项

- 本项目仅供学习和参考，请勿用于商业用途。
- 运行时请确保网络连接正常，以便加载外部资源（如字体和图标）。
- 部署到生产环境时，请使用更安全的密钥和配置。
- 语音交互服务在 Google Chrome 浏览器可正常使用，在 Firefox 浏览器可能会被拦截，关闭网站增强跟踪保护即可使用。

## 许可证

本项目采用 MIT 许可证。详情请参见 [LICENSE](LICENSE) 文件。