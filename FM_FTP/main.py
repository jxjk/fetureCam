import tkinter as tk
from tkinter import messagebox, filedialog
import ftplib
import os
import csv
import configparser
# from comtypes.client import GetActiveObject
import win32com.client

app = win32com.client.Dispatch("FeatureCAM.Application")
# app = GetActiveObject("FeatureCAM.Application")
doc = app.Documents


# 从 config.ini 文件中读取 FTP 相关设置
def load_ftp_settings():
    settings = {}
    config = configparser.ConfigParser()
    
    # 读取 config.ini 文件
    config.read('config.ini',encoding='utf-8')
    
    # 从 [FTP] 部分读取配置
    settings['hostname'] = config.get('FTP', 'hostname')
    settings['username'] = config.get('FTP', 'username')
    settings['password'] = config.get('FTP', 'password')
    settings['remote_dir'] = config.get('FTP', 'remote_dir')
    
    # 从 [CONFIG_DIRECTORY] 部分读取配置
    settings['default_config_folder'] = config.get('CONFIG_DIRECTORY', 'default_config_folder')
    settings['default_folder'] = config.get('CONFIG_DIRECTORY', 'default_folder')
    
    # 从 [MATERIALS] 部分读取材料选项
    settings['materials'] = [option.upper() for option in config.options('MATERIALS')]
    settings['materials'] = [config.get('MATERIALS', option) for option in config.options('MATERIALS')]
    print(dir(settings['materials']))
    return settings


# 读取配置文件
ftp_settings = load_ftp_settings()
print(ftp_settings["materials"])

def send_program_to_machine():
    # 获取扫描枪读取的文件名
    filename_all = scan_entry.get().strip()
    if not filename_all:
        messagebox.showerror("输入错误", "扫描枪读取的文件名不能为空！")
        return
    if len(filename_all) > 8:
        filename = filename_all[0:8]
    else:
        filename = filename_all

    # 添加 .nc 扩展名
    filename_with_extension = f"{filename}.nc"

    # 获取用户输入的文件夹
    dirname = featurecam_folder_entry.get().strip()
    if not dirname:
        messagebox.showerror("输入错误", "文件夹不能为空！")
        return

    # 构建本地文件路径
    local_file_path = os.path.join(dirname, filename_with_extension)

    # 检查文件是否存在
    if not os.path.exists(local_file_path):
        messagebox.showerror("文件错误", f"文件 {local_file_path} 不存在！")
        return

    try:
        with ftplib.FTP() as ftp:
            ftp.connect(ftp_settings['hostname'])
            ftp.login(user=ftp_settings['username'], passwd=ftp_settings['password'])
            ftp.cwd(ftp_settings['remote_dir'])

            # 创建以零件名为名称的文件夹
            remote_part_dir = os.path.join(ftp_settings['remote_dir'], filename_all)
            try:
                ftp.mkd(remote_part_dir)
            except ftplib.error_perm as e:
                if "550" in str(e):  # 文件夹已存在
                    pass
                else:
                    raise

            # 切换到新创建的文件夹
            ftp.cwd(remote_part_dir)


            # 列出根目录下的所有文件
            files = ftp.nlst()
            for file in files:
                # 删除文件
                print("*" * 10)
                print(file)
                # ftp.delete(file)

            with open(local_file_path, 'rb') as file:
                ftp.storbinary(f'STOR {filename_with_extension}', file)
        messagebox.showinfo("成功", f"文件 {filename_with_extension} 发送成功！")
    except Exception as e:
        messagebox.showerror("FTP 错误", f"FTP 错误: {e}")

