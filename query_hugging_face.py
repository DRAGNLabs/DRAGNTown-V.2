from os import system as sys
from os import environ
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from typing import Dict, List
import datetime

def create_pipe(model_path:str, tok=None):
    """
    Either:
        - load the model locally or
        - download the model from hugging face, and optionally cache the downloaded model;
    Return a pipeline object
    """
    
    if tok:
        #return 0
        tokenizer = AutoTokenizer.from_pretrained(model_path, token=tok)
        #return 0
        model = AutoModelForCausalLM.from_pretrained(model_path, token=tok, cache_dir="/home/evie/.cache/torch")  # This file path is redundant; it saves here by default
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path, cache_dir="/home/evie/.cache/torch")  # This file path is redundant; it saves here by default
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, device='cpu', max_length= 150) #'cuda:0')
    print("pipe created")
    return pipe

def build_prompt(input_dict: Dict)-> List[str]:
    
    target_item = input_dict["item"]
    search_bank = input_dict['items']

    options_list = []
    for option in search_bank:
        options_list.append(option['name'])
    options_str = ", a ".join(options_list[:-1]) + f", and a {options_list[-1]}"

    prompt = f"""I have a box with items. I want to find the item in my box that is most similar to a {target_item}. The items in my box are a {options_str}. The item in my box most similar to a {target_item} is a """
    return [prompt]


def query_hf_lm(unreal_input: Dict, model_path: str = None, api_token=None, pipe=None) -> Dict:
    """
    Queries the language model with a given prompt and returns the generated text.

    Args:
        prompt (List[str], optional): The prompt to query the language model with. Defaults to [""].
        pipe (transformers.pipelines.text_generation.TextGenerationPipeline object, optional): The language model pipeline. If not provided, it will be created using the model_path. Defaults to None.
        model_path (str, optional): The path to the language model. Required if pipe is not provided. Defaults to None.
        
    Returns:
        List[str]: The generated text from the language model.
    """
    template = unreal_input["items"][-1]
  # Check if prompt is empty
    if not unreal_input["item"]:
        print("Prompt was empty; returning empty item dictionary.")
    else:
        prompt = build_prompt(unreal_input)
        # Check if pipe is not provided and model_path is not provided
        if pipe == None:
            if model_path == None:
                raise Exception("Either pipe or model_path must be specified")
            pipe = create_pipe(model_path, tok=api_token)
        print(f"Running inference on {pipe.device}...")

        # Generate response using the language model pipeline
        generated_response: List[List[Dict[str,str]]]= pipe(prompt)
        # Extract the generated text from the response and return list of strings
        template["name"] = generated_response[0][0]['generated_text'][len(prompt[0]):]
        template["containerCapacity"] = (len(prompt), len(generated_response[0][0]['generated_text']))
    return template

## Sample Usage
#model_path = "meta-llama/Llama-2-7b-hf"
#model_path = "princeton-nlp/Sheared-LLaMA-1.3B"
#prompts: List[str] = ["Hello, my name is", "In 1492, "]
#print(query_lm(prompts=prompts, model_path=model_path, pipe=None))







# def old_query_lm(prompts: List[str] = [""], model_path: str = None, api_token=None, pipe=None) -> List[str]:
#     """
#     Queries the language model with a given prompt and returns the generated text.

#     Args:
#         prompt (List[str], optional): The prompt to query the language model with. Defaults to [""].
#         pipe (transformers.pipelines.text_generation.TextGenerationPipeline object, optional): The language model pipeline. If not provided, it will be created using the model_path. Defaults to None.
#         model_path (str, optional): The path to the language model. Required if pipe is not provided. Defaults to None.
        
#     Returns:
#         List[str]: The generated text from the language model.
#     """

#   # Check if prompt is empty
#     if prompts == [""]:
#         print("Prompt was empty; returning empty string.")
#         return [""]
    
#     # Check if pipe is not provided and model_path is not provided
#     if pipe == None:
#         if model_path == None:
#             raise Exception("Either pipe or model_path must be specified")
#         pipe = create_pipe(model_path, tok=api_token)
#     print(f"Running inference on {pipe.device}...")
#     #return f"Running inference on {pipe.device}..."
#     # Generate response using the language model pipeline

#     prompts = [""]


#     generated_response: List[List[Dict[str,str]]]= pipe(prompts)

#     # Extract the generated text from the response and return list of strings
#     return [generated_response[i][0]['generated_text'] for i in range(len(prompts))]