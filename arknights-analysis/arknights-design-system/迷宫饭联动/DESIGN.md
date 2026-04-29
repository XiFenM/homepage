---
name: 明日方舟 × 迷宫饭 / Arknights × Delicious in Dungeon
description: 2024 联动活动，羊皮卷食谱手账 + 探险者任务板的视觉系统
colors:
  parchment-cream: "oklch(92% 0.04 80)"
  parchment-deep: "oklch(84% 0.05 75)"
  burgundy: "oklch(38% 0.13 25)"
  wine-red: "oklch(48% 0.15 22)"
  dungeon-olive: "oklch(36% 0.025 130)"
  ink-charcoal: "oklch(20% 0.012 80)"
  warm-tan: "oklch(78% 0.07 65)"
  mustard-gold: "oklch(72% 0.13 80)"
  star-glow: "oklch(82% 0.14 88)"
  seal-vermilion: "oklch(48% 0.18 28)"
typography:
  display:
    fontFamily: "Cormorant Garamond, 'Cinzel', 'EB Garamond', serif"
    fontSize: "clamp(2.5rem, 6vw, 4.5rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.04em"
  display-italic:
    fontFamily: "Cormorant Garamond Italic, 'EB Garamond Italic', serif"
    fontSize: "clamp(2.25rem, 5vw, 4rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.02em"
    fontStyle: "italic"
  display-cjk:
    fontFamily: "Source Han Serif SC, FZSongKeBenXiuKaiS-R, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(2rem, 5vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.02em"
  recipe-title:
    fontFamily: "Source Han Sans SC Heavy, 'Noto Sans CJK SC', sans-serif"
    fontSize: "clamp(1.5rem, 3vw, 2rem)"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.04em"
  headline:
    fontFamily: "Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(1.5rem, 3vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0"
  title:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0"
  body:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0"
  label-latin:
    fontFamily: "Cormorant Garamond, 'EB Garamond', serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.22em"
  tape-handwritten:
    fontFamily: "'Caveat', 'Patrick Hand', 'Architects Daughter', cursive"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.02em"
  bender-mono:
    fontFamily: "Bender, 'Saira Semi Condensed', sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.06em"
rounded:
  none: "0"
  hairline: "1px"
  card: "4px"
  tape: "2px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.burgundy}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.card}"
    padding: "12px 28px"
  button-primary-hover:
    backgroundColor: "{colors.wine-red}"
    textColor: "{colors.star-glow}"
  button-mission:
    backgroundColor: "{colors.warm-tan}"
    textColor: "{colors.ink-charcoal}"
    rounded: "{rounded.card}"
    padding: "14px 20px"
  button-recipe:
    backgroundColor: "{colors.mustard-gold}"
    textColor: "{colors.ink-charcoal}"
    rounded: "{rounded.card}"
    padding: "12px 24px"
  card-recipe:
    backgroundColor: "{colors.dungeon-olive}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.card}"
    padding: "24px"
  card-tome:
    backgroundColor: "{colors.parchment-cream}"
    textColor: "{colors.ink-charcoal}"
    rounded: "{rounded.card}"
    padding: "32px"
  tape-label:
    backgroundColor: "{colors.parchment-deep}"
    textColor: "{colors.ink-charcoal}"
    rounded: "{rounded.tape}"
    padding: "4px 10px"
  seal-stamp:
    backgroundColor: "{colors.seal-vermilion}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.card}"
    size: "48px"
---

# Design System: 明日方舟 × 迷宫饭 / Arknights × Delicious in Dungeon

## 1. Overview

