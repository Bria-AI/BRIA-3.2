---
library_name: diffusers
inference: false
tags:
- text-to-image
- legal liability
- Non Commercial Use
extra_gated_description: >-
  Bria AI Model weights are open source for non commercial use only, per the
  provided [license](https://creativecommons.org/licenses/by-nc/4.0/deed.en).
extra_gated_heading: Fill in this form to immediatly access the model for non commercial use
extra_gated_fields:
  Name: text
  Email: text
  Company/Org name: text
  Company Website URL: text
  Discord user: text
  I agree to BRIA’s Privacy policy, Terms & conditions, and acknowledge Non commercial use to be Personal use / Academy / Non profit (direct or indirect): checkbox
license: other
license_name: bria-3.2
license_link: https://creativecommons.org/licenses/by-nc/4.0/deed.en
---



# TL;DR

Bria 3.2 is the next-generation commercial-ready text-to-image model.
**With just 4 billion parameters**, it provides exceptional aesthetics and text rendering, evaluated to provide **equivalent results to Flux.1, and outperform Adobe FireFly**.

In Addition to being **built entirely on licensed data**, 3.2 provides several advantages for enterprise and commercial use:
* Efficient Compute - the model is X3 smaller than the equivalent models in the market (4B parameters vs 12B parameters Flux.1)
* Architecture Consistency: Same architecture as 3.1—ideal for users looking to upgrade without disruption.
* Latency Gains: 6.84-second inference latency on an L40S (reduced from 10.6s with Bria 3.1).
* Fine-tuning Speedup: 2x faster fine-tuning on L40S, A10, and A100 (vs Bria 3.1).


[CLICK HERE FOR A DEMO](https://huggingface.co/spaces/briaai/BRIA-3.2-API)




![](32-photo.jpg)



# BRIA 3.2: Training data and Commercial Licensing

BRIA 3.2 is our latest text-to-image model explicitly designed for commercial applications. 
This model combines technological innovation with ethical responsibility and legal security, setting a new standard in the AI industry. 
Bria AI licenses the foundation model with full legal liability coverage. 
Our dataset does not contain copyrighted materials, such as fictional characters, logos, trademarks, public figures, harmful content, or privacy-infringing content.

For more information, please visit our [website](https://bria.ai/).

Join our [Discord community](https://discord.gg/Nxe9YW9zHS) for more information, tutorials, tools, and to connect with other users!

### For Commercial License : click [Here](https://bria.ai/contact-us?hsCtaAttrib=114250296256).


# What's New vs pervious models:

- **Improved Aesthetics**:

  - 65% user preference for BRIA 3.2 over BRIA 3.1.
  - 76% user preference for BRIA 3.2 over BRIA 2.3.

- **Superior Text Rendering**: The model is optimized to generate short text consists of 1-6 words. OCR Score improvement from 5% (3.1) to 70% (3.2).

- **Consistent Prompt Alignment**: Maintains high-quality textual description adherence.



### Get Access
Bria 3.2 is available everywhere you build, either as source-code and weights, ComfyUI nodes or API endpoints.

- **API Endpoint**: [Bria.ai](https://platform.bria.ai/console/api/image-generation) , [Fal.ai](https://fal.ai/models/bria/text-to-image/3.2)
- **ComfyUI**: [Use it in workflows](https://github.com/Bria-AI/ComfyUI-BRIA-API)
- **Interested in BRIA 3.2 source code and weights for commercial use?** Purchase is required to license BRIA 3.2 got commercial use, ensuring royalty management with our data partners and full liability coverage.
- Are you a startup or a student? We encourage you to apply for our [Startup Program](https://pages.bria.ai/the-visual-generative-ai-platform-for-builders-startups-plan?_gl=1*cqrl81*_ga*MTIxMDI2NzI5OC4xNjk5NTQ3MDAz*_ga_WRN60H46X4*MTcwOTM5OTMzNC4yNzguMC4xNzA5Mzk5MzM0LjYwLjAuMA..) to request access. This program are designed to support emerging businesses and academic pursuits with our cutting-edge technology.
- By submitting the form above, you agree to BRIA’s [Privacy policy](https://bria.ai/privacy-policy/) and [Terms & conditions](https://bria.ai/terms-and-conditions/).



# Key Features

- **Architecture**: 4B parameter, rectified flow transformer based model with T5 text encoder.

- **Legally Compliant**: Offers full legal liability coverage for copyright and privacy infringements. Thanks to training on 100% licensed data from leading data partners, we ensure the ethical use of content.

- **Patented Attribution Engine**: Our attribution engine is our way to compensate our data partners, powered by our proprietary and patented algorithms. 

- **Enterprise-Ready**: Specifically designed for business applications, Bria AI 3.0 delivers high-quality, compliant imagery for a variety of commercial needs.

- **Customizable Technology**: Provides access to source code and weights for extensive customization, catering to specific business requirements.

### Model Description

- **Developed by:** BRIA AI
- **Model type:** Latent diffusion text-to-image model
- **Resources for more information:** [BRIA AI](https://bria.ai/)





### Code example using Diffusers 


```python
pip install diffusers, hf_hub_download
```



```python
from huggingface_hub import hf_hub_download
import os

try:
    local_dir = os.path.dirname(__file__)
except:
    local_dir = '.'
    
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='pipeline_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='transformer_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.2", filename='bria_utils.py', local_dir=local_dir)

import torch
from pipeline_bria import BriaPipeline, BriaTransformer2DModel

# trust_remote_code = True - allows loading a transformer which is not present at the transformers library(from transformer/bria_transformer.py)
pipe = BriaPipeline.from_pretrained("briaai/BRIA-3.2", torch_dtype=torch.bfloat16,trust_remote_code=True)
pipe.to(device="cuda")

prompt = "A portrait of a Beautiful and playful ethereal singer, golden designs, highly detailed, blurry background"
negative_prompt = "Logo,Watermark,Ugly,Morbid,Extra fingers,Poorly drawn hands,Mutation,Blurry,Extra limbs,Gross proportions,Missing arms,Mutated hands,Long neck,Duplicate,Mutilated,Mutilated hands,Poorly drawn face,Deformed,Bad anatomy,Cloned face,Malformed limbs,Missing legs,Too many fingers"

images = pipe(prompt=prompt, negative_prompt=negative_prompt, height=1024, width=1024).images[0]
```


### Some tips for using our text-to-image model at inference: 


1. Using negative prompt is recommended.
2. For Fine-tuning, use zeros instead of null text embedding.
3. We support multiple aspect ratios, yet resolution should overall consists approximately `1024*1024=1M` pixels, for example:
`((1024,1024), (1280, 768), (1344, 768), (832, 1216), (1152, 832), (1216, 832), (960,1088)`

4. Use 30-50 steps (higher is better)
5. Use `guidance_scale` of  5.0


