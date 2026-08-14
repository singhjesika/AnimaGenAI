from pathlib import Path
from app.models.sd_loader import load_pipeline
from app.config import IMAGE_WIDTH, IMAGE_HEIGHT, INFERENCE_STEPS, GUIDANCE_SCALE
from app.utils.logger import get_logger

logger = get_logger(__name__)

def generate_scene_images(scene_prompts: list[str], style: str, out_dir: Path) -> list[Path]:
    pipeline = load_pipeline(style)
    image_paths = []

    for idx, prompt in enumerate(scene_prompts):
        logger.info(f"generating image {idx + 1}/{len(scene_prompts)}")
        result = pipeline(
            prompt=prompt,
            width=IMAGE_WIDTH,
            height=IMAGE_HEIGHT,
            num_inference_steps=INFERENCE_STEPS,
            guidance_scale=GUIDANCE_SCALE,
        )
        image = result.images[0]
        image_path = out_dir / f"scene_{idx:03d}.png"
        image.save(image_path)
        image_paths.append(image_path)

    return image_paths