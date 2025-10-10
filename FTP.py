import tkinter as tk
from tkinter import messagebox,filedialog
import ftplib 
import os
import time
from comtypes.client import GetActiveObject

app = GetActiveObject("FeatureCAM.Application")

# app.Configurations.Import("D:\\Users\\00596\\Desktop\\test.cdb")
# app.Configurations.Import("D:\\Users\\00596\\Desktop\\mySet.cdb")
# iConfigs = app.Configurations
# for i in range(1,iConfigs.Count+1):
    # print(iConfigs.Item(i).Name)
    # iConfigs.Item(i).Delete()
doc = app.Documents


def send_program_to_machine():
    # 获取扫描枪读取的文件名
    filename = scan_entry.get().strip()
    if not filename:
        messagebox.showerror("输入错误", "扫描枪读取的文件名不能为空！")
        return
    if len(filename)>8:
        filename = filename[0:8]

    # 添加 .nc 扩展名
    filename_with_extension = f"{filename}.nc"

    # 获取用户输入的文件夹
    dirname = featurecam_folder_entry.get().strip()
    if not dirname:
        messagebox.showerror("输入错误", "文件夹不能为空！")
        return

    # 获取用户输入的主机名、用户名、密码和远程目录
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    remote_dir = remote_dir_entry.get()

    if not all([hostname, username, password, remote_dir]):
        messagebox.showerror("输入错误", "所有字段都必须填写！")
        return

    # 构建本地文件路径
    local_file_path = os.path.join(dirname, filename_with_extension)

    # 检查文件是否存在
    if not os.path.exists(local_file_path):
        messagebox.showerror("文件错误", f"文件 {local_file_path} 不存在！")
        return

    try:
        with ftplib .FTP() as ftp:
            ftp.connect(hostname)
            ftp.login(user=username, passwd=password)
            ftp.cwd(remote_dir)

            # 列出根目录下的所有文件
            files = ftp.nlst()
            for file in files:
                # 删除文件
                print("*"*10)
                print(file)
                ftp.delete(file)

            with open(local_file_path, 'rb') as file:
                ftp.storbinary(f'STOR {filename_with_extension}', file)
        messagebox.showinfo("成功", f"文件 {filename_with_extension} 发送成功！")
    except Exception as e:
        messagebox.showerror("FTP 错误", f"FTP 错误: {e}")

def reload_featurecam_part():
    filename = scan_entry.get().strip()
    if not filename:
        messagebox.showerror("输入错误", "扫描枪读取的文件名不能为空！")
        return

    # 获取用户输入的文件夹
    dirname = featurecam_folder_entry.get().strip()
    if not dirname:
        messagebox.showerror("输入错误", "文件夹不能为空！")
        return

    config_name = config_entry.get().strip()
    if not config_name:
        messagebox.showerror("输入错误", "配置文件的文件名不能为空！")
        return

    # 添加 .step 扩展名
    filename_with_extension = f"{filename}.step"

    # 构建本地文件路径
    local_file_path = os.path.join( dirname, filename_with_extension)

    # 检查文件是否存在
    if not os.path.exists(local_file_path):
        messagebox.showerror("文件错误", f"文件 {local_file_path} 不存在！")
        return

    try:
        # 假设这里有一个函数用于重新加载 FeatureCAM 零件
        # 这里只是一个示例，实际实现可能需要调用 FeatureCAM 的 API 或者其他方法
        reload_featurecam_part_file(filename,local_file_path,config_name)
        messagebox.showinfo("成功", f"文件 {filename_with_extension} 重新加载成功！")
    except Exception as e:
        messagebox.showerror("错误", f"重新加载文件时出错: {e}")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        featurecam_folder_entry.delete(0, tk.END)
        featurecam_folder_entry.insert(0, folder_selected)

def browse_config():
    config_file = filedialog.askopenfilename(
        title="选择配置文件",
        filetypes=[("配置文件", "*.cdb"), ("所有文件", "*.*")]
    )
    if config_file:
        config_entry.delete(0, tk.END)
        config_entry.insert(0, config_file)

