import pytest
from app.core.prompt_parser import build_scene_prompts, validate

def test_validate_bad_duration():
    with pytest.raises(ValueError):
        validate("5s", "anime")

def test_validate_bad_style():
    with pytest.raises(ValueError):
        validate("10s", "watercolor")

def test_scene_count_matches_preset():
    scenes = build_scene_prompts("a fox in a forest", "10s", "anime")
    assert len(scenes) == 3

def test_style_tag_included():
    scenes = build_scene_prompts("a fox in a forest", "10s", "cartoon")
    assert "cartoon style" in scenes[0]