def reload_featurecam_part(direction=None, alignment=None):
    filename = scan_entry.get().strip()
    if not filename:
        messagebox.showerror("输入错误", "扫描枪读取的文件名不能为空！")
        return

    # 获取用户输入的文件夹
    dirname = featurecam_folder_entry.get().strip()
    if not dirname:
        messagebox.showerror("输入错误", "文件夹不能为空！")
        return

    config_name = config_dropdown.get()
    if not config_name:
        messagebox.showerror("输入错误", "配置文件的文件名不能为空！")
        return

    # 添加 .step 扩展名
    filename_with_extension = f"{filename}.step"

    # 构建本地文件路径
    local_file_path = os.path.join(dirname, filename_with_extension)

    # 检查文件是否存在
    if not os.path.exists(local_file_path):
        messagebox.showerror("文件错误", f"文件 {local_file_path} 不存在！")
        return

    try:
        # 假设这里有一个函数用于重新加载 FeatureCAM 零件
        # 这里只是一个示例，实际实现可能需要调用 FeatureCAM 的 API 或者其他方法
        reload_featurecam_part_file(filename, local_file_path, config_name, direction, alignment)
        messagebox.showinfo("成功", f"文件 {filename_with_extension} 重新加载成功！")
    except Exception as e:
        print(e)
        messagebox.showerror("错误", f"重新加载文件时出错: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        featurecam_folder_entry.delete(0, tk.END)
        featurecam_folder_entry.insert(0, folder_selected)

def reload_featurecam_part_file(filename, file_path, config_name, direction, alignment):
    # 这里是一个示例函数，假设它用于重新加载 FeatureCAM 零件
    # 实际实现可能需要调用 FeatureCAM 的 API 或者其他方法
    # 加载配置文件
    global author_value, title_value, revision_value, comments_value


    print(config_name)
    print(filename)
    print(direction,alignment)
    # 提取配置文件名（不含扩展名）
    config_base_name = os.path.splitext(os.path.basename(config_name))[0]
    app.Configurations.Import(config_name)
    doc.Open(file_path)
    active_document = app.ActiveDocument

    iPart = active_document.PartDocumentation
    comments_value =direction_dropdown.get() +"面,"+alignment_dropdown.get() +"对齐，"+material_dropdown.get() +"材质。"
    iPart.comments = comments_value
    iPart.Author = author_value
    iPart.Title = title_value
    iPart.Company = company_value
    iPart.PartNumber = scan_entry.get().strip()
    iPart.Revision = revision_value
    print(f"重新加载文件: {file_path}")
    # 加载配置文件
    iConfigs = app.Configurations
    iConfigSample = iConfigs.Item(config_base_name)
    iConfig = iConfigs.Item(filename)
    iConfig.CopyConfiguration(iConfigSample)

    # 零件外形尺寸 获取
    iSolid = active_document.Solids.Item("_001") 
    iSolid.Color=65535
    print("实体颜色：",iSolid.Color)
    print(iSolid.Name)
    maoPi=iSolid.BoundingBox() 
    print(maoPi)
    Sx,Sy,Sz = maoPi[3]-maoPi[0],maoPi[4]-maoPi[1],maoPi[5]-maoPi[2]
    print("零件外形：",Sx,Sy,Sz)
    # 加工坐标系设置
    iUcss = active_document.UCSs
    direction = direction_dropdown.get()
    alignment = alignment_dropdown.get()

    # 定义方向和对齐方式的映射
    direction_map = {
        "上": {
            "Xx": 1, "Xy": 0, "Xz": 0,
            "Yx": 0, "Yy": 1, "Yz": 0,
            "Zx": 0, "Zy": 0, "Zz": 1},
        "下": {
            "Xx": -1, "Xy": 0, "Xz": 0, 
            "Yx": 0, "Yy": 1, "Yz": 0, 
            "Zx": 0, "Zy": 0, "Zz": -1},
        "左": {
            "Xx": 0, "Xy": 0, "Xz": 1, 
            "Yx": 0, "Yy": 1, "Yz": 0, 
            "Zx": -1, "Zy": 0, "Zz": 0},
        "右": {
              "Xx": 0, "Xy": 0, "Xz": -1, 
              "Yx": 0, "Yy": 1, "Yz": 0, 
              "Zx": 1, "Zy": 0, "Zz": 0},
        "前": {
              "Xx": 1, "Xy": 0, "Xz": 0, 
              "Yx": 0, "Yy": 0, "Yz": 1, 
              "Zx": 0, "Zy": -1, "Zz": 0},
        "后": {
              "Xx": 1, "Xy": 0, "Xz": 0, 
              "Yx": 0, "Yy": 0, "Yz": -1,
              "Zx": 0, "Zy": 1, "Zz": 0},
    }

    alignment_map = {
        "上": {
            "Center": {"X": Sx/2, "Y": Sy/2, "Z": 0},
            "UR": {"X": Sx, "Y": Sy, "Z": 0},
            "UL": {"X": 0, "Y": Sy, "Z": 0},
            "LR": {"X": Sx, "Y": 0, "Z": 0},
            "LL": {"X": 0, "Y": 0, "Z": 0},
        },
        "下": {
            "Center": {"X": Sx/2, "Y": Sy/2, "Z": -Sz},
            "UR": {"X": 0, "Y": Sy, "Z": -Sz},
            "UL": {"X": Sx, "Y": Sy, "Z": -Sz},
            "LR": {"X": 0, "Y": 0, "Z": -Sz},
            "LL": {"X": Sx, "Y": 0, "Z": -Sz},
        },
        "左": {
            "Center": {"X": 0, "Y": Sy/2, "Z": -Sz/2},
            "UR": {"X": 0, "Y": Sy, "Z": 0},
            "UL": {"X": 0, "Y": Sy, "Z": -Sz},
            "LR": {"X": 0, "Y": 0, "Z": 0},
            "LL": {"X": 0, "Y": 0, "Z": -Sz},
        },
        "右": {
            "Center": {"X": Sx, "Y": Sy/2, "Z": -Sz/2},
            "UR": {"X": Sx, "Y": Sy, "Z": -Sz},
            "UL": {"X": Sx, "Y": Sy, "Z": 0},
            "LR": {"X": Sx, "Y": 0, "Z": -Sz},
            "LL": {"X": Sx, "Y": 0, "Z": 0},
        },
        "前": {
            "Center": {"X": Sx/2, "Y": 0, "Z": -Sz/2},
            "UR": {"X": Sx, "Y": 0, "Z": 0},
            "UL": {"X": 0, "Y": 0, "Z": 0},
            "LR": {"X": Sx, "Y": 0, "Z": -Sz},
            "LL": {"X": 0, "Y": 0, "Z": -Sz},
        },
        "后": {
            "Center": {"X": Sx/2, "Y": Sy, "Z": -Sz/2},
            "UR": {"X": Sx, "Y": Sy, "Z": -Sz},
            "UL": {"X": 0, "Y": Sy, "Z": -Sz},
            "LR": {"X": Sx, "Y": Sy, "Z": 0},
            "LL": {"X": 0, "Y": Sy, "Z": 0},
        },
    }

    # 获取方向和对齐方式的参数
    direction_params = direction_map.get(direction, {})
    alignment_params = alignment_map.get(direction, {}).get(alignment, {})
    # 示例：打印获取到的参数
    print("Direction Params:", direction_params)
    print("Alignment Params:", alignment_params)

    # 设置UCS
    ucs = active_document.AddUCS(
        Name=direction,
        Align=iUcss.Item(1),
        X=alignment_params["X"],
        Y=alignment_params["Y"],
        Z=alignment_params["Z"],
        Xx=direction_params["Xx"], Xy=direction_params["Xy"], Xz=direction_params["Xz"],
        Yx=direction_params["Yx"], Yy=direction_params["Yy"], Yz=direction_params["Yz"],
        Zx=direction_params["Zx"], Zy=direction_params["Zy"], Zz=direction_params["Zz"]
    )

    iUcs_set = iUcss.Item("用户坐标系_设置1")
    iUcs_set.SetLocation(alignment_params["X"], alignment_params["Y"], alignment_params["Z"])

    
    """
    # 加工坐标系设置
    iUcss = active_document.UCSs
    direction = direction_dropdown.get()
    if direction == "上":
        print("上")

        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                  Name=direction,
                  Align=iUcss.Item(1),
                  X=Sx/2, 
                  Y=Sy/2, 
                  Z=0,
                  Xx=1,Xy=0,Xz=0,
                  Yx=0,Yy=1,Yz=0,
                  Zx=0,Zy=0,Zz=1
                  )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx/2,Sy/2,0)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                  Name=direction,
                  Align=iUcss.Item(1),
                  X=Sx, 
                  Y=Sy, 
                  Z=0,
                  Xx=1,Xy=0,Xz=0,
                  Yx=0,Yy=1,Yz=0,
                  Zx=0,Zy=0,Zz=1
                  )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,0)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                  Name=direction,
                  Align=iUcss.Item(1),
                  X=0, 
                  Y=Sy, 
                  Z=0,
                  Xx=1,Xy=0,Xz=0,
                  Yx=0,Yy=1,Yz=0,
                  Zx=0,Zy=0,Zz=1
                  )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,0)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                  Name=direction,
                  Align=iUcss.Item(1),
                  X=Sx, 
                  Y=0, 
                  Z=0,
                  Xx=1,Xy=0,Xz=0,
                  Yx=0,Yy=1,Yz=0,
                  Zx=0,Zy=0,Zz=1
                  )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,0)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                  Name=direction,
                  Align=iUcss.Item(1),
                  X=0, 
                  Y=0, 
                  Z=0,
                  Xx=1,Xy=0,Xz=0,
                  Yx=0,Yy=1,Yz=0,
                  Zx=0,Zy=0,Zz=1
                  )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,0)

    elif direction == "下":
        print("下")
        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx/2, 
                    Y=Sy/2, 
                    Z=-Sz,
                    Xx=-1,Xy=0,Xz=0,
                    Yx=0,Yy=1,Yz=0,
                    Zx=0,Zy=0,Zz=-1
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx/2,Sy/2,-Sz)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=-1,Xy=0,Xz=0,
                    Yx=0,Yy=1,Yz=0,
                    Zx=0,Zy=0,Zz=-1
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,-Sz)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=-1,Xy=0,Xz=0,
                    Yx=0,Yy=1,Yz=0,
                    Zx=0,Zy=0,Zz=-1
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,-Sz)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=0, 
                    Z=-Sz,
                    Xx=-1,Xy=0,Xz=0,
                    Yx=0,Yy=1,Yz=0,
                    Zx=0,Zy=0,Zz=-1
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,-Sz)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=0, 
                    Z=-Sz,
                    Xx=-1,Xy=0,Xz=0,
                    Yx=0,Yy=1,Yz=0,
                    Zx=0,Zy=0,Zz=-1
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,-Sz)
    elif direction == "左":
        print("左")
        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy/2, 
                    Z=-Sz/2,
                    Xx=0,Xy=0,Xz=1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=-1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy/2,-Sz/2)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy, 
                    Z=0,
                    Xx=0,Xy=0,Xz=1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=-1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,0)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=0,Xy=0,Xz=1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=-1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,-Sz)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=0, 
                    Z=0,
                    Xx=0,Xy=0,Xz=1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=-1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,0)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=0, 
                    Z=-Sz,
                    Xx=0,Xy=0,Xz=1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=-1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,-Sz)
    elif direction == "右":
        print("右")
        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy/2, 
                    Z=-Sz/2,
                    Xx=0,Xy=0,Xz=-1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy/2,-Sz/2)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=0,Xy=0,Xz=-1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,-Sz)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy, 
                    Z=0,
                    Xx=0,Xy=0,Xz=-1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,0)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=0, 
                    Z=-Sz,
                    Xx=0,Xy=0,Xz=-1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,-Sz)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=0, 
                    Z=0,
                    Xx=0,Xy=0,Xz=-1,
                    Yx=0,Yy=1,Yz=0,
                    Zx=1,Zy=0,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,0)
    elif direction == "前":
        print("前")
        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx/2, 
                    Y=0, 
                    Z=-Sz/2,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=1,
                    Zx=0,Zy=-1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx/2,0,-Sz/2)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=0, 
                    Z=0,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=1,
                    Zx=0,Zy=-1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,0)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=0, 
                    Z=0,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=1,
                    Zx=0,Zy=-1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,0)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=0, 
                    Z=-Sz,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=1,
                    Zx=0,Zy=-1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,0,-Sz)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=0, 
                    Z=-Sz,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=1,
                    Zx=0,Zy=-1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,0,-Sz)
    elif direction == "后":
        print("后")
        if alignment_dropdown.get()=="Center":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx/2, 
                    Y=Sy, 
                    Z=-Sz/2,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=-1,
                    Zx=0,Zy=1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx/2,Sy,-Sz/2)
        elif alignment_dropdown.get()=="UR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=-1,
                    Zx=0,Zy=1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,-Sz)
        elif alignment_dropdown.get()=="UL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy, 
                    Z=-Sz,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=-1,
                    Zx=0,Zy=1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,-Sz)
        elif alignment_dropdown.get()=="LR":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=Sx, 
                    Y=Sy, 
                    Z=0,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=-1,
                    Zx=0,Zy=1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(Sx,Sy,0)
        elif alignment_dropdown.get()=="LL":
            ucs = active_document.AddUCS(
                    Name=direction,
                    Align=iUcss.Item(1),
                    X=0, 
                    Y=Sy, 
                    Z=0,
                    Xx=1,Xy=0,Xz=0,
                    Yx=0,Yy=0,Yz=-1,
                    Zx=0,Zy=1,Zz=0
            )
            iUcs_set =iUcss.Item("用户坐标系_设置1")
            iUcs_set.SetLocation(0,Sy,0)
    """


    print("++++++++++++++++")
    iUcss = active_document.UCSs
    for i in range(1,iUcss.Count):
        print(iUcss[i],iUcss[i].Name)
    print("++++++++++++++++")
    # 加载毛坯设置
    iUcs = active_document.UCSs.Item(direction)
    active_document.AddSetup(direction,1,55,iUcs)
    # active_document.AddSetup2(direction,1,56,iUcs,True,False)
    active_document.Setups.Item("设置1").Delete() # 删除默认设置

    # iUcs_set =iUcss.Item("用户坐标系_设置1")
    # iUcs_set.SetLocation(Sx/2,Sy/2,0)
    # print("iUcs_set.Order",iUcs_set.Order)
    iStock = active_document.Stock
    iStock.Material = material_dropdown.get()# 毛坯材料设置
    print(iStock.GetDimensions())
    # iStock.SetStockSolid((0,0,0,Sx,Sy,Sz))
    # iStock.SetStockSolid(maoPi)
    iStock.SetDimensions(1,Sx,Sy,Sz)
    iStock.SetLocation(0,0,0) 

    dimensions=iStock.GetDimensions()
    x,y,z = dimensions[1]/2,dimensions[2]/2,dimensions[3]/2
    print(x,y,z)
    # iSetup.SetMachineSimLocation(0,0,z) #机床仿真零点偏移


    print("********************************")
    # 当前设置检验
    iSetup = active_document.Setups.Item(1)
    print(iSetup.Name)
    print(iSetup.Order)
    print(iStock.Material)
    print("********************************")

    # 提取曲线几何特征
    iFaces = iSolid.Faces
    iCurvers = active_document.curves
    for i in range(1,iFaces.Count):
        icurver,_n= iCurvers.AddCurveExtractTrimLoop(iFaces[i],1,1)
        icurver.ToGeometry()
        icurver.Delete()
    active_document.SetView(7)
    # active_document.SetView(0)





# 创建主窗口
root = tk.Tk()
root.title("Fanuc NC 文件上传")

# 创建并放置标签和输入框
tk.Label(root, text="扫描枪读取的文件名:").grid(row=0, column=0, padx=10, pady=5)
scan_entry = tk.Entry(root, width=30)
scan_entry.grid(row=0, column=1, padx=10, pady=5)

# 新增 FeatureCAM 零件文件夹输入框
tk.Label(root, text="FeatureCAM 零件文件夹:").grid(row=1, column=0, padx=10, pady=5)
featurecam_folder_entry = tk.Entry(root, width=30)
featurecam_folder_entry.grid(row=1, column=1, padx=10, pady=5)
featurecam_folder_entry.insert(0, ftp_settings["default_folder"])  # 设置默认文件夹

# 新增浏览文件夹按钮
browse_button = tk.Button(root, text="_浏览文件夹_", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=5)

# 新增方向下拉框
direction_options = ["上", "下", "左", "右", "前", "后"]
direction_dropdown = tk.StringVar(root)
direction_dropdown.set(direction_options[0])  # 默认值
direction_menu = tk.OptionMenu(root, direction_dropdown, *direction_options)
direction_menu.grid(row=2, column=0, padx=10, pady=5)

# 新增对齐方式下拉框
alignment_options = ["Center", "LL", "LR", "UL", "UR"]
alignment_dropdown = tk.StringVar(root)
alignment_dropdown.set(alignment_options[0])  # 默认值
alignment_menu = tk.OptionMenu(root, alignment_dropdown, *alignment_options)
alignment_menu.grid(row=2, column=1, padx=10, pady=5)

# 新增配置文件下拉框
config_directory = ftp_settings['default_config_folder']
config_files = [f for f in os.listdir(config_directory) if f.endswith('.cdb')]
config_dropdown = tk.StringVar(root)
config_dropdown.set(config_files[0])  # 默认值
config_menu = tk.OptionMenu(root, config_dropdown, *config_files)
config_menu.grid(row=2, column=2, padx=10, pady=5)

# 新增材料下拉框
material_dropdown = tk.StringVar(root)
material_dropdown.set(ftp_settings['materials'][0])  # 默认值
material_menu = tk.OptionMenu(root, material_dropdown, *ftp_settings['materials'])
material_menu.grid(row=2, column=3, padx=10, pady=5)

# 创建并放置重新加载 FeatureCAM 零件按钮
reload_button = tk.Button(root, text="重新加载零件",  command=lambda: reload_featurecam_part(
        direction=direction_dropdown.get(),
        alignment=alignment_dropdown.get()
    ))
reload_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)