def reload_featurecam_part_file(filename,file_path,config_name):
    # 这里是一个示例函数，假设它用于重新加载 FeatureCAM 零件
    # 实际实现可能需要调用 FeatureCAM 的 API 或者其他方法
    # 加载配置文件
    print(config_name )
    print(filename)
    # 提取配置文件名（不含扩展名）
    config_base_name = os.path.splitext(os.path.basename(config_name))[0]
    app.Configurations.Import(config_name)
    doc.Open(file_path)
    iPart = app.ActiveDocument.PartDocumentation
    iPart.comments = "四面分中，顶部为0。"
    iPart.Author = "蒋小军"
    iPart.Title = "test"
    iPart.Company = "思路咖精机南通有限公司"
    iPart.PartNumber = scan_entry.get().strip()
    iPart.Revision = "1.0"
    print(f"重新加载文件: {file_path}")
    iConfigs = app.Configurations
    iConfigSample = iConfigs.Item(config_base_name)
    # for i in range(1,iConfigs.Count+1):
        #print(iConfigs.Item(i).Name)
    # 复制配置
    iConfig = iConfigs.Item(filename)
    # iConfigSample = iConfigs.Item("iTest")
    iConfig.CopyConfiguration(iConfigSample)


# 创建主窗口
root = tk.Tk()
root.title("Fanuc NC 文件上传")

# 创建并放置标签和输入框
tk.Label(root, text="主机名:").grid(row=0, column=0, padx=10, pady=5)
hostname_entry = tk.Entry(root, width=30)
hostname_entry.grid(row=0, column=1, padx=10, pady=5)
hostname_entry.insert(0, "127.0.0.1")  # 设置默认主机名

tk.Label(root, text="用户名:").grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)
username_entry.insert(0, "CNC")  # 设置默认用户名

tk.Label(root, text="密码:").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=2, column=1, padx=10, pady=5)
password_entry.insert(0, "CNC")  # 设置默认密码

tk.Label(root, text="远程目录:").grid(row=4, column=0, padx=10, pady=5)
remote_dir_entry = tk.Entry(root, width=30)
remote_dir_entry.grid(row=4, column=1, padx=10, pady=5)
remote_dir_entry.insert(0, "/")  # 设置默认远程目录

# 新增扫描枪读取的文件名输入框
tk.Label(root, text="扫描枪读取的文件名:").grid(row=5, column=0, padx=10, pady=5)
scan_entry = tk.Entry(root, width=30)
scan_entry.grid(row=5, column=1, padx=10, pady=5)

# 新增 FeatureCAM 零件文件名输入框
tk.Label(root, text="FeatureCAM 零件文件夹:").grid(row=6, column=0, padx=10, pady=5)
featurecam_folder_entry = tk.Entry(root, width=30)
featurecam_folder_entry.grid(row=6, column=1, padx=10, pady=5)
featurecam_folder_entry.insert(0,r"D:\Users\00596\Desktop\featureCAM 培训\图纸-含3D") #设置默认文件夹

# 新增浏览文件夹按钮
browse_button = tk.Button(root, text="_浏览文件夹_", command=browse_folder)
browse_button.grid(row=6, column=2, padx=10, pady=5)

# 新增配置文件输入框
tk.Label(root, text="配置文件:").grid(row=7, column=0, padx=10, pady=5)
config_entry = tk.Entry(root, width=30)
config_entry .grid(row=7, column=1, padx=10, pady=5)
config_entry .insert(0, r"D:\Users\00596\Desktop\mySet.cdb")  # 设置默认配置文件名

# 新增浏览配置文件按钮
browse_config_button= tk.Button(root, text="—浏览配置文件—", command=browse_config)
browse_config_button.grid(row=7, column=2,  columnspan=2,padx=10, pady=10)


# 创建并放置重新加载 FeatureCAM 零件按钮
reload_button = tk.Button(root, text="重新加载零件", command=reload_featurecam_part)
reload_button.grid(row=8, column=0,  columnspan=2,padx=10, pady=10)

# 创建并放置发送按钮
send_button = tk.Button(root, text="发送CNC程序", command=send_program_to_machine)
send_button.grid(row=8, column=2, padx=10, pady=10)

# 将焦点设置到扫描枪读取的输入框上
scan_entry.focus_set()

# 启动主循环
root.mainloop()