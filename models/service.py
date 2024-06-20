from zhipuai import ZhipuAI
from transformers import BertTokenizer, BertForSequenceClassification
import torch

import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*Torch was not compiled with flash attention.*")

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class ChatGLM:
    def __init__(self):
        self.api_key = '2b3a454472b53ae5f240a2799eafb489.buaYBXVJkr36BHVy'
        self.client = ZhipuAI(api_key=self.api_key)

    def chat(self, input_text, emotion=None, intensity=None):
        if emotion:
            input_text_with_emotion = f"我感觉有点{emotion}（强度：{intensity * 100}%）。{input_text}"
        else:
            input_text_with_emotion = input_text
        
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "system", "content": "你是一个朋友，和用户随意聊天，提供一些简洁的建议和信息。\
                                            请基于用户的输入情感判断结果在回复中添加一些情感表达，并保持短对话的风格。\
                                            如果用户的输入不包含明显的情感，比如是中性，那么回复中不需要添加情感表达。"},
                {"role": "user", "content": input_text_with_emotion},
            ],
            stream=True,
        )
        complete_response = ''.join([chunk.choices[0].delta.content for chunk in response])
        return complete_response
    

class SentimentAnalyzer:
    def __init__(self):
        model_path = "models/bert_epoch_0"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.label_map = {0: "中性", 1: "高兴", 2: "生气", 3: "伤心", 4: "恐惧", 5: "惊讶"}

    def predict(self, text, label=None):
        self.model.eval()

        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=64).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predict_label = torch.argmax(logits, dim=-1).item()
            predict_confidence = torch.max(torch.softmax(logits, dim=-1)).item()
        
        info = f"inputs: '{text}', predict: '{self.label_map[predict_label]}'"
        if label is not None:
            info += f" , label: '{self.label_map[label]}'"
        return self.label_map[predict_label], predict_confidence
    

def generate_emotional_reply(user_input, sentiment_analyzer, chatglm):
    emotion_label, intensity = sentiment_analyzer.predict(user_input)
    
    raw_reply = chatglm.chat(user_input, emotion=emotion_label, intensity=intensity)
    
    return raw_reply
