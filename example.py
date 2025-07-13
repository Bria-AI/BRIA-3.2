from huggingface_hub import hf_hub_download
import os
import torch
from pipeline_bria import BriaPipeline, BriaTransformer2DModel


try:
    local_dir = os.path.dirname(__file__)
except:
    local_dir = '.'
    
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='pipeline_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='transformer_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='bria_utils.py', local_dir=local_dir)


# trust_remote_code = True - allows loading a transformer which is not present at the transformers library(from transformer/bria_transformer.py)
pipe = BriaPipeline.from_pretrained("briaai/BRIA-3.2", torch_dtype=torch.bfloat16,trust_remote_code=True)
pipe.to(device="cuda")

prompt = "A portrait of a Beautiful and playful ethereal singer, golden designs, highly detailed, blurry background"
negative_prompt = "Logo,Watermark,Ugly,Morbid,Extra fingers,Poorly drawn hands,Mutation,Blurry,Extra limbs,Gross proportions,Missing arms,Mutated hands,Long neck,Duplicate,Mutilated,Mutilated hands,Poorly drawn face,Deformed,Bad anatomy,Cloned face,Malformed limbs,Missing legs,Too many fingers"

images = pipe(prompt=prompt, negative_prompt=negative_prompt, height=1024, width=1024).images[0]