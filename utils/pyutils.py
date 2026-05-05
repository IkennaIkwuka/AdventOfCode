from pathlib import Path
import sys


def project_path(
    file: str | None = None,
    *relative_parts: str,
    marker: str = "src",
) -> Path:
    """
    Build a path relative to the project root (folder containing 'marker', default 'src').

    Automatically adds the project root to sys.path to isolate imports from sibling projects.

    :param file: MUST be __file__ from the calling script
    :type file: str | None
    :param relative_parts: folder/file parts, e.g. ("docs", "Tasks_file.txt")
    :type relative_parts: str
    :param create: whether to auto-create directories/files if missing
    :type create: bool
    :param marker: folder or file that identifies the project root (default 'src')
    :type marker: str
    :return: pathlib.Path pointing to the requested path
    :rtype: Path
    """

    # Require __file__
    if file is None:
        raise TypeError("project_path() missing required first argument '__file__'")

    # Ensure file exists
    file_path = Path(file).resolve()
    if not file_path.exists():
        raise ValueError(f"The first argument must be __file__, got '{file}'")

    # Find project root (folder containing 'marker')
    for parent in [file_path] + list(file_path.parents):
        if (parent / marker).exists():
            root = parent
            break
    else:
        root = file_path.parent  # fallback

    # Add project root to sys.path to isolate project imports
    root_str = str(root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)

    # Build the requested path relative to the root
    path = root.joinpath(*relative_parts)

    # Optionally create directories/files
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

    return path


def project_path_(file: str | None = None, *relative_parts: str) -> Path:
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

    # # Optional: add grandparent to sys.path
    # sys.path.append(str(root.parent.parent))  # adds 2 levels up from root

    path = root.joinpath(*relative_parts)

    # Ensure file and directory exist
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

    return path
