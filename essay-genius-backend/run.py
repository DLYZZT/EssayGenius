import uvicorn
import os
import sys
from dotenv import load_dotenv

# 尝试加载环境变量
if os.path.exists(".env"):
    load_dotenv(".env")
    print("从.env文件加载配置成功")
else:
    print("未找到.env文件，将使用默认配置或环境变量")

if __name__ == "__main__":
    # 确保设置了OpenAI API密钥
    if "OPENAI_API_KEY" not in os.environ:
        print("警告: 未设置OPENAI_API_KEY环境变量，需要在请求中提供api_key")
    
    # 从环境变量或使用默认值获取端口
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"启动服务器在 {host}:{port}")
    
    # 启动服务器
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True  # 开发模式下启用热重载
    ) 