import torch
from diffusers import StableDiffusionPipeline
from app.config import STYLE_CHECKPOINTS, CHECKPOINT_DIR

_pipelines: dict[str, StableDiffusionPipeline] = {}

def load_pipeline(style: str) -> StableDiffusionPipeline:
    if style in _pipelines:
        return _pipelines[style]

    model_id = STYLE_CHECKPOINTS[style]
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    pipeline = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=dtype,
        cache_dir=str(CHECKPOINT_DIR),
        safety_checker=None,
    )
    pipeline = pipeline.to(device)

    _pipelines[style] = pipeline
    return pipeline