from unittest.mock import patch
from pathlib import Path
from app.core.pipeline import run_pipeline

@patch("app.core.pipeline.stitch_clips")
@patch("app.core.pipeline.animate_scenes")
def test_run_pipeline_returns_path(mock_animate, mock_stitch):
    mock_animate.return_value = [Path("clip_000.mp4")]
    mock_stitch.side_effect = lambda clips, out_path: out_path

    result = run_pipeline("a fox in a forest", "10s", "anime")

    assert result.endswith(".mp4")
    mock_animate.assert_called_once()
    mock_stitch.assert_called_once()