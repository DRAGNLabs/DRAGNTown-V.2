from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def create_pipe(model_path:str, cache_model:bool=False, path_to_save:str=""):
    """
    Either:
        - load the model locally or
        - download the model from hugging face, and optionally cache the downloaded model;
    Return a pipeline object
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    if cache_model:
        if path_to_save=="":
            path_to_save = model_path
        model.save_pretrained(path_to_save)

    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer)
    return pipe


def query_lm(prompt: list[str] = [""], pipe=None, model_path: str = None) -> list[str]:
    """
    Queries the language model with a given prompt and returns the generated text.

    Args:
        prompt (list[str], optional): The prompt to query the language model with. Defaults to [""].
        pipe (transformers.pipelines.text_generation.TextGenerationPipeline object, optional): The language model pipeline. If not provided, it will be created using the model_path. Defaults to None.
        model_path (str, optional): The path to the language model. Required if pipe is not provided. Defaults to None.
        
    Returns:
        list[str]: The generated text from the language model.
    """
    # Check if prompt is empty
    if prompt == [""]:
        return [""]
    
    # Check if pipe is not provided and model_path is not provided
    if pipe == None:
        if model_path == None:
            raise Exception("Either pipe or model_path must be specified")
        pipe = create_pipe(model_path)
    
    # Generate response using the language model pipeline
    generated_response: list[list[dict[str:str]]] = pipe(prompt)
    
    # Extract the generated text from the response and return list of strings
    return [generated_response[i][0]['generated_text'] for i in range(len(prompt))]

# Sample Usage
prompts: list[str] = ["Hello, my name is", "In 1776, the United States of America"]
print(query_lm(prompt=prompts))