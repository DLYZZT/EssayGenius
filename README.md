# 作文批改系统 (Paper-Check)

基于Vue.js, LangChain和OpenAI GPT-4o的作文批改系统，支持Docker部署。

## 系统架构

本系统包含两个主要部分：

1. **前端 (paper-check)**：
   - 基于Vue.js框架
   - 简洁现代的用户界面
   - 作文输入和批改结果展示

2. **后端 (paper-check-backend)**：
   - 基于FastAPI, LangChain和LangServe
   - 调用OpenAI GPT-4o进行作文批改
   - RESTful API设计

## 使用Docker部署

### 前提条件

- 安装 Docker 和 Docker Compose
- 拥有OpenAI API密钥（可以从 [OpenAI平台](https://platform.openai.com/) 获取）

### 快速启动

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/paper-check-system.git
cd paper-check-system
```

2. 使用启动脚本运行系统：

```bash
chmod +x start.sh
./start.sh
```

3. 编辑自动创建的`.env`文件，填入你的OpenAI API密钥：

```bash
nano .env
```

> **⚠️ 安全警告**：永远不要将包含真实API密钥的`.env`文件提交到版本控制系统中。该文件已在`.gitignore`中配置为忽略。

4. 重启服务以应用设置：

```bash
docker-compose restart
```

5. 访问系统：
   - 前端界面：http://localhost:8080
   - 后端API：http://localhost:8000

### 手动配置

如果你需要更详细的配置，可以按照以下步骤操作：

1. 拷贝环境变量示例文件：

```bash
cp .env.example .env
```

2. 编辑`.env`文件，填写必要的配置

3. 构建并启动Docker容器：

```bash
docker-compose up -d
```

## 手动运行（不使用Docker）

### 前端

```bash
cd paper-check
npm install
npm run dev
```

### 后端

```bash
cd paper-check-backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py
```

## 环境变量配置

主要环境变量说明：

- `OPENAI_API_KEY`: OpenAI API密钥（必填）
- `PORT`: 后端服务端口（默认8000）
- `HOST`: 后端服务主机（默认0.0.0.0）
- `DEFAULT_MODEL`: 使用的OpenAI模型（默认gpt-4o）
- `VITE_API_URL`: 前端访问后端的地址

## 发布到GitHub

如果您想复刻或贡献该项目，请确保：

1. **不要提交敏感信息**：包括API密钥、个人身份信息等
2. **使用环境变量**：所有配置都应通过`.env`文件或环境变量提供
3. **遵循许可协议**：本项目使用MIT许可证

## 贡献

欢迎提交Pull Request或Issue来帮助改进此项目。

## 许可

MIT 