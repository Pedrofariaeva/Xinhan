#!/usr/bin/env python3
"""Generate a progressive HSK 1–6 trial-lesson cycle."""
import os

LESSONS = [
    {
        'id': 'hsk-1',
        'titleZh': '你好！',
        'titlePy': 'Nǐ hǎo!',
        'titleEn': 'Hello!',
        'subtitle': 'Greetings & Self-introduction',
        'level': 'HSK 1',
        'theme': '#d8f3dc',
        'accent': '#2d6a4f',
        'icon': '👋',
        'desc': 'HSK 1 words only: greet people, say your name, and say goodbye.',
        'vocab': [
            ('你好', 'nǐ hǎo', 'hello'),
            ('我', 'wǒ', 'I / me'),
            ('叫', 'jiào', 'to be called'),
            ('什么', 'shénme', 'what'),
            ('名字', 'míngzi', 'name'),
            ('很高兴', 'hěn gāoxìng', 'very glad'),
            ('认识', 'rènshi', 'to know / meet'),
            ('你', 'nǐ', 'you'),
            ('再见', 'zàijiàn', 'goodbye'),
            ('谢谢', 'xièxie', 'thank you'),
        ],
        'grammar': [
            {
                'title': 'A 叫 B · A is called B',
                'zh': '我 叫 李明。',
                'py': 'Wǒ jiào Lǐ Míng.',
                'en': 'My name is Li Ming.',
            },
            {
                'title': '很高兴认识你 · Glad to meet you',
                'zh': '很高兴认识你。',
                'py': 'Hěn gāoxìng rènshi nǐ.',
                'en': 'Glad to meet you.',
            },
        ],
        'examples': [
            ('你好！我叫李明。', 'Nǐ hǎo! Wǒ jiào Lǐ Míng.', 'Hello! My name is Li Ming.'),
            ('你叫什么名字？', 'Nǐ jiào shénme míngzi?', 'What is your name?'),
            ('很高兴认识你。', 'Hěn gāoxìng rènshi nǐ.', 'Glad to meet you.'),
            ('再见！谢谢！', 'Zàijiàn! Xièxie!', 'Goodbye! Thank you!'),
        ],
        'quiz': {
            'group-1': [
                {'q': "'hello' 用中文怎么说？<span class=\"py\">How do you say 'hello'?</span>", 'answers': '你好|nǐ hǎo|ni hao', 'reveal': '你好 <span class=\"py\">nǐ hǎo · hello</span>', 'placeholder': '你好...'},
                {'q': "'I / me' 用中文怎么说？<span class=\"py\">How do you say 'I / me'?</span>", 'answers': '我|wǒ|wo', 'reveal': '我 <span class=\"py\">wǒ · I / me</span>', 'placeholder': '我...'},
                {'q': "'name' 用中文怎么说？<span class=\"py\">How do you say 'name'?</span>", 'answers': '名字|míngzi|ming zi|mingzi', 'reveal': '名字 <span class=\"py\">míngzi · name</span>', 'placeholder': '名字...'},
            ],
            'group-2': [
                {'q': "我____李明。 <span class=\"py\">Wǒ ___ Lǐ Míng.</span>", 'answers': '叫|jiào|jiao', 'reveal': '叫 <span class=\"py\">jiào · to be called</span>', 'placeholder': '叫...'},
                {'q': "你叫什么____？ <span class=\"py\">Nǐ jiào shénme ___?</span>", 'answers': '名字|míngzi|mingzi', 'reveal': '名字 <span class=\"py\">míngzi · name</span>', 'placeholder': '名字...'},
                {'q': "很高兴____你。 <span class=\"py\">Hěn gāoxìng ___ nǐ.</span>", 'answers': '认识|rènshi|ren shi|renshi', 'reveal': '认识 <span class=\"py\">rènshi · to know / meet</span>', 'placeholder': '认识...'},
            ],
            'final': [
                {'q': "'thank you' 用中文怎么说？<span class=\"py\">How do you say 'thank you'?</span>", 'answers': '谢谢|xièxie|xie xie|xiexie', 'reveal': '谢谢 <span class=\"py\">xièxie · thank you</span>', 'placeholder': '谢谢...'},
                {'q': "'goodbye' 用中文怎么说？<span class=\"py\">How do you say 'goodbye'?</span>", 'answers': '再见|zàijiàn|zai jian|zaijian', 'reveal': '再见 <span class=\"py\">zàijiàn · goodbye</span>', 'placeholder': '再见...'},
                {'q': "'what' 用中文怎么说？<span class=\"py\">How do you say 'what'?</span>", 'answers': '什么|shénme|shen me|shenme', 'reveal': '什么 <span class=\"py\">shénme · what</span>', 'placeholder': '什么...'},
                {'q': "'you' 用中文怎么说？<span class=\"py\">How do you say 'you'?</span>", 'answers': '你|nǐ|ni', 'reveal': '你 <span class=\"py\">nǐ · you</span>', 'placeholder': '你...'},
            ],
        },
    },
    {
        'id': 'hsk-2',
        'titleZh': '我要一杯咖啡',
        'titlePy': 'Wǒ yào yì bēi kāfēi',
        'titleEn': 'I Want a Cup of Coffee',
        'subtitle': 'Ordering Food & Drink',
        'level': 'HSK 2',
        'theme': '#fff5eb',
        'accent': '#c05621',
        'icon': '☕',
        'desc': 'HSK 2 words: order drinks, ask for things, and pay.',
        'vocab': [
            ('要', 'yào', 'to want'),
            ('杯', 'bēi', 'cup / glass'),
            ('咖啡', 'kāfēi', 'coffee'),
            ('茶', 'chá', 'tea'),
            ('水', 'shuǐ', 'water'),
            ('吃', 'chī', 'to eat'),
            ('饭', 'fàn', 'rice / meal'),
            ('想', 'xiǎng', 'to want / would like'),
            ('多少钱', 'duōshao qián', 'how much'),
            ('块', 'kuài', 'measure word for money'),
        ],
        'grammar': [
            {
                'title': '我要 + number + measure + noun',
                'zh': '我要一杯咖啡。',
                'py': 'Wǒ yào yì bēi kāfēi.',
                'en': 'I want a cup of coffee.',
            },
            {
                'title': '多少钱？ · How much?',
                'zh': '这个多少钱？',
                'py': 'Zhège duōshao qián?',
                'en': 'How much is this?',
            },
        ],
        'examples': [
            ('我要一杯咖啡。', 'Wǒ yào yì bēi kāfēi.', 'I want a cup of coffee.'),
            ('你想吃什么？', 'Nǐ xiǎng chī shénme?', 'What would you like to eat?'),
            ('我要一杯茶。', 'Wǒ yào yì bēi chá.', 'I want a cup of tea.'),
            ('多少钱？', 'Duōshao qián?', 'How much is it?'),
        ],
        'quiz': {
            'group-1': [
                {'q': "'coffee' 用中文怎么说？<span class=\"py\">How do you say 'coffee'?</span>", 'answers': '咖啡|kāfēi|ka fei|kafei', 'reveal': '咖啡 <span class=\"py\">kāfēi · coffee</span>', 'placeholder': '咖啡...'},
                {'q': "'tea' 用中文怎么说？<span class=\"py\">How do you say 'tea'?</span>", 'answers': '茶|chá|cha', 'reveal': '茶 <span class=\"py\">chá · tea</span>', 'placeholder': '茶...'},
                {'q': "'to want' 用中文怎么说？<span class=\"py\">How do you say 'to want'?</span>", 'answers': '要|yào|yao|想|xiǎng|xiang', 'reveal': '要 / 想 <span class=\"py\">yào / xiǎng · to want</span>', 'placeholder': '要/想...'},
            ],
            'group-2': [
                {'q': "我____一杯咖啡。 <span class=\"py\">Wǒ ___ yì bēi kāfēi.</span>", 'answers': '要|yào|yao|想|xiǎng|xiang', 'reveal': '要 / 想 <span class=\"py\">yào / xiǎng · want</span>', 'placeholder': '要...'},
                {'q': "你____吃什么？ <span class=\"py\">Nǐ ___ chī shénme?</span>", 'answers': '想|xiǎng|xiang', 'reveal': '想 <span class=\"py\">xiǎng · would like</span>', 'placeholder': '想...'},
                {'q': "这个____钱？ <span class=\"py\">Zhège ___ qián?</span>", 'answers': '多少|duōshao|duo shao|duoshao', 'reveal': '多少 <span class=\"py\">duōshao · how much</span>', 'placeholder': '多少...'},
            ],
            'final': [
                {'q': "'cup / glass' 用中文怎么说？<span class=\"py\">How do you say 'cup / glass'?</span>", 'answers': '杯|bēi|bei', 'reveal': '杯 <span class=\"py\">bēi · cup / glass</span>', 'placeholder': '杯...'},
                {'q': "'water' 用中文怎么说？<span class=\"py\">How do you say 'water'?</span>", 'answers': '水|shuǐ|shui', 'reveal': '水 <span class=\"py\">shuǐ · water</span>', 'placeholder': '水...'},
                {'q': "'to eat' 用中文怎么说？<span class=\"py\">How do you say 'to eat'?</span>", 'answers': '吃|chī|chi', 'reveal': '吃 <span class=\"py\">chī · to eat</span>', 'placeholder': '吃...'},
                {'q': "'rice / meal' 用中文怎么说？<span class=\"py\">How do you say 'rice / meal'?</span>", 'answers': '饭|fàn|fan', 'reveal': '饭 <span class=\"py\">fàn · rice / meal</span>', 'placeholder': '饭...'},
            ],
        },
    },
    {
        'id': 'hsk-3',
        'titleZh': '你的爱好是什么？',
        'titlePy': 'Nǐ de àihào shì shénme?',
        'titleEn': 'What Are Your Hobbies?',
        'subtitle': 'Hobbies & Weekend Plans',
        'level': 'HSK 3',
        'theme': '#e8f4fd',
        'accent': '#1d5f8a',
        'icon': '🎸',
        'desc': 'HSK 3 words: talk about hobbies, weekends, and making plans.',
        'vocab': [
            ('爱好', 'àihào', 'hobby'),
            ('喜欢', 'xǐhuan', 'to like'),
            ('运动', 'yùndòng', 'sports / exercise'),
            ('游泳', 'yóuyǒng', 'to swim'),
            ('跑步', 'pǎobù', 'to run'),
            ('唱歌', 'chànggē', 'to sing'),
            ('跳舞', 'tiàowǔ', 'to dance'),
            ('周末', 'zhōumò', 'weekend'),
            ('打算', 'dǎsuàn', 'to plan'),
            ('一起', 'yìqǐ', 'together'),
        ],
        'grammar': [
            {
                'title': '你喜欢 + verb + 吗？',
                'zh': '你喜欢游泳吗？',
                'py': 'Nǐ xǐhuan yóuyǒng ma?',
                'en': 'Do you like swimming?',
            },
            {
                'title': '我打算 + verb · I plan to…',
                'zh': '我周末打算去跑步。',
                'py': 'Wǒ zhōumò dǎsuàn qù pǎobù.',
                'en': 'I plan to go running this weekend.',
            },
        ],
        'examples': [
            ('你的爱好是什么？', 'Nǐ de àihào shì shénme?', 'What are your hobbies?'),
            ('我喜欢唱歌和跳舞。', 'Wǒ xǐhuan chànggē hé tiàowǔ.', 'I like singing and dancing.'),
            ('周末你打算做什么？', 'Zhōumò nǐ dǎsuàn zuò shénme?', 'What do you plan to do this weekend?'),
            ('我们一起去看电影吧。', 'Wǒmen yìqǐ qù kàn diànyǐng ba.', "Let's go watch a movie together."),
        ],
        'quiz': {
            'group-1': [
                {'q': "'hobby' 用中文怎么说？<span class=\"py\">How do you say 'hobby'?</span>", 'answers': '爱好|àihào|ai hao|aihao', 'reveal': '爱好 <span class=\"py\">àihào · hobby</span>', 'placeholder': '爱好...'},
                {'q': "'to swim' 用中文怎么说？<span class=\"py\">How do you say 'to swim'?</span>", 'answers': '游泳|yóuyǒng|you yong|youyong', 'reveal': '游泳 <span class=\"py\">yóuyǒng · to swim</span>', 'placeholder': '游泳...'},
                {'q': "'weekend' 用中文怎么说？<span class=\"py\">How do you say 'weekend'?</span>", 'answers': '周末|zhōumò|zhou mo|zhoumo', 'reveal': '周末 <span class=\"py\">zhōumò · weekend</span>', 'placeholder': '周末...'},
            ],
            'group-2': [
                {'q': "你____游泳吗？ <span class=\"py\">Nǐ ___ yóuyǒng ma?</span>", 'answers': '喜欢|xǐhuan|xi huan|xihuan', 'reveal': '喜欢 <span class=\"py\">xǐhuan · to like</span>', 'placeholder': '喜欢...'},
                {'q': "我周末____去跑步。 <span class=\"py\">Wǒ zhōumò ___ qù pǎobù.</span>", 'answers': '打算|dǎsuàn|da suan|dasuan', 'reveal': '打算 <span class=\"py\">dǎsuàn · to plan</span>', 'placeholder': '打算...'},
                {'q': "我们____去看电影吧。 <span class=\"py\">Wǒmen ___ qù kàn diànyǐng ba.</span>", 'answers': '一起|yìqǐ|yi qi|yiqi', 'reveal': '一起 <span class=\"py\">yìqǐ · together</span>', 'placeholder': '一起...'},
            ],
            'final': [
                {'q': "'to run' 用中文怎么说？<span class=\"py\">How do you say 'to run'?</span>", 'answers': '跑步|pǎobù|pao bu|paobu', 'reveal': '跑步 <span class=\"py\">pǎobù · to run</span>', 'placeholder': '跑步...'},
                {'q': "'to sing' 用中文怎么说？<span class=\"py\">How do you say 'to sing'?</span>", 'answers': '唱歌|chànggē|chang ge|changge', 'reveal': '唱歌 <span class=\"py\">chànggē · to sing</span>', 'placeholder': '唱歌...'},
                {'q': "'to dance' 用中文怎么说？<span class=\"py\">How do you say 'to dance'?</span>", 'answers': '跳舞|tiàowǔ|tiao wu|tiaowu', 'reveal': '跳舞 <span class=\"py\">tiàowǔ · to dance</span>', 'placeholder': '跳舞...'},
                {'q': "'sports / exercise' 用中文怎么说？<span class=\"py\">How do you say 'sports / exercise'?</span>", 'answers': '运动|yùndòng|yun dong|yundong', 'reveal': '运动 <span class=\"py\">yùndòng · sports / exercise</span>', 'placeholder': '运动...'},
            ],
        },
    },
    {
        'id': 'hsk-4',
        'titleZh': '旅行计划',
        'titlePy': 'Lǚxíng jìhuà',
        'titleEn': 'Travel Plans',
        'subtitle': 'City, Transport & Booking',
        'level': 'HSK 4',
        'theme': '#fff0ee',
        'accent': '#9b2226',
        'icon': '✈️',
        'desc': 'HSK 4 words: plan a trip, describe places, compare options.',
        'vocab': [
            ('旅行', 'lǚxíng', 'travel'),
            ('计划', 'jìhuà', 'plan'),
            ('出发', 'chūfā', 'to depart'),
            ('到达', 'dàodá', 'to arrive'),
            ('方便', 'fāngbiàn', 'convenient'),
            ('便宜', 'piányi', 'cheap'),
            ('贵', 'guì', 'expensive'),
            ('推荐', 'tuījiàn', 'to recommend'),
            ('预订', 'yùdìng', 'to book'),
            ('护照', 'hùzhào', 'passport'),
            ('签证', 'qiānzhèng', 'visa'),
        ],
        'grammar': [
            {
                'title': 'A 比 B + adjective',
                'zh': '火车比飞机便宜。',
                'py': 'Huǒchē bǐ fēijī piányi.',
                'en': 'The train is cheaper than the plane.',
            },
            {
                'title': '虽然…，但是… · although…, …',
                'zh': '虽然飞机贵，但是很快。',
                'py': 'Suīrán fēijī guì, dànshì hěn kuài.',
                'en': 'Although the plane is expensive, it is fast.',
            },
        ],
        'examples': [
            ('你的旅行计划是什么？', 'Nǐ de lǚxíng jìhuà shì shénme?', 'What is your travel plan?'),
            ('我打算下个月去中国旅行。', 'Wǒ dǎsuàn xià ge yuè qù Zhōngguó lǚxíng.', 'I plan to travel to China next month.'),
            ('这家酒店很方便，但是有点贵。', 'Zhè jiā jiǔdiàn hěn fāngbiàn, dànshì yǒudiǎn guì.', 'This hotel is convenient, but a bit expensive.'),
            ('你能推荐一个好地方吗？', 'Nǐ néng tuījiàn yí ge hǎo dìfang ma?', 'Can you recommend a good place?'),
        ],
        'quiz': {
            'group-1': [
                {'q': "'travel' 用中文怎么说？<span class=\"py\">How do you say 'travel'?</span>", 'answers': '旅行|lǚxíng|lv xing|lvxing', 'reveal': '旅行 <span class=\"py\">lǚxíng · travel</span>', 'placeholder': '旅行...'},
                {'q': "'plan' 用中文怎么说？<span class=\"py\">How do you say 'plan'?</span>", 'answers': '计划|jìhuà|ji hua|jihua|打算|dǎsuàn', 'reveal': '计划 / 打算 <span class=\"py\">jìhuà / dǎsuàn · plan</span>', 'placeholder': '计划...'},
                {'q': "'convenient' 用中文怎么说？<span class=\"py\">How do you say 'convenient'?</span>", 'answers': '方便|fāngbiàn|fang bian|fangbian', 'reveal': '方便 <span class=\"py\">fāngbiàn · convenient</span>', 'placeholder': '方便...'},
            ],
            'group-2': [
                {'q': "火车____飞机便宜。 <span class=\"py\">Huǒchē ___ fēijī piányi.</span>", 'answers': '比|bǐ|bi', 'reveal': '比 <span class=\"py\">bǐ · than</span>', 'placeholder': '比...'},
                {'q': "____飞机贵，____很快。 <span class=\"py\">___ fēijī guì, ___ hěn kuài.</span>", 'answers': '虽然但是|suīrán dànshì|suiran danshi|虽然...但是...', 'reveal': '虽然…但是… <span class=\"py\">suīrán…dànshì… · although…but…</span>', 'placeholder': '虽然...但是...'},
                {'q': "你能____一个好地方吗？ <span class=\"py\">Nǐ néng ___ yí ge hǎo dìfang ma?</span>", 'answers': '推荐|tuījiàn|tui jian|tuijian', 'reveal': '推荐 <span class=\"py\">tuījiàn · to recommend</span>', 'placeholder': '推荐...'},
            ],
            'final': [
                {'q': "'expensive' 用中文怎么说？<span class=\"py\">How do you say 'expensive'?</span>", 'answers': '贵|guì|gui', 'reveal': '贵 <span class=\"py\">guì · expensive</span>', 'placeholder': '贵...'},
                {'q': "'cheap' 用中文怎么说？<span class=\"py\">How do you say 'cheap'?</span>", 'answers': '便宜|piányi|pian yi|pianyi', 'reveal': '便宜 <span class=\"py\">piányi · cheap</span>', 'placeholder': '便宜...'},
                {'q': "'to book' 用中文怎么说？<span class=\"py\">How do you say 'to book'?</span>", 'answers': '预订|yùdìng|yu ding|yuding', 'reveal': '预订 <span class=\"py\">yùdìng · to book</span>', 'placeholder': '预订...'},
                {'q': "'visa' 用中文怎么说？<span class=\"py\">How do you say 'visa'?</span>", 'answers': '签证|qiānzhèng|qian zheng|qianzheng', 'reveal': '签证 <span class=\"py\">qiānzhèng · visa</span>', 'placeholder': '签证...'},
            ],
        },
    },
    {
        'id': 'hsk-5',
        'titleZh': '职业与发展',
        'titlePy': 'Zhíyè yǔ fāzhǎn',
        'titleEn': 'Career & Development',
        'subtitle': 'Work, Goals & Choices',
        'level': 'HSK 5',
        'theme': '#f3e8ff',
        'accent': '#7c3aed',
        'icon': '💼',
        'desc': 'HSK 5 words: discuss career, goals, and professional choices.',
        'vocab': [
            ('职业', 'zhíyè', 'career / occupation'),
            ('发展', 'fāzhǎn', 'development / to develop'),
            ('经验', 'jīngyàn', 'experience'),
            ('收获', 'shōuhuò', 'gain / harvest'),
            ('挑战', 'tiǎozhàn', 'challenge'),
            ('机会', 'jīhuì', 'opportunity'),
            ('能力', 'nénglì', 'ability'),
            ('态度', 'tàidu', 'attitude'),
            ('理想', 'lǐxiǎng', 'ideal / dream'),
            ('担任', 'dānrèn', 'to hold a position'),
            ('责任', 'zérèn', 'responsibility'),
        ],
        'grammar': [
            {
                'title': '不管…，都… · no matter…, …',
                'zh': '不管遇到什么困难，我都不会放弃。',
                'py': 'Bùguǎn yù dào shénme kùnnan, wǒ dōu bù huì fàngqì.',
                'en': 'No matter what difficulties I meet, I will not give up.',
            },
            {
                'title': '与其…，不如… · rather than…, better to…',
                'zh': '与其抱怨，不如努力。',
                'py': 'Yǔqí bàoyuàn, bùrú nǔlì.',
                'en': 'Rather than complain, it is better to work hard.',
            },
        ],
        'examples': [
            ('你对未来的职业发展有什么计划？', 'Nǐ duì wèilái de zhíyè fāzhǎn yǒu shénme jìhuà?', 'What plans do you have for your future career development?'),
            ('这份工作让我学到了很多经验。', 'Zhè fèn gōngzuò ràng wǒ xué dào le hěn duō jīngyàn.', 'This job has taught me a lot of experience.'),
            ('面对挑战时，态度很重要。', 'Miàn duì tiǎozhàn shí, tàidu hěn zhòngyào.', 'Attitude is very important when facing challenges.'),
            ('我希望将来能担任更重要的责任。', 'Wǒ xīwàng jiānglái néng dānrèn gèng zhòngyào de zérèn.', 'I hope to take on more important responsibilities in the future.'),
        ],
        'quiz': {
            'group-1': [
                {'q': "'career / occupation' 用中文怎么说？<span class=\"py\">How do you say 'career / occupation'?</span>", 'answers': '职业|zhíyè|zhi ye|zhiye', 'reveal': '职业 <span class=\"py\">zhíyè · career / occupation</span>', 'placeholder': '职业...'},
                {'q': "'development / to develop' 用中文怎么说？<span class=\"py\">How do you say 'development'?</span>", 'answers': '发展|fāzhǎn|fa zhan|fazhan', 'reveal': '发展 <span class=\"py\">fāzhǎn · development</span>', 'placeholder': '发展...'},
                {'q': "'experience' 用中文怎么说？<span class=\"py\">How do you say 'experience'?</span>", 'answers': '经验|jīngyàn|jing yan|jingyan', 'reveal': '经验 <span class=\"py\">jīngyàn · experience</span>', 'placeholder': '经验...'},
            ],
            'group-2': [
                {'q': "____抱怨，____努力。 <span class=\"py\">___ bàoyuàn, ___ nǔlì.</span>", 'answers': '与其不如|yǔqí bùrú|yuqi buru|与其...不如...', 'reveal': '与其…不如… <span class=\"py\">yǔqí…bùrú… · rather than…better to…</span>', 'placeholder': '与其...不如...'},
                {'q': "'challenge' 用中文怎么说？<span class=\"py\">How do you say 'challenge'?</span>", 'answers': '挑战|tiǎozhàn|tiao zhan|tiaozhan', 'reveal': '挑战 <span class=\"py\">tiǎozhàn · challenge</span>', 'placeholder': '挑战...'},
                {'q': "'responsibility' 用中文怎么说？<span class=\"py\">How do you say 'responsibility'?</span>", 'answers': '责任|zérèn|ze ren|zeren', 'reveal': '责任 <span class=\"py\">zérèn · responsibility</span>', 'placeholder': '责任...'},
            ],
            'final': [
                {'q': "'opportunity' 用中文怎么说？<span class=\"py\">How do you say 'opportunity'?</span>", 'answers': '机会|jīhuì|ji hui|jihui', 'reveal': '机会 <span class=\"py\">jīhuì · opportunity</span>', 'placeholder': '机会...'},
                {'q': "'ability' 用中文怎么说？<span class=\"py\">How do you say 'ability'?</span>", 'answers': '能力|nénglì|neng li|nengli', 'reveal': '能力 <span class=\"py\">nénglì · ability</span>', 'placeholder': '能力...'},
                {'q': "'attitude' 用中文怎么说？<span class=\"py\">How do you say 'attitude'?</span>", 'answers': '态度|tàidu|tai du|taidu', 'reveal': '态度 <span class=\"py\">tàidu · attitude</span>', 'placeholder': '态度...'},
                {'q': "'ideal / dream' 用中文怎么说？<span class=\"py\">How do you say 'ideal / dream'?</span>", 'answers': '理想|lǐxiǎng|li xiang|lixiang', 'reveal': '理想 <span class=\"py\">lǐxiǎng · ideal / dream</span>', 'placeholder': '理想...'},
            ],
        },
    },
    {
        'id': 'hsk-6',
        'titleZh': '科技与社会',
        'titlePy': 'Kējì yǔ shèhuì',
        'titleEn': 'Technology & Society',
        'subtitle': 'Change, Impact & Future Trends',
        'level': 'HSK 6',
        'theme': '#ede9fe',
        'accent': '#5b21b6',
        'icon': '🌐',
        'desc': 'HSK 6 words: discuss technology, social change, and complex arguments.',
        'vocab': [
            ('科技', 'kējì', 'technology'),
            ('社会', 'shèhuì', 'society'),
            ('影响', 'yǐngxiǎng', 'influence / impact'),
            ('变革', 'biàngé', 'transformation'),
            ('趋势', 'qūshì', 'trend'),
            ('人工智能', 'réngōng zhìnéng', 'artificial intelligence'),
            ('隐私', 'yǐnsī', 'privacy'),
            ('数据', 'shùjù', 'data'),
            ('依赖', 'yīlài', 'to depend on'),
            ('忽视', 'hūshì', 'to ignore / neglect'),
            ('关注', 'guānzhù', 'to pay attention to'),
        ],
        'grammar': [
            {
                'title': '随着…，… · along with…, …',
                'zh': '随着科技的发展，人们的生活方式发生了很大的变化。',
                'py': 'Suízhe kējì de fāzhǎn, rénmen de shēnghuó fāngshì fāshēng le hěn dà de biànhuà.',
                'en': 'Along with the development of technology, people\'s lifestyles have changed greatly.',
            },
            {
                'title': '不仅…，而且… · not only…, but also…',
                'zh': '人工智能不仅提高了效率，而且改变了我们的工作方式。',
                'py': 'Réngōng zhìnéng bùjǐn tígāo le xiàolǜ, érqiě gǎibiàn le wǒmen de gōngzuò fāngshì.',
                'en': 'AI not only improves efficiency, but also changes the way we work.',
            },
        ],
        'examples': [
            ('科技的发展对社会有什么影响？', 'Kējì de fāzhǎn duì shèhuì yǒu shénme yǐngxiǎng?', 'What impact does technological development have on society?'),
            ('随着互联网的普及，人们的交流方式发生了巨大变化。', 'Suízhe hùliánwǎng de pǔjí, rénmen de jiāoliú fāngshì fāshēng le jùdà biànhuà.', 'With the popularization of the Internet, people\'s ways of communicating have changed tremendously.'),
            ('我们不能忽视隐私保护的重要性。', 'Wǒmen bù néng hūshì yǐnsī bǎohù de zhòngyào xìng.', 'We cannot ignore the importance of privacy protection.'),
            ('未来的趋势不仅是技术进步，而且是社会责任的提升。', 'Wèilái de qūshì bùjǐn shì jìshù jìnbù, érqiě shì shèhuì zérèn de tíshēng.', 'The future trend is not only technological progress, but also the improvement of social responsibility.'),
        ],
        'quiz': {
            'group-1': [
                {'q': "'technology' 用中文怎么说？<span class=\"py\">How do you say 'technology'?</span>", 'answers': '科技|kējì|ke ji|keji', 'reveal': '科技 <span class=\"py\">kējì · technology</span>', 'placeholder': '科技...'},
                {'q': "'society' 用中文怎么说？<span class=\"py\">How do you say 'society'?</span>", 'answers': '社会|shèhuì|she hui|shehui', 'reveal': '社会 <span class=\"py\">shèhuì · society</span>', 'placeholder': '社会...'},
                {'q': "'artificial intelligence' 用中文怎么说？<span class=\"py\">How do you say 'artificial intelligence'?</span>", 'answers': '人工智能|réngōng zhìnéng|ren gong zhi neng|rengongzhineng', 'reveal': '人工智能 <span class=\"py\">réngōng zhìnéng · artificial intelligence</span>', 'placeholder': '人工智能...'},
            ],
            'group-2': [
                {'q': "'influence / impact' 用中文怎么说？<span class=\"py\">How do you say 'influence / impact'?</span>", 'answers': '影响|yǐngxiǎng|ying xiang|yingxiang', 'reveal': '影响 <span class=\"py\">yǐngxiǎng · influence / impact</span>', 'placeholder': '影响...'},
                {'q': "'trend' 用中文怎么说？<span class=\"py\">How do you say 'trend'?</span>", 'answers': '趋势|qūshì|qu shi|qushi', 'reveal': '趋势 <span class=\"py\">qūshì · trend</span>', 'placeholder': '趋势...'},
                {'q': "____科技的发展，人们的生活方式发生了很大的变化。 <span class=\"py\">___ kējì de fāzhǎn, rénmen de shēnghuó fāngshì fāshēng le hěn dà de biànhuà.</span>", 'answers': '随着|suízhe|sui zhe|suizhe', 'reveal': '随着 <span class=\"py\">suízhe · along with</span>', 'placeholder': '随着...'},
            ],
            'final': [
                {'q': "'privacy' 用中文怎么说？<span class=\"py\">How do you say 'privacy'?</span>", 'answers': '隐私|yǐnsī|yin si|yinsi', 'reveal': '隐私 <span class=\"py\">yǐnsī · privacy</span>', 'placeholder': '隐私...'},
                {'q': "'data' 用中文怎么说？<span class=\"py\">How do you say 'data'?</span>", 'answers': '数据|shùjù|shu ju|shuju', 'reveal': '数据 <span class=\"py\">shùjù · data</span>', 'placeholder': '数据...'},
                {'q': "'to depend on' 用中文怎么说？<span class=\"py\">How do you say 'to depend on'?</span>", 'answers': '依赖|yīlài|yi lai|yilai', 'reveal': '依赖 <span class=\"py\">yīlài · to depend on</span>', 'placeholder': '依赖...'},
                {'q': "'not only…, but also…' 用中文怎么说？<span class=\"py\">How do you say 'not only…but also…'?</span>", 'answers': '不仅而且|bùjǐn érqiě|bu jin er qie|bujinerqie|不仅...而且...', 'reveal': '不仅…而且… <span class=\"py\">bùjǐn…érqiě… · not only…but also…</span>', 'placeholder': '不仅...而且...'},
            ],
        },
    },
]


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titleZh} — {titleEn} · Xinhan Chinese</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --jade: #2d6a4f; --jade-mid: #40916c; --jade-light: #74c69d; --jade-pale: #d8f3dc;
  --gold: #b7791f; --gold-mid: #d69e2e; --gold-pale: #fffff0;
  --rust: #9b2226; --rust-light: #e76f51; --rust-pale: #fff0ee;
  --cream: #faf7f2; --cream-dark: #ede8df;
  --ink: #1a1a1a; --ink-2: #3d3d3d; --ink-3: #7a7a7a;
  --white: #fff;
  --accent: {accent};
}}
body {{ font-family: 'Inter', sans-serif; background: #d6cfc4; color: var(--ink); padding: 2.5rem 1rem 5rem; }}
.deck {{ max-width: 940px; margin: 0 auto; }}
.deck-brand {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }}
.brand-name {{ font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--accent); }}
.brand-sub  {{ font-size: 0.68rem; color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.12em; }}
.slide {{ display: grid; background: var(--white); overflow: hidden; margin-bottom: 3px; }}
.slide:first-of-type {{ border-radius: 14px 14px 0 0; }}
.slide:last-of-type {{ border-radius: 0 0 14px 14px; }}
.sidebar {{
  display: flex; flex-direction: column;
  padding: 1.5rem 0.65rem 1.5rem 0.9rem;
  background: var(--accent);
  gap: 1.8rem; min-width: 64px;
  position: relative;
}}
.sidebar::after {{ content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, rgba(255,255,255,0.25), transparent); }}
.sb-icon {{ display: flex; flex-direction: column; align-items: center; gap: 0.3rem; }}
.sb-icon svg {{ width: 28px; height: 28px; }}
.sb-label {{ font-size: 0.48rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.55); text-align: center; line-height: 1.2; }}
.sb-prog {{ display: flex; flex-direction: column; align-items: center; gap: 5px; margin-top: auto; }}
.dot {{ width: 7px; height: 7px; border-radius: 50%; background: rgba(255,255,255,0.2); }}
.dot.active {{ background: #f6e05e; }}
.dot.done {{ background: var(--rust-light); }}
.content {{ padding: 2rem 2.5rem 2rem 2rem; flex: 1; }}
.sec-label {{ font-size: 0.6rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent); margin-bottom: 0.9rem; }}
.content h2 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 600; margin-bottom: 1.25rem; line-height: 1.3; }}
.py-inline {{ font-size: 0.72rem; font-family: 'Inter', sans-serif; font-weight: 400; color: var(--gold); letter-spacing: 0.07em; }}
.scene {{ width: 100%; border-radius: 10px; overflow: hidden; margin-bottom: 1.25rem; background: var(--cream); }}
.scene svg {{ display: block; width: 100%; }}
.slide-cover {{ grid-template-columns: 90px 1fr; }}
.cover-content {{ background: var(--accent); padding: 2.5rem 2.5rem 2rem; position: relative; min-height: 300px; display: flex; flex-direction: column; justify-content: flex-end; overflow: hidden; }}
.cover-scene {{ position: absolute; top: 0; right: 0; left: 0; bottom: 0; opacity: 0.16; }}
.cover-eyebrow {{ font-size: 0.65rem; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; color: rgba(255,255,255,0.7); margin-bottom: 0.7rem; position: relative; }}
.cover-zh {{ font-family: 'Noto Serif SC', serif; font-size: 4.2rem; font-weight: 700; color: var(--white); line-height: 1.1; letter-spacing: -0.02em; position: relative; }}
.cover-py {{ font-size: 1.25rem; font-weight: 300; color: rgba(255,255,255,0.75); letter-spacing: 0.18em; margin: 0.3rem 0; position: relative; }}
.cover-en {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.45rem; color: #f6e05e; position: relative; margin-bottom: 1.5rem; }}
.cover-tags {{ display: flex; gap: 0.5rem; flex-wrap: wrap; position: relative; }}
.tag {{ padding: 0.22rem 0.8rem; border-radius: 999px; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9); }}
.grammar-strip {{ display: flex; align-items: center; gap: 0; background: var(--cream); border-radius: 10px; overflow: hidden; margin-bottom: 1.4rem; }}
.gs-part {{ padding: 0.75rem 1rem; display: flex; flex-direction: column; align-items: center; }}
.gs-part.colored {{ background: var(--accent); }}
.gs-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1.5rem; font-weight: 700; color: var(--white); line-height: 1; }}
.gs-py {{ font-size: 0.58rem; color: rgba(255,255,255,0.7); letter-spacing: 0.06em; margin-top: 2px; }}
.gs-sep {{ font-size: 1.1rem; color: var(--ink-3); padding: 0 0.3rem; }}
.gs-plain-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1.1rem; font-weight: 500; color: var(--accent); }}
.gs-plain-py {{ font-size: 0.58rem; color: var(--gold); margin-top: 2px; }}
.gs-en {{ margin-left: auto; padding: 0.75rem 1.25rem; font-size: 0.72rem; color: var(--ink-3); font-style: italic; border-left: 1px solid var(--cream-dark); }}
.ex-block {{ display: flex; flex-direction: column; gap: 0.65rem; margin-bottom: 1.25rem; }}
.ex {{ background: var(--cream); border-radius: 8px; padding: 0.8rem 1rem; border-left: 3px solid var(--accent); }}
.ex-zh {{ font-family: 'Noto Serif SC', serif; font-size: 0.98rem; color: var(--ink); margin-bottom: 0.15rem; }}
.key {{ color: var(--accent); font-weight: 700; }}
.ex-py {{ font-size: 0.63rem; color: var(--gold); letter-spacing: 0.03em; margin-bottom: 0.1rem; }}
.ex-en {{ font-size: 0.69rem; color: var(--ink-3); font-style: italic; }}
.vocab-grid {{ display: grid; grid-template-columns: repeat(5,1fr); gap: 6px; }}
.vc {{ background: var(--white); border: 1px solid var(--cream-dark); border-radius: 7px; padding: 0.55rem 0.7rem; border-top: 3px solid var(--accent); }}
.vc-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1rem; font-weight: 500; color: var(--accent); }}
.vc-py {{ font-size: 0.58rem; color: var(--gold); margin: 2px 0 1px; }}
.vc-en {{ font-size: 0.62rem; color: var(--ink-3); }}
.tip {{ background: {theme}; border-radius: 7px; padding: 0.65rem 0.95rem; font-size: 0.7rem; color: var(--accent); line-height: 1.55; margin-top: 0.9rem; }}
.tip strong {{ font-weight: 600; }}
.slide-close {{ display: block; background: var(--accent); border-radius: 0 0 14px 14px; }}
.close-inner {{ padding: 3rem 3.5rem; display: flex; align-items: center; justify-content: space-between; }}
.close-zh {{ font-family: 'Noto Serif SC', serif; font-size: 5rem; font-weight: 700; color: var(--white); }}
.close-detail .py {{ font-size: 1rem; color: rgba(255,255,255,0.75); letter-spacing: 0.2em; }}
.close-detail .en {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.9rem; color: #f6e05e; margin-top: 0.2rem; }}
.close-detail .sub {{ font-size: 0.62rem; color: rgba(255,255,255,0.3); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 1rem; }}

.phone-row {{ display: flex; gap: 16px; flex-wrap: wrap; justify-content: flex-start; margin-bottom: 0.5rem; }}
.phone-block {{ display: flex; flex-direction: column; gap: 0.55rem; width: 150px; }}
.phone-block.wide {{ width: 200px; }}
.quiz-q {{ background: var(--cream); border-radius: 8px; padding: 0.5rem 0.65rem; font-size: 0.66rem; color: var(--ink); line-height: 1.45; }}
.quiz-q .py {{ display: block; color: var(--gold); font-size: 0.6rem; margin-top: 1px; }}
.quiz-game {{ display: flex; flex-direction: column; gap: 0.3rem; }}
.quiz-row {{ display: flex; gap: 0.3rem; }}
.quiz-input {{ flex: 1; width: 100%; box-sizing: border-box; padding: 6px 8px; font-size: 0.66rem; font-family: inherit; border: 1px solid #d2d2d2; border-radius: 6px; background: var(--white); color: var(--ink); transition: border-color 0.15s, background 0.15s; }}
.quiz-input:focus {{ outline: 2px solid var(--gold); outline-offset: 1px; }}
.quiz-input:disabled {{ background: var(--cream); opacity: 0.85; }}
.quiz-input.flash-correct {{ border-color: #2f7d52; background: #eaf7ef; animation: quiz-pop 0.4s ease; }}
.quiz-input.flash-wrong {{ border-color: #c0392b; background: #fbeaea; animation: quiz-shake 0.4s ease; }}
.quiz-check-btn {{ flex-shrink: 0; padding: 6px 10px; font-size: 0.62rem; font-weight: 700; border: none; border-radius: 6px; background: var(--gold); color: var(--accent); cursor: pointer; transition: background 0.15s, transform 0.15s; }}
.quiz-check-btn:hover:not(:disabled) {{ transform: translateY(-1px); }}
.quiz-check-btn:disabled {{ cursor: default; }}
.quiz-check-btn.correct {{ background: #2f7d52; color: white; animation: quiz-pop 0.4s ease; }}
.quiz-check-btn.wrong {{ background: #c0392b; color: white; animation: quiz-shake 0.4s ease; }}
@keyframes quiz-pop {{ 0% {{ transform: scale(1); }} 40% {{ transform: scale(1.12); }} 100% {{ transform: scale(1); }} }}
@keyframes quiz-shake {{ 0%, 100% {{ transform: translateX(0); }} 20% {{ transform: translateX(-5px); }} 40% {{ transform: translateX(5px); }} 60% {{ transform: translateX(-4px); }} 80% {{ transform: translateX(4px); }} }}
.quiz-feedback {{ font-size: 0.68rem; font-weight: 700; min-height: 1.1em; }}
.quiz-feedback.correct {{ color: #2f7d52; }}
.quiz-feedback.wrong {{ color: #c0392b; }}
.quiz-feedback .reveal {{ display: block; font-weight: 500; color: var(--ink); margin-top: 2px; font-size: 0.62rem; }}
.quiz-feedback .reveal .py {{ color: var(--gold); }}
.quiz-score {{ display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.66rem; font-weight: 700; color: var(--accent); background: var(--cream); border-radius: 20px; padding: 0.3rem 0.8rem; margin-bottom: 0.8rem; }}
.quiz-score .stars {{ color: var(--gold); letter-spacing: 1px; }}
.test-badge {{ display: inline-block; font-size: 0.6rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--rust); background: #fbeaea; border-radius: 20px; padding: 0.25rem 0.7rem; margin-bottom: 0.6rem; }}
.report-score {{ display: flex; align-items: baseline; gap: 0.6rem; margin: 0.5rem 0 1rem; }}
.report-score .big {{ font-size: 2.4rem; font-weight: 800; color: var(--jade); }}
.report-score .pct {{ font-size: 1rem; font-weight: 700; color: var(--gold); }}
.report-groups {{ display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.2rem; }}
.report-group-row {{ display: flex; align-items: center; gap: 0.6rem; font-size: 0.66rem; }}
.report-group-name {{ width: 150px; flex-shrink: 0; color: var(--ink); }}
.report-group-bar {{ flex: 1; height: 8px; border-radius: 5px; background: var(--cream); overflow: hidden; }}
.report-group-fill {{ height: 100%; background: var(--jade-mid); border-radius: 5px; }}
.report-group-fill.weak {{ background: var(--rust-light); }}
.report-group-score {{ width: 36px; flex-shrink: 0; text-align: right; color: var(--ink-3); }}
.report-missed {{ background: #fbeaea; border-radius: 8px; padding: 0.8rem 1rem; }}
.report-missed h4 {{ margin: 0 0 0.5rem; font-size: 0.72rem; color: var(--rust); }}
.report-missed-item {{ display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: baseline; font-size: 0.66rem; padding: 0.35rem 0; border-bottom: 1px solid rgba(155,34,38,0.12); }}
.report-missed-item:last-child {{ border-bottom: none; }}
.report-missed-q {{ color: var(--ink); flex: 1; min-width: 200px; }}
.report-missed-you {{ color: #c0392b; text-decoration: line-through; }}
.report-missed-correct {{ color: #2f7d52; font-weight: 600; }}
.report-perfect {{ background: var(--jade-pale); border-radius: 8px; padding: 1rem; font-size: 0.72rem; color: var(--jade); font-weight: 600; text-align: center; }}
.sidebar.dark {{ background: #1a3a2b; }}
@media print {{ body {{ background: white; padding: 0; }} .deck {{ max-width: 100%; }} .slide {{ break-inside: avoid; margin-bottom: 0; }} .deck-brand {{ display: none; }} }}
@media (max-width: 640px) {{ .slide {{ grid-template-columns: 48px 1fr !important; }} .sidebar {{ padding: 1rem 0.4rem; }} .content {{ padding: 1.25rem; }} .vocab-grid {{ grid-template-columns: repeat(2,1fr); }} .cover-zh {{ font-size: 3rem; }} }}
</style>
</head>
<body data-lesson-id="{id}">

<div class="deck">
<div class="deck-brand">
  <span class="brand-name">新汉 Xīnhàn</span>
  <span class="brand-sub">{level} · {subtitle}</span>
</div>

<!-- ① COVER -->
<div class="slide slide-cover">
  <div class="sidebar" style="justify-content:center;align-items:center;min-height:300px;">
    <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <circle cx="16" cy="16" r="12" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
      <text x="16" y="21" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="12" fill="rgba(255,255,255,0.9)" font-weight="700">{level_short}</text>
    </svg>
  </div>
  <div class="cover-content">
    <div class="cover-scene">
      <svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
        <rect width="700" height="300" fill="var(--accent)"/>
        <circle cx="580" cy="60" r="60" fill="rgba(255,255,255,0.12)"/>
        <circle cx="120" cy="200" r="80" fill="rgba(255,255,255,0.08)"/>
        <circle cx="640" cy="240" r="50" fill="rgba(255,255,255,0.08)"/>
      </svg>
    </div>
    <div class="cover-eyebrow">{level} · {subtitle}</div>
    <div class="cover-zh">{titleZh}</div>
    <div class="cover-py">{titlePy}</div>
    <div class="cover-en">{titleEn}</div>
    <div class="cover-tags">
      <span class="tag">{level}</span>
      <span class="tag">{vocab_count} words</span>
      <span class="tag">progressive cycle</span>
    </div>
  </div>
</div>

<!-- ② WARM-UP -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="14" cy="14" r="7" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <path d="M14 8v3M14 17v3M8 14h3M17 14h3" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">warm up</div>
    </div>
    <div class="sb-prog"><div class="dot active"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">Warm-up · 热身</div>
    <h2>{titleZh} <span class="py-inline">{titlePy}</span></h2>
    <div class="scene" style="padding:1.5rem;">
      <svg viewBox="0 0 700 100" xmlns="http://www.w3.org/2000/svg">
        <rect width="700" height="100" fill="{theme}" rx="8"/>
        <text x="350" y="45" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="16" fill="var(--accent)" font-weight="700">{subtitle}</text>
        <text x="350" y="70" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="var(--ink-3)">{desc}</text>
      </svg>
    </div>
    <div class="tip"><strong>Goal:</strong> Learn {vocab_count} core {level} words and use them in real sentences.</div>
  </div>
</div>

<!-- ③ VOCABULARY -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4" y="3" width="20" height="22" rx="2" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <line x1="8" y1="9" x2="20" y2="9" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="8" y1="14" x2="20" y2="14" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="8" y1="19" x2="15" y2="19" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">vocab</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot active"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">New Words · 新词 — {vocab_count} words</div>
    <h2>{level} core vocabulary <span class="py-inline">héxīn cíhuì</span></h2>
    <div class="vocab-grid">
      {vocab_grid}
    </div>
  </div>
</div>

<!-- ④ GRAMMAR -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <line x1="14" y1="5" x2="14" y2="24" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <line x1="5" y1="11" x2="23" y2="11" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <circle cx="5" cy="17" r="4" fill="rgba(255,255,255,0.7)"/>
        <circle cx="23" cy="8" r="4" fill="rgba(255,255,255,0.5)"/>
      </svg>
      <div class="sb-label">grammar</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">Grammar · 语法</div>
    <h2>Key sentence patterns <span class="py-inline">guānjiàn jùxíng</span></h2>
    {grammar_blocks}
    <div class="ex-block">
      {example_blocks}
    </div>
  </div>
</div>

<!-- ⑤ PRACTICE -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar" style="background:#7b5a1a">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 20 Q14 10 22 20" stroke="rgba(255,255,255,0.9)" stroke-width="1.8" fill="none" stroke-linecap="round"/>
        <ellipse cx="14" cy="12" rx="4" ry="3" fill="rgba(255,255,255,0.85)"/>
      </svg>
      <div class="sb-label">practice</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div><div class="dot"></div><div class="dot"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">Practice · 练习</div>
    <h2>Make your own sentences <span class="py-inline">zào jù</span></h2>
    <div class="scene" style="padding:1.5rem;">
      <svg viewBox="0 0 700 80" xmlns="http://www.w3.org/2000/svg">
        <rect width="700" height="80" fill="{theme}" rx="8"/>
        <text x="350" y="35" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="14" fill="var(--accent)" font-weight="700">Try saying one sentence from this lesson out loud.</text>
        <text x="350" y="58" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="var(--ink-3)">Use at least 2 new words. Don't worry about mistakes.</text>
      </svg>
    </div>
    <div class="tip"><strong>Tip:</strong> Say it three times — slow, normal, fast.</div>
  </div>
</div>

{quiz_slides}

<!-- REPORT -->
<div class="slide" id="lesson-report-slide" style="grid-template-columns:64px 1fr; display:none;">
  <div class="sidebar dark">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 21 L5 13 M12 21 L12 8 M19 21 L19 16 M23 21 L23 11" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">your report</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">Lesson Report · 学习报告</div>
    <h2>你的学习报告 <span class="py-inline">Nǐ de xuéxí bàogào</span></h2>
    <div id="report-score" class="report-score"></div>
    <div id="report-groups" class="report-groups"></div>
    <div id="report-missed"></div>
  </div>
</div>

<!-- CLOSING -->
<div class="slide slide-close">
  <div class="close-inner">
    <div class="close-zh">加油</div>
    <div class="close-detail">
      <div class="py">Jiāyóu</div>
      <div class="en">Keep going — next level awaits</div>
      <div class="sub">{level} · {titleEn}</div>
    </div>
  </div>
</div>

</div>

<script>
(function () {{
  var lessonId = document.body.dataset.lessonId || '';
  var allInputs = Array.prototype.slice.call(document.querySelectorAll('.quiz-input'));
  var reportShown = false;
  var wrongAnswers = [];

  var GROUP_NAMES = {{
    'group-1': 'Vocabulary · 词汇',
    'group-2': 'Grammar · 语法',
    'final': 'Final Challenge · 综合挑战'
  }};

  function escapeHtml(s) {{
    return String(s).replace(/[&<>"]/g, function (c) {{
      return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }}[c];
    }});
  }}

  function logAttempt(payload) {{
    if (!lessonId) return;
    fetch('/api/lessons/attempt', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify(payload),
    }}).catch(function () {{}});
  }}

  function logCompletion(score, total, groupList) {{
    if (!lessonId) return;
    fetch('/api/lessons/complete', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ lessonId: lessonId, score: score, total: total, groups: groupList }}),
    }}).catch(function () {{}});
  }}

  function buildReport() {{
    var groups = {{}};
    document.querySelectorAll('[data-quiz-score]').forEach(function (box) {{
      var groupId = box.dataset.group || 'default';
      groups[groupId] = {{
        groupId: groupId,
        score: Number(box.querySelector('.score-correct').textContent),
        total: Number(box.dataset.total),
      }};
    }});
    var groupList = Object.keys(groups).map(function (k) {{ return groups[k]; }});
    var score = groupList.reduce(function (s, g) {{ return s + g.score; }}, 0);
    var total = groupList.reduce(function (s, g) {{ return s + g.total; }}, 0);
    var pct = total > 0 ? Math.round((score / total) * 100) : 0;

    var scoreBox = document.getElementById('report-score');
    if (scoreBox) {{
      scoreBox.innerHTML = '<span class="big">' + score + '/' + total + '</span><span class="pct">' + pct + '%</span>';
    }}

    var groupsBox = document.getElementById('report-groups');
    if (groupsBox) {{
      groupsBox.innerHTML = groupList.map(function (g) {{
        var p = g.total > 0 ? (g.score / g.total) * 100 : 0;
        var weak = p < 100 ? ' weak' : '';
        return '<div class="report-group-row">' +
          '<div class="report-group-name">' + (GROUP_NAMES[g.groupId] || g.groupId) + '</div>' +
          '<div class="report-group-bar"><div class="report-group-fill' + weak + '" style="width:' + p + '%"></div></div>' +
          '<div class="report-group-score">' + g.score + '/' + g.total + '</div>' +
          '</div>';
      }}).join('');
    }}

    var missedBox = document.getElementById('report-missed');
    if (missedBox) {{
      if (wrongAnswers.length === 0) {{
        missedBox.innerHTML = '<div class="report-perfect">完美！Perfect score — every answer right. 🎉</div>';
      }} else {{
        missedBox.innerHTML = '<div class="report-missed"><h4>Words &amp; phrases to review · 需要复习的词</h4>' +
          wrongAnswers.map(function (w) {{
            return '<div class="report-missed-item">' +
              '<span class="report-missed-q">' + escapeHtml(w.questionText) + '</span>' +
              '<span class="report-missed-you">' + escapeHtml(w.userAnswer || '(blank)') + '</span>' +
              '<span class="report-missed-correct">' + w.reveal + '</span>' +
              '</div>';
          }}).join('') + '</div>';
      }}
    }}

    var slide = document.getElementById('lesson-report-slide');
    if (slide) {{
      slide.style.display = 'grid';
      slide.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}

    logCompletion(score, total, groupList);
  }}

  function maybeShowReport() {{
    if (reportShown) return;
    var allDone = allInputs.every(function (i) {{ return i.disabled; }});
    if (!allDone) return;
    reportShown = true;
    buildReport();
  }}

  allInputs.forEach(function (input, globalIndex) {{
    var row = input.closest('.quiz-game');
    var feedback = row.querySelector('.quiz-feedback');
    var checkBtn = row.querySelector('.quiz-check-btn');
    var answers = (input.dataset.answer || '').split('|').map(function (a) {{ return a.trim().toLowerCase(); }});
    var reveal = input.dataset.reveal || '';
    var scoreBox = input.closest('.content') ? input.closest('.content').querySelector('[data-quiz-score]') : null;
    var questionText = input.closest('.phone-block') ? input.closest('.phone-block').querySelector('.quiz-q').textContent.trim() : '';

    function check() {{
      if (input.disabled) return;
      var val = input.value.trim().toLowerCase();
      if (!val) return;
      var correct = answers.indexOf(val) !== -1;

      feedback.className = 'quiz-feedback ' + (correct ? 'correct' : 'wrong');
      feedback.innerHTML = (correct ? '对! Duì! Right!' : '错! Cuò! Wrong!') + (reveal ? '<span class="reveal">' + reveal + '</span>' : '');

      input.classList.add(correct ? 'flash-correct' : 'flash-wrong');
      if (checkBtn) {{
        checkBtn.classList.add(correct ? 'correct' : 'wrong');
        checkBtn.textContent = correct ? '✓' : '✗';
        checkBtn.disabled = true;
      }}
      input.disabled = true;

      if (correct && scoreBox) {{
        var counter = scoreBox.querySelector('.score-correct');
        counter.textContent = String(Number(counter.textContent) + 1);
      }}
      if (!correct) {{
        wrongAnswers.push({{ questionText: questionText, userAnswer: input.value.trim(), reveal: reveal }});
      }}

      logAttempt({{
        lessonId: lessonId,
        groupId: scoreBox ? scoreBox.dataset.group : 'default',
        questionIndex: globalIndex,
        questionText: questionText,
        userAnswer: input.value.trim(),
        correct: correct,
      }});
      maybeShowReport();
    }}

    input.addEventListener('keydown', function (e) {{ if (e.key === 'Enter') check(); }});
    if (checkBtn) checkBtn.addEventListener('click', check);
  }});
}})();
</script>
</body>
</html>
"""


def quiz_block(question, answers, reveal, placeholder=""):
    safe_reveal = reveal.replace('"', '&quot;')
    safe_answers = answers.replace('"', '&quot;')
    safe_placeholder = placeholder.replace('"', '&quot;')
    return f"""<div class="phone-block wide">
        <div class="quiz-q">{question}</div>
        <div class="quiz-game">
          <div class="quiz-row">
            <input type="text" class="quiz-input" placeholder="{safe_placeholder}" data-answer="{safe_answers}" data-reveal="{safe_reveal}"/>
            <button type="button" class="quiz-check-btn">检查</button>
          </div>
          <div class="quiz-feedback"></div>
        </div>
      </div>"""


def build_quiz_slide(title, group, total, questions, index):
    blocks = '\n      '.join(quiz_block(q['q'], q['answers'], q['reveal'], q.get('placeholder', '')) for q in questions)
    return f"""<!-- TEST {index} -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 14 L12 20 L22 8" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="sb-label">test {index}</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div><div class="dot"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">{title}</div>
    <h2>Check your understanding <span class="py-inline">jiǎnchá lǐjiě</span></h2>
    <div class="quiz-score" data-quiz-score data-group="{group}" data-total="{total}">✅ <span class="score-correct">0</span>/<span class="score-total">{total}</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type your answer</strong> in Chinese, pinyin, or English.</div>
    <div class="phone-row">
      {blocks}
    </div>
  </div>
</div>
"""


def render_lesson(lesson):
    vocab_grid = '\n      '.join(
        f'<div class="vc"><div class="vc-zh">{zh}</div><div class="vc-py">{py}</div><div class="vc-en">{en}</div></div>'
        for zh, py, en in lesson['vocab']
    )

    grammar_blocks = ''
    for g in lesson['grammar']:
        grammar_blocks += f"""
    <div class="grammar-strip">
      <div class="gs-part colored"><div class="gs-zh">{g['title'].split(' · ')[0]}</div></div>
      <div class="gs-en">{g['title'].split(' · ')[1] if ' · ' in g['title'] else ''}</div>
    </div>
    <div class="ex-block" style="margin-top:0.5rem;">
      <div class="ex">
        <div class="ex-zh">{g['zh']}</div>
        <div class="ex-py">{g['py']}</div>
        <div class="ex-en">{g['en']}</div>
      </div>
    </div>"""

    example_blocks = '\n      '.join(
        f"""<div class="ex">
        <div class="ex-zh">{zh}</div>
        <div class="ex-py">{py}</div>
        <div class="ex-en">{en}</div>
      </div>"""
        for zh, py, en in lesson['examples']
    )

    quiz = lesson['quiz']
    quiz_slides = build_quiz_slide('Vocabulary · 词汇', 'group-1', len(quiz['group-1']), quiz['group-1'], '1/3') + \
                  build_quiz_slide('Grammar · 语法', 'group-2', len(quiz['group-2']), quiz['group-2'], '2/3') + \
                  build_quiz_slide('Final Challenge · 综合挑战', 'final', len(quiz['final']), quiz['final'], '3/3')

    html = HTML_TEMPLATE.format(
        id=lesson['id'],
        titleZh=lesson['titleZh'],
        titlePy=lesson['titlePy'],
        titleEn=lesson['titleEn'],
        subtitle=lesson['subtitle'],
        level=lesson['level'],
        level_short=lesson['level'].replace('HSK ', ''),
        accent=lesson['accent'],
        theme=lesson['theme'],
        desc=lesson['desc'],
        vocab_count=len(lesson['vocab']),
        vocab_grid=vocab_grid,
        grammar_blocks=grammar_blocks,
        example_blocks=example_blocks,
        quiz_slides=quiz_slides,
    )

    out_dir = os.path.join('/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson', lesson['id'])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote {out_path} ({len(html)} bytes)")


if __name__ == '__main__':
    for lesson in LESSONS:
        render_lesson(lesson)
