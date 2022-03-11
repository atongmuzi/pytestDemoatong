import jpype
import os.path

from jpype._core import startJVM
from jpype._jvmfinder import getDefaultJVMPath

jarpath = os.path.join(os.path.abspath('.'), "MathFuns.jar")
# os.path.abspath这个函数用来获取当前 python 脚本所在的绝对路径

print(os.path.abspath('.'))
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
#"D:/jdk/jre/bin/server/jvm.dll"