**Creative North Star: "桌游夜里被反复翻阅的一本探险者烹饪手账" (A Worn Adventurer's Cookbook on the Game-Night Table)**

这套视觉系统的工作是把迷宫饭 IP 的"探险 + 烹饪"双循环翻译成方舟 UI 形制。它显式拒绝两件事：(1) 现代手游烹饪类内容默认的"高光油亮 PBR 食物摄影"——那是商业广告的修辞，不是手账的修辞；(2) 国内联动惯用的"两个 LOGO + 渐变 + 巨大 CROSSOVER 字"懒惰模板——这条原则与罗小黑联动同源。

整套系统在《明日方舟》全局视觉规范 ([../README.md](../README.md)) 之上做的最大偏移是：把全局"工业警戒色 + 毛玻璃 acrylic"完全替换为**羊皮卷 + 暗墨纸感**。所有承载内容的画布都必须是有边缘磨损、纸纹噪点、轻微染色的纸或羊皮。任何纯色塑料底都视作违规。

它有两种调式 (mode)：
- *Recipe Mode* (食谱模式)：用于烹饪 minigame、食谱合成卡、食材展示。底色走 dungeon-olive 暗墨绿 (模拟旧手账深色封面) + parchment-cream (内页)。
- *Tome Mode* (羊皮卷模式)：用于干员档案、活动入口、剧情卡、任务中心。底色走 parchment-cream 主导 + burgundy / wine-red 包边 (模拟探险者卷宗皮革边)。

两种模式可以**在同一活动伞下出现**，但单一画面内仍然只能选一种。

**Key Characteristics:**
- 所有底色必须是纸 / 羊皮材质，禁止纯色塑料底
- 食物 / 食材 / 道具走手绘 sticker 风，禁止 3D / 写实摄影
- 食谱卡守恒结构：成品图 + 配料图 + 配料名 三段式
- 双 IP 字标平等共存，× 符号相连
- 字怀按模式区分：Tome 走衬线 italic，Recipe 走黑体 Heavy
- 装饰元素允许"草图涂鸦"——星点、箭头、罗盘、丝带

## 2. Colors

整套色板锚定在"被反复翻阅的旧探险手册"上——封面的暗皮革绿 (dungeon-olive)、内页的羊皮纸 (parchment-cream)、烫金标题的酒红镶边 (burgundy / wine-red)、章节首页的火漆印 (seal-vermilion)。色板带轻微的"做旧"气息——所有色相都向暖调偏移 5%–10%。

### Primary
- **Parchment Cream** (`oklch(92% 0.04 80)`): 主底色，承担 Tome Mode 70% 以上的画布。比怀黍离的 paper-white 多一份黄气，比罗小黑的 paper-cream 略深一档。
- **Burgundy** (`oklch(38% 0.13 25)`): 主调反差锚点，承担 Tome Mode 的卷宗包边、header bar、深色 CTA 主底。
- **Dungeon Olive** (`oklch(36% 0.025 130)`): Recipe Mode 的封面色，承担食谱卡上半区背景、深色装饰底。**带极轻微绿调**——它是"旧皮革染料"，不是"军绿"。

### Secondary
- **Wine Red** (`oklch(48% 0.15 22)`): burgundy 的亮版，承担 hover 态、丝带条、章节图标。
- **Parchment Deep** (`oklch(84% 0.05 75)`): cream 的暗版，承担纸面分层、tape label 底色、磨损区域。
- **Ink Charcoal** (`oklch(20% 0.012 80)`): 主笔墨色，承担文字、轮廓线、剪影。比 ink-black 略带暖意——这是"棕墨水"而非"碳墨水"。

### Tertiary
- **Warm Tan** (`oklch(78% 0.07 65)`): 暖米色，承担木牌、皮革标签、地图边缘。
- **Mustard Gold** (`oklch(72% 0.13 80)`): 芥末金，承担食谱卡顶部"配方"标签、精选高亮、星级数字。
- **Star Glow** (`oklch(82% 0.14 88)`): 星点黄，承担食谱卡上的"美味光点" sticker (装饰性星星与火花)。
- **Seal Vermilion** (`oklch(48% 0.18 28)`): 火漆印章红。沿用前述活动惯例——只作落款 / 章号 / 章节徽章。

### Neutral
- 不引入纯灰；所有"灰"通过 parchment-deep + ink-charcoal 的混合色实现。

### Named Rules

**The Parchment-Substrate Rule.** 所有承载内容的画布必须是纸 / 羊皮材质——带可见纸纹噪点 (≥6% 不透明度的颗粒贴图)、边缘有轻微磨损或染色、四角允许卷边。**禁止纯色塑料底** (e.g. `background: #f3e9d3`)。

**The Recipe-Three-Tier Rule.** 食谱卡严格遵循"成品图 (上) + 箭头分隔 + 配料图组 (下)" 三段式结构——这是迷宫饭原作图鉴的视觉语法。即便 UI 收纳到很小尺寸，三段式也不能合并或省略。

**The Two-IPs-Equal Rule.** 沿用罗小黑联动原则——「明日方舟 ARKNIGHTS」与「迷宫饭 DELICIOUS IN DUNGEON / ダンジョン飯」两个完整字标必须同等高度共存，× 符号相连。**禁止用机翻或自制字代替原 IP 字标**。

**The Vermilion-Seals-Only Rule.** Seal-vermilion 单帧最多两枚，仅作落款印 / 章节徽章 / 火漆封缄。任何作为"装饰小红点"的用法均视为违规。

## 3. Typography

**Display (Latin):** Cormorant Garamond + Cormorant Garamond Italic——Tome Mode 的灵魂字怀。Italic 形态承担干员名 *MARCILLE*、*LAIOS* 等核心标识；Roman 形态承担副标。
**Display (CJK):** Source Han Serif SC——承担"迷宫饭"等中文 IP 字标位置。
**Recipe Title:** Source Han Sans SC Heavy——食谱菜名 ("红烧角兽""爆炒源石虫") 必须走粗黑体，模拟日漫食谱书的视觉惯例。
**Body Font:** Source Han Sans SC——长段功能性文字。
**Latin Label:** Cormorant Garamond——*NEW OPERATOR*、*DELICIOUS ON TERRA* 等小标。
**Tape Handwritten:** Caveat / Patrick Hand——食谱卡上的"01""02""配方"等 tape label，模拟手写胶带感。
**Bender Mono:** 继承自方舟基建系统，承担关卡代号、metadata 类标签。

**Character:** 这是一组"卷宗 + 手账"的双面字型组合。Tome 模式走衬线 italic 的 D&D 角色卡惯例，Recipe 模式走粗黑体 + 手写胶带的日漫食谱书惯例。两套各自承担不同的视觉职能。

### Hierarchy
- **Display (Tome Italic)** (Cormorant Italic 600, 2.25–4rem clamp, line-height 1, letter-spacing 0.02em)：干员名 *MARCILLE*。配丝带横幅 (ribbon banner) 衬底。
- **Display (CJK)** (Source Han Serif 700, 2–3.5rem)：「迷宫饭」「玛露西尔」等中文识别字。
- **Recipe Title** (Source Han Sans Heavy 900, 1.5–2rem, letter-spacing 0.04em)：食谱菜名。允许加 1–2px ink-charcoal 描边。
- **Headline** (Source Han Serif 600, 1.5–2rem)：副标题、章节名。
- **Title** (Source Han Sans 700, 1.0625rem)：UI 卡片标题、关卡名、按钮内文。
- **Body** (Source Han Sans 400, 0.9375rem, line-height 1.7)：正文、剧情对话、奖励说明。行宽 ≤70ch。
- **Label Latin** (Cormorant 500, 0.875rem, letter-spacing 0.22em)：英文小标。
- **Tape Handwritten** (Caveat 600, 0.875rem)：食谱卡的 tape label 序号 (01, 02, …) 与"配方"标签。
- **Bender Mono** (Bender 500, 0.875rem, letter-spacing 0.06em)：关卡代号、metadata。

### Named Rules

**The Italic-Names-the-Hero Rule.** 干员名识别位置必须走 Cormorant Italic 600+——这是 D&D 角色卡 / 探险者档案的字怀惯例。**禁止用 Roman 衬线、几何 sans 或 display sans 替代**——它们会让卷宗变成博物馆标签。

**The Heavy-Names-the-Dish Rule.** 食谱菜名必须走 Source Han Sans Heavy 900——这是日漫食谱书 / 烹饪节目字幕的字怀惯例。**禁止用衬线、宋体或细黑替代**——它们会让食谱失去"美味宣告感"。

**The Tape-Is-Handwritten-Only Rule.** Caveat / Patrick Hand 类手写体只允许出现在 tape label (序号、"配方"二字、菜单分类) 位置。**禁止用于功能性 UI、按钮内文、奖励名**——可读性损失立刻沦为"过度装饰"。

## 4. Elevation

整套系统的深度走**纸面层叠 + 火漆压印 + 丝带垂落**三种隐喻，几乎不用 box-shadow 表达 z 轴。

### Shadow Vocabulary

- **Paper Layer** (`box-shadow: 0 1px 0 rgba(48, 32, 18, 0.08), 0 8px 16px -8px rgba(48, 32, 18, 0.18)`)：纸面层叠投影。用于 tape label 贴在 cream 底上、菜单卡叠在画布上。投影方向永远向下偏 1px，模拟纸张厚度。
- **Wax Press** (`box-shadow: 0 0 0 2px rgba(48, 32, 18, 0.12), 0 4px 0 -2px {colors.wine-red}`)：火漆压印阴影。用于 seal-stamp 的边缘压痕——内层 2px 暗描边 + 下方 wine-red 厚度。
- **Ribbon Drop** (`filter: drop-shadow(0 6px 12px rgba(56, 20, 16, 0.32))`)：丝带垂落阴影。用于 burgundy 丝带横幅 (ribbon banner) 在 parchment 底上的悬垂感。
- **Tome Edge** (`box-shadow: inset 0 0 24px rgba(56, 36, 20, 0.18)`)：羊皮卷边缘内阴影——用于卡片本身，让 cream 底的四周比中心更深，模拟"被反复抚摸的旧纸边"。

### Named Rules

**The No-Glow Rule.** 整套系统**禁止任何形式的 box-shadow glow**——发光、霓虹、外发光 halo 都属于现代 UI 词汇，与卷宗手账的修辞互斥。"亮"通过 mustard-gold / star-glow 色相直接表达，**而不是通过光晕表达**。

## 5. Components

### Buttons
- **Shape:** `rounded.card = 4px` 微圆角。模仿"被磨过的纸边"的圆滑感。
- **Primary (Tome):** burgundy 底 + parchment-cream 字，padding `12px 28px`。Hover 切到 wine-red 底 + star-glow 字。
- **Mission Button:** warm-tan 底 + ink-charcoal 字，左右两端各带一个细木纹装饰图标 (`◆ … ◆`) 模拟"探险者任务条"。padding `14px 20px`。**这是网页设计可直接借鉴的版式**——见下方 Signature Component。
- **Recipe Button:** mustard-gold 底 + ink-charcoal 字，padding `12px 24px`。仅用于 Recipe Mode 内的"开始烹饪"等动作。
- **Hover / Focus:** 200ms ease-out-quart 色相位移 + 1px 上浮 (translateY(-1px))。**禁止粒子飞溅、禁止火花、禁止落叶**。

### Chips
- **Style:** parchment-deep 底 + ink-charcoal 字 + 1px ink-charcoal 边框，圆角 `rounded.card = 4px`。
- **Selected:** 反相为 burgundy 底 + parchment-cream 字。
- **Tape variant:** parchment-deep 底 + Caveat 手写字 + 边角"撕痕"装饰 (使用 SVG mask 实现的不规则锯齿边)——专门用于食谱序号、章节标签。

### Cards / Containers (Tome)
- **Corner Style:** `rounded.card = 4px`。允许四角各自微弧 (e.g. 左上 6px 右下 2px) 模拟手撕纸边。
- **Background:** parchment-cream + ≥6% 不透明度纸纹噪点 + Tome Edge 内阴影。
- **Border:** **必须有 burgundy 包边** (≥6px solid 或装饰图案带)——这是 Tome Mode 的视觉标志。
- **Internal Padding:** `xl = 48px`。卷宗里的字从来不贴边。
- **Decoration:** 顶部 ribbon banner 横幅 (burgundy + wine-red 双层) 承载干员名或章节标题。

### Cards / Containers (Recipe)
- **Corner Style:** `rounded.card = 4px`。
- **Background:** **上下两段式** —— 上段 dungeon-olive 占 50% (承载成品图 + 菜名)，下段 parchment-cream 占 50% (承载配料行)，分界处用一道 1px ink-charcoal 横线 + 三个向上箭头分隔。
- **Shadow Strategy:** Paper Layer (用于卡片整体悬浮) + tape-label 顶角的小投影。
- **Decoration:** 左上角 "01""02" 序号 tape label (parchment-deep 底 + Caveat 手写)；右上角"配方"红 tape label (seal-vermilion 底 + 白字)；菜品图周围散落 3–5 个 star-glow 小星点 (静态 SVG)。
- **Internal Padding:** `lg = 24px`。

### Inputs / Fields
- **Style:** 4px 圆角矩形，parchment-cream 底，1px ink-charcoal 描边。
- **Focus:** 描边切换为 burgundy (1.5px)。
- **Error:** 描边切换为 wine-red。

### Navigation
- **Style:** Tome Mode 走 Cormorant Italic 横向排列；Recipe Mode 走 Source Han Sans Heavy 标签条。
- **Active state:** Tome 走丝带书签 (ribbon bookmark) 标记 (一道下垂的 wine-red 短带)；Recipe 走 mustard-gold 胶囊背景。

### Signature Component: Mission Central / 任务中心面板

**这是本系统的标志性组件，对网页设计 (尤其是 dashboard / hero panel / mission board 类形态) 参考价值最大。** 它演示了如何把"装饰性立绘 + 功能性按钮堆叠"在同一屏内并置，而不让两者互相破坏。

参考资料：[../../arknights-art/迷宫饭联动/12_*.webp](../../arknights-art/迷宫饭联动/12_ming-ri-fang-zhou-ge-ren-dong-tai-ming-ri-fang-zhou-dong-tai-ji-lu-bi-li-bi-li-shi-pin.webp)

**Layout (vertical / mobile-portrait baseline，桌面端按需扩展为左右分栏):**

```
┌─────────────────────────────────────┐
│ ▌新增商主题  [chibi]    [明日方舟标]│  ← header bar (burgundy)
├─────────────────────────────────────┤
│                                     │
│   [角色立绘穿过整个画面，              │
│    向右下方延伸，与按钮堆叠错位]        │
│                                     │
│         ╭──────────────────╮       │
│         │  13.5             │       │  ← floor / level numeric
│         │  Mission Central  │       │     (Cormorant italic + Bender)
│         ╰──────────────────╯       │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ ◆ 任务一名称           ▶    │   │  ← mission button (warm-tan)
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │ ◆ 任务二名称           ▶    │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │ ◆ 任务三名称           ▶    │   │
│  └─────────────────────────────┘   │
│                                     │
├─────────────────────────────────────┤
│       明日方舟  ×  迷宫饭            │  ← footer (双 IP 字标)
└─────────────────────────────────────┘
```

**Specs:**
- **Outer Frame:** parchment-cream 底 + 顶部 burgundy 32px header bar + 底部 burgundy 24px footer bar，整张 panel 用 Tome Edge 内阴影包裹。
- **Header Bar:** 左侧 Source Han Sans Heavy 1.0625rem "新增商主题"标签 + 中央装饰图标 (chibi sticker 或火漆图章) + 右侧"明日方舟"字标。背景 `burgundy` + 底部 1px wine-red 分隔线。
- **Hero Character Slot:** 角色立绘 (e.g. 玛露西尔) 从 panel 上半区中心起发，**允许越过中部到下半区按钮区**——立绘的脚步会"踩"到第一个 mission button 的左上角。这是本系统标志性的"立绘穿越功能边界"手法，让画面不显得呆板。
- **Mission Central Title Block:** 居中放置，外框 parchment-deep + 1px ink-charcoal hairline，内填两行：(1) 大数字 "13.5" 走 Bender 关卡代号字; (2) "Mission Central" 走 Cormorant Italic 1.25rem。两行之间一道 1px wine-red 装饰横线。
- **Mission Button Stack:** 3–6 条横向按钮垂直堆叠，间距 8px。每条按钮：warm-tan 底 (`{colors.warm-tan}`)，padding `14px 20px`，左侧一枚 ink-charcoal 装饰菱形图标 (`◆`)，右侧一枚 ink-charcoal 箭头 (`▶`)，中间任务名走 Source Han Sans 700 1.0625rem。**Hover:** 底色加深 6% + translateX(-2px) 左移露出右侧装饰条 (一道 wine-red 4px 高的标记)。
- **Footer:** 居中双 IP 字标 + × 符号 + 极小 Cormorant 版权字 (e.g. "© Hypergryph & Kadokawa")。

**Web Adaptation Notes:**
- 桌面端 (≥1024px): 把竖版 panel 拆为左右分栏——左侧 40% 角色立绘 + 右侧 60% Mission Central title + button stack。立绘仍可越过中线 5–10% 进入按钮区。
- 移动端 (≤640px): 保持原始竖版形制，立绘按比例缩小，按钮全宽。
- 按钮堆叠不要超过 6 条——超过则改用 2 列网格 (仍保持 warm-tan 横条样式)。
- 这套形制可直接复用于 web hero / dashboard landing / quest log 等场景。

## 6. Do's and Don'ts

### Do:
- **Do** 让所有承载内容的画布都是纸 / 羊皮材质——带噪点、带磨损、带轻微染色——参见 The Parchment-Substrate Rule。
- **Do** 让食谱卡严格遵循"成品图 + 配料图 + 配料名"三段式结构——参见 The Recipe-Three-Tier Rule。
- **Do** 让两个 IP 字标按 1:1 高度比同等呈现，× 符号相连——参见 The Two-IPs-Equal Rule。
- **Do** 用 Cormorant Italic 600+ 写干员名 (Marcille / Laios)——参见 The Italic-Names-the-Hero Rule。
- **Do** 用 Source Han Sans Heavy 900 写食谱菜名——参见 The Heavy-Names-the-Dish Rule。
- **Do** 让 tape label 上的手写字 (Caveat) 只承担装饰序号 / "配方" 标签——参见 The Tape-Is-Handwritten-Only Rule。
- **Do** 让 Mission Central 任务板的角色立绘越过功能边界 (从装饰区延伸到按钮区)——这是本系统标志性的"立绘穿越"手法。
- **Do** 让 seal-vermilion 沿用前述活动的克制原则——参见 The Vermilion-Seals-Only Rule。

### Don't:
- **Don't** 用纯色塑料底承载内容，必须是纸感。
- **Don't** 用 3D 渲染图 / 写实摄影做食物 / 食材 / 道具插画——必须是手绘 sticker。
- **Don't** 用现代手游烹饪类常见的"高光油亮 PBR 食物渲染 + 蒸汽光晕"——参见 PRODUCT.md 反例清单。
- **Don't** 用米哈游"原神料理"式高对比度发光蒸汽 + 角色聚光灯演出。
- **Don't** 用国内联动惯用的"两个 LOGO + 渐变 + 巨大 CROSSOVER 字"模板。
- **Don't** 把方舟的工业警戒色 (alert orange、警戒条纹、霓虹) 带入本活动——羊皮卷上没有警戒条纹。
- **Don't** 用 box-shadow glow / 外发光 halo——参见 The No-Glow Rule。
- **Don't** 用 Roman 衬线、几何 sans 或 display sans 写干员名——参见 The Italic-Names-the-Hero Rule。
- **Don't** 用宋体 / 细黑写食谱菜名——参见 The Heavy-Names-the-Dish Rule。
- **Don't** 用手写体 (Caveat) 写按钮内文 / 奖励名 / 关卡名——参见 The Tape-Is-Handwritten-Only Rule。
- **Don't** 用机翻或自制字代替原 IP 字标——双 IP 字标必须用各自的官方版本。
- **Don't** 用过度卡通化的低龄烹饪游戏画风 (高饱和糖果色 + 圆头几何字)——迷宫饭原作是成人向漫画。
- **Don't** 用现代极简餐厅风 (大留白 + 无衬线 + 白底冷色)——它表达"高级餐饮"，与"地下城烹饪"完全相反。
