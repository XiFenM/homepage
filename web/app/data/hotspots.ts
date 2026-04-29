/**
 * 勿忘我地图 — hotspot data.
 *
 * Array order = Tab order (per DESIGN.md "narrative-recommended sequence,
 * not geographic"). Visitors most likely to keep reading land first on the
 * "self" entry (Wayfarer's Inn), and the Cosmos hotspot — which steals the
 * whole viewport — is reached last.
 *
 * Bilingual content lives here, not in i18n JSON, because each hotspot is
 * a structured artifact (paragraphs / three-column / wishes) and inlining
 * keeps the editorial context readable.
 */

export type HotspotKind = 'peek' | 'cosmos'
export type Region = 'self' | 'tech' | 'life' | 'interests' | 'thoughts' | 'cosmos'

export interface Bilingual {
  zh: string
  en: string
}

export interface ParagraphBody {
  type: 'paragraphs'
  paragraphs: Bilingual[]
}

export interface ColumnBody {
  type: 'columns'
  columns: {
    label: Bilingual
    items: Bilingual[]
  }[]
}

export interface WishBody {
  type: 'wishes'
  wishes: Bilingual[]
}

export interface Hotspot {
  id: string
  kind: HotspotKind
  region: Region
  title: Bilingual
  /** Position on the map image, percentages relative to the 16:9 frame. */
  position: { x: string; y: string }
  body: ParagraphBody | ColumnBody | WishBody
  /** Bender mono metadata strip at the bottom of the peek card. */
  meta?: Bilingual
  /** "延伸阅读" link to a quiet-mode category page; absent for map-only notes. */
  link?: { to: string; label: Bilingual }
}

