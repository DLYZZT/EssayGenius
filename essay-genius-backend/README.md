# 作文批改系统后端

这是一个基于LangChain、LangServe和OpenAI GPT-4o模型实现的作文批改系统后端。

## 功能特点

- 使用OpenAI GPT-4o模型进行智能作文批改
- 提供详细的批改结果，包括总体评价、详细批改、修改建议和评分
- RESTful API设计，易于与前端集成
- 支持CORS，允许跨域请求

## 技术栈

- Python 3.9+
- FastAPI
- LangChain/LangServe
- OpenAI GPT-4o

## 安装

1. 克隆仓库

```bash
git clone <repository-url>
cd paper-check-backend
```

2. 创建虚拟环境并激活

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者
venv\Scripts\activate  # Windows
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 配置环境变量

拷贝`.env.example`文件为`.env`，并填入你的OpenAI API密钥：

```bash
cp app/.env.example .env
```

## 运行

启动服务器：

```bash
python run.py
```

服务器将在`http://localhost:8000`上运行。

## API接口

### 作文批改

**端点**: `/api/correct`

**方法**: POST

**参数**:

```json
{
  "essay": "学生作文内容",
  "api_key": "你的OpenAI API密钥(可选，也可以在环境变量中设置)",
  "model_name": "gpt-4o"
}
```

**返回**:

```json
{
  "result": "批改结果"
}
```

### 健康检查

**端点**: `/health`

**方法**: GET

**返回**:

```json
{
  "status": "healthy"
}
```

## 与前端集成

前端可以通过API调用后端服务。例如使用axios：

```javascript
axios.post('http://localhost:8000/api/correct', {
  essay: essay,
  api_key: 'your_api_key'
})
.then(response => {
  console.log(response.data.result);
})
.catch(error => {
  console.error('Error:', error);
});
```

## 许可

MIT 