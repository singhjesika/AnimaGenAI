from unittest.mock import patch, MagicMock
from pathlib import Path
from app.core.stitcher import stitch_clips

@patch("app.core.stitcher.ffmpeg")
def test_stitch_clips_calls_ffmpeg(mock_ffmpeg, tmp_path):
    clips = [tmp_path / "a.mp4", tmp_path / "b.mp4"]
    for c in clips:
        c.touch()

    out_path = tmp_path / "final.mp4"
    mock_input = MagicMock()
    mock_ffmpeg.input.return_value = mock_input
    mock_input.output.return_value = mock_input
    mock_input.overwrite_output.return_value = mock_input

    result = stitch_clips(clips, out_path)

    assert result == out_path
    mock_ffmpeg.input.assert_called_once()