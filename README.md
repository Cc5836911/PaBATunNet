本研究采用环境：
       Python == 3.8.0
       Tensorflow == 2.10.0
       Jupyter == 1.0.0
       scikit-learn == 1.1.3
在PaBATunNet文件夹中：
       beerdemo:啤酒近红外光谱数据处理
       dieseldemo：柴油近红外光谱数据处理
       graindemo：谷物近红外光谱数据处理
       milkdemo：牛奶近红外光谱数据处理
       data：近红外光谱数据集
       resultsdemo：所有结果
在resultsdemo文件中：
       allbestmodel.csv:不同数据集最优模型数据
       allresults.csv：不同数据集的PaBATunNet模型运行50次的平均值
       bestmodel：最优模型
注：如需对各数据集进行预测检验，可以直接运行resultsdemo/bestmodel/所对应物质的模型
