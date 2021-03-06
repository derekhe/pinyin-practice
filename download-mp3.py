from concurrent.futures.thread import ThreadPoolExecutor

from gtts import gTTS

all_pinyin = {'ba4': '爸', 'ma1': '妈', 'wo3': '我', 'da4': '大', 'mi3': '米', 'tu3': '土', 'de': '地', 'ma3': '马',
              'hua1': '花', 'ge1': '哥', 'di4': '弟', 'ge4': '个', 'hua4': '画', 'xia4': '下', 'xi3': '洗', 'yi1': '衣',
              'fu2': '服', 'ji1': '鸡', 'zuo4': '做', 'guo4': '过', 'le': '了', 'bu4': '不', 'le4': '乐', 'chu1': '出',
              'du2': '读', 'shu1': '书', 'qi2': '骑', 'che1': '车', 'ni3': '你', 'ta1': '他', 'shui3': '水', 'bai2': '白',
              'pi2': '皮', 'zi': '子', 'zai4': '在', 'xiao3': '小', 'ai4': '爱', 'chi1': '吃', 'yu2': '鱼', 'he2': '和',
              'niu2': '牛', 'cao3': '草', 'hao3': '好', 'jia1': '家', 'fei1': '飞', 'you3': '有', 'er2': '儿', 'ru4': '入',
              'xiao4': '校', 'shan1': '山', 'tian2': '田', 'zuo3': '左', 'pian4': '片', 'you4': '右', 'ban4': '半',
              'yun2': '云', 'lao3': '老', 'shi1': '师', 'wen2': '文', 'duo3': '朵', 'e2': '鹅', 'tiao2': '条', 'yu3': '雨',
              'tian1': '天', 'qiao2': '桥', 'qu4': '去', 'er4': '二', 'san1': '三', 'li3': '里', 'si4': '四', 'wu3': '五',
              'liu4': '六', 'qi1': '七', 'ba1': '八', 'jiu3': '九', 'shi2': '十', 'kou3': '口', 'er3': '耳', 'mu4': '目',
              'yang2': '羊', 'niao3': '鸟', 'tu4': '兔', 'ri4': '日', 'yue4': '月', 'huo3': '火', 'zhu2': '竹', 'sha1': '沙',
              'fa1': '发', 'bao4': '报', 'zhi3': '纸', 'tai2': '台', 'deng1': '灯', 'dian4': '电', 'shi4': '视', 'wan3': '晚',
              'shang4': '上', 'song4': '送', 'guo3': '果', 'ye3': '也', 'da3': '打', 'qiu2': '球', 'ba2': '拔', 'pai1': '拍',
              'tiao4': '跳', 'gao1': '高', 'pao3': '跑', 'zu2': '足', 'xiang3': '响', 'ke4': '课', 'zhen1': '真', 'shen1': '身',
              'ti3': '体', 'yuan3': '远', 'se4': '色', 'jin4': '近', 'ting1': '听', 'wu2': '无', 'sheng1': '声', 'chun1': '春',
              'hai2': '还', 'ren2': '人', 'lai2': '来', 'jing1': '惊', 'dui4': '对', 'shuo1': '说', 'ye4': '叶', 'yuan2': '圆',
              'qiu1': '秋', 'xue3': '雪', 'du4': '肚', 'jiu4': '就', 'dong1': '冬', 'pai2': '排', 'zhong1': '中', 'you2': '游',
              'liu2': '流', 'chang4': '唱', 'liang3': '两', 'an4': '岸', 'shu4': '树', 'miao2': '苗', 'lv4': '绿',
              'jiang1': '江', 'nan2': '南', 'na3': '哪', 'fang2': '房', 'piao4': '漂', 'liang4': '亮', 'qing1': '青',
              'men2': '门', 'chuang1': '窗', 'xiang1': '香', 'wu1': '屋', 'yao4': '要', 'men': '们', 'ye2': '爷', 'ke1': '棵',
              'dao4': '到', 'gei3': '给', 'chuan1': '穿', 'nuan3': '暖', 'leng3': '冷', 'kai1': '开', 'san3': '伞', 're4': '热',
              'jing4': '静', 'chuang2': '床', 'guang1': '光', 'ju3': '举', 'tou2': '头', 'wang4': '望', 'di1': '低',
              'gu4': '故', 'chuan2': '船', 'wan1': '弯', 'kan4': '看', 'jian4': '见', 'shan3': '闪', 'xing1': '星',
              'lan2': '蓝', 'xiang4': '像', 'jin1': '金', 'geng4': '更', 'mian4': '面', 'zhang3': '长', 'zao3': '早',
              'chen2': '晨', 'la1': '拉', 'shei2': '谁', 'ying3': '影', 'qian2': '前', 'hou4': '后', 'chang2': '常',
              'gen1': '跟', 'zhe': '着', 'hei1': '黑', 'gou3': '狗', 'peng2': '朋', 'bi3': '比', 'wei3': '尾', 'duan3': '短',
              'ba3': '把', 'hou2': '猴', 'song1': '松', 'shu3': '鼠', 'bian3': '扁', 'zui4': '最', 'gong1': '公', 'ya1': '鸭',
              'huang2': '黄', 'mao1': '猫', 'xing4': '杏', 'tao2': '桃', 'ping2': '苹', 'hong2': '红', 'bian1': '边',
              'duo1': '多', 'shao3': '少', 'qun2': '群', 'dui1': '堆', 'shang1': '商', 'chang3': '场', 'bao1': '包',
              'nai3': '奶', 'ya2': '牙', 'mao2': '毛', 'chi3': '尺', 'ben3': '本', 'xi1': '西', 'cai4': '菜', 'dou4': '豆',
              'jiao3': '角', 'luo2': '萝', 'bo': '卜', 'xin1': '心', 'zhuo1': '捉', 'mi2': '迷', 'cang2': '藏', 'zui3': '嘴',
              'feng1': '风', 'ming2': '明', 'xian1': '鲜', 'mie4': '灭', 'li4': '力', 'xiu1': '休', 'shou3': '手', 'lin2': '林',
              'sen1': '森', 'cong2': '从', 'zhong4': '众', 'gao4': '告', 'su4': '诉', 'lu4': '路', 'neng2': '能', 'zou3': '走',
              'bei3': '北', 'cheng2': '城', 'an1': '安', 'guang3': '广', 'dian3': '点', 'cai3': '彩', 'piao1': '飘',
              'luo4': '落', 'kong1': '空', 'wen4': '问', 'hui2': '回', 'da2': '答', 'fang1': '方', 'da1': '搭', 'jian1': '间',
              'zhe4': '这', 'xie1': '些', 'dou1': '都', 'zhu4': '住', 'ne': '呢', 'a': '啊', 'mei2': '没', 'hen3': '很',
              'zi4': '自', 'yi3': '已', 'ba': '吧', 'nin2': '您', 'dai4': '带', 'ma': '吗', 'xue2': '学', 'hui4': '会',
              'na4': '那', 'jing3': '景', 'mei3': '美', 'ci4': '次', 'gua1': '瓜', 'yan4': '燕', 'shen2': '什', 'me': '么',
              'yang4': '样', 'de2': '得', 'ke3': '可', 'zai3': '仔', 'xi4': '细', 'xian4': '现', 'zhao3': '找', 'pang2': '旁',
              'zhong3': '种', 'xu3': '许', 'ge2': '格', 'wai4': '外', 'ya': '呀', 'yan2': '言', 'la': '啦', 'yong4': '用',
              'ji3': '几', 'wa1': '蛙', 'wei4': '为', 'can1': '参', 'dong4': '洞', 'shui4': '睡', 'fang4': '放', 'xiong2': '熊',
              'kuai4': '快', 'zen3': '怎', 'fan4': '饭', 'ban1': '班', 'na2': '拿', 'zheng4': '正', 'wu4': '物', 'rang4': '让',
              'qi3': '起', 'wan2': '玩', 'wang3': '往', 'jue2': '觉', 'shao1': '烧', 'zhi1': '知', 'kan3': '砍', 'zao4': '造',
              'man3': '满', 'she3': '舍', 'jie2': '结', 'nian2': '年', 'zhi2': '直', 'gong4': '共', 'ce4': '册', 'wan4': '万',
              'fu4': '复', 'su1': '苏', 'liu3': '柳', 'bing1': '冰', 'quan2': '泉', 'ding1': '丁', 'bai3': '百', 'zheng1': '争',
              'xing3': '醒', 'lei2': '雷', 'ruan3': '软', 'shua3': '耍', 'lun4': '论', 'ti2': '题', 'di3': '底', 'sa3': '洒',
              'huan1': '欢', 'deng4': '邓', 'sui4': '岁', 'ling2': '龄', 'zhan4': '站', 'xing2': '行', 'zai1': '栽',
              'qin1': '亲', 'gu3': '古', 'mian2': '眠', 'chu4': '处', 'cun1': '村', 'ju1': '居', 'yan1': '烟', 'tong2': '童',
              'san4': '散', 'mang2': '忙', 'fang3': '访', 'ju2': '局', 'jiao4': '轿', 'dong3': '懂', 'mao4': '貌', 'mu3': '母',
              'ren4': '认', 'cuo4': '错', 'gai3': '改', 'yuan4': '愿', 'sao3': '扫', 'kua1': '夸', 'miao4': '妙', 'que4': '却',
              'sai4': '赛', 'guan1': '关', 'diao4': '掉', 'huan4': '换', 'xie3': '写', 'yin1': '音', 'dao3': '蹈',
              'pang4': '胖', 'zhang1': '张', 'gang1': '刚', 'tie1': '贴', 'qiang2': '墙', 'ti4': '替', 'tuo1': '拖',
              'xie2': '鞋', 'bang1': '帮', 'deng3': '等', 'bian4': '变', 'qing2': '情', 'zhao4': '照', 'shai4': '晒',
              'bei4': '被', 'gai4': '盖', 'shou1': '收', 'tang3': '躺', 'yan3': '眼', 'lian2': '帘', 'nv3': '女',
              'zhuang1': '装', 'qi4': '气', 'ling4': '另', 'bing4': '病', 'tai4': '太', 'lei4': '累', 'qiao1': '悄',
              'li2': '离', 'hu4': '户', 'dan4': '旦', 'pian1': '篇', 'shuang1': '霜', 'chao2': '朝', 'xia2': '霞', 'die2': '蝶',
              'bi4': '碧', 'zi3': '紫', 'qian1': '千', 'xiu4': '秀', 'qu3': '取', 'liang2': '凉', 'ding4': '定', 'bang4': '棒',
              'cong1': '聪', 'huo2': '活', 'po1': '泼', 'hu1': '忽', 'ran2': '然', 'zha3': '眨', 'ru2': '如', 'zong3': '总',
              'zhu3': '主', 'yi4': '意', 'man4': '慢', 'bi2': '鼻', 'nao3': '脑', 'guai4': '怪', 'tui1': '推', 'gan3': '赶',
              'gan4': '干', 'ji2': '级', 'wei2': '围', 'zhuan1': '专', 'zhun3': '准', 'cai2': '才', 'qing3': '请', 'she2': '舌',
              'miao3': '秒', 'chao3': '炒', 'ting2': '蜓', 'zhan3': '展', 'hu2': '蝴', 'yin3': '蚓', 'yun4': '运', 'dou3': '蚪',
              'zhu1': '蛛', 'suo3': '所', 'bu3': '捕', 'chan2': '蝉', 'chi2': '池', 'rou2': '柔', 'yao2': '摇', 'tou4': '透',
              'chi4': '翅', 'bang3': '膀', 'dun1': '蹲', 'ku1': '哭', 'pa1': '趴', 'yao1': '腰', 'pa2': '爬', 'xie4': '谢',
              'men4': '闷', 'han3': '喊', 'chong2': '虫', 'xiao1': '消', 'zhen4': '阵', 'hu3': '虎', 'jie4': '借', 'jie3': '姐',
              'ca1': '擦', 'chao1': '抄', 'shuai1': '摔', 'bo1': '拨', 'mo1': '摸', 'tuan2': '团', 'yu4': '遇', 'pa4': '怕',
              'zun1': '尊', 'chun2': '纯', 'gua4': '挂', 'jie1': '街', 'shu2': '熟', 'wen1': '温', 'lian3': '脸', 'gai1': '该',
              'ji4': '季', 'he1': '喝', 'fa3': '法', 'si1': '司', 'jia3': '假', 'bie2': '别', 'huang1': '慌', 'shi3': '使',
              'za2': '砸', 'po4': '破', 'cheng1': '称', 'tui3': '腿', 'gan1': '杆', 'cheng4': '秤', 'sou1': '艘', 'wei1': '微',
              'ai3': '矮', 'shou4': '瘦', 'chou3': '丑', 'xian2': '闲', 'hai3': '海', 'ou1': '鸥', 'tan1': '滩', 'jun1': '军',
              'fan1': '帆', 'yang1': '秧', 'tang2': '塘', 'hao4': '号', 'ling3': '领', 'xi2': '席', 'ming4': '命',
              'nian4': '念', 'wang2': '王', 'shao4': '哨', 'di2': '敌', 'dang4': '荡', 'shun4': '顺', 'tu1': '突',
              'qiang1': '枪', 'hai4': '害', 'ying1': '英', 'chong1': '冲', 'kuan1': '宽', 'xia1': '虾', 'jian3': '捡',
              'ke2': '壳', 'ben1': '奔', 'mi4': '密', 'pi3': '匹', 'lou2': '楼', 'chui1': '吹', 'he4': '贺', 'zu3': '祖',
              'guo2': '国', 'yong3': '勇', 'ju4': '句', 'xiong1': '兄', 'xu1': '虚', 'jiao1': '骄', 'ao4': '傲', 'ying2': '赢',
              'zan4': '赞', 'zhao1': '招', 'fei2': '肥', 'e4': '饿', 'tiao1': '挑', 'dan1': '担', 'zheng3': '整', 'lian4': '练',
              'gun3': '滚', 'pu1': '扑', 'yao3': '咬', 'ku3': '苦', 'lan3': '懒', 'tun1': '吞', 'kao4': '靠', 'diu1': '丢',
              'kuang4': '矿', 'zao1': '糟', 'cu1': '粗', 'bao3': '保', 'guan3': '管', 'pen2': '盆', 'xuan3': '选',
              'xuan1': '宣', 'fen1': '分', 'gui1': '规', 'sheng4': '盛', 'biao3': '表', 'bing3': '饼', 'lang2': '狼',
              'zhuan3': '转', 'han2': '寒', 'gu1': '姑', 'niang2': '娘', 'pan4': '盼', 'zhi4': '治', 'zhuo2': '啄',
              'lia3': '俩', 'zhai1': '摘', 'bo2': '伯', 'qie3': '且', 'ti1': '踢', 'jia4': '架', 'te4': '特', 'bao2': '薄',
              'qiao3': '巧', 'wen3': '稳', 'lie4': '列', 'nong4': '弄', 'cha2': '查', 'duan4': '断', 'chuang4': '创',
              'meng4': '梦', 'hui1': '灰', 'a1': '阿', 'yi2': '姨', 'zhui1': '追', 'ding3': '顶', 'pi1': '披', 'mai2': '埋',
              'chuang3': '闯', 'bai1': '掰', 'die1': '跌', 'ceng2': '层', 'jin3': '尽', 'ran3': '染', 'cui4': '翠',
              'shuang3': '爽', 'zhuang4': '壮', 'hua2': '华', 'tu2': '图', 'long2': '笼', 'lang4': '浪', 'qin2': '勤',
              'lao2': '劳', 'qu1': '区', 'pan2': '盘', 'dang1': '当', 'lv3': '旅', 'pu2': '蒲', 'jiang4': '降', 'wa2': '娃',
              'cang1': '苍', 'zha4': '炸', 'beng4': '蹦', 'can2': '残', 'fan2': '凡', 'yang3': '养', 'hang2': '航', 'mo2': '模',
              'chu2': '除', 'juan4': '倦', 'kun4': '困', 'ning2': '宁', 'leng4': '愣', 'qie4': '切', 'nao4': '闹', 'ha1': '哈',
              'qian4': '欠', 'tan4': '叹', 'hui3': '悔', 'suan4': '算', 'peng1': '怦', 'wo4': '握', 'rong2': '容', 'pu3': '普',
              'fen4': '奋', 'can4': '灿', 'lan4': '烂', 'you1': '优', 'zhou1': '州', 'min2': '民', 'qing4': '庆', 'zou4': '奏',
              'wa3': '瓦', 'kuo4': '阔', 'bei1': '碑', 'pin1': '拼', 'tan2': '坛', 'sha4': '厦', 'xun4': '讯', 'yue1': '约',
              'yong1': '拥', 'ze2': '泽', 'sheng3': '省', 'jiang3': '讲', 'pu4': '铺', 'tan3': '毯', 'yin2': '银',
              'zhang4': '仗', 'tui4': '退', 'xian3': '险', 'mai3': '买', 'mai4': '卖', 'fan3': '反', 'cun4': '寸', 'qu2': '渠',
              'xin4': '信', 'lu2': '芦', 'teng2': '藤', 'wa': '哇', 'qian3': '浅', 'ren3': '忍', 'bei': '呗', 'sui1': '虽',
              'chou1': '抽', 'xu4': '续', 'fu1': '夫', 'han4': '汗', 'zong1': '踪', 'suan1': '酸', 'chuan4': '串',
              'ying4': '硬', 'pao4': '泡', 'pao2': '袍', 'mou2': '谋', 'chai2': '柴', 'zhe2': '折', 'cuo1': '搓',
              'sheng2': '绳', 'ban3': '板', 'cao1': '糙', 're3': '惹', 'xue1': '削', 'zhou4': '皱', 'huai4': '坏', 'zha1': '扎',
              'zhua1': '抓', 'lun2': '轮', 'guan4': '惯', 'mi1': '眯', 'tie3': '铁', 'ku4': '裤', 'ao3': '袄', 'tong4': '痛',
              'hen4': '恨', 'mo4': '漠', 'pin2': '贫', 'feng4': '奉', 'ya4': '亚', 'dai1': '呆', 'cai1': '猜', 'shuan1': '拴',
              'suo1': '缩', 'xun2': '寻', 'kang1': '康', 'zuo2': '昨', 'fen3': '粉', 'liao4': '料', 'tao4': '套', 'mei4': '妹',
              'gui4': '贵', 'fei4': '费', 'zeng4': '赠', 'wang1': '汪', 'ta4': '踏', 'ken3': '肯', 'shan4': '扇', 'chou2': '愁',
              'kong3': '孔', 'leng2': '棱', 'juan3': '卷', 'shang3': '赏', 'reng1': '扔', 'kua4': '跨', 'si3': '死',
              'dao1': '叨', 'meng2': '蒙', 'nong2': '浓', 'she4': '射', 'li1': '哩', 'quan1': '圈', 'peng4': '碰',
              'tong1': '通', 'hai1': '咳', 'sou4': '嗽', 'gou1': '钩', 'pen1': '喷', 'sun1': '孙', 'rou4': '肉', 'que1': '缺',
              'fa2': '乏', 'pei2': '培', 'chan3': '产', 'kong4': '控', 'ni2': '泥', 'ci2': '词', 'heng2': '横', 'sa1': '撒',
              'chui2': '垂', 'chen4': '趁', 'ang2': '昂', 'ting3': '挺', 'qiang3': '抢', 'huai2': '怀', 'kui1': '亏',
              'duo2': '夺', 'fu3': '府', 'huan2': '环', 'rao4': '绕', 'xue4': '血', 'min3': '皿', 'quan3': '犬', 'wo1': '窝',
              'wa4': '袜', 'huan3': '缓', 'ruo4': '弱', 'duo4': '惰', 'bai4': '败', 'luan4': '乱', 'gou4': '够', 'en1': '恩',
              'pai4': '派', 'che4': '澈', 'cao2': '曹', 'cui1': '催', 'zang4': '脏', 'zuan1': '钻', 'tao3': '讨', 'cou4': '凑',
              'rao3': '扰', 'lang3': '朗', 'huo4': '或', 'qia4': '恰', 'ci3': '此', 'chan4': '颤', 'pan1': '攀', 'ru3': '乳',
              'chuan3': '喘', 'diao1': '叼', 'quan4': '劝', 'du3': '堵', 'cun2': '存', 'feng2': '逢', 'cha1': '插',
              'dun4': '顿', 'ka3': '卡', 'chu3': '础', 'cha4': '差', 'kao3': '考', 'nu3': '努', 'pei4': '佩', 'guai1': '乖',
              'reng2': '仍', 'hou3': '吼', 'duan1': '端', 'rang3': '嚷', 'hao2': '豪', 'lou3': '搂', 'geng1': '耕',
              'sang1': '桑', 'shen3': '审', 'luan3': '卵', 'zeng1': '增', 'peng3': '捧', 'dang3': '党', 'nei4': '内',
              'bin1': '宾', 'rui4': '锐', 'huang3': '晃', 'cu4': '簇', 'meng3': '猛', 'ai1': '挨', 'nen4': '嫩', 'zi1': '姿',
              'shang': '裳', 'sui2': '随', 'tao1': '涛', 'fou3': '否', 'mian3': '免', 'zhen3': '诊', 'xuan2': '旋',
              'lve4': '掠', 'tou1': '偷', 'cuan4': '窜', 'can3': '惨', 'kang4': '抗', 'lu3': '鲁', 'kuang2': '狂', 'guo1': '锅',
              'shua1': '刷', 'yin4': '印', 'sang3': '嗓', 'kun3': '捆', 'hong1': '轰', 'nu4': '怒', 'kun1': '昆', 'hen2': '痕',
              'sun3': '笋', 'beng1': '崩', 'pao1': '抛', 'zong4': '纵', 'sang4': '丧', 'niu3': '纽', 'jiu1': '纠', 'jun4': '峻',
              'tun2': '屯', 'lei3': '垒', 'qiao4': '峭', 'tong3': '桶', 'guai3': '拐', 'an3': '俺', 'zao2': '凿', 'kui4': '愧',
              'nai4': '奈', 'hun2': '浑', 'ya3': '哑', 'gao3': '稿', 'dan3': '胆', 'pi4': '辟', 'gui3': '鬼', 'gang3': '港',
              'po2': '婆', 'bi1': '逼', 'rao2': '饶', 'hun1': '昏', 'kai3': '凯', 'shuo4': '硕', 'ou3': '偶', 'bin4': '鬓',
              'liao2': '疗', 'run4': '润', 'liu1': '溜', 'ma4': '骂', 'sai1': '腮', 'hun4': '混', 'lei1': '勒', 'song3': '耸',
              'kou4': '寇', 'fei3': '匪', 'heng1': '哼', 'yun1': '晕', 'kan1': '堪', 'nie1': '捏', 'zu1': '租', 'yun3': '允',
              'zei2': '贼', 'tai1': '胎', 'zhai2': '宅', 'shen4': '慎', 'gun4': '棍', 'dai3': '逮', 'long3': '拢',
              'zhan1': '沾', 'lai4': '赖', 'lie3': '咧', 'la4': '蜡', 'mo3': '抹', 'feng3': '讽', 'zhe1': '遮', 'tuo2': '鸵',
              'tuo3': '椭', 'che3': '扯', 'piao2': '瓢', 'lou4': '漏', 'o1': '噢', 'weng1': '嗡', 'bie1': '憋', 'luan2': '峦',
              'niang4': '酿', 'fen2': '焚', 'xu2': '徐', 'nuo2': '挪', 'rong1': '茸', 'dian1': '甸', 'su2': '俗', 'man2': '馒',
              'tang1': '汤', 'biao1': '标', 'chai1': '拆', 'nao2': '挠', 'kang2': '扛', 'kui2': '葵', 'du1': '督',
              'zhai4': '寨', 'nuo4': '诺', 'po3': '颇', 'luo3': '裸', 'geng3': '梗', 'gua3': '寡', 'shao2': '勺', 'ao2': '熬',
              'chang1': '昌'}


def download(pinyin, word):
    print(word, pinyin)
    tts = gTTS(word, lang='zh-cn', slow=True)
    filename = f"{pinyin}.mp3"
    with open(f"./resource/pinyin/{filename}", 'wb') as f:
        tts.write_to_fp(f)


with ThreadPoolExecutor(max_workers=8) as exec:
    for pinyin, word in all_pinyin.items():
        exec.submit(download, pinyin, word)
