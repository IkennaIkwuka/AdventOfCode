from pathlib import Path


def project_path(file: str | None = None, *relative_parts: str) -> Path:
    """
    Build a path relative to the project root (folder containing 'src/').

    :param file: MUST be __file__ from the calling script
    :type file: str | None
    :param relative_parts: folder/file parts, e.g. ("docs", "Tasks_file.txt")
    :type relative_parts: str
    :return: returns pathlib.Path
    :rtype: Path

    """

    if file is None:
        raise TypeError("project_path() missing required first argument '__file__'")

    # Ensure file really points to an existing file
    if not Path(file).exists():
        raise ValueError(f"The first argument must be __file__, got '{file}'")

    # Start from the file's directory
    p = Path(file).resolve()

    # Search upward for the nearest folder containing 'src'
    for parent in [p] + list(p.parents):
        if (parent / "src").is_dir():
            root = parent
            break
    else:
        # fallback: use current file's directory
        root = p.parent

    path = root.joinpath(*relative_parts)

    # Ensure file and directory exist
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

    return path
