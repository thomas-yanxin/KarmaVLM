from modelscope import snapshot_download
import os
os.environ['CURL_CA_BUNDLE'] = ''
model_dir = snapshot_download('X-D-Lab/KarmaVLM-Qwen1.5-0_5B',cache_dir="your_path/KarmaVLM-Qwen1.5-0_5B/")
model_dir = snapshot_download('thomas/clip-vit-large-patch14',cache_dir="your_path/clip-vit-large-patch14/")
