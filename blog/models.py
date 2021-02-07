from django.db import models

# Create your models here.


class Article(models.Model):# 继承models.Model
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)  # 自增，主键
    # 文章标题
    title = models.TextField() # 文本类型
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True) # 如果没有指定的发布日期，默认是当前日期

    # objects = models.Manager()
    """
    以上是模型的定义
    需要模型的迁移把它保存到数据库里面:
    python manage.py makemigrations 把模型的变更生成迁移文件 
    
    python manage.py migrate 运行迁移文件，把迁移文件的内容同步到数据库里面
    
    """