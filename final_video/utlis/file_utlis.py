import shutil
import uuid
from pathlib import Path

def new_run_id() -> str:
    return uuid.uuid4().hex[:10]

def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

def clear_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)

def run_subdir(base: Path, run_id: str) -> Path:
    return ensure_dir(base / run_id)