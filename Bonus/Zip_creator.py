import zipfile
import pathlib


def create_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file in filepaths:
            archive.write(file, arcname=pathlib.Path(file).name)


if __name__ == "__main__":
    create_archive(filepaths=["a.txt", "b.txt"], dest_dir="")