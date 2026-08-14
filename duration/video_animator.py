from pathlib import Path
from diffusers.utils import export_to_video
from app.models.animatediff_loader import load_animate_pipeline
from app.config import INFERENCE_STEPS, GUIDANCE_SCALE, FPS
from app.utils.logger import get_logger

logger = get_logger(__name__)

def animate_scenes(scene_prompts: list[str], style: str, out_dir: Path) -> list[Path]:
    pipeline = load_animate_pipeline(style)
    clip_paths = []

    for idx, prompt in enumerate(scene_prompts):
        logger.info(f"animating clip {idx + 1}/{len(scene_prompts)}")
        result = pipeline(
            prompt=prompt,
            num_inference_steps=INFERENCE_STEPS,
            guidance_scale=GUIDANCE_SCALE,
        )
        frames = result.frames[0]
        clip_path = out_dir / f"clip_{idx:03d}.mp4"
        export_to_video(frames, str(clip_path), fps=FPS)
        clip_paths.append(clip_path)

    return clip_paths