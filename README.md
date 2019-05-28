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
### 2019.05.17
#### [如何看待韩国警方不再申请李胜利拘捕令，李胜利全身而退？](https://www.zhihu.com/question/324528790)
#警方不再申请胜利拘捕令#今日, 首尔地方警察厅相关者在记者会中表示，尊重法院的判断。虽然未能拘捕#胜利#、#刘仁锡#，但调查已经接近尾声， 之后的调查也不会有问题。并表示，目前尚未仔细调查驳回拘捕令的原因，很难再次申请拘捕， 但会尽力无阻碍地履行调查机关的义务。 李胜利真的没有犯罪吗？真的如粉丝说的一样堂堂正正吗？
### 2019.05.18
### 2019.05.19
#### [如何看待大夏天校园里男生不撑伞的现象？](https://www.zhihu.com/question/324189039)

#### [有个漂亮女朋友是什么体验？](https://www.zhihu.com/question/28997505)

#### [18-19 赛季西甲末轮武磊破门西班牙人 2:0 皇家社会挺进欧联资格赛，如何评价本场武磊的表现？](https://www.zhihu.com/question/324981875)
在 8 分钟后，武磊单刀破门！打进个人生涯西甲第 3 球！西班牙人 2-0 领先！还收到 1 好消息：毕尔巴鄂还是落后 0-1！ 第 81 分钟，武磊被替换下场，结束了自己本赛季的西甲征程，他在 16 场联赛中打进 3 球并送出 1 个助攻，西班牙人在武磊加盟前只领先降级区 3 分，在武磊加盟后直接杀进了前七！ 相关问题： 西甲处子赛季 3 球 2 助攻，如何评价武磊在 18-19 赛季的表现？ 结束了西甲首个赛季的征程，如何看待武磊在下赛季西甲联赛的前景？
### 2019.05.20
#### [如何评价《权力的游戏》第八季第六集（S08E06）？](https://www.zhihu.com/question/325173949)
** 剧透预警，慎点 ** 最后一集，终于即将迎来大结局。你对这个结局是否还满意？未来的冰火世界还可能有哪些可能性？
#### [如何看待华为确认正自主研发手机操作系统替代 Android？](https://www.zhihu.com/question/304118539)
最新进展：华为确认自研操作系统：任正非推进 手机 PC 都支持 如图所示
#### [你听过哪些让你沉默震惊的真相？](https://www.zhihu.com/question/25684380)
随便说
### 2019.05.21
#### [如何看待 5 月 20 日艺人聚会王源公共场所抽烟一事？](https://www.zhihu.com/question/325344148)
进展：王源道歉 针对王源被曝 5 月 20 日在北京某餐厅与好友聚餐频频抽烟一事，5 月 21 日，北京市卫生监督所党委副书记王本进对澎湃新闻表示，朝阳区卫生监督所已派人到现场调查取证。 王本进指出，按照法律规定，在公共场所吸烟，场所不劝阻的话将遭受罚款 5000-10000 元，对于吸烟的个人一般将处罚 50 元，拒不改正的将处罚 200 元，「上次罚文章也是这样罚的。」 贾乃亮 520 饭局，王源抽烟杨超越一直吃独家: 贾乃亮 520 饭局超欢乐 王源抽烟杨超越一直吃 - 图库 - 手机搜狐
#### [你听过哪些让你沉默震惊的真相？](https://www.zhihu.com/question/25684380)
随便说
### 2019.05.22
#### [如何看待 5 月 20 日艺人聚会王源公共场所抽烟一事？](https://www.zhihu.com/question/325344148)
进展：王源道歉 针对王源被曝 5 月 20 日在北京某餐厅与好友聚餐频频抽烟一事，5 月 21 日，北京市卫生监督所党委副书记王本进对澎湃新闻表示，朝阳区卫生监督所已派人到现场调查取证。 王本进指出，按照法律规定，在公共场所吸烟，场所不劝阻的话将遭受罚款 5000-10000 元，对于吸烟的个人一般将处罚 50 元，拒不改正的将处罚 200 元，「上次罚文章也是这样罚的。」 贾乃亮 520 饭局，王源抽烟杨超越一直吃独家: 贾乃亮 520 饭局超欢乐 王源抽烟杨超越一直吃 - 图库 - 手机搜狐
### 2019.05.23
#### [英国 ARM 公司宣布停止与华为的业务，将造成多大范围的影响？](https://www.zhihu.com/question/325589578)
ARM 是芯片架构设计公司，现有的麒麟处理器就是基于 ARM 的架构授权而设计的，ARM 官方宣布停止与华为的业务，将产生多大的影响？华为是否有可替代的方案？ 在处理器设计方面，国内公司的水平如何？英国芯片设计公司 ARM 已告知员工，必须暂停和华为的业务往来。ARM 要员工停止和华为及其子公司的「所有有效合同、支持权利和任何待定合作」，以遵守最近的美国贸易禁令。在一份公司备忘录中，该公司称其设计包含「美国原产技术」，虽然 ARM 不是美国的公司，也会受到特朗普政府禁令的影响。 软银持有的芯片设计公司 ARM 将遵守美国对华为的禁令 _ 手机网易网
#### [「福岛核电站」是不是继续在泄露？](https://www.zhihu.com/question/324721418)
当年俄罗斯人 50 万人前赴后继，耗费当年的 180 亿美金，最后造了个大石棺把四号机组给罩住。日本，50 死士解决问题？ 对比切尔诺贝利，石棺的寿命也快到了，下面乌克兰要造个更大的罩外面，看样子根本不可能彻底制止，只能不停提防，估计人类灭绝了，核原料半衰期都没到。 而福岛核电站是个沿海建造，核污染直接泄露入海，造石棺罩估计得到先填海，所以看样子，是不是依旧在泄露，只是大家不说而已？ 如果不说，又是为什么全世界媒体都不说？
#### [如何面对有些父母的「你不要比吃，不要比穿，就比学习」的想法？](https://www.zhihu.com/question/324437913)
衣服磨烂了都还在穿，自己省吃俭用剩下的钱买衣服，被父母说三道四的。
### 2019.05.24
#### [如何看待水氢发动机在南阳诞生？不加油只加水的汽车有技术可能性吗？](https://www.zhihu.com/question/325786298)
是技术突破还是？浙江青年汽车氢能源整车项目落户南阳 含水氢发动机
#### [如何看待黄磊 13 岁女儿黄多多，染了一头紫发？](https://www.zhihu.com/question/325618602)

#### [如何评价《创造营 2019》节目组官宣学员王晨艺退赛？](https://www.zhihu.com/question/325877334)
尊敬的男团创始人大家好， 《创造营 2019》学员王晨艺因个人原因向节目组提出退赛，经双方坦诚沟通并达成共识，王晨艺即日起离开创造营的舞台。 在此，我们深深感谢这些日子以来，每一位学员和男团创始人付出的努力。 节目终有落幕，团训不会止步。期待每一个离开或是仍在创造营的学员，都可以永怀赤子之心，一路乘风破浪！ 《创造营 2019》节目组 2019 年 5 月 24 日 相关讨论 如何看待「大举报时代已经来临」一文？反映了哪些问题？ - 知乎如何看待「大举报时代已经来临」一文？反映了哪些问题？
### 2019.05.25
#### [为什么牛奶卖不完宁可倒掉也不免费送人？](https://www.zhihu.com/question/36274714)

#### [男生谈恋爱久了真的会腻吗？](https://www.zhihu.com/question/314691125)
我跟男朋友在一起快一年了，是异地恋，相隔两千多公里吧最开始的时候感觉他对我挺好的，也很喜欢我。他会在我难过的时候安慰我，会鼓励我不要自卑 (本人有些胖)。可是不知道为什么，从前几个月开始我感觉他对我不是那么好了。有一次我去看他，他把我惹生气了我就跑出去了，想着他应该会找我吧，结果他在酒店里睡着了。我手机也忘了带，敲门他也不开。还有每次跟我开视频的时候总是说自己困了，要睡觉了，然后我说什么他都只会回「嗯」。有时候跟他说什么他也好像没有听，每次打电话的时候动不动就要挂电话了。所以说，他这是腻了么？
### 2019.05.26
#### [传 Wi-Fi 、 SD 、 Bluetooth 联盟撤销华为的会员资格，如消息属实会对华为产生哪些影响？](https://www.zhihu.com/question/326056186)
外媒称 Wi-Fi 联盟宣布暂时撤销华为的会员资格；而华为最近不再是 SD 协会的成员；另外负责批准和认证所有蓝牙设备的 Bluetooth SIG 也很有可能会暂停华为蓝牙技术的授权。 这些基础性的设备支持如果被切断，那么将对华为产生哪些方面的影响？
### 2019.05.27
#### [《破冰行动》是以哪起真实事件改编的？具体情况是怎样的？](https://www.zhihu.com/question/323513958)
网上说是根据 12 · 29 专项行动改的，但是不大了解案件本身是什么样的~
#### [安卓一旦「抛弃」华为，华为改用自研的「鸿蒙」系统，你是否愿意尝试？](https://www.zhihu.com/question/325324112)

#### [网传微软停止与华为合作 Windows 暂停供应新订单，对华为笔记本 Windows 授权会有何影响？](https://www.zhihu.com/question/325543931)
事件背景 据《南华早报》消息，知情人士透露，在华为被列入美国黑名单、因而无法购买美国技术后，微软效仿谷歌的做法，停止接受华为的新订单。微软面向这家中国公司的服务团队已经搬出了位于深圳的总部。 该知情人士表示，华为和微软之间的两大业务领域：笔记本电脑 Windows 操作系统和其他内容相关服务都已被微软暂停，这家美国公司在遵守美国政府的限制。 界面新闻记者就此事向微软中国区方面求证，对方回应称，目前没有更多信息分享。微软停止与华为合作：Windows 暂停供应新订单
### 2019.05.28
#### [如何看待南昌红谷滩女孩子大街上被陌生人杀害事件?](https://www.zhihu.com/question/326429999)
[6 张图片]
#### [2019 年 5 月 28 日发布的红米新旗舰 K20 手机有哪些值得一提的亮点和想吐槽的方面？](https://www.zhihu.com/question/326551601)
这款 855 是否符合你的预期？与竞品相比又如何？售价方面，红米 K20 Pro 6GB+64GB 2499 元、 6GB+128GB 2599 元、 8GB+128GB 2799 元。今晚 6 点开启预约，6 月 1 日早 10 点首卖。此前参与现金预订的用户，6 月 1 日首批发货。 红米 K20 6GB+64GB 1999 元、 6GB+128GB 2099 元。今晚 6 点开启预约， 6 月 6 日早 10 点首卖 。 相关问题 2019 年 5 月 28 号下午召开的红米 K20 发布会，有哪些亮点与槽点？大家理想中的红米旗舰机是怎样的？
#### [如何看待珠穆朗玛峰大拥堵致 14 人死亡重大事件？](https://www.zhihu.com/question/326112572)
[视频]
