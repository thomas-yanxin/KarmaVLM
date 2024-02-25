<h1 align="center">🧘🏻‍♂️ KarmaVLM (相生) </h1>
<div align=center><img src ="./images/logo-github.png"/></div> 

# 👏 Introduction
KarmaVLM is a family of lightweight but powerful visual language model (VLM) pretrained with interleaved image-text data at scale, enabling content comprehension, recognition, and multi-round conversations about images.

# 🎉 News
* [2024/02] KarmaVLM is released. 

# ⚡️Features
KarmaVLM offers the following features:

**High Efficiency**: KarmaVLM focuses on exploring the capabilities of small parametric quantitative models on multimodal tasks. So, KarmaVLM can be efficiently deployed on most GPU cards and personal computers, and even on end devices such as mobile phones.

**Multi-round text-image conversations**: KarmaVLM can take both text and images as inputs and produce text outputs. Currently, it supports multi-round visual question answering with one image.

**Strong image comprehension**: KarmaVLM is adept at analyzing visuals, making it an efficient tool for tasks like extracting, organizing, and summarizing information from images. 

# 🔥Model Zoo
| Checkpoint | Vision Encoder | LLM | MMBench | 
| :----: | :----: | :----: | :----: |
| KarmaVLM-Qwen1.5-0_5B | openai/clip-vit-large-patch14-336 | Qwen/Qwen1.5-0.5B | 53.5 |

Other Benchmark evaluations are in progress!

# 🙇‍ Architecture
We build our project based on [LLaVA](https://github.com/haotian-liu/LLaVA): Large Language and Vision Assistant.


