from bento_service import TransformerService
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "eunsour/en-ko-transliterator"

service = TransformerService()

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

"""
input_text = "transformer"
input_ids = tokenizer.encode(input_text, return_tensors="pt", add_special_tokens=True)
generated_ids = model.generate(input_ids=input_ids,num_beams=5,max_length=50,repetition_penalty=2.5,length_penalty=1,early_stopping=True,num_return_sequences=3)
preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in generated_ids]
"""

artifact = {"model": model, "tokenizer": tokenizer}

service.pack("mt5Model", artifact)
service.save()
