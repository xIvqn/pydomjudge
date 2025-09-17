import sys
import re

def bump_version_in_file(filepath, pattern, replacement):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, count = re.subn(pattern, replacement, content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    if count == 0:
        print(f"Warning: No version string found in {filepath}")
    else:
        print(f"Bumped version in {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py NEW_VERSION")
        sys.exit(1)
    new_version = sys.argv[1]

    # pyproject.toml
    bump_version_in_file(
        "pyproject.toml",
        r'version\s*=\s*"[0-9a-zA-Z\.\-\+]+"',
        f'version = "{new_version}"'
    )

    # docs/conf.py
    bump_version_in_file(
        "docs/conf.py",
        r'release\s*=\s*\'[0-9a-zA-Z\.\-\+]+\'',
        f'release = \'{new_version}\''
    )
