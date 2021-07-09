# kaggle

## 注意事项

** 建议每组对照实验以本仓库为基准进行修改 **

1. 该仓库使用了与kaggle平台相同的目录结构
2. 请保证仓库根目录下包含input文件夹(内含：commonlitreadabilityprize； enhance-data, roberta-base)用于存放数据集和预训练模型
3. 请在kaggle平台运行前保证，GPU已打开，Internet已关闭
4. 请根据运行时间酌情调整训练数据集的大小，修改数据集的命令代码中有详细的注释
5. 该仓库的tools文件夹包含两个脚本：data_divide.py和reset_taget.py 
   data_divide.py：将从训练集数据中分割出一部分验证集，并将回文增强数据中对应的数据删除。这部分验证集并不会参与训练，并在训练结束后用于验证模型得分。必须说明的是，新的训练集，验证集和增强数据将会覆盖原文件。如果你不希望这样做请在程序末尾自行更改输出路径。
   reset_taget.py：将回文增强数据中的target进行调整，新得到的target服从对应数据估值的正态分布
   

## 更新日志
7.9.19:12----增加文件test_model_in_valid.py用于测试模型在验证集上的效果