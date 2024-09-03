## 使用说明
1. 选择PDF文件夹后，点击执行即可开始提取属性

**输出** 
```
|--- 无法提取的PDF
|--- 提取结果.xlsx
```

## 打包命令
```shell
pip install pyinstaller=5.13
pyinstaller -F -c -w -i ico\cloud.ico gui.py --hidden-import openpyxl.cell._writer
# 或者采用sepc文件
pyinstaller .\gui.spec
```

