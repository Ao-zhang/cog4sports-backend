import os
# import pandas as pd
# import zipfile
import shutil
import time

_thisDir = os.getcwd()
dataDir = os.path.join(_thisDir, 'data')
outDir = os.path.join(_thisDir, 'output')


def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


create_dir_not_exist(outDir)
create_dir_not_exist(dataDir)


def del_(rootdir):
    filelist = []
    filelist = os.listdir(rootdir)  # 列出该目录下的所有文件名
    for f in filelist:
        filepath = os.path.join(rootdir, f)  # 将文件名映射成绝对路劲
        if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
            os.remove(filepath)  # 若为文件，则直接删除
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件
    shutil.rmtree(rootdir, True)


# def zipDir(dirpath, outFullName,subdir=None):
#     zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
#     for path, dirnames, filenames in os.walk(dirpath):
#         # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
#         fpath = path.replace(dirpath, '')
#
#         for filename in filenames:
#             zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
#     zip.close()

def mycopyfile(srcfile, dstpath, subdir=None):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if subdir is not None:
            dstpath = os.path.join(dstpath, subdir)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, os.path.join(dstpath, fname))  # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


def get_all_participant_sessions(admin):
    outDirName = os.path.join(outDir, admin + time.strftime("_%Y%m%d-%H:%M:%S", time.localtime()))
    for root, dirs, files in os.walk(dataDir):
        for c_test_type in dirs:
            path = os.path.join(root, c_test_type, admin)  # admin directory list
            for root1, dirs1, files1 in os.walk(path):
                for c_par in dirs1:  # dirs1代表不同的参与者
                    path1 = os.path.join(root1, c_par)  # path1代表参与者的测试记录文件夹
                    for root2, dirs2, files2 in os.walk(path1):
                        for c_test_file in files2:  # dirs2代不同的测试结果文件内容
                            path2 = os.path.join(root2, c_test_file)
                            mycopyfile(path2, outDirName, subdir=os.path.join(c_test_type, c_par))
    return outDirName


def get_all_sessions(admin, participant):
    outDirName = os.path.join(outDir, admin + "_" + participant + time.strftime("_%Y%m%d-%H:%M:%S", time.localtime()))
    for root, dirs, files in os.walk(dataDir):
        for c_test_type in dirs:
            path = os.path.join(root, c_test_type, admin)  # admin directory list
            for root1, dirs1, files1 in os.walk(path):
                for c_par in dirs1:  # dirs1代表不同的参与者
                    path1 = os.path.join(root1, c_par)  # path1代表参与者的测试记录文件夹
                    for root2, dirs2, files2 in os.walk(path1):
                        for c_test_file in files2:  # dirs2代不同的测试结果文件内容
                            path2 = os.path.join(root2, c_test_file)
                            mycopyfile(path2, outDirName, subdir=c_test_type)
    return outDirName


def get_all_results_of_one_test(test):
    outDirName = os.path.join(outDir, test + time.strftime("_%Y%m%d-%H:%M:%S", time.localtime()))
    for root, dirs, files in os.walk(os.path.join(dataDir, test)):
        for c_admin in dirs:
            path = os.path.join(root, c_admin)  # admin directory list
            for root1, dirs1, files1 in os.walk(path):
                for c_par in dirs1:  # dirs1代表不同的参与者
                    path1 = os.path.join(root1, c_par)  # path1代表参与者的测试记录文件夹
                    for root2, dirs2, files2 in os.walk(path1):
                        for c_test_file in files2:  # dirs2代不同的测试结果文件内容
                            path2 = os.path.join(root2, c_test_file)
                            mycopyfile(path2, outDirName, subdir=os.path.join(c_admin, c_par))
    return outDirName


# get_all_participant_sessions("admin")
# print(get_all_sessions("admin", 'participant'))
# get_all_results_of_one_test("flanker")
