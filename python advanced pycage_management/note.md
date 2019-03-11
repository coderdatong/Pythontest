#1模块
-包含python代码的文件，后缀名.py
-为什么用模块
    -程序太大不方便，需要拆分
    -模块增加代码重复利用的方式
    -当作命名空间使用，避免命名冲突
-如何定义模块
    -模块就是普通文件
    -根据模块规范，要编写以下内容：
        -函数（单一功能）
        -类（相似功能的组合，或者业务模块）
        -测试代码
-如何使用模块
    -模块直接导入:
        -假如加入模块名称不能以数字开头，需要借助importlib帮助
        import module_name
        module_name.function_name
        module_name.class_name
        -import 模块 as 别名 给导入模块起一个别名
        -from module_name import func_name,class_name
         案例p04 按上述方法有选择性导入，不需要使用前缀
        -from module_name import *
        导入模块所有内容
#2.模块的搜索路径与存储
    搜索路径：加载模块的时候，系统在哪些地方寻找模块
-系统默认的模块搜索路径
    import sys
    sys.path 属性可以获取路径列表 
-添加搜索路径
    sys.path.append(dir)
-模块加载顺序
    1搜素内存中已经加载的模块
    2搜素python内置模块（print。。。）
    3搜素sys.path的路径



#包
-包里面存放的就是模块，一个文件夹
-自定义包的结构
    __init__.py 包的标志性文件
    模块1
    模块2
    子包 
        __init__.py
        子包模块1
        子包模块2
-包的导入操作
    -import package_name
    -直接导入一个包， 可以使用__init__.py中的内容（正常来讲应该为空）
    -使用方式是：
        package_name.func_name
        package_name.class_name_func_name()
        案例 pkb01，p07
- '__all__'的用法
    -在使用from package import *的时候，*可以导入的内容   
    __init__.py中如果文件为空，而且没有__all__，那么只可以把__init__中的内容导入，设定了则按照设定的导入子包或者模块
       案例 package2，p10
       
#命名空间
-用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
-作用是防止命名冲突