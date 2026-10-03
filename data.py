# -*- coding: utf-8 -*-
# 美食攻略数据：城市 → 菜系 → 菜品 → 推荐店。生成 index.html 用。
CITIES = [
 {
  "id": "perth", "name": "Perth 珀斯", "short": "Perth",
  "intro": "选店规则：英文侧看 WA Good Food Guide、Broadsheet、Perth is OK 等榜单，中文侧看小红书真实探店和评论区。两边都认的排前面；只有一边有口碑的会明确标出来。",
  "checked": "资料核对于 2026 年 10 月",
  "groups": [
   {
    "id": "sea", "name": "东南亚菜",
    "note": "一个小发现：Victoria Park 的 Albany Highway 是东南亚菜一条街，下面的肉骨茶和印尼炸鸡饭有五家都在这条路上，可以一次逛完。",
    "dishes": [
     {
      "id": "bkt", "name": "肉骨茶", "en": "Bak Kut Teh",
      "lead": "要药材味重的，就找马来西亚巴生（Klang）派：汤色深、当归和药材香浓。新加坡是胡椒派，汤清、白胡椒辣，不是一回事。",
      "warn": "英文榜单都没有单独收录肉骨茶，下面两家只有华人口碑，没有英文榜单背书。",
      "picks": [
       {
        "name": "Kee Hiong Klang Bak Kut Teh", "zh": "奇香巴生肉骨茶",
        "area": "Victoria Park", "addr": "4/393 Albany Hwy, Victoria Park WA 6100",
        "hours": "每天 11:00–14:30、17:30–20:30（各平台略有出入，去前确认）",
        "en_ok": False, "en_note": "英文榜单未收录",
        "xhs_ok": True, "xhs_note": "华人好评，巴生本地人认证",
        "why": ["巴生老字号奇香肉骨茶的珀斯店，走的就是药材派。",
                "小红书上有巴生人留言：这个味道真的是家里的味道；探店说汤味超浓、肉很多。"],
        "order": "肉骨茶（2–3 人份），不吃内脏跟柜台说；另外点干锅肉骨茶。",
        "tip": "老帖里的地址是 800 Albany Hwy，现在搬到了 393 号。"
       },
       {
        "name": "Yum Yum Tree", "zh": "原 Lepak Kopitiam Vic Park",
        "area": "Victoria Park", "addr": "319 Albany Hwy, Victoria Park WA 6100", "phone": "+61431391119",
        "hours": "周一、三至六 9:00–14:00、17:00–20:00；周日 9:00–14:00；周二休",
        "en_ok": False, "en_note": "英文榜单未收录",
        "xhs_ok": True, "xhs_note": "华人好评为主，也有嫌腻、嫌贵",
        "why": ["小红书高赞帖：肉骨茶一端上桌就飘来很浓的药膳味，汤头偏甘甜，越喝越上头。",
                "评论区有人说在珀斯算顶流，但有点腻；也有人嫌价格偏高。"],
        "order": "肉骨茶；顺便试猪脚姜和煎蕊。",
        "tip": "周二不开门，周日只有中午。"
       }
      ],
      "avoid": "不推荐：Crown 酒店 Silks 的新加坡白胡椒肉骨茶，有华人探店说只尝到白胡椒、没有肉骨茶味，价格还高。"
     },
     {
      "id": "krapao", "name": "泰式打抛", "en": "Pad Kra Pao",
      "lead": "打抛是罗勒炒肉碎盖饭，好吃的标准是罗勒香、锅气足、敢放辣，再加一个溏心煎蛋。",
      "picks": [
       {
        "name": "Thailicious", "zh": "Perth Thailicious Restaurant",
        "area": "Northbridge", "addr": "7/160 James St, Northbridge WA 6003", "phone": "+61893285403",
        "hours": "每天 11:30–21:30",
        "en_ok": False, "en_note": "未进英文榜单，但点评网站 4.4 分、两千多条评价",
        "xhs_ok": True, "xhs_note": "小红书打抛帖最多的一家",
        "why": ["小红书专门写它打抛的帖子最多：打抛猪真的离不开、必回访的半熟蛋打抛猪饭、泰国朋友推荐。",
                "近 1000 赞的珀斯前十必吃榜也有它：打抛猪、猪颈肉、绿咖喱、泰奶，口味重、超敢放辣。"],
        "order": "打抛猪饭加煎蛋，辣度直接说要泰辣。",
        "tip": "2012 年开到现在，泰国人也常去。服务时好时坏。"
       },
       {
        "name": "Rym Tarng", "zh": "",
        "area": "Bicton（近 Fremantle）", "addr": "Shop 8, 258 Canning Hwy, Bicton WA 6157", "phone": "+61862465789",
        "hours": "周三至周日 11:30–15:00、17:00–20:30；周一、二休",
        "en_ok": True, "en_note": "WA Good Food Guide 2026 Top 100，泰餐榜点名它的打抛猪",
        "xhs_ok": True, "xhs_note": "小红书探店标题都是好评",
        "why": ["主厨出自 Long Chim、Wildflower、Hearth，英文榜单两边都认可。",
                "WA Good Food Guide 的泰餐榜直接点名它的打抛猪，罗勒香很足。"],
        "order": "打抛猪（pad ka pao pork）；招牌还有炭烤猪颈肉、虾肉饼。",
        "tip": "只有 16 个位，官网 rymtarng.com 订位。"
       },
       {
        "name": "Bangkok Brothers", "zh": "",
        "area": "Northbridge", "addr": "91 James St, Northbridge WA 6003", "phone": "+61404371667",
        "hours": "周一至四 11:00–15:00、17:00–21:00；周五到 22:00；周六 16:30 起开到凌晨 2:00；周日 11:30–15:00、16:30–21:00",
        "en_ok": True, "en_note": "WA Good Food Guide 泰餐榜收录，点名脆皮猪打抛",
        "xhs_ok": None, "xhs_note": "以前评价很高，近期有差评",
        "why": ["小红书 2023 年的帖子称它珀斯泰国菜天花板，牛肉打抛饭和在泰国吃的一样，可以选辣度。",
                "2025 年 9 月有评论说海鲜不新鲜，原帖作者回复可能换了厨师。"],
        "order": "脆皮猪打抛（graprao moo grob）或牛肉打抛。",
        "tip": "外卖常送错，建议堂食。份量大，适合人多。"
       }
      ],
      "aside": "南下顺路：Busselton 的 Thai Lemongrass 在小红书上被称为全西澳最好吃的泰餐，打抛和脆皮五花肉炒空心菜都必点，常客满要预约。离 Perth 开车约两个半小时，只适合去南边玩时顺路。"
     },
     {
      "id": "pho", "name": "越南河粉", "en": "Phở",
      "lead": "先降低预期：小红书上有位吃遍越南和东澳的河粉爱好者，整体评价珀斯的河粉不太行。下面是两边口碑里相对最稳的。",
      "picks": [
       {
        "name": "Pho Thanh Dat", "zh": "Thanh Dat Vietnamese Noodle House",
        "area": "Northbridge", "addr": "425 William St, Northbridge WA 6003（Robinson Ave 路口）", "phone": "+61892289988",
        "hours": "周一、二、四、五 11:00–15:00、17:30–20:00；周六、日 11:00–20:00；周三休",
        "en_ok": True, "en_note": "Perth is OK 越南菜榜单收录",
        "xhs_ok": True, "xhs_note": "华人口碑最集中",
        "why": ["Perth is OK 点名它的牛肋排河粉和 Pho the Lot（全料河粉）。",
                "小红书评论区反复出现永远的神，最近还有人说比旁边的越华和 Trang 好吃多了；也有人说份量缩水了。"],
        "order": "牛肋排河粉，或者全料的 Pho the Lot。",
        "tip": "周三不开门。"
       },
       {
        "name": "Sup So Good", "zh": "",
        "area": "Northbridge", "addr": "3/297 William St, Northbridge WA 6003", "phone": "+61892289917",
        "hours": "周二至四 11:30–20:30；周五至日 11:30–21:30；周一休",
        "en_ok": True, "en_note": "Broadsheet 收录",
        "xhs_ok": None, "xhs_note": "石锅版好评，普通版一般",
        "why": ["招牌是石锅牛肋排河粉，石锅端上来汤还在冒泡，Broadsheet 专门介绍过。",
                "小红书：石锅版值得试，普通版一般；也有人嫌汤蒜味重、粉煮得太软。"],
        "order": "只点石锅牛肋排河粉。",
        "tip": "周一不开门。"
       }
      ],
      "aside": "关于 Trang's Cafe & Noodle House（Girrawheen 越南区）：小红书上曾被称为全珀斯汤最好喝的河粉，Perth is OK 也收录过。但 2026 年初有好几条评论说去了两次都关门、疑似永久停业，去之前务必先打电话确认：(08) 9247 3880。"
     },
     {
      "id": "ayam", "name": "印尼炸鸡饭", "en": "Ayam Penyet / Ayam Geprek",
      "lead": "印尼炸鸡饭有两种：Ayam Penyet 是炸鸡压扁配参巴辣酱，Ayam Geprek 是炸鸡用锤子捶碎再淋酱。",
      "warn": "说实话，这道菜没有一家是英文榜单和小红书都明确夸鸡本身的，下面按各自的长处排，你自己挑。",
      "picks": [
       {
        "name": "Batavia Corner", "zh": "",
        "area": "East Victoria Park", "addr": "3/912 Albany Hwy, East Victoria Park WA 6101",
        "hours": "每天 11:00–21:00",
        "en_ok": True, "en_note": "Perth is OK 印尼菜榜单收录",
        "xhs_ok": False, "xhs_note": "小红书讨论很少",
        "why": ["1998 年开到现在的家族老店，Perth is OK 形容它的 ayam penyet 炸得非常酥，烤牛排骨是传奇级。",
                "小红书只找到一条简短好评，说味道很正宗。"],
        "order": "Ayam penyet；加一份烤牛排骨（iga bakar）。",
        "tip": ""
       },
       {
        "name": "Ria Ayam Penyet", "zh": "",
        "area": "Victoria Park", "addr": "417 Albany Hwy, Victoria Park WA 6100", "phone": "+61865073901",
        "hours": "每天 11:00–21:00",
        "en_ok": True, "en_note": "Perth is OK 印尼菜榜单收录",
        "xhs_ok": None, "xhs_note": "炸鸡评价一般，烤牛排骨和珍多冰被夸",
        "why": ["印尼起家的连锁店，Perth is OK 说它的 ayam penyet 最接近印尼本地的味道。",
                "小红书对炸鸡本身多是中规中矩；2026 年有印尼同学力荐，说配的参巴虾酱辣椒很好吃。最被夸的是烤牛排骨和珍多冰。"],
        "order": "Ayam penyet 配参巴虾酱；必加烤牛排骨（iga bakar）和珍多冰（es cendol）。",
        "tip": "米饭要另点，辣椒酱很辣，可以选辣度。Kardinya 有分店。"
       },
       {
        "name": "Geprek in Perth", "zh": "印尼捶打炸鸡",
        "area": "Victoria Park", "addr": "393 Albany Hwy, Victoria Park WA 6100",
        "hours": "每天 11:00–20:00",
        "en_ok": False, "en_note": "2025 年 10 月新开，英文榜单还没收录",
        "xhs_ok": True, "xhs_note": "好评为主，也有嫌咸",
        "why": ["小红书好几篇探店：炸鸡捶碎淋酱，参巴辣椒很下饭；最受欢迎的是咸蛋黄酱和明太子松露；套餐配的茶被夸很香，有人一周去三次。",
                "也有评论说太咸、不好吃。"],
        "order": "Geprek sambalado，或者咸蛋黄酱口味，点含茶的套餐。",
        "tip": "饭点要排队，开门就去基本不用等。"
       }
      ]
     }
    ]
   }
  ]
 }
]
SOURCES = [
 ("WA Good Food Guide 2026 Top 100", "https://wagoodfoodguide.com/top-100/"),
 ("WA Good Food Guide：Perth 最好的泰餐", "https://wagoodfoodguide.com/best-thai-restaurants-perth/"),
 ("Broadsheet：Perth 七家最好的泰餐", "https://www.broadsheet.com.au/perth/food-and-drink/article/seven-spicy-contenders-title-best-thai-restaurant-perth"),
 ("Broadsheet：Sup So Good", "https://www.broadsheet.com.au/perth/northbridge/restaurants/sup-so-good"),
 ("Perth is OK：最好的越南菜", "https://perthisok.com/eat-drink/best-vietnamese-restaurant-perth/"),
 ("Perth is OK：最好的印尼菜", "https://perthisok.com/eat-drink/best-indonesian-restaurants-perth/"),
]
