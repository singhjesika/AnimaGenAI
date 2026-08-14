import torch
from diffusers import AnimateDiffPipeline, MotionAdapter, DDIMScheduler
from app.config import STYLE_CHECKPOINTS, MOTION_ADAPTER, CHECKPOINT_DIR, MOTION_DIR

_animate_pipelines: dict[str, AnimateDiffPipeline] = {}

def load_animate_pipeline(style: str) -> AnimateDiffPipeline:
    if style in _animate_pipelines:
        return _animate_pipelines[style]

    model_id = STYLE_CHECKPOINTS[style]
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    adapter = MotionAdapter.from_pretrained(MOTION_ADAPTER, cache_dir=str(MOTION_DIR))

    pipeline = AnimateDiffPipeline.from_pretrained(
        model_id,
        motion_adapter=adapter,
        torch_dtype=dtype,
        cache_dir=str(CHECKPOINT_DIR),
    )
    pipeline.scheduler = DDIMScheduler.from_config(
        pipeline.scheduler.config,
        beta_schedule="linear",
        clip_sample=False,
        timestep_spacing="linspace",
        steps_offset=1,
    )
    pipeline = pipeline.to(device)

    _animate_pipelines[style] = pipeline
    return pipeline