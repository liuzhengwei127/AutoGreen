# AutoGreen

基于Selenium爬虫的自动每天点绿github主页的python脚本

此脚本将每天自动爬取知乎上热度前三的话题写入README.md中，并通过git操作提交到远程仓库(github)

## 如何使用

### 环境要求

* python
  * selenium	`pip install selenium`
  * gitpython	`pip install gitpython`
* firefox
  * 下载[geckodriver](https://github.com/mozilla/geckodriver)驱动
* 建议放于linux云服务器上

### 使用教程

1. github上新建一个用来点绿的仓库

2. 在服务器上创建本地git仓库并将其与远端仓库（github）绑定

3. 后台运行AutoGreen.py脚本

   linux环境下	`nohup python AutoGreen.py &`



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