export const hotspots: Hotspot[] = [
  {
    id: 'wayfarer',
    kind: 'peek',
    region: 'self',
    title: { zh: '旅人客栈', en: "Wayfarer's Inn" },
    position: { x: '47%', y: '78%' },
    body: {
      type: 'columns',
      columns: [
        {
          label: { zh: '我相信', en: 'I believe in' },
          items: [
            { zh: '慢一点比快一点更接近真实。', en: 'Slow being closer to true than fast.' },
            { zh: '别人喜欢什么，远比他在做什么更说明问题。', en: 'What people love tells you more than what they do.' },
            { zh: '一个能把"还没想清楚"四个字讲完的人。', en: 'Someone who can finish the sentence "I haven\'t thought it through yet."' },
          ],
        },
        {
          label: { zh: '我感动于', en: "I'm moved by" },
          items: [
            { zh: '朋友为我解释完一个复杂概念后，问我"还想再听一遍吗"。', en: 'A friend who finishes explaining something hard and asks, "want me to go through it once more?"' },
            { zh: '路边遛狗的人停下来等狗闻完一棵树。', en: 'People who pause while walking their dog so the dog can finish smelling a tree.' },
            { zh: '一段代码的注释只写了"不要碰这里"。', en: 'A code comment that just says "don\'t touch this".' },
          ],
        },
        {
          label: { zh: '我害怕', en: 'I fear' },
          items: [
            { zh: '把"忙"当成不必跟自己对话的借口。', en: 'Using "busy" as an excuse not to have a conversation with myself.' },
            { zh: '表演热情来代替真的喜欢。', en: 'Performing enthusiasm in place of actually liking something.' },
          ],
        },
      ],
    },
    meta: { zh: '坐标 47.78°西 · 上次造访：私下', en: 'Coords 47.78°W · last visit: privately' },
  },
  {
    id: 'ironbound-library',
    kind: 'peek',
    region: 'tech',
    title: { zh: '钢铁书库', en: 'Ironbound Library' },
    position: { x: '17%', y: '18%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '墙上挂着的书目大多没读完。我留下笔记不是为了完工——是为了让"还没想清楚"这四个字看起来有形状。',
          en: "Most of the books on the wall are unfinished. I keep notes not to wrap things up, but to give shape to the sentence “I haven’t thought it through yet”.",
        },
      ],
    },
    meta: { zh: '坐标 17.18°北 · 灯一直亮着', en: 'Coords 17.18°N · the lamp stays on' },
    link: { to: '/tech', label: { zh: '在书库里读完整 →', en: 'read on at the library →' } },
  },
  {
    id: 'iris-plains-north',
    kind: 'peek',
    region: 'life',
    title: { zh: '鸢尾平原·北', en: 'Iris Plains, North' },
    position: { x: '16%', y: '47%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '风大的日子。一段路走完，鞋底沾的全是花粉。生活里大部分事情其实就跟散步差不多——你不知道下一段路会不会更好，但脚不停就是了。',
          en: 'A windy day. By the end of the walk my soles were dusted with pollen. Most of life is like walking — you can’t tell if the next stretch will be better, you just keep your feet moving.',
        },
      ],
    },
    meta: { zh: '坐标 16.47°西 · 风四级', en: 'Coords 16.47°W · wind: fresh breeze' },
    link: { to: '/life', label: { zh: '在平原上走得更远 →', en: 'keep walking →' } },
  },
  {
    id: 'cooking-hut',
    kind: 'peek',
    region: 'interests',
    title: { zh: '烹饪窝棚', en: 'Cooking Hut' },
    position: { x: '79%', y: '48%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '屋后种着迷迭香、罗勒、几株不开花的薄荷。锅里在炖什么没说——但门口有一排不同时期的桌游骰子摆得整整齐齐。',
          en: 'Rosemary, basil, and a few stubborn unflowering mints out back. What’s in the pot isn’t said — but a row of board-game dice from different eras lines up neatly by the door.',
        },
      ],
    },
    meta: { zh: '坐标 79.48°东 · 锅里咕嘟咕嘟', en: 'Coords 79.48°E · something simmering' },
    link: { to: '/interests', label: { zh: '在窝棚里坐久一点 →', en: 'linger at the hut →' } },
  },
  {
    id: 'mountain-path',
    kind: 'peek',
    region: 'thoughts',
    title: { zh: '山径杂记', en: 'Mountain Path Notes' },
    position: { x: '38%', y: '30%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '这条路没有名字。走在上面经常想起不该这个钟点想的事。',
          en: 'This path doesn’t have a name. Walking it tends to bring up things I shouldn’t be thinking about at this hour.',
        },
      ],
    },
    meta: { zh: '坐标 38.30°中 · 凌晨一点之后', en: 'Coords 38.30° · past 1 AM' },
    link: { to: '/thoughts', label: { zh: '听更多杂念 →', en: 'more late-night thoughts →' } },
  },
  {
    id: 'iris-plains-south',
    kind: 'peek',
    region: 'life',
    title: { zh: '鸢尾平原·南', en: 'Iris Plains, South' },
    position: { x: '12%', y: '62%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '南边的鸢尾比北边的小一些，颜色更深。',
          en: 'The irises in the south are smaller and darker than in the north.',
        },
      ],
    },
    meta: { zh: '一片不上图的小田', en: 'a small field, off any map' },
  },
  {
    id: 'forest-tree',
    kind: 'peek',
    region: 'thoughts',
    title: { zh: '林间一棵树', en: 'A Tree in the Forest' },
    position: { x: '62%', y: '60%' },
    body: {
      type: 'paragraphs',
      paragraphs: [
        {
          zh: '林子里有一棵和别的树都不一样的树。我没有拍下来。',
          en: 'There’s a tree in this forest that doesn’t match any of the others. I didn’t photograph it.',
        },
      ],
    },
    meta: { zh: '一处不要标注的位置', en: 'a spot best left unmarked' },
  },
  {
    id: 'stargazer-tower',
    kind: 'cosmos',
    region: 'cosmos',
    title: { zh: '观星塔', en: "Stargazer's Tower" },
    position: { x: '50%', y: '8%' },
    body: {
      type: 'wishes',
      wishes: [
        {
          zh: '我希望某个夜里，能在阳台上认全一个新星座。',
          en: 'I wish to learn a new constellation by name from my balcony, on some night.',
        },
        {
          zh: '我希望系外行星里，至少有一颗有人正在看回来。',
          en: 'I wish that on at least one of those exoplanets, someone is looking back.',
        },
        {
          zh: '我希望弄清楚为什么我看星空时会安静。',
          en: 'I wish I could figure out why looking at the sky makes me quiet.',
        },
      ],
    },
    meta: { zh: '观测日期 2026 · BX-7 反射式 · 坐标 N/A', en: 'observation 2026 · BX-7 reflector · coords N/A' },
  },
]
