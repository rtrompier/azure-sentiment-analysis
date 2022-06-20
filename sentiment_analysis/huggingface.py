from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

class HuggingFace:
    def __init__(self, modelName) -> None:
        self.modelName = modelName
        self.tokenizer = AutoTokenizer.from_pretrained(modelName)
        self.model = AutoModelForSequenceClassification.from_pretrained(modelName)

    def analyze(self, text):
        sentimentAnalysis = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
        out = sentimentAnalysis(text)
        return out