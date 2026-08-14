from pathlib import Path
import ffmpeg
from app.utils.logger import get_logger

logger = get_logger(__name__)

def stitch_clips(clip_paths: list[Path], out_path: Path) -> Path:
    list_file = out_path.parent / "concat_list.txt"
    with open(list_file, "w") as f:
        for clip in clip_paths:
            f.write(f"file '{clip.resolve()}'\n")

    logger.info(f"stitching {len(clip_paths)} clips into {out_path.name}")

    (
        ffmpeg
        .input(str(list_file), format="concat", safe=0)
        .output(str(out_path), c="copy")
        .overwrite_output()
        .run(quiet=True)
    )

    list_file.unlink()
    return out_path