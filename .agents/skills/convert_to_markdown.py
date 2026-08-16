import sys
from pathlib import Path
from markitdown import MarkItDown


def ingest_document(input_path: str, output_dir: str):
    md = MarkItDown()
    src = Path(input_path)
    if not src.exists():
        print(f"Error: Source file not found at {src}")
        sys.exit(1)

    dest_dir = Path(output_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Convert file to markdown
    result = md.convert(str(src))

    # Save output
    output_file = dest_dir / f"{src.stem}.md"
    output_file.write_text(result.text_content, encoding="utf-8")
    print(f"Successfully converted: {src.name} -> {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_to_markdown.py <input_file> <target_folder>")
        sys.exit(1)
    ingest_document(sys.argv[1], sys.argv[2])
