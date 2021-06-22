import os
import sys
import shutil

"""
shutil 모듈은 시스템에서 파일을 조작할 때 유용하다. 다음 코드는 터미널에서 파일 및 확장자를 지정하면 새 확장자의 이름으로 복사본을 만든다.
아래는 실행법
root@DESKTOP-JPGB0S5:/mnt/d/Mastering-Python-Design-Patterns-Second-Edition/algo/module_structure# python3.6 6_change_ext_file.py hello.py txt
hello.txt
"""

def change_file_ext():
    if len(sys.argv) < 2:
        print("Usage: python {0} filename.old_ext 'new_ext'".format(sys.argv[0]))
        sys.exit()

    name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
    print(name)

    try:
        shutil.copyfile(sys.argv[1],name)
    except OSError as err:
        print(err)

if __name__ == "__main__":
    change_file_ext()