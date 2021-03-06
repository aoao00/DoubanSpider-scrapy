# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    m_l=scrapy.Field()
        #案例页：https://movie.douban.com/subject/26266893/ 
    m_co_l=scrapy.Field() 
        #https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2545472803.jpg
    m_nam=scrapy.Field() 
        #流浪地球
    m_cat=scrapy.Field() 
        #类型: 科幻 / 灾难
    m_area=scrapy.Field() 
        #制片国家/地区：中国大陆
    m_lan=scrapy.Field() 
        #汉语普通话/英语/俄语/法语/日语/韩语/印尼语
    m_relea_tim_reg=scrapy.Field() 
        #上映日期: 2019-02-05(中国大陆)
    m_len=scrapy.Field()
        #片长: 125分钟
    m_IMDb_l=scrapy.Field()
        #IMDb链接: tt7605074 http://www.imdb.com/title/tt7605074
    m_sco=scrapy.Field()
        # 7.9
    m_elsename=scrapy.Field()
        # The Wandering Earth
    m_tag=scrapy.Field()
        #['科幻', '中国大陆', '太空', '灾难', '小说改编', '2019', '人性', '行星发动机',]
    m_sum=scrapy.Field()
        #近未来，科学家们发现太阳急速衰老膨胀，
        #短时间内包括地球在内的整个太阳系都将被太阳所吞没。
        # 为了自救，人类提出一个名为“流浪地球”的大胆计划，
        # 即倾全球之力在地球表面建造上万座发动机和转向发动机，
        # 推动地球离开太阳系，用2500年的时间奔往另外一个栖息之地。
        # 中国航天员刘培强（吴京 饰）在儿子刘启四岁那年前往国际空间站，
        # 和国际同侪肩负起领航者的重任。转眼刘启（屈楚萧 饰）长大，
        # 他带着妹妹朵朵（赵今麦 饰）偷偷跑到地表，偷开外公韩子昂（吴孟达 饰）
        # 的运输车，结果不仅遭到逮捕，还遭遇了全球发动机停摆的事件。
        # 为了修好发动机，阻止地球坠入木星，全球开始展开饱和式营救，
        # 连刘启他们的车也被强征加入。在与时间赛跑的过程中，无数的人前仆后继，
        # 奋不顾身，只为延续百代子孙生存的希望……本片根据刘慈欣的同名小说改编。
        #TODO 以下部分待处理
    m_staff_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/celebrities
    m_v_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/trailer#trailer
    m_v_trailer=scrapy.Field()
    m_v_tri=scrapy.Field()
    m_v_cmt=scrapy.Field()
    m_pic_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/all_photos
    m_pic_stills=scrapy.Field()
    m_pic_posters=scrapy.Field()
    m_awa_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/awards/
    m_awa_awa=scrapy.Field()
    m_com_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/comments?status=P
    m_com_l=scrapy.Field()
        #TODO['头像url':'https://img1.doubanio.com/icon/u1005928-127.jpg',
        #TODO '昵称':'',
        #TODO'评分':'',
        #TODO'时间':'',
        #TODO'评论':'']
    
        #!话题部分极为复杂暂时不考虑
    m_view_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/reviews
    m_dis_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/discussion/
    m_qa_l=scrapy.Field()
        #https://movie.douban.com/subject/26266893/questions/?from=subject


        #*以下是剧组成员的字段*#
    m_dir=scrapy.Field()
    m_dir_l=scrapy.Field()
    m_dir_p=scrapy.Field()
        #郭帆 Frant Gwo
        #TODO['导演':'郭帆 Frant Gwo','代表作':' 流浪地球 同桌的妳 你好，疯子！']
    m_cast=scrapy.Field()
    m_cast_l=scrapy.Field()
    m_cast_p=scrapy.Field()
        #演员 Cast
        #?定义为字典?#
        #TODO['演员':'吴京 Jing Wu','饰演':'刘培强','代表作':'流浪地球 战狼2 分手大师']
        #吴京 Jing Wu 演员 Actor (饰 刘培强) 代表作： 流浪地球 战狼2 分手大师 
    m_writer=scrapy.Field()
    m_writer_l=scrapy.Field()
    m_writer_p=scrapy.Field()
        #编剧 Writer
        #TODO['编剧:'龚格尔 Frant Gwo','职位':'编剧','代表作':' 流浪地球 同桌的妳 星游记 第一季']
    m_producer=scrapy.Field()
    m_producer_l=scrapy.Field()
    m_producer_p=scrapy.Field()
        #编剧 Writer
        #TODO['制片人:'刘慈欣 Cixin Liu','职位':'监制 Exucutive Producer','代表作':' 流浪地球 疯狂的外星人 我的三体']
    m_mus=scrapy.Field()
    m_mus_l=scrapy.Field()
    m_mus_p=scrapy.Field()
        #音乐 Music Department
        #TODO['音乐:'阿鲲 Roc Chen','职位':'原创音乐 Original Music','代表作':'流浪地球 功夫熊猫3 十二生肖']
    m_cam=scrapy.Field()
    m_cam_l=scrapy.Field()
    m_cam_p=scrapy.Field()
        #摄影 Camera Department
        #TODO['摄影 Camera Department:'刘寅 Ying Liu','职位':'摄影指导 Director of Photography','代表作':' 流浪地球']
    m_edit=scrapy.Field()
    m_edit_l=scrapy.Field()
    m_edit_p=scrapy.Field()
        #剪辑 Editorial Department
        #TODO['剪辑:'张嘉辉 Ka-fai Cheung','职位':'张嘉辉 Ka-fai Cheung','代表作':' 流浪地球 北京遇上西雅图 不能说的秘密']
    m_art=scrapy.Field()
    m_art_l=scrapy.Field()
    m_art_p=scrapy.Field()
        #音乐 Music Department
        #TODO['美术':'郜昂 Ang Gao','职位':'美术指导 Art Director','代表作':'流浪地球']
    m_cos=scrapy.Field()
    m_cos_l=scrapy.Field()
    m_cos_p=scrapy.Field()

    m_adir=scrapy.Field()
    m_adir_l=scrapy.Field()
    m_adur_p=scrapy.Field()
    
    m_sound=scrapy.Field()
    m_sound_l=scrapy.Field()
    m_sound_p=scrapy.Field()
    
    m_visul=scrapy.Field()
    m_visul_l=scrapy.Field()
    m_visul_p=scrapy.Field()
    
    m_se=scrapy.Field()
    m_se_l=scrapy.Field()
    m_se_p=scrapy.Field()
    
    m_action=scrapy.Field()
    m_action_l=scrapy.Field()
    m_action_p=scrapy.Field()
    
    m_action=scrapy.Field()
    m_action_l=scrapy.Field()
    m_action_p=scrapy.Field()
    
    

    
    pass



class Movie_reveiews_Item(scrapy.Item):
    pass

class Movie_comments_Item(scrapy.Item):
    pass

class Movie_topic_Item(scrapy.Item):
    pass

class Movie_video_Item(scrapy.Item):
    pass

class Movie_pic_Item(scrapy.Item):
    pass

class Movie_discussion_Item(scrapy.Item):
    pass

class Movie_questions_Item(scrapy.Item):
    pass