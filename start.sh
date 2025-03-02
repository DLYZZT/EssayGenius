#!/bin/bash

# 确保.env文件存在
if [ ! -f .env ]; then
  echo "创建.env文件..."
  cp .env.example .env
  echo "请编辑.env文件，填写您的OpenAI API密钥"
fi

# 启动Docker容器
echo "启动作文批改系统..."
docker-compose up -d

echo "系统启动成功！"
echo "前端访问地址: http://localhost:8080"
echo "后端API地址: http://localhost:8000" 