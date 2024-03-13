<h1 align="center">🧘🏻‍♂️ KarmaVLM (相生) </h1>
<div align=center><img src ="./images/logo-github.png"/></div> 

<p align="center">
<a href="https://github.com/X-D-Lab/KarmaVLM"><img src="https://img.shields.io/badge/GitHub-24292e" alt="github"></a>
<a href="https://huggingface.co/X-D-Lab"><img src="https://img.shields.io/badge/-HuggingFace-yellow" alt="HuggingFace"></a>
<a href="https://modelscope.cn/organization/X-D-Lab"><img src="https://img.shields.io/badge/ModelScope-blueviolet" alt="modelscope"></a>
<a href="https://openi.pcl.ac.cn/XD-LAB/KarmaVLM"><img src="https://img.shields.io/badge/-OpenI-337AFF" alt="OpenI"></a>
<a href="https://WiseModel.cn/models/X-D%20Lab"><img src="https://img.shields.io/badge/WiseModel-561253" alt="WiseModel"></a>
</p> 


<div align="center">

[![GitHub license](https://img.shields.io/github/license/X-D-Lab/KarmaVLM
)](https://github.com/X-D-Lab/KarmaVLM/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/X-D-Lab/KarmaVLM)](https://github.com/X-D-Lab/KarmaVLM/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/X-D-Lab/KarmaVLM)](https://github.com/X-D-Lab/KarmaVLM/fork)
[![GitHub Contributors](https://img.shields.io/github/contributors/X-D-Lab/KarmaVLM)](https://github.com/X-D-Lab/KarmaVLM/graphs/contributors)  

</div>

<div align="center">

👋 **联系我们**: xd.lab2023@gmail.com

</div>

# 👏 Introduction
KarmaVLM is a family of high efficiency and powerful visual language model (VLM) pretrained with interleaved image-text data at scale, enabling content comprehension, recognition, and multi-round conversations about images.

# 🎉 News
* [2024/02] KarmaVLM is released. 

# ⚡️Features
KarmaVLM offers the following features:

- **High Efficiency**: KarmaVLM focuses on exploring the capabilities of small parametric quantitative models on multimodal tasks. So, KarmaVLM can be efficiently deployed on most GPU cards and personal computers, and even on end devices such as mobile phones.

- **Multi-round text-image conversations**: KarmaVLM can take both text and images as inputs and produce text outputs. Currently, it supports multi-round visual question answering with one image.

- **Strong image comprehension**: KarmaVLM is adept at analyzing visuals, making it an efficient tool for tasks like extracting, organizing, and summarizing information from images. 

# 🔥Model Zoo
| Name | Download | Language |Vision Encoder | LLM | MMBench | LLaVA-Bench-Wild | ScienceQA | TextVQA |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| KarmaVLM-Qwen1.5-0_5B | [🤗](https://huggingface.co/X-D-Lab/KarmaVLM-Qwen1.5-0_5B) / [🤖](https://modelscope.cn/models/X-D-Lab/KarmaVLM-Qwen1.5-0_5B/summary) / [✡️]() | EN | openai/clip-vit-large-patch14-336 | Qwen/Qwen1.5-0.5B | 53.5 | 40.4 | 43.22 | 36.1 |
| KarmaVLM-Qwen1.5-0_5B_Siglip | [🤗]() / [🤖]() / [✡️]() | EN | google/siglip-so400m-patch14-384 | Qwen/Qwen1.5-0.5B | 54.6 | 47.5 | 53.81 | 44.98 |
| KarmaVLM-Qwen1.5-0_5B_Siglip_moe | [🤗]() / [🤖]() / [✡️]() | EN | google/siglip-so400m-patch14-384 | Qwen/Qwen1.5-0.5B | 55.7 | 47.5 | 53.81 | 45.25 |

Basically we have achieved **SOTA** among models of the same parameter order of magnitude, even beyond some models with larger parameters. More Benchmark evaluations are in progress!

# 👨‍💻 Quick Start

## Requirements and Installation

```
git clone https://github.com/X-D-Lab/KarmaVLM.git
cd KarmaVLM

conda create -n karmavlm python=3.10 -y
conda activate karmavlm

pip install --upgrade pip  # enable PEP 660 support
pip install modelscope
pip install -e .
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```

you can download model:X-D-Lab/KarmaVLM-Qwen1.5-0_5B,and vision tower:openai/clip-vit-large-patch14 by run download.py
```
python download.py
```
you need to change the path in the download.py to your path,also, you need to change the path of vision tower in the config.json to your local vision tower path

```
from modelscope import snapshot_download
import os
os.environ['CURL_CA_BUNDLE'] = ''
model_dir = snapshot_download('X-D-Lab/KarmaVLM-Qwen1.5-0_5B',cache_dir="your_path/KarmaVLM-Qwen1.5-0_5B/") #where you need change
model_dir = snapshot_download('thomas/clip-vit-large-patch14',cache_dir="your_path/clip-vit-large-patch14/")#where you need change

```

## 🌏 Demo
1. CLI Inference
    ```
    python -m llava.serve.cli \
        --model-path /path/to/karmavlm/model \
        --image-file /path/to/the/test/image
    ```
2. Gradio Web UI

  - Starting the Controller
    ```
    python -m llava.serve.gradio_web_server \
        --controller http://localhost:10000 \
        --model-list-mode reload
        --share ##(optional)
    ```
  - Launching the Gradio Web Server
    ```
    python -m llava.serve.model_worker \
        --host 0.0.0.0 \
        --controller http://localhost:10000 \
        --port 40000 \
        --worker http://localhost:40000 \
        --model-path /path/to/karmavlm/model 
    ```

# 📋 License
This project utilizes certain datasets and checkpoints that are subject to their respective original licenses. Users must comply with all terms and conditions of these original licenses. The content of this project itself is licensed under the [Apache license 2.0](./LICENSE).

# 🙇‍ Architecture
We build our project based on [LLaVA](https://github.com/haotian-liu/LLaVA): Large Language and Vision Assistant.

# 💪 Contributors

<a href="https://github.com/X-D-Lab/KarmaVLM/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=X-D-Lab/KarmaVLM" />
</a>  

### 其他

<div align="center">

***感谢上海人工智能实验室组织的 书生·浦语实战营 学习活动~***

***感谢 OpenXLab 对项目部署的算力支持~***

***感谢 浦语小助手 对项目的支持~***

***感谢上海人工智能实验室推出的书生·浦语大模型实战营，为我们的项目提供宝贵的技术指导和强大的算力支持！***

[**InternLM-tutorial**](https://github.com/InternLM/tutorial)、[**InternStudio**](https://studio.intern-ai.org.cn/)、[**xtuner**](https://github.com/InternLM/xtuner)、[**InternLM-Math**](https://github.com/InternLM/InternLM-Math)



</div>



## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=X-D-Lab/KarmaVLM&type=Date)](https://star-history.com/#X-D-Lab/KarmaVLM&Date)

