import dragn_client as client
from typing import List

item = "candy"
model_path = "EleutherAI/gpt-neo-1.3B"
# model_path = "princeton-nlp/Sheared-LLaMA-1.3B"
#model_path = "llama"
#model_path = "TheBloke/Llama-2-7B-Chat-GGUF"
#model_path = "HuggingFaceH4/zephyr-7b-beta"
#model_path = "elinas/llama-7b-hf-transformers-4.29"
#model_path = "xglm"
token = "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"
print(f"This is the model path: {model_path}\n")

false = False

ue_bank = {
    "items": [
        {
            "name": "Pool Table",
            "description": "a pool table",
            "advancedDescription": "rectangular plan, raised borders around the edge, holes at the 4 corners and middle of the long ends, with four legs for it to stand on",
            "itemScale": {
                "x": 123.65702795982361,
                "y": 193.93731689453125,
                "z": 57.050535671412945
            },
            "collectable": False,
            "stackSize": 0,
            "wieldable": False,
            "consumaable": False,
            "wearable": False,
            "container": False,
            "containerCapacity": 0
        },
        {
            "name": "Cardboard Box",
            "description": "a closed cardboard box",
            "advancedDescription": "cube shaped object",
            "itemScale": {
                "x": 100,
                "y": 100.00000762939453,
                "z": 90.000007629394531
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Young Girl",
            "description": "a cardboard cutout of a young girl",
            "advancedDescription": "a thin board, cut to appear roughyl human shaped from one side, with a piece  to help it stand from one side",
            "itemScale": {
                "x": 41.361700057983398,
                "y": 19.654299736022949,
                "z": 89.647505199536681
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Stair Case",
            "description": "staircas made out of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 612.62515342235565,
                "y": 526.71521109211608,
                "z": 682.92120931304589
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Buster Sword",
            "description": "A large sword made out of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 3.0434792041778564,
                "y": 13.997142314910889,
                "z": 83.404660224914551
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Cat Head",
            "description": "a hat that is shapped like a cat head",
            "advancedDescription": "a box shaped item, with an open bottom and front, designed to be worn, giving the wearer a limited view in front of themself only",
            "itemScale": {
                "x": 19.592357635498047,
                "y": 19.300000190734863,
                "z": 25.544981002807617
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Helmet",
            "description": "a carboard helmet",
            "advancedDescription": "None",
            "itemScale": {
                "x": 12,
                "y": 13.000000953674316,
                "z": 9
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Assult Rifle",
            "description": "assult rifle made out of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 75.793952941894531,
                "y": 423.02970886230469,
                "z": 98.640880584716797
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Tree Trunk",
            "description": "None",
            "advancedDescription": "None",
            "itemScale": {
                "x": 314.01535034179688,
                "y": 157.07208251953125,
                "z": 96.827163696289062
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Shield",
            "description": "medium sized shiled made of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 21.5,
                "y": 2.5000000298023224,
                "z": 25
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Short Sword",
            "description": "a short sword made out of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 8.5,
                "y": 1.5,
                "z": 30.000001907348633
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Emotional Support Carry Box",
            "description": "box to carry your emotional support rock in",
            "advancedDescription": "None",
            "itemScale": {
                "x": 17.641695022583008,
                "y": 11.761131763458252,
                "z": 30.091439664363861
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Split Log",
            "description": "a log split down the middle made out of cardboard",
            "advancedDescription": "None",
            "itemScale": {
                "x": 19.208846092224121,
                "y": 61.479255676269531,
                "z": 12.15187931060791
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "Pen",
            "description": "normal ballpoint pen",
            "advancedDescription": "None",
            "itemScale": {
                "x": 4.9270830154418945,
                "y": 61.348251342773438,
                "z": 5.8937549591064453
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "NewRow_13",
            "description": "None",
            "advancedDescription": "None",
            "itemScale": {
                "x": 0,
                "y": 0,
                "z": 0
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        },
        {
            "name": "None",
            "description": "None",
            "advancedDescription": "None",
            "itemScale": {
                "x": 0,
                "y": 0,
                "z": 0
            },
            "collectable": false,
            "stackSize": 0,
            "wieldable": false,
            "consumaable": false,
            "wearable": false,
            "container": false,
            "containerCapacity": 0
        }
    ]
}
ue_dict = ue_bank
ue_dict['item'] = item
item = client.run("call_llm", "call_llm", unreal_input=ue_dict, model_path=model_path, api_token=token)
print(item)
