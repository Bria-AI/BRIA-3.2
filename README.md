# BRIA 3.2
<p align="center"><img src="https://platform.bria.ai/assets/Bria-logo-5e0c53b1.svg" alt="BRIA Logo" width="400" /></p>

<p align="center">
  <img src="https://img.shields.io/badge/License-Commercial-blue.svg" alt="License Badge" />
  <img src="https://img.shields.io/badge/Model%20Size-4B%20parameters-green.svg" alt="Model Size Badge" />
  <img src="https://img.shields.io/badge/Trained%20on-Licensed%20Data-brightgreen.svg" alt="Licensed Data Badge" />
  <img src="https://img.shields.io/badge/Commercial%20Ready-Yes-orange.svg" alt="Commercial Ready Badge" />
  <a href="https://huggingface.co/briaai/BRIA-3.2">
    <img src="https://img.shields.io/badge/🤗%20HuggingFace-Model-yellow.svg" alt="HuggingFace Model Badge" />
  </a>
  <a href="https://huggingface.co/spaces/briaai/BRIA-3.2">
    <img src="https://img.shields.io/badge/🤗%20HuggingFace-Space-blueviolet.svg" alt="HuggingFace Space Badge" />
  </a>
</p>
<p align="center">
<a href="[https://huggingface.co/spaces/briaai/BRIA-3.2](https://go.bria.ai/46gzn20)">
    <img src=https://img.shields.io/badge/check%20out%20our%20platform-8A2BE2 />
  </a>
</p>



# TL;DR

Bria 3.2 is the next-generation commercial-ready text-to-image model.
**With just 4 billion parameters**, it provides exceptional aesthetics and text rendering, evaluated to provide **on par results to leading open-source models, and outperforming other licensed models**.

In addition to being **built entirely on licensed data**, 3.2 provides several advantages for enterprise and commercial use:
* Efficient Compute - the model is X3 smaller than the equivalent models in the market (4B parameters vs 12B parameters other open source models)
* Architecture Consistency: Same architecture as 3.1—ideal for users looking to upgrade without disruption.
* Fine-tuning Speedup: 2x faster fine-tuning on L40S and A100.


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

- **API Endpoint**: [Bria.ai](https://docs.bria.ai/image-generation/endpoints/text-to-image-base) , [Fal.ai](https://fal.ai/models/bria/text-to-image/3.2), [Replicate](https://replicate.com/bria/image-3.2)
- **ComfyUI**: [Use it in workflows](https://github.com/Bria-AI/ComfyUI-BRIA-API)
- **Interested in BRIA 3.2 source code and weights for commercial use?** Purchase is required to license BRIA 3.2 got commercial use, ensuring royalty management with our data partners and full liability coverage.
- Are you a startup or a student? We encourage you to apply for our [Startup Program](https://pages.bria.ai/the-visual-generative-ai-platform-for-builders-startups-plan?_gl=1*cqrl81*_ga*MTIxMDI2NzI5OC4xNjk5NTQ3MDAz*_ga_WRN60H46X4*MTcwOTM5OTMzNC4yNzguMC4xNzA5Mzk5MzM0LjYwLjAuMA..) to request access. This program are designed to support emerging businesses and academic pursuits with our cutting-edge technology.
- By submitting the form above, you agree to BRIA’s [Privacy policy](https://bria.ai/privacy-policy/) and [Terms & conditions](https://bria.ai/terms-and-conditions/).



# Key Features

- **Architecture**: 4B parameter, rectified flow transformer based model with T5 text encoder.

- **Legally Compliant**: Offers full legal liability coverage for copyright and privacy infringements. Thanks to training on 100% licensed data from leading data partners, we ensure the ethical use of content.

- **Patented Attribution Engine**: Our attribution engine is our way to compensate our data partners, powered by our proprietary and patented algorithms. 

- **Enterprise-Ready**: Specifically designed for business applications, Bria AI 3.2 delivers high-quality, compliant imagery for a variety of commercial needs.

- **Customizable Technology**: Provides access to source code and weights for extensive customization, catering to specific business requirements.

### Model Description

- **Developed by:** BRIA AI
- **Model type:** Latent diffusion text-to-image model
- **Resources for more information:** [BRIA AI](https://bria.ai/)




### Code example using Diffusers 

install the latest version of diffusers:
```python
pip install git+https://github.com/huggingface/diffusers
```



```python
import torch
from diffusers import BriaPipeline

pipe = BriaPipeline.from_pretrained("briaai/BRIA-3.2", torch_dtype=torch.bfloat16)
pipe.to(device="cuda")

prompt = "A vibrant birthday cake displayed on a festive table, frosted in smooth sky-blue icing with colorful sprinkles along the edges. Piped in bold white frosting across the top are the words “BIG BOY NOW” in playful, slightly uneven lettering. The cake is decorated with mini stars, balloons made of fondant, and a single candle burning brightly in the center. Soft, warm lighting highlights the texture of the frosting, while a blurred background of party decorations—streamers, confetti, and balloons—adds a joyful, celebratory atmosphere."
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


