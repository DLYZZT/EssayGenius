import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from pydantic import BaseModel, Field
from typing import Optional
from .chains import create_essay_correction_chain


app = FastAPI(
    title="作文批改API",
    description="基于LangChain和OpenAI GPT-4o的作文批改系统",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "http://frontend", "http://frontend:80", "http://localhost:5174"],  # 在生产环境中设置为具体的前端URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
    expose_headers=["Content-Length"],
    max_age=600
)


class EssayInput(BaseModel):
    essay: str = Field(..., description="学生提交的作文内容")
    api_key: Optional[str] = Field(None, description="OpenAI API 密钥（可选）")
    model_name: Optional[str] = Field("gpt-4o", description="使用的模型名称")


class EssayCorrection(BaseModel):
    result: str = Field(..., description="作文批改结果")


def get_api_key(input_data: EssayInput):
    api_key = input_data.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=400, detail="未提供OpenAI API密钥")
    return api_key


@app.post("/api/correct", response_model=EssayCorrection)
async def correct_essay(input_data: EssayInput):
    try:
        api_key = get_api_key(input_data)
        chain = create_essay_correction_chain(
            api_key=api_key,
            model_name=input_data.model_name
        )
        result = chain.invoke({"essay": input_data.essay})
        
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"作文批改过程发生错误: {str(e)}")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


add_routes(
    app,
    create_essay_correction_chain(),
    path="/api/chain",
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 