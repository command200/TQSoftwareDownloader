# TQ Software Downloader
## 腾讯软件库和360软件库下载器

# 因为涉及读取文件代码，可能会报毒
# 此项目仅供学习和参考，代码写的很垃圾，逻辑混乱

# 推荐列表格式 
          1、格式为每行["搜索词","搜索到的第几行","软件库"], 
          2、软件库只能填腾讯和360，不能填其他。
          3、建议添加前搜索一次找到位置。
          4、请在分割线内添加，其他地方添加无效。
          -------------在下面添加--------------------
          ["QQ",3,"腾讯"],
          ["360安全卫士",1,"360"],
          ["微信",1,"腾讯"],
          ["WPS",1,"腾讯"],
          --------------在上面添加-------------------

<<<<<<< HEAD

#列表读不到ini时的默认软件
          ["QQ", 1, "腾讯"],
          ["360安全卫士", 1, "360"],
          ["微信", 1, "腾讯"],
          ["企业微信", 1, "腾讯"],
          ["WPS", 1, "腾讯"], 

#该项目有部分代码是参考https://github.com/lighterEB/SoftwareDownloader   修改
=======
#静默运行 
          ./TQSoftwareDownloader.exe -S 静默下载推荐列表，找不到ini时下载默认
          ./TQSoftwareDownloader.exe -s 静默下载推荐列表，找不到ini时不下载

#列表读不到ini时的默认软件
                           ["QQ", 1, "腾讯"],
                           ["360安全卫士", 1, "360"],
                           ["微信", 1, "腾讯"],
                           ["企业微信", 1, "腾讯"],
                           ["WPS", 1, "腾讯"], 
#该项目有部分代码是参考https://github.com/lighterEB/SoftwareDownloader    修改
>>>>>>> 1cd2391361c2b31c3f0d6586c742a754023a3195
