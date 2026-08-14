from app.config import DURATION_PRESETS, STYLE_CHECKPOINTS

STYLE_TAGS = {
    "anime": "anime style, cel shading, vibrant colors, detailed background",
    "cartoon": "cartoon style, bold outlines, flat colors, playful",
    "realistic-lite": "cinematic lighting, high detail, photorealistic",
}

def validate(duration_key: str, style: str) -> None:
    if duration_key not in DURATION_PRESETS:
        raise ValueError(f"unknown duration preset: {duration_key}")
    if style not in STYLE_CHECKPOINTS:
        raise ValueError(f"unknown style: {style}")

def build_scene_prompts(prompt: str, duration_key: str, style: str) -> list[str]:
    validate(duration_key, style)
    scene_count = DURATION_PRESETS[duration_key]["scenes"]
    style_tag = STYLE_TAGS[style]
    base = prompt.strip().rstrip(".")
    scenes = []
    for i in range(scene_count):
        progress = f"scene {i + 1} of {scene_count}"
        scenes.append(f"{base}, {progress}, {style_tag}")
    return scenes