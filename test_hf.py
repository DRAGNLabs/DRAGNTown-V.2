import dragn_client as client
from typing import List

prompts: List[str] = ["Knock knock! Go, ", "Hey, what's black white and red all over?"]
model_path = "EleutherAI/gpt-neo-1.3B"
# model_path = "princeton-nlp/Sheared-LLaMA-1.3B"
#model_path = "llama"
#model_path = "TheBloke/Llama-2-7B-Chat-GGUF"
#model_path = "HuggingFaceH4/zephyr-7b-beta"
#model_path = "elinas/llama-7b-hf-transformers-4.29"
#model_path = "xglm"
token = "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"
print(f"This is the model path: {model_path}\n")



item = client.run("call_lm", "call_lm", prompts=prompts, model_path=model_path, api_token=token)
print(item)
