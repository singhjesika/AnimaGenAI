from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CHECKPOINT_DIR = BASE_DIR / "checkpoints" / "sd_models"
MOTION_DIR = BASE_DIR / "checkpoints" / "motion_modules"
IMAGE_OUT_DIR = BASE_DIR / "outputs" / "images"
CLIP_OUT_DIR = BASE_DIR / "outputs" / "clips"
FINAL_OUT_DIR = BASE_DIR / "outputs" / "final"

STYLE_CHECKPOINTS = {
    "anime": "Linaqruf/anything-v3.0",
    "cartoon": "stablediffusionapi/toonyou",
    "realistic-lite": "runwayml/stable-diffusion-v1-5",
}

DURATION_PRESETS = {
    "10s": {"seconds": 10, "scenes": 3, "clip_seconds": 3.3},
    "20s": {"seconds": 20, "scenes": 6, "clip_seconds": 3.3},
    "60s": {"seconds": 60, "scenes": 18, "clip_seconds": 3.3},
    "120s": {"seconds": 120, "scenes": 36, "clip_seconds": 3.3},
}

MOTION_ADAPTER = "guoyww/animatediff-motion-adapter-v1-5-2"

IMAGE_WIDTH = 512
IMAGE_HEIGHT = 512
INFERENCE_STEPS = 25
GUIDANCE_SCALE = 7.5
FPS = 8