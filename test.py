from llm_sdk.llm_sdk import Small_LLM_Model
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("GPT2")
text = "Hello khawla"

#model = Small_LLM_Model()
print(tokenizer.tokenize(text))
#print(model.encode(text))
#print(tokenizer(text)) #DICT
print(tokenizer(text, return_tensors="pt")) # dict with value pytorch tensors
