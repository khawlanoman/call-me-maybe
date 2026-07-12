from llm_sdk.llm_sdk import Small_LLM_Model
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("GPT2")
text = "khawla"

model = Small_LLM_Model()
print(tokenizer.tokenize(text))
ids = model.encode(text)
print(ids)
#print(tokenizer(text)) #DICT
#print(tokenizer(text, return_tensors="pt")) # dict with value pytorch tensors
print(model.decode(ids))
print("hna",model.get_logits_from_input_ids(ids))