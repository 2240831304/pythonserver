# #encoding:utf-8
# '''
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML。
# '''
# from xml.dom.minidom import Document
# doc = Document()  #创建DOM文档对象
# DOCUMENT = doc.createElement('DOCUMENT') #创建根元素
# DOCUMENT.setAttribute('content_method',"full")#设置命名空间
# #DOCUMENT.setAttribute('xsi:noNamespaceSchemaLocation','DOCUMENT.xsd')#引用本地XML Schema
# doc.appendChild(DOCUMENT)
# ############item:Python处理XML之Minidom################
# item = doc.createElement('item')
# #item.setAttribute('genre','XML')
# DOCUMENT.appendChild(item)
# key = doc.createElement('key')
#
# key_text = doc.createTextNode('Key1') #元素内容写入
# key.appendChild(key_text)
# item.appendChild(key)
# display = doc.createElement('display')
# item.appendChild(display)
# display_url = doc.createElement('url')
# display_title  = doc.createElement('title')
# display_url_text = doc.createTextNode('https://baidu.com/')
# display_title_text  = doc.createTextNode('北京市公积金咨询电话')
# display.appendChild(display_url)
# display.appendChild(display_title)
# display_url.appendChild(display_url_text)
# display_title.appendChild(display_title_text)
# item.appendChild(display)
# '''
# price = doc.createElement('price')
# price_text = doc.createTextNode('28')
# price.appendChild(price_text)
# item.appendChild(price)
# '''
# ########### 将DOM对象doc写入文件
# f = open('../templates/tell.xml','w')
# #f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
# doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
# f.close()


# import ConfigParser
# cf = ConfigParser.ConfigParser()
#
# cf.read('../conf/app_id.conf')
# # section = cf.get('keyword','type')
# # print(type(section))
# # section = section.split(',')
# # print(type(section))
# # print(section)
# # str = 'vip'
# # for s in section:
# #     a = cf.get('keyword',s)
# #     print('a:%s'%a)
# #     # print(type(a))
# #     if a.find(str) != -1:
# #         type = cf.get(s,'type')
# #         if type == 'news':
# #             title = cf.get(s, 'title')
# #             description = cf.get(s, 'description')
# #             picurl = cf.get(s, 'picurl')
# #             url = cf.get(s, 'url')
# #
# #
# #
# #
# #         elif type =='text':
# #             content = cf.get(s,'content')
# #             print('这下面是%s'%s)
# #             print('content:%s'%content)
# #
# #         else:
# #             pass
# #     else:
# #         print('***********')
#
# value = cf.get('app','app_secret')
# # value=cf.get('db','today')
# print(value)


import sys
import time
import fcntl
import multiprocessing
lock = multiprocessing.Lock()
import random
import ConfigParser

class FLOCK(object):

    def __init__(self):
        pass

    def lock(self,txtFile):

        # update_time = time.time()
        try:
            # with open(txtFile, 'w') as f:
                f = open(txtFile)
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 加锁
                cc = ConfigParser.ConfigParser()
                cc.read(txtFile)
                # # token_value = cc.get('token', 'token_access_token')
                today_value = cc.get('db', 'today')
                expires_in_value = cc.get('db', 'expires_in')
                if (time.time() - float(today_value) > int(expires_in_value)):
                    update_time = time.time()
                    name = random.randint(0,10**10)
                    # f.write("write from {0} \r\n".format(update_time))
                    cc.set('db','today',update_time)
                    # cc.set('db','name',name)

                    # print('update_time:%s'%update_time)
                    # print('name:%s'%name)
                    cc.write(open("../conf/test.conf", "w"))
                    # print "{0} acquire lock".format(id)
                    print(cc.get('db','today'))
                    time.sleep(5)
                    return
                else:
                    print('还没过期')
                    print(cc.get('db','today'))
            # 在with块外，文件关闭，自动解锁
            # print "{0} exit".format(id)

        except Exception as e:
            print('文件当前被加锁，请等到锁释放')
# def unlock(self):
#     self.fobj.close()
#     print '已解锁'

if __name__ == "__main__":
    # print sys.argv[1]
    locker = FLOCK()
    locker.lock('../conf/test.conf')
