from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def create_pipe(model_path:str, cache_model:bool=False, path_to_save:str=""):
    """
    Either:
        - load the model locally or
        - download the model from hugging face 

    Then return a pipeline object
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    if cache_model:
        if path_to_save=="":
            path_to_save = model_path
        model.save_pretrained(path_to_save)

    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer)
    return pipe


# Sample Usage
model_path = "distilgpt2"
pipe = create_pipe(model_path=model_path)# cache_model=True, path_to_save="models/"+model_name)
prompts: list[str] = ["Hello, my name is", "In 1776, the United States of America"]
generated_response: list[list[dict[str:str]]] = pipe(prompts)

# print((generated_response))
# print((generated_response[0][0]['generated_text']))

print([generated_response[i][0]['generated_text'] for i in range(len(prompts))])