# 创建并放置发送按钮
send_button = tk.Button(root, text="发送CNC程序", command=send_program_to_machine)
send_button.grid(row=3, column=2, padx=10, pady=10)
# 全局变量
sub_window = None
comments_value =direction_dropdown.get() +"面,"+alignment_dropdown.get() +"对齐，"+material_dropdown.get() +"材质。"
author_value = "蒋小军"
title_value = "TEST"
company_value ="思路咖精机南通有限公司"
revision_value = "V0.0"

def open_sub_window():
    global sub_window, comments_value, author_value, title_value, company_value, revision_value
    if not sub_window or not sub_window.winfo_exists():
        sub_window = tk.Toplevel(root)
        sub_window.title("设置详细信息")
        sub_window.protocol("WM_DELETE_WINDOW", on_close_sub_window)

        # 创建并放置标签和输入框
        tk.Label(sub_window, text="注释:").grid(row=0, column=0, padx=10, pady=5)
        comments_entry = tk.Entry(sub_window, width=30)
        comments_entry.grid(row=0, column=1, padx=10, pady=5)
        comments_entry.insert(0, comments_value )  # 设置默认值

        tk.Label(sub_window, text="CAM程序员:").grid(row=1, column=0, padx=10, pady=5)
        author_entry = tk.Entry(sub_window, width=30)
        author_entry.grid(row=1, column=1, padx=10, pady=5)
        author_entry.insert(0, author_value )  # 设置默认值

        tk.Label(sub_window, text="标题:").grid(row=2, column=0, padx=10, pady=5)
        title_entry = tk.Entry(sub_window, width=30)
        title_entry.grid(row=2, column=1, padx=10, pady=5)
        title_entry.insert(0, title_value )  # 设置默认值

        tk.Label(sub_window, text="公司:").grid(row=3, column=0, padx=10, pady=5)
        company_entry = tk.Entry(sub_window, width=30)
        company_entry.grid(row=3, column=1, padx=10, pady=5)
        company_entry.insert(0, company_value )  # 设置默认值

        tk.Label(sub_window, text="版本:").grid(row=4, column=0, padx=10, pady=5)
        revision_entry = tk.Entry(sub_window, width=30)
        revision_entry.grid(row=4, column=1, padx=10, pady=5)
        revision_entry.insert(-1, revision_value )  # 设置默认值

        # 绑定关闭事件，保存当前输入值
        sub_window.bind("<Destroy>", on_close_sub_window)

    sub_window.deiconify()

def on_close_sub_window(event=None):
    global comments_value, author_value, title_value, company_value, revision_value
    if sub_window and sub_window.winfo_exists():
        comments_value = sub_window.children["!entry"].get()
        author_value = sub_window.children["!entry2"].get()
        title_value = sub_window.children["!entry3"].get()
        company_value = sub_window.children["!entry4"].get()
        revision_value = sub_window.children["!entry5"].get()
    sub_window.withdraw()

open_sub_window_button = tk.Button(root, text="设置详细信息", command=open_sub_window)
open_sub_window_button.grid(row=1, column=3, columnspan=3, padx=10, pady=10)

# 将焦点设置到扫描枪读取的输入框上
scan_entry.focus_set()
# # 
# 启动主循环
root.mainloop()
