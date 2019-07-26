
import win32com.client


#连接solidworks对象
swapp = win32com.client.Dispatch("sldworks.Application")

#窗口可见（窗口显示、隐藏）
visible = swapp.visible

#打开文件-参数（文件路径名称，1）
open_file = swapp.OpenDoc(r"path + part_name", 1)

#实例化活动文档
part = swapp.ActiveDoc

#活动文档另存为
new_name = part.SaveAs3(r"path + part_name", 0, 2)
