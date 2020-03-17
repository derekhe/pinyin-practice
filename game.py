import glob
import os
import random

import pygame
from pygame.locals import *

import arrow

pygame.mixer.init()

pinyinfiles = list(glob.glob("./resource/pinyin/*.mp3"))

freq_pinyin = ['a', 'a1', 'a2', 'a3', 'a4', 'ai1', 'ai2', 'ai3', 'ai4', 'an1', 'an3', 'an4', 'ang2', 'ao1', 'ao2',
               'ao3', 'ao4', 'ba', 'ba1', 'ba2', 'ba3', 'ba4', 'bai1', 'bai2', 'bai3', 'bai4', 'ban1', 'ban3', 'ban4',
               'bang1', 'bang3', 'bang4', 'bao1', 'bao2', 'bao3', 'bao4', 'bei', 'bei1', 'bei3', 'bei4', 'ben1', 'ben3',
               'ben4', 'beng1', 'beng4', 'bi1', 'bi2', 'bi3', 'bi4', 'bian', 'bian1', 'bian3', 'bian4', 'biao1',
               'biao3', 'bie1', 'bie2', 'bie4', 'bin1', 'bin4', 'bing1', 'bing3', 'bing4', 'bo', 'bo1', 'bo2', 'bo3',
               'bo4', 'bu1', 'bu2', 'bu3', 'bu4', 'ca1', 'cai1', 'cai2', 'cai3', 'cai4', 'can1', 'can2', 'can3', 'can4',
               'cang1', 'cang2', 'cao1', 'cao2', 'cao3', 'cao4', 'ce4', 'cen1', 'ceng2', 'cha1', 'cha2', 'cha3', 'cha4',
               'chai1', 'chai2', 'chai4', 'chan1', 'chan2', 'chan3', 'chan4', 'chang1', 'chang2', 'chang3', 'chang4',
               'chao1', 'chao2', 'chao3', 'chao4', 'che1', 'che3', 'che4', 'chen2', 'chen3', 'chen4', 'cheng1',
               'cheng2', 'cheng3', 'cheng4', 'chi1', 'chi2', 'chi3', 'chi4', 'chong1', 'chong2', 'chong4', 'chou1',
               'chou2', 'chou3', 'chu1', 'chu2', 'chu3', 'chu4', 'chuan1', 'chuan2', 'chuan3', 'chuan4', 'chuang1',
               'chuang2', 'chuang3', 'chuang4', 'chui1', 'chui2', 'chui4', 'chun1', 'chun2', 'chun3', 'chuo4', 'ci1',
               'ci2', 'ci3', 'ci4', 'cong1', 'cong2', 'cou3', 'cou4', 'cu1', 'cu2', 'cu4', 'cuan2', 'cuan4', 'cui1',
               'cui3', 'cui4', 'cun1', 'cun2', 'cun3', 'cun4', 'cuo1', 'cuo3', 'cuo4', 'da1', 'da2', 'da3', 'da4',
               'dai1', 'dai3', 'dai4', 'dan1', 'dan3', 'dan4', 'dang1', 'dang3', 'dang4', 'dao1', 'dao2', 'dao3',
               'dao4', 'de', 'de2', 'dei3', 'deng1', 'deng3', 'deng4', 'di1', 'di2', 'di3', 'di4', 'dian1', 'dian3',
               'dian4', 'diao1', 'diao3', 'diao4', 'die1', 'die2', 'ding1', 'ding3', 'ding4', 'diu1', 'dong1', 'dong3',
               'dong4', 'dou1', 'dou3', 'dou4', 'du1', 'du2', 'du3', 'du4', 'duan1', 'duan3', 'duan4', 'dui1', 'dui4',
               'dun1', 'dun4', 'duo1', 'duo2', 'duo3', 'duo4', 'e1', 'e2', 'e3', 'e4', 'en1', 'er2', 'er3', 'er4',
               'fa1', 'fa2', 'fa3', 'fa4', 'fan1', 'fan2', 'fan3', 'fan4', 'fang1', 'fang2', 'fang3', 'fang4', 'fei1',
               'fei2', 'fei3', 'fei4', 'fen1', 'fen2', 'fen3', 'fen4', 'feng1', 'feng2', 'feng3', 'feng4', 'fo2',
               'fou1', 'fou3', 'fu1', 'fu2', 'fu3', 'fu4', 'ga1', 'ga2', 'gai1', 'gai3', 'gai4', 'gan1', 'gan3', 'gan4',
               'gang1', 'gang3', 'gang4', 'gao1', 'gao3', 'gao4', 'ge1', 'ge2', 'ge3', 'ge4', 'gei3', 'gen1', 'gen4',
               'geng1', 'geng3', 'geng4', 'gong1', 'gong3', 'gong4', 'gou1', 'gou3', 'gou4', 'gu1', 'gu2', 'gu3', 'gu4',
               'gua1', 'gua3', 'gua4', 'guai1', 'guai3', 'guai4', 'guan1', 'guan3', 'guan4', 'guang1', 'guang3',
               'guang4', 'gui1', 'gui3', 'gui4', 'gun3', 'gun4', 'guo1', 'guo2', 'guo3', 'guo4', 'ha1', 'ha2', 'ha3',
               'ha4', 'hai1', 'hai2', 'hai3', 'hai4', 'han1', 'han2', 'han3', 'han4', 'hang1', 'hang2', 'hang3',
               'hang4', 'hao2', 'hao3', 'hao4', 'he1', 'he2', 'he4', 'hei1', 'hen2', 'hen3', 'hen4', 'heng1', 'heng2',
               'heng4', 'hng', 'hong1', 'hong2', 'hong3', 'hong4', 'hou2', 'hou3', 'hou4', 'hu1', 'hu2', 'hu3', 'hu4',
               'hua1', 'hua2', 'hua4', 'huai', 'huai2', 'huai4', 'huan1', 'huan2', 'huan3', 'huan4', 'huang', 'huang1',
               'huang2', 'huang3', 'huang4', 'hui1', 'hui2', 'hui3', 'hui4', 'hun1', 'hun2', 'hun4', 'huo', 'huo1',
               'huo2', 'huo3', 'huo4', 'ji1', 'ji2', 'ji3', 'ji4', 'jia', 'jia1', 'jia2', 'jia3', 'jia4', 'jian1',
               'jian3', 'jian4', 'jiang1', 'jiang3', 'jiang4', 'jiao1', 'jiao2', 'jiao3', 'jiao4', 'jie', 'jie1',
               'jie2', 'jie3', 'jie4', 'jin1', 'jin3', 'jin4', 'jing1', 'jing3', 'jing4', 'jiu1', 'jiu3', 'jiu4', 'ju1',
               'ju2', 'ju3', 'ju4', 'juan1', 'juan3', 'juan4', 'jue2', 'jue4', 'jun1', 'jun4', 'ka3', 'kai1', 'kai3',
               'kai4', 'kan1', 'kan3', 'kan4', 'kang1', 'kang2', 'kang3', 'kang4', 'kao3', 'kao4', 'ke1', 'ke2', 'ke3',
               'ke4', 'kei1', 'ken3', 'kong1', 'kong3', 'kong4', 'kou1', 'kou3', 'kou4', 'ku1', 'ku3', 'ku4', 'kua1',
               'kua3', 'kua4', 'kuai4', 'kuan1', 'kuan3', 'kuang2', 'kuang4', 'kui1', 'kui2', 'kui3', 'kui4', 'kun1',
               'kun3', 'kun4', 'kuo4', 'la', 'la1', 'la2', 'la3', 'la4', 'lai2', 'lai4', 'lan2', 'lan3', 'lan4',
               'lang2', 'lang3', 'lang4', 'lao2', 'lao3', 'lao4', 'le', 'le4', 'lei', 'lei1', 'lei2', 'lei3', 'lei4',
               'leng1', 'leng2', 'leng3', 'leng4', 'li', 'li1', 'li2', 'li3', 'li4', 'lia3', 'lian2', 'lian3', 'lian4',
               'liang2', 'liang3', 'liang4', 'liao2', 'liao3', 'liao4', 'lie', 'lie1', 'lie2', 'lie3', 'lie4', 'lin2',
               'lin3', 'lin4', 'ling2', 'ling3', 'ling4', 'liu1', 'liu2', 'liu3', 'liu4', 'long1', 'long2', 'long3',
               'long4', 'lou1', 'lou2', 'lou3', 'lou4', 'lu2', 'lu3', 'lu4', 'luan2', 'luan3', 'luan4', 'lun2', 'lun4',
               'luo1', 'luo2', 'luo3', 'luo4', 'lv2', 'lv3', 'lv4', 'lve3', 'lve4', 'ma', 'ma1', 'ma2', 'ma3', 'ma4',
               'mai2', 'mai3', 'mai4', 'man2', 'man3', 'man4', 'mang2', 'mao1', 'mao2', 'mao4', 'me', 'mei2', 'mei3',
               'mei4', 'men', 'men1', 'men2', 'men4', 'meng1', 'meng2', 'meng3', 'meng4', 'mi1', 'mi2', 'mi3', 'mi4',
               'mian2', 'mian3', 'mian4', 'miao2', 'miao3', 'miao4', 'mie4', 'min2', 'min3', 'ming2', 'ming3', 'ming4',
               'mo1', 'mo2', 'mo3', 'mo4', 'mou2', 'mu2', 'mu3', 'mu4', 'na', 'na1', 'na2', 'na3', 'na4', 'nai2',
               'nai3', 'nai4', 'nan2', 'nan3', 'nan4', 'nao2', 'nao3', 'nao4', 'ne', 'ne2', 'ne4', 'nei3', 'nei4',
               'nen4', 'neng2', 'ni1', 'ni2', 'ni3', 'ni4', 'nian2', 'nian3', 'nian4', 'niang2', 'niang4', 'niao3',
               'nie1', 'nie4', 'nin2', 'ning2', 'ning4', 'niu2', 'niu3', 'nong2', 'nong4', 'nu2', 'nu3', 'nu4', 'nuan3',
               'nuo2', 'nuo4', 'nv3', 'nv4', 'o1', 'ou1', 'ou3', 'ou4', 'pa1', 'pa2', 'pa4', 'pai1', 'pai2', 'pai3',
               'pai4', 'pan1', 'pan2', 'pan4', 'pang1', 'pang2', 'pang3', 'pang4', 'pao1', 'pao2', 'pao3', 'pao4',
               'pei2', 'pei4', 'pen1', 'pen2', 'pen4', 'peng1', 'peng2', 'peng3', 'peng4', 'pi1', 'pi2', 'pi3', 'pi4',
               'pian1', 'pian2', 'pian4', 'piao1', 'piao2', 'piao3', 'piao4', 'pie1', 'pin1', 'pin2', 'ping2', 'po1',
               'po2', 'po3', 'po4', 'pou3', 'pu1', 'pu2', 'pu3', 'pu4', 'qi1', 'qi2', 'qi3', 'qi4', 'qia3', 'qia4',
               'qian1', 'qian2', 'qian3', 'qian4', 'qiang1', 'qiang2', 'qiang3', 'qiao1', 'qiao2', 'qiao3', 'qiao4',
               'qie1', 'qie2', 'qie3', 'qie4', 'qin1', 'qin2', 'qin3', 'qing1', 'qing2', 'qing3', 'qing4', 'qiong1',
               'qiu1', 'qiu2', 'qu1', 'qu2', 'qu3', 'qu4', 'quan1', 'quan2', 'quan3', 'quan4', 'que1', 'que4', 'qun2',
               'qun3', 'ran2', 'ran3', 'rang1', 'rang3', 'rang4', 'rao2', 'rao3', 'rao4', 're2', 're3', 're4', 'ren2',
               'ren3', 'ren4', 'reng1', 'reng2', 'reng4', 'ri4', 'rong1', 'rong2', 'rong3', 'rou2', 'rou4', 'ru2',
               'ru3', 'ru4', 'ruan3', 'rui4', 'run4', 'ruo4', 'sa1', 'sa3', 'sai1', 'sai4', 'san1', 'san3', 'san4',
               'sang1', 'sang3', 'sang4', 'sao1', 'sao3', 'sao4', 'se4', 'sen1', 'sen3', 'sha1', 'sha4', 'shai3',
               'shai4', 'shan1', 'shan3', 'shan4', 'shang', 'shang1', 'shang3', 'shang4', 'shao1', 'shao2', 'shao3',
               'shao4', 'she2', 'she3', 'she4', 'shei2', 'shen1', 'shen2', 'shen3', 'shen4', 'sheng1', 'sheng2',
               'sheng3', 'sheng4', 'shi', 'shi1', 'shi2', 'shi3', 'shi4', 'shou1', 'shou2', 'shou3', 'shou4', 'shu1',
               'shu2', 'shu3', 'shu4', 'shua1', 'shua3', 'shua4', 'shuai1', 'shuai4', 'shuan1', 'shuang1', 'shuang3',
               'shui2', 'shui3', 'shui4', 'shun3', 'shun4', 'shuo1', 'shuo4', 'si', 'si1', 'si3', 'si4', 'song1',
               'song3', 'song4', 'sou1', 'sou3', 'sou4', 'su1', 'su2', 'su4', 'suan1', 'suan4', 'sui1', 'sui2', 'sui4',
               'sun1', 'sun3', 'suo1', 'suo3', 'suo4', 'ta1', 'ta4', 'tai1', 'tai2', 'tai4', 'tan1', 'tan2', 'tan3',
               'tan4', 'tang1', 'tang2', 'tang3', 'tang4', 'tao1', 'tao2', 'tao3', 'tao4', 'te4', 'teng2', 'ti1', 'ti2',
               'ti3', 'ti4', 'tian1', 'tian2', 'tian3', 'tian4', 'tiao', 'tiao1', 'tiao2', 'tiao3', 'tiao4', 'tie1',
               'tie3', 'tie4', 'ting1', 'ting2', 'ting3', 'tong1', 'tong2', 'tong3', 'tong4', 'tou', 'tou1', 'tou2',
               'tou4', 'tu1', 'tu2', 'tu3', 'tu4', 'tuan2', 'tui1', 'tui2', 'tui3', 'tui4', 'tun1', 'tun2', 'tun3',
               'tuo1', 'tuo2', 'tuo3', 'tuo4', 'wa', 'wa1', 'wa2', 'wa3', 'wa4', 'wai4', 'wan1', 'wan2', 'wan3', 'wan4',
               'wang1', 'wang2', 'wang3', 'wang4', 'wei1', 'wei2', 'wei3', 'wei4', 'wen1', 'wen2', 'wen3', 'wen4',
               'weng1', 'weng3', 'wo1', 'wo3', 'wo4', 'wu1', 'wu2', 'wu3', 'wu4', 'xi1', 'xi2', 'xi3', 'xi4', 'xia1',
               'xia2', 'xia4', 'xian1', 'xian2', 'xian3', 'xian4', 'xiang1', 'xiang2', 'xiang3', 'xiang4', 'xiao1',
               'xiao2', 'xiao3', 'xiao4', 'xie1', 'xie2', 'xie3', 'xie4', 'xin1', 'xin2', 'xin4', 'xing1', 'xing2',
               'xing3', 'xing4', 'xiong1', 'xiong2', 'xiong4', 'xiu1', 'xiu4', 'xu1', 'xu2', 'xu3', 'xu4', 'xuan1',
               'xuan2', 'xuan3', 'xuan4', 'xue1', 'xue2', 'xue3', 'xue4', 'xun2', 'xun4', 'ya', 'ya1', 'ya2', 'ya3',
               'ya4', 'yan1', 'yan2', 'yan3', 'yan4', 'yang1', 'yang2', 'yang3', 'yang4', 'yao1', 'yao2', 'yao3',
               'yao4', 'ye2', 'ye3', 'ye4', 'yi1', 'yi2', 'yi3', 'yi4', 'yin1', 'yin2', 'yin3', 'yin4', 'ying1',
               'ying2', 'ying3', 'ying4', 'yo1', 'yong1', 'yong2', 'yong3', 'yong4', 'you1', 'you2', 'you3', 'you4',
               'yu1', 'yu2', 'yu3', 'yu4', 'yuan1', 'yuan2', 'yuan3', 'yuan4', 'yue1', 'yue2', 'yue4', 'yun1', 'yun2',
               'yun3', 'yun4', 'za1', 'za2', 'zai1', 'zai3', 'zai4', 'zan4', 'zang1', 'zang4', 'zao1', 'zao2', 'zao3',
               'zao4', 'ze2', 'ze4', 'zei2', 'zen3', 'zeng1', 'zeng4', 'zha', 'zha1', 'zha2', 'zha3', 'zha4', 'zhai1',
               'zhai2', 'zhai4', 'zhan1', 'zhan3', 'zhan4', 'zhang1', 'zhang3', 'zhang4', 'zhao1', 'zhao2', 'zhao3',
               'zhao4', 'zhe', 'zhe1', 'zhe2', 'zhe3', 'zhe4', 'zhei4', 'zhen1', 'zhen3', 'zhen4', 'zheng1', 'zheng3',
               'zheng4', 'zhi1', 'zhi2', 'zhi3', 'zhi4', 'zhong1', 'zhong3', 'zhong4', 'zhou1', 'zhou3', 'zhou4',
               'zhu1', 'zhu2', 'zhu3', 'zhu4', 'zhua1', 'zhua3', 'zhuai3', 'zhuan1', 'zhuan3', 'zhuan4', 'zhuang1',
               'zhuang4', 'zhui1', 'zhui4', 'zhun1', 'zhun3', 'zhuo1', 'zhuo2', 'zi', 'zi1', 'zi3', 'zi4', 'zong1',
               'zong3', 'zong4', 'zou1', 'zou3', 'zou4', 'zu1', 'zu2', 'zu3', 'zuan1', 'zuan4', 'zui1', 'zui3', 'zui4',
               'zun1', 'zun2', 'zuo1', 'zuo2', 'zuo3', 'zuo4']


def play_mp3(pinyinfile):
    pygame.mixer.music.load(pinyinfile)
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)


with open("score.csv", "wt") as score:
    while True:
        pinyinfile = random.choice(pinyinfiles)
        correct_answer = os.path.basename(pinyinfile).split(".")[0]

        if correct_answer not in freq_pinyin:
            continue

        while True:
            print("听音")
            play_mp3(pinyinfile)
            answer = input("答：")

            if answer.lower() == "r":
                continue

            if answer.lower() == "q":
                print("正确答案", correct_answer)
                break

            score.write(f"{arrow.now().format('YYYY-MM-DD HH:mm:ss')},{correct_answer},{answer}\n")
            score.flush()

            if answer != correct_answer:
                print("错误")
                play_mp3("./resource/incorrect.mp3")
                continue
            else:
                print("正确")
                play_mp3("./resource/correct.mp3")
                break
