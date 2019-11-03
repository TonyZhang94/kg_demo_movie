# -*- coding: utf-8 -*-

from ProductQuery.predicate.predicate import W

# TODO
pos_person = "nr"
pos_movie = "nz"
pos_number = "m"

person_entity = (W(pos=pos_person))
movie_entity = (W(pos=pos_movie))
number_entity = (W(pos=pos_number))

adventure = W("冒险")
fantasy = W("奇幻")
animation = (W("动画") | W("动画片"))
drama = (W("剧情") | W("剧情片"))
thriller = (W("恐怖") | W("恐怖片"))
action = (W("动作") | W("动作片"))
comedy = (W("喜剧") | W("喜剧片"))
history = (W("历史") | W("历史剧"))
western = (W("西部") | W("西部片"))
horror = (W("惊悚") | W("惊悚片"))
crime = (W("犯罪") | W("犯罪片"))
documentary = (W("纪录") | W("纪录片"))
science_fiction = (W("科幻") | W("科幻片"))
mystery = (W("悬疑") | W("悬疑片"))
music = (W("音乐") | W("音乐片"))
romance = (W("爱情") | W("爱情片"))
family = W("家庭")
war = (W("战争") | W("战争片"))
TV = W("电视")
genre = (adventure | fantasy | animation | drama | thriller | action
         | comedy | history | western | horror | crime | documentary |
         science_fiction | mystery | music | romance | family | war
         | TV)


actor = (W("演员") | W("艺人") | W("表演者") | W("优伶"))
movie = (W("电影") | W("影片") | W("片子") | W("片") | W("剧") | W("主演"))
category = (W("类型") | W("种类"))
several = (W("多少") | W("几部"))

higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)

birth = (W("生日") | W("出生") + W("日期") | W("出生"))
birth_place = (W("出生地") | W("出生"))
english_name = (W("英文名") | W("英文") + W("名字"))
introduction = (W("介绍") | W("是") + W("谁") | W("简介"))
person_basic = (birth | birth_place | english_name | introduction)

rating = (W("评分") | W("分") | W("分数"))
release = (W("上映"))
movie_basic = (rating | introduction | release)

when = (W("何时") | W("时候"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))
