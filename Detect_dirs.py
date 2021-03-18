import os,collections,json,datetime

cwd =os.path.split(__file__)[0]

os.chdir(cwd)
# print(os.getcwd())

dirname = '文件夹差异情况'
db_name = 'db.json'

source_dir_name = os.path.join(cwd,dirname)
if not os.path.exists(source_dir_name):
    os.makedirs(source_dir_name)

db_path_name = os.path.join(source_dir_name,db_name)
if not os.path.exists(db_path_name):

    f = open(db_path_name,'w')
    f.close()
#获取当前文件夹列表
cur_dirs =[]
for dir in os.listdir('./'):
    if os.path.isdir(dir):
        cur_dirs.append(dir)
# print(cur_dirs)
dirs_dict = {str(datetime.datetime.now()):cur_dirs}

dir_list = []
# 获取之前文件夹列表
with open(db_path_name,'r+') as f:
    # print(bool(f.read()))
    if os.path.getsize(db_path_name) == 0:
        print('进入为0')
        dir_list.append(dirs_dict)
        json.dump(dir_list,f)
        #此处应改为写个txt文件,注明情况
        remind_text = '第一次扫描,有个屁的差别'
        with open(os.path.join(source_dir_name,'具体情况.txt'),'a+') as f2:
            f2.write(str(datetime.datetime.now())+' '+remind_text+'\r\n')


    else:
        # print('ha')
        # print((f.read()))
        bef_db = json.load(f)
        print(bef_db)
        bef_dirs = list(bef_db[-1].values())[0]
        #比较差异
        # print(bef_dirs)
        # print(cur_dirs)

        if cur_dirs == bef_dirs:
            remind_text = '屁的差别都没有'
            with open(os.path.join(source_dir_name, '具体情况.txt'), 'a+') as f2:
                f2.write(str(datetime.datetime.now()) + ' ' + remind_text + '\r\n')


        else:
            #后有前没有,新增
            remind_text = '新增文件夹: '
            for i in cur_dirs:
                if i not in bef_dirs  :
                    remind_text = remind_text + ' ' + i
            with open(os.path.join(source_dir_name, '具体情况.txt'), 'a+') as f2:
                f2.write(str(datetime.datetime.now()) + ' ' + remind_text + '\r')
            # 更新对比数据库,原数据追加,写回去
            bef_db.append(dirs_dict)
            print(bef_db)
            f.seek(0)
            json.dump(bef_db,f)

            #前有后没有,删除
            remind_text = '删除文件夹: '
            for j in bef_dirs:

                if j not in cur_dirs  :
                    remind_text = remind_text + ' ' + j
            with open(os.path.join(source_dir_name, '具体情况.txt'), 'a+') as f2:
                f2.write(str(datetime.datetime.now()) + ' ' + remind_text + '\r\n')
            # 更新对比数据库,原数据追加,写回去
            bef_db.append(dirs_dict)
            print(bef_db)
            f.seek(0)
            json.dump(bef_db,f)

