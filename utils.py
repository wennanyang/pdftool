import shutil
import re
from pathlib import Path
def check_dir(dir : Path, exp_basename=Path('异常文件汇总')) -> Path:
    dir = exp_basename.joinpath(dir)
    if not dir.exists():
        dir.mkdir(parents=True)
        return dir
    shutil.rmtree(dir)
    dir.mkdir(parents=True)
    return dir
def find_match_txt_recursion(parent_dir : Path, re_pattern) -> Path:
    files = parent_dir.rglob("*.txt")
    for file in files:
            if re.match(re_pattern, file.name) is not None:
                return file.resolve()
    return None
def ignore_hidden_files(src, names):
    """忽略隐藏文件和目录"""
    ignored_names = []
    for name in names:
        if name.startswith('~'):
            ignored_names.append(name)
    return set(ignored_names)
if __name__ == '__main__':
    path = Path(r"F:\专题库\原数据\放线txt补充")
    dest = Path(r"F:\专题库\原数据\放线补充")
    if not dest.exists():
        dest.mkdir(parents=True, exist_ok=True)
    files = path.glob("*.txt")
    for file in files:
        print(file.name.split(".")[0])
        dest.joinpath(file.name.split(".")[0]).mkdir(parents=True, exist_ok=True)
        shutil.copy(file, dest.joinpath(file.name.split(".")[0]).joinpath(file.name))
