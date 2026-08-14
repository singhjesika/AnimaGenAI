from app.config import IMAGE_OUT_DIR, CLIP_OUT_DIR, FINAL_OUT_DIR
from app.core.prompt_parser import build_scene_prompts
from app.core.video_animator import animate_scenes
from app.core.stitcher import stitch_clips
from app.utils.file_utils import new_run_id, run_subdir
from app.utils.logger import get_logger

logger = get_logger(__name__)

def run_pipeline(prompt: str, duration_key: str, style: str) -> str:
    run_id = new_run_id()
    logger.info(f"starting run {run_id}")

    scene_prompts = build_scene_prompts(prompt, duration_key, style)

    clip_dir = run_subdir(CLIP_OUT_DIR, run_id)
    clip_paths = animate_scenes(scene_prompts, style, clip_dir)

    final_dir = run_subdir(FINAL_OUT_DIR, run_id)
    final_path = final_dir / f"{run_id}_{duration_key}.mp4"
    stitch_clips(clip_paths, final_path)

    logger.info(f"finished run {run_id}")
    return str(final_path)