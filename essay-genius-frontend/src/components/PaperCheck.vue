<script setup lang="ts">
import { ref, computed } from 'vue';


const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const paperContent = ref('');
const correctionResult = ref('');
const isLoading = ref(false);
const errorMessage = ref('');
const apiKey = ref('');

// 格式化批改结果，增强可读性
const formattedResult = computed(() => {
  if (!correctionResult.value) return '';
  
  // 将结果文本转换为HTML，保留格式并添加样式
  return correctionResult.value
    .replace(/【(.+?)】/g, '<h3 class="result-section-title">【$1】</h3>')
    .replace(/(\d+)\. (.+?)：/g, '<strong>$1. $2：</strong>')
    .replace(/(\d+)\/(\d+)/g, '<span class="score">$1/$2</span>')
    .replace(/\n/g, '<br>');
});

// 提交作文进行批改
const submitPaper = async () => {
  if (!paperContent.value.trim()) {
    alert('请输入作文内容');
    return;
  }
  
  isLoading.value = true;
  errorMessage.value = '';
  
  try {
    // 连接到后端API进行作文批改
    const response = await fetch(`${API_URL}api/correct`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        essay: paperContent.value,
        api_key: apiKey.value || undefined,
        model_name: 'gpt-4o'
      })
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || '批改过程中发生错误');
    }
    
    const data = await response.json();
    correctionResult.value = data.result;
  } catch (error) {
    console.error('批改过程发生错误:', error);
    errorMessage.value = error instanceof Error ? error.message : '批改过程中发生未知错误，请稍后再试';
  } finally {
    isLoading.value = false;
  }
};

// 清空内容
const clearContent = () => {
  paperContent.value = '';
  correctionResult.value = '';
  errorMessage.value = '';
};
</script>

<template>
  <div class="paper-check-container">
    <h1 class="title">AI英语作文批改</h1>
    
    <div class="content-area">
      <div class="paper-section">
        <textarea
          v-model="paperContent"
          class="paper-textarea"
          placeholder="请在此处输入您的作文..."
        ></textarea>
        
        <div class="api-key-section">
          <input 
            v-model="apiKey"
            type="password"
            class="api-key-input"
            placeholder="OpenAI API密钥（可选）"
          />
          <small>如果服务器未配置API密钥，请在此输入您的OpenAI API密钥</small>
        </div>
        
        <div class="action-buttons">
          <button 
            class="submit-button" 
            @click="submitPaper"
            :disabled="isLoading"
          >
            {{ isLoading ? '批改中...' : '批改' }}
          </button>
          
          <button 
            class="clear-button" 
            @click="clearContent"
            :disabled="isLoading"
          >
            清空
          </button>
        </div>
        
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
      </div>
      
      <div v-if="correctionResult" class="result-section">
        <h2>批改结果</h2>
        <div class="correction-result">
          <div v-html="formattedResult"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.paper-check-container {
  max-width: 1800px;
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 500;
  color: #333;
}

.content-area {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  align-items: center;
}

.paper-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 95%;
  min-width: 90%;
  margin: 0 auto;
}

.paper-textarea {
  width: 100%;
  min-height: 400px;
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  resize: vertical;
  font-size: 1.1rem;
  line-height: 1.6;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  transition: border-color 0.3s, box-shadow 0.3s;
}

.paper-textarea:focus {
  outline: none;
  border-color: #409eff;
  box-shadow: 0 0 0 3px rgba(64, 158, 255, 0.1);
}

.action-buttons {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  margin-top: 1rem;
}

.submit-button,
.clear-button {
  padding: 0.85rem 2.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.submit-button {
  background-color: #409eff;
  color: white;
}

.submit-button:hover {
  background-color: #3089e8;
  transform: translateY(-2px);
}

.submit-button:disabled {
  background-color: #a0cfff;
  cursor: not-allowed;
  transform: none;
}

.clear-button {
  background-color: #f5f5f5;
  color: #606266;
}

.clear-button:hover {
  background-color: #e6e6e6;
  transform: translateY(-2px);
}

.clear-button:disabled {
  background-color: #f5f5f5;
  color: #c0c4cc;
  cursor: not-allowed;
  transform: none;
}

.result-section {
  margin-top: 1rem;
  padding: 1.5rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
  width: 95%;
  min-width: 90%;
  max-height: 600px;
  overflow-y: auto;
}

.result-section h2 {
  margin-top: 0;
  margin-bottom: 1rem;
  font-weight: 500;
  color: #333;
  position: sticky;
  top: 0;
  background-color: #f9f9f9;
  padding: 0.5rem 0;
  z-index: 1;
  border-bottom: 1px solid #eee;
}

.correction-result {
  white-space: pre-wrap;
  line-height: 1.6;
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
}

.correction-result pre {
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  white-space: pre-wrap;
  overflow-wrap: break-word;
}

.api-key-section {
  margin-top: 1rem;
  text-align: center;
}

.api-key-input {
  width: 100%;
  max-width: 500px;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.9rem;
}

.api-key-section small {
  display: block;
  margin-top: 0.5rem;
  color: #606266;
  font-size: 0.8rem;
}

.error-message {
  margin-top: 1rem;
  padding: 0.75rem;
  background-color: #fff2f0;
  border: 1px solid #ffccc7;
  border-radius: 4px;
  color: #ff4d4f;
  text-align: center;
}

/* 添加批改结果中标题和分数的样式 */
:deep(.result-section-title) {
  margin: 1rem 0 0.5rem 0;
  color: #409eff;
  font-weight: 600;
  font-size: 1.2rem;
}

:deep(.score) {
  font-weight: bold;
  color: #f56c6c;
}

:deep(strong) {
  color: #303133;
}

/* 移动端样式 */
@media (max-width: 768px) {
  .content-area {
    flex-direction: column;
    align-items: center;
  }
  
  .paper-section,
  .result-section {
    width: 95%;
  }
  
  .result-section {
    max-height: 500px;
  }
  
  :deep(.result-section-title) {
    font-size: 1.1rem;
  }
  
  .paper-textarea {
    min-height: 350px;
  }
}

/* 桌面端样式 */
@media (min-width: 1024px) {
  .content-area {
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
  }
  
  .paper-section,
  .result-section {
    width: 48%;
    min-width: 0;
    max-width: 900px;
  }
  
  .result-section {
    margin-top: 0;
    height: 650px;
    max-height: 650px;
  }
  
  .paper-textarea {
    height: 550px;
    min-height: 550px;
  }
}
</style> 