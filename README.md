---
license: other
license_name: bria-t2i
license_link: https://bria.ai/customer-general-terms-and-conditions
library_name: diffusers
inference: False
    
tags:
- text-to-image
- legal liability
- commercial use
extra_gated_description: 
  Model weights from BRIA AI can be obtained with the purchase of a commercial license. Fill in the form below and we reach out to you. 
  Need API Access? Get it [here](https://platform.bria.ai/console/api/image-generation) (1K Monthly Free API Calls).
  Startup or a student? Get access by applying for our [Startup Program](https://pages.bria.ai/the-visual-generative-ai-platform-for-builders-startups-plan?_gl=1*cqrl81*_ga*MTIxMDI2NzI5OC4xNjk5NTQ3MDAz*_ga_WRN60H46X4*MTcwOTM5OTMzNC4yNzguMC4xNzA5Mzk5MzM0LjYwLjAuMA..) 
extra_gated_heading: "Fill in this form to request a commercial license for the model"
extra_gated_fields:
  Name: text
  Company/Org name: text
  Org Type (Early/Growth Startup, Enterprise, Academy): text
  Role: text
  Country: text
  Email: text
  By submitting this form, I agree to BRIA’s Privacy policy and Terms & conditions, see links below: checkbox
---

# TL;DR

BRIA 3.2 is our latest commercial-ready text-to-image model that significantly improves aesthetics over Bria 3.1 and **excels at rendering clear, readable text**, particularly optimized for short phrases (1-6 words). Still ethically trained on licensed data, it offers unmatched legal compliance and customization.

[CLICK HERE FOR A DEMO](https://huggingface.co/spaces/briaai/BRIA-3.2)




![](32-photo.jpg)



# BRIA 3.2: Text-to-Image Model for Commercial Licensing

BRIA 3.2 is our new groundbreaking text-to-image model explicitly designed for commercial applications. This model combines technological innovation with ethical responsibility and legal security, setting a new standard in the AI industry. Bria AI licenses the foundation model with full legal liability coverage. Our dataset does not contain copyrighted materials, such as fictional characters, logos, trademarks, public figures, harmful content, or privacy-infringing content.

For more information, please visit our [website](https://bria.ai/).

Join our [Discord community](https://discord.gg/Nxe9YW9zHS) for more information, tutorials, tools, and to connect with other users!


# What's New

- **Improved Aesthetics**: 55% user preference for BRIA 3.2 over BRIA 3.1.

- **Superior Text Rendering**: The model is optimized to generate short text consists of 1-6 words. OCR Score improvement from 5% (3.1) to 60% (3.2).

- **Consistent Prompt Alignment**: Maintains high-quality textual description adherence.






### Get Access
Interested in BRIA 3.2? Purchase is required to license and access BRIA 3.2, ensuring royalty management with our data partners and full liability coverage for commercial use. 

Are you a startup or a student? We encourage you to apply for our [Startup Program](https://pages.bria.ai/the-visual-generative-ai-platform-for-builders-startups-plan?_gl=1*cqrl81*_ga*MTIxMDI2NzI5OC4xNjk5NTQ3MDAz*_ga_WRN60H46X4*MTcwOTM5OTMzNC4yNzguMC4xNzA5Mzk5MzM0LjYwLjAuMA..) to request access. This program are designed to support emerging businesses and academic pursuits with our cutting-edge technology.

Contact us today to unlock the potential of BRIA 3.2! By submitting the form above, you agree to BRIA’s [Privacy policy](https://bria.ai/privacy-policy/) and [Terms & conditions](https://bria.ai/terms-and-conditions/).


# Key Features

- **Legally Compliant**: Offers full legal liability coverage for copyright and privacy infringements. Thanks to training on 100% licensed data from leading data partners, we ensure the ethical use of content.

- **Patented Attribution Engine**: Our attribution engine is our way to compensate our data partners, powered by our proprietary and patented algorithms. 

- **Enterprise-Ready**: Specifically designed for business applications, Bria AI 3.0 delivers high-quality, compliant imagery for a variety of commercial needs.

- **Customizable Technology**: Provides access to source code and weights for extensive customization, catering to specific business requirements.

### Model Description

- **Developed by:** BRIA AI
- **Model type:** Latent diffusion text-to-image model
- **License:** [Commercial licensing terms & conditions.](https://bria.ai/customer-general-terms-and-conditions)
- Purchase is required to license and access the model.

- **Model Description:** BRIA 3.2 is a text-to-image model trained exclusively on a professional-grade, licensed dataset. It is designed for commercial use and includes full legal liability coverage.
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
    
hf_hub_download(repo_id="briaai/BRIA-3.1", filename='pipeline_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.1", filename='transformer_bria.py', local_dir=local_dir)
hf_hub_download(repo_id="briaai/BRIA-3.1", filename='bria_utils.py', local_dir=local_dir)

import torch
from pipeline_bria import BriaPipeline, BriaTransformer2DModel

# trust_remote_code = True - allows loading a transformer which is not present at the transformers library(from transformer/bria_transformer.py)
transformer = BriaTransformer2DModel.from_pretrained("briaai/BRIA-3.2",subfolder='transformer',torch_dtype=torch.bfloat16)
pipe = BriaPipeline.from_pretrained("briaai/BRIA-3.1", transformer=transformer, torch_dtype=torch.bfloat16,trust_remote_code=True)
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
5. Use `guidance_scale` of 5.0


