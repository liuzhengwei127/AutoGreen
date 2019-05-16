# AutoGreen

基于Selenium爬虫的自动每天点绿github主页的python脚本

此脚本将每天自动爬取知乎上热度前三的话题写入README.md中，并通过git操作提交到远程仓库(github)

## 如何使用

### 环境要求

* python
  * selenium	`pip install selenium`
  * gitpython	`pip install gitpython`
  * argparse	`pip install argparse`
* firefox/chrome
  * 用firefox的话下载[geckodriver](https://github.com/mozilla/geckodriver)驱动
  * 用chrome的话下载[chromedriver](<https://blog.csdn.net/qq_41188944/article/details/79039690>)驱动
* 建议放于linux云服务器上

### 使用教程

1. github上新建一个用来点绿的仓库

2. 在服务器上创建本地git仓库并将其与远端仓库（github）绑定

3. 后台运行AutoGreen.py脚本

   linux环境下	`nohup python -u AutoGreen.py --browser chrome &`或

   `nohup python -u AutoGreen.py --browser firefox&`

   



## 建议与问题

如果有建议或者问题，欢迎在issue区提出



## 知乎每日Top3话题

### 2019.05.09

#### [有没有可能自己这一辈子都遇不到自己喜欢的那个人？](https://www.zhihu.com/question/318144086)

#### [如何评价腾讯最新手游《和平精英》？](https://www.zhihu.com/question/321337007)

随着最新一批版号的下发，腾讯的一款最新手游《和平精英》吸引了大家的视线，如何评价这款游戏呢？
#### [勇士 104:99 险胜火箭拿下赛点，杜兰特受伤水花兄弟 52 分，如何评价这场比赛？](https://www.zhihu.com/question/323597879)

本场比赛汤普森一甩往日阴霾，开局 7 投 5 中帮助勇士获得两位数领先，但火箭顽强追分，在第三节一度追平。杜兰特投篮落地右小腿扭伤离场，水花兄弟和格林越战越勇，将分差拉开到 8 分，格林六犯离场，库里强硬突破两罚都有，汤普森突破火箭包夹两分打进，比赛就此失去悬念。

### 2019.05.10

#### [如何看待《爱情公寓》电视剧开拍第五部？](https://www.zhihu.com/question/299027051)

#### [如何评价马云「工作要有 996 精神 生活上要 669」的言论？](https://www.zhihu.com/question/323764429)

5 月 10 日，马云在阿里巴巴集体婚礼上表示，身为阿里人工作上要有 996 的精神，生活上要 669，也就是 6 天 6 次关键要「久」。 马云集体婚礼 「 开车 」：工作要有 996 精神 生活上要 669 真实情况如何？报道是否属实？

#### [又漂亮又丑的长相是什么样子的？](https://www.zhihu.com/question/323389488)

### 2019.05.11

#### [勇士 118:113 险胜火箭晋级西决，库里末节 22 分哈登 32 分，如何评价这场比赛？](https://www.zhihu.com/question/323874698)

本场比赛杜兰特缺阵，库里开局状态低迷，5 投 0 中送出 2 次犯规，但汤普森手感出色，连续命中远射帮助勇士咬住分差。火箭和勇士打成胶着战，哈登进攻状态一般，保罗和汤普森互飙远射，第四节的火箭进攻受阻，被勇士打出 28-17 的攻势，库里低迷一整场后开始自我救赎，连得五分拉开分差，第四节连得 18 分一举逆转，火箭手感继续冰凉，塔克和小里弗斯两记三分续命，库里两罚全中，比赛就此失去悬念。
#### [如何评价马云「工作要有 996 精神 生活上要 669」的言论？](https://www.zhihu.com/question/323764429)

5 月 10 日，马云在阿里巴巴集体婚礼上表示，身为阿里人工作上要有 996 的精神，生活上要 669，也就是 6 天 6 次关键要「久」。 马云集体婚礼 「 开车 」：工作要有 996 精神 生活上要 669 真实情况如何？报道是否属实？

#### [在行驶的公交车上打了司机一巴掌被判 4 年，是否量刑过重？](https://www.zhihu.com/question/323741382)

前两天还有一个哈尔滨的打了公交车司机被判七年。这量刑是不是太重了？如果想要惩戒，完全可以处以巨额罚款为主，拘留教育为辅啊，做公交的也基本上不会有很有钱的人，所以巨额罚款应该足够有震慑力了啊。 如果相关法律一字没改，而判决却前后（公交车坠江）力度大不同，是否应该给民众一个解释？这在法律层面来说是不是有点儿戏，类似严打什么的？

### 2019.05.12
#### [我男朋友总是和我讲道理，明明知道我生气了他还不哄我是什么意思？](https://www.zhihu.com/question/318568532)

#### [英雄联盟 2019 MSI 小组赛 iG 16 分钟速胜 SKT 创纪录，如何评价这场比赛?](https://www.zhihu.com/question/323935018)
比赛刚开始，双方爆发一级团，泰坦被宝石晕住被盲僧击杀拿下一血，侧翼德莱文击杀琴女；前期青钢影到处游走，在下路先将盲僧血线压低，随后配合下路越塔击杀两人；青钢影复活后继续 gank，帮助中下建立优势；6 分钟，IG 直接推下下路一塔，控下水龙；12 分钟，IG 在中路释放峡谷先锋，刀妹绕后 TP 打出 2 换 2，但德莱文无人能处理，IG 在 13 分钟破下中路高地；15 分钟，SKT 下路开团反扑，同样问题是德莱文五人能处理，IG 打出 1 换 3，IG 直接平推拿下比赛。
#### [怎么才能活出春秋战国诸侯的感觉？](https://www.zhihu.com/question/315763635)
谢谢老哥帮我搞联动 联动： 怎么才能活出古罗马贵族的感觉？ 怎么能过上中世纪的贵族生活？ 怎么才能活出日本战国大名的感觉？
### 2019.05.13
#### [如何评价《权力的游戏》第八季第五集 S08E05「The Bells」?](https://www.zhihu.com/question/324121374)
第五集里有什么重要的细节方面可以讲讲吗？为最后一集做了哪些铺垫？ 前情提要： 如何评价《权力的游戏》第八季第四集 S08E04「The Last Of The Starks」 ? 如何评价《权力的游戏》第八季第三集 S08E03「The Long Night」? 如何评价《权力的游戏》第八季第二集「A Knight of the Seven Kingdoms」? 如何评价《权力的游戏》第八季第一集 S08E01「Winterfell」?
#### [你们看到过最丧的句子是什么？](https://www.zhihu.com/question/318185970)

#### [猛龙 92:90 险胜 76 人晋级东决，伦纳德 41 分绝杀，如何评价这场比赛？](https://www.zhihu.com/question/324127219)
本场比赛双方互相打铁，伦纳德 35 投 14 中，恩比德 18 投 6 中，双方比分犬牙交错，一路纠缠到最后时刻，76 人连续丢后场篮板，最后两分钟两次被防出 24 秒，伦纳德打进关键三分，洛瑞抢断助攻西亚卡姆扣篮得手，猛龙领先到 4 分，伦纳德中投不进，伊巴卡拼下前场篮板，暂停回来双方混战一团，恩比德两罚都有，伦纳德两罚中一，巴特勒快攻扳平，暂停回来伦纳德干拔压哨绝杀，猛龙 4:3 晋级东决。
### 2019.05.14
#### [如何看待江西鹰潭因订婚纠纷引发的女方被杀害一事？反映了哪些问题？](https://www.zhihu.com/question/321045968)
事件背景 江西鹰潭少女遭未婚夫虐杀，40 多万彩礼不是借的就是贷的...
#### [如何看待何猷君要向奚梦瑶求婚这件事？](https://www.zhihu.com/question/324166956)
感觉男方挺喜欢女方的吧 女方变成「豪太太」后还会走秀么
### 2019.05.15
#### [长期喝可乐的人后来都怎么样了？](https://www.zhihu.com/question/318595867)
于我个人而言，几乎不喝白开水。从小酷爱喝可乐。最近两三年，每天至少喝一个小瓶装的可乐。 想了解各位「乐友」的情况，也希望能呼吁大家，注意身体健康，少喝饮料多喝水，不能「以酒为浆」。
#### [你有什么真实的恐怖故事？](https://www.zhihu.com/question/323305666)
你身边有什么真实的恐怖故事，请讲出来，让惊悚一下…
#### [怀上双胞胎是幸还是不幸？](https://www.zhihu.com/question/319260888)

### 2019.05.16
#### [如何看待韩国警方不再申请李胜利拘捕令，李胜利全身而退？](https://www.zhihu.com/question/324528790)
#警方不再申请胜利拘捕令#今日, 首尔地方警察厅相关者在记者会中表示，尊重法院的判断。虽然未能拘捕#胜利#、#刘仁锡#，但调查已经接近尾声， 之后的调查也不会有问题。并表示，目前尚未仔细调查驳回拘捕令的原因，很难再次申请拘捕， 但会尽力无阻碍地履行调查机关的义务。 李胜利真的没有犯罪吗？真的如粉丝说的一样堂堂正正吗？
#### [你有什么真实的恐怖故事？](https://www.zhihu.com/question/323305666)
你身边有什么真实的恐怖故事，请讲出来，让惊悚一下…
#### [自律就是在压抑自己的欲望吗？](https://www.zhihu.com/question/22347972)
两个问题： 1 、自律是每个人所应该培养的一种优秀的品质，可自律就必须压抑自己的欲望吗？ 2 、心理学说心理疾病来源于对欲望的过分压抑，严格的自律会不会引起心理疾病？ 求大神解答
