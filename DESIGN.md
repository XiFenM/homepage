---
name: 晚樵庐 / The Late Woodcutter's Hut
description: 沈殷桀（夕丰木）的个人网站 — 晚樵庐主站 + 勿忘我彩蛋，桌游夜的灯下记事
colors:
  # ── Signature Layer (怀黍离继承，全站可见)
  ink-black: "oklch(22% 0.01 250)"
  paper-white: "oklch(97% 0.005 85)"
  seal-red: "oklch(48% 0.18 28)"

  # ── Homepage Fork (书桌场景，桥接 Quiet + Map)
  desk-walnut: "oklch(28% 0.04 55)"
  desk-walnut-deep: "oklch(20% 0.03 50)"
  lamp-glow: "oklch(82% 0.10 75)"
  dust-mote: "oklch(70% 0.02 60)"

  # ── Quiet Mode (罗小黑联动继承)
  quiet-paper: "oklch(96% 0.012 90)"
  quiet-lime: "oklch(86% 0.16 125)"
  quiet-lime-deep: "oklch(72% 0.18 130)"
  quiet-ink-mountain: "oklch(38% 0.02 145)"
  quiet-mist: "oklch(88% 0.01 145)"

  # ── Map Mode (迷宫饭联动继承)
  map-parchment: "oklch(89% 0.04 80)"
  map-parchment-deep: "oklch(78% 0.05 75)"
  map-parchment-edge: "oklch(68% 0.06 70)"
  map-burgundy: "oklch(34% 0.12 25)"
  map-dungeon-olive: "oklch(42% 0.08 110)"
  map-mustard-gold: "oklch(72% 0.14 75)"

  # ── Cosmos Sub-zone (星语共愿继承，仅观星塔)
  cosmos-deep-night: "oklch(15% 0.03 260)"
  cosmos-pearl-blue: "oklch(72% 0.08 240)"
  cosmos-ice-white: "oklch(95% 0.01 240)"
  cosmos-tangerine: "oklch(78% 0.13 60)"

typography:
  display-brush:
    fontFamily: "晚樵庐 手写字标 (custom hand-lettered SVG)"
    fontSize: "clamp(2.8rem, 8vw, 5rem)"
    fontWeight: "n/a (vector)"
    lineHeight: 1
    letterSpacing: "normal"
  display-serif-zh:
    fontFamily: "Source Han Serif SC, 思源宋体, Songti SC, serif"
    fontSize: "clamp(2rem, 5vw, 3.2rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  display-serif-en:
    fontFamily: "Cormorant Garamond, EB Garamond, Georgia, serif"
    fontSize: "clamp(2rem, 5vw, 3.2rem)"
    fontWeight: 400
    fontStyle: "italic"
    lineHeight: 1.2
    letterSpacing: "0.01em"
  heading-zh:
    fontFamily: "Source Han Sans SC, 思源黑体, PingFang SC, sans-serif"
    fontSize: "clamp(1.4rem, 2.6vw, 1.8rem)"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "-0.03em"
  heading-en:
    fontFamily: "Cinzel, Trajan Pro, serif"
    fontSize: "clamp(1.4rem, 2.6vw, 1.8rem)"
    fontWeight: 600
    letterSpacing: "0.05em"
  body-zh:
    fontFamily: "Source Han Sans SC, 思源黑体, PingFang SC, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "-0.005em"
  body-en:
    fontFamily: "Inter, Source Han Sans SC, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  label-mono:
    fontFamily: "Bender, JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.78rem"
    fontWeight: 500
    letterSpacing: "0.08em"
  handwritten:
    fontFamily: "Caveat, Kalam, cursive"
    fontSize: "1.05rem"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "normal"

rounded:
  none: "0"
  sticker: "2px"
  pill: "9999px"

spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
  xxl: "128px"
  scroll-margin: "12vw"

components:
  homepage-scroll-card:
    backgroundColor: "{colors.map-parchment}"
    textColor: "{colors.map-burgundy}"
    rounded: "{rounded.none}"
    padding: "32px"
  homepage-sticky-note:
    backgroundColor: "{colors.quiet-lime}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.sticker}"
    padding: "24px"
  hotspot-marker:
    backgroundColor: "{colors.map-mustard-gold}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.pill}"
    size: "20px"
  hotspot-peek-card:
    backgroundColor: "{colors.map-parchment}"
    textColor: "{colors.map-burgundy}"
    rounded: "{rounded.none}"
    padding: "24px"
  quiet-tag-pill:
    backgroundColor: "{colors.quiet-paper}"
    textColor: "{colors.quiet-ink-mountain}"
    rounded: "{rounded.pill}"
    padding: "6px 14px"
  quiet-archive-card:
    backgroundColor: "{colors.quiet-paper}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.sticker}"
    padding: "32px"
  cosmos-observation-card:
    backgroundColor: "{colors.cosmos-deep-night}"
    textColor: "{colors.cosmos-ice-white}"
    rounded: "{rounded.none}"
    padding: "32px"
  signature-seal:
    backgroundColor: "{colors.seal-red}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.none}"
    size: "44px"
  language-toggle:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.sticker}"
    padding: "4px 10px"
---

# Design System: 晚樵庐 / The Late Woodcutter's Hut

## 1. Overview

**Creative North Star: "深夜的一间晚樵庐——桌上摊开一堆春绿丝带束扎的卡片，桌角微露一卷未走完的旧地图 (A late woodcutter's hut at night, with a stack of cards tied in spring-green silk at the desk's center, and an old half-unrolled map peeking out from one corner)"**

整个站点是一个比喻：访客打开浏览器的那一刻，是在推开**晚樵庐**的门——屋里只点了一盏暖灯，桌上摊着樵夫晚归后留下的卡片堆（5 张卡片，各代表他的一个面）。这就是站点的全部主体——访客随时可以读完卡片离开，也可以多停留看看屋里别的东西。如果他们仔细看，会发现桌子的某一角微微露出一卷羊皮——那是 **勿忘我**，樵夫的旧地图，**只有好奇心强、停留够久的访客才会发现并打开它**。樵夫不在屋里——但屋里所有东西都是他的，所以**屋子本身就是他的自我介绍**。

这套设计系统**显式拒绝**程序员个人页的所有训练数据反射：拒绝黑底终端字体的 hacker chic、拒绝 Linktree-style 按钮列、拒绝 about/projects/contact 三段式 SaaS 模板、拒绝 GitHub-contribution-grid 等"勤奋指标"、拒绝米哈游式高饱和发光二游 KV、拒绝任何 30 秒 self-intro 段落、拒绝凡尔赛腔与 LinkedIn 简历腔、拒绝交友站措辞、拒绝任何**显式 CTA 引导访客去找彩蛋**。**所有这些反例的对立面才是这套系统。**

它的方法是**四源继承，非平分** — 全站风格脉络精确分配到五个区域：

| 区域 | 继承源 | DESIGN.md 引用 |
|---|---|---|
| Signature Layer (印章 / 章节落款 / 语言切换 — 全站可见) | **怀黍离** (印章红 + 卷轴留白) | `arknights-analysis/arknights-design-system/怀黍离/DESIGN.md` |
| 晚樵庐 Hero Zone (站点主体落地，书桌 + 卡片堆 + 微露卷轴) | 桥接 — 桌面木色 + 灯光 + 卡片 + 彩蛋触发器 | (本文件原创) |
| 晚樵庐 Quiet Mode (简约站内容区) | **罗小黑联动** (春绿关节 + 纸感档案) | `arknights-analysis/arknights-design-system/罗小黑联动/DESIGN.md` |
| 勿忘我 Map Mode (彩蛋地图主面) | **迷宫饭联动** (羊皮卷 + 桌游夜手账) | `arknights-analysis/arknights-design-system/迷宫饭联动/DESIGN.md` |
| Cosmos Sub-zone (勿忘我观星塔 hotspot) | **星语共愿** (深夜天文台 + 手写贺卡) | `arknights-analysis/arknights-design-system/星语共愿/DESIGN.md` |

**Key Characteristics:**

- 五区，每区单一调色板 — 不在同一帧内混用两区的色
- 全站 OKLCH，无 `#000` / `#fff` — 所有"黑白"向品牌色相微偏移
- 留白 ≥40%（勿忘我羊皮卷四周）/ ≥50%（晚樵庐默认页）
- 中英对等，字号比与排版比一致；语言切换不丢位
- 静态画 + 微动效 — 不做拖拽地图、不做横向滑动 hero、不做视差欺骗
- 无 box-shadow（勿忘我 / 晚樵庐）；纸感来自 grain 纹与 ink 描边
- 印章红 (seal-red) 是站点签名 — 仅出现于落款 / 章节分隔 / 语言切换标签
- AI 生成视觉资产 — 每个图像位的提示词都在本文件 §5 内成规
- **彩蛋触发的视觉路径无 CTA 文字** — 卷轴一角的微露 + 鼠标接近时 V2 慢慢展开本身就是邀请；任何"点击探索 / Click for surprise"类提示语都违反 spec

## 2. Colors: The Five-Zone Palette

整套色彩策略是 **Multi-zone Committed** — 全站不是单一调色板，而是五块调色板各占其地。每块单独看是 Committed (一个主色相承担 30–60% 表面)，合在一起又靠 Signature Layer 的印章红 + ink-black + paper-white 串成一根线。

### Signature Layer（全站使用）

仅出现在落款、章节分隔、印章、语言切换这些"签名级别"的地方——**像署名印章而非装饰元素**。

- **Ink Black** (`oklch(22% 0.01 250)`)：所有正文字色。蓝偏移而非纯黑——比 `#000` 柔和、读久不刺眼。
- **Paper White** (`oklch(97% 0.005 85)`)：所有"白色"的实际值。米偏移——印章红压在它上面比压在纯白上更协调。
- **Seal Red / 印章红** (`oklch(48% 0.18 28)`)：仅用于盖印 / 落款 / 章节切片末尾的小三角符 / 语言切换标签的活跃态。**绝不大面积铺涂**。

### 晚樵庐 Hero Zone（站点主体首屏：书桌 + 卡片堆 + 彩蛋卷轴）

访客落地的全部第一印象——他们不需要"选边"，直接坐在了晚樵庐的桌前。

- **Desk Walnut** (`oklch(28% 0.04 55)`)：桌面主色。深木色，温暖偏冷。
- **Desk Walnut Deep** (`oklch(20% 0.03 50)`)：桌面阴影部分（不是 shadow，是绘画里的暗部）。
- **Lamp Glow** (`oklch(82% 0.10 75)`)：暖灯光圈。圆形 radial gradient，从中心 100% opacity 衰减到外缘 0%，覆盖整个 hero 视口的中央 60%。
- **Dust Mote** (`oklch(70% 0.02 60)`)：飘动的微尘颗粒，4–6px，opacity 0.3–0.6。

> **桌上摊放位置**：S5C 卡片堆居中（视觉重心，主导航）；S4 卷轴在桌面**左下角或抽屉一角**仅微露 5–10%（彩蛋触发器，鼠标接近时 V2 展开）。绝不让卷轴与卡片堆并排同等大小——比例约 1:3，卷轴仅作"角落细节"。

### Quiet Mode Palette（简约站）

继承自罗小黑联动。**春绿是关节，不是底色** (lime is a hinge, not a wash)——简约站的底色是 paper，不是 lime。

- **Quiet Paper** (`oklch(96% 0.012 90)`)：默认背景 / 卡片底。比 paper-white 略暖一档。
- **Quiet Lime** (`oklch(86% 0.16 125)`)：accent 仅用于 link / hover / tag pill 的活跃态 / 章节小图标。**总占面 ≤8%**。
- **Quiet Lime Deep** (`oklch(72% 0.18 130)`)：链接 visited / 强调段落中的 inline mark 颜色。
- **Quiet Ink Mountain** (`oklch(38% 0.02 145)`)：副文本 / 元数据色。绿偏移的灰，与 ink-black 区分但仍在同一冷线上。
- **Quiet Mist** (`oklch(88% 0.01 145)`)：分隔线 / 章节背景 tint，极弱的绿灰。

### 勿忘我 Map Palette（彩蛋地图主面）

继承自迷宫饭联动。**羊皮卷是底层语言** (parchment is the substrate)——所有承载内容的"画布"必须是羊皮纸材质。

- **Map Parchment** (`oklch(89% 0.04 80)`)：异世界地图的主底色。淡黄牛皮纸调。
- **Map Parchment Deep** (`oklch(78% 0.05 75)`)：羊皮被翻多了的深旧区，hotspot 周围的轻微染色。
- **Map Parchment Edge** (`oklch(68% 0.06 70)`)：纸边磨损 / 卷起处的暗色。
- **Map Burgundy** (`oklch(34% 0.12 25)`)：勿忘我地图正文色 / 章节标题 / hotspot peek 卡片标题。沉郁的酒红，像旧手册的标注墨水。
- **Map Dungeon Olive** (`oklch(42% 0.08 110)`)：地图上"地形"颜色——森林、山林、地下城阴影。
- **Map Mustard Gold** (`oklch(72% 0.14 75)`)：hotspot 标记圆点的主色。亮但不刺眼。

### Cosmos Sub-zone Palette（勿忘我观星塔 hotspot）

继承自星语共愿。**仅在观星塔 hotspot 弹出时切换**——其它任何 hotspot 都不沾这套色。

- **Cosmos Deep Night** (`oklch(15% 0.03 260)`)：星空底色。极深的蓝紫，不是黑。
- **Cosmos Pearl Blue** (`oklch(72% 0.08 240)`)：星座与天文标记的主色。澄澈，温柔。
- **Cosmos Ice White** (`oklch(95% 0.01 240)`)：星点 / 银河带 / 文字色。蓝偏移的白。
- **Cosmos Tangerine** (`oklch(78% 0.13 60)`)：手写愿望文本色（仅"我希望"开头的句子用这个）。来自星语共愿对"愿望文本"的处理。

### Named Rules

**The Zone Doctrine.** 五个区域的色板**绝不在同一帧内混用**。访客在晚樵庐内容区看到 quiet-lime 时不可能同时看到 map-burgundy；走到 Cosmos Sub-zone 时背景必须从 parchment 整体过渡到 cosmos-deep-night（V3 5 秒过场视频 / reduced-motion 下用 600ms opacity-blend）。混用即违规。**例外**：晚樵庐 Hero Zone 因含彩蛋触发器（卷轴一角微露），允许 desk-walnut + 极小一角 map-parchment 共存——这是叙事必要，不是混用。

**The Signature-Red-Reserved Rule.** seal-red 是签名色，全站任何位置的占面 ≤2%。**禁止做按钮主色 / 链接默认色 / 大标题色**。它出现的位置永远像"盖了一个章"——小、方、有重量。

**The No-Pure-Black/White Rule.** 全站禁用 `#000` 与 `#fff`。所有"黑白"都通过 chroma 0.005–0.015 的微偏移 (向蓝 / 米 / 绿) 与品牌色相对齐。这一条无例外。

**The Lime-As-Hinge Rule.** quiet-lime 不铺底色——只在 (a) 链接 / hover、(b) tag pill 活跃态、(c) 章节小图标、(d) 晚樵庐签名落款的小绿点、(e) S5C 卡片堆的束扎丝带 出现。**禁止用作区块背景或大色块**。

**The Cosmos-Lockout Rule.** Cosmos Sub-zone 的 4 个色仅在观星塔 hotspot 内部使用。勿忘我地图主面、其它 hotspot、晚樵庐 Hero Zone、晚樵庐内容区均**禁止**使用 cosmos-* 任何 token。

## 3. Typography

**Display 手写字标:** 「晚樵庐」自定义手写 SVG (从星语共愿"主标保留笔触感"借来的手法 — 见 §5 Component "Brush Wordmark")
**Display Serif 中文:** Source Han Serif SC (思源宋体) — 勿忘我章节大标题、卷首语
**Display Serif 英文:** Cormorant Garamond Italic — 干员 / 内容主体的英文标题、引文
**Heading 中文:** Source Han Sans SC Heavy (思源黑体重) — 简约站章节标题、技术博客标题
**Heading 英文:** Cinzel — 勿忘我 hotspot 名 / 章节标题英文版
**Body 中文:** Source Han Sans SC Regular — 全站正文中文
**Body 英文:** Inter — 全站正文英文
**Label / Mono:** Bender — 元数据 / 标签 / 时间戳 (从方舟基建系统继承的"工业残留")
**Handwritten:** Caveat — 简约站便签内的手写关键词、首页便签内容、Cosmos 愿望文本

**Character:** 中西并置、衬无衬分工。中文宋体 (Source Han Serif) 与英文 Cormorant Garamond Italic 共同承担"古典骑士精神"——这是勿忘我的字体气场；简约站走中文黑体 (Source Han Sans Heavy) + 英文 Cinzel 承担"档案 / 卷宗"气场；Bender 在两个模式都作为元数据标识"工业 / 系统残留"。Caveat 仅在"私人手写"位置出现 (便签 / 愿望)，禁止承担 UI 文本。

### Hierarchy

- **Display Brush** (custom SVG, clamp 2.8–5rem, line-height 1)：仅用于站名 "晚樵庐" 在 hero 出现的位置 — 首页一次、简约站头一次、勿忘我不出现 (勿忘我 hero 是地图本身)。
- **Display Serif 中文** (Source Han Serif SC 600, clamp 2–3.2rem, line-height 1.2)：勿忘我章节大标题、卷首语。
- **Display Serif 英文** (Cormorant Garamond Italic 400, clamp 2–3.2rem)：勿忘我英文版章节大标题、引文起首。
- **Heading 中文** (Source Han Sans SC 700, clamp 1.4–1.8rem, letter-spacing -0.03em)：简约站章节标题、博客标题。
- **Heading 英文** (Cinzel 600, clamp 1.4–1.8rem, letter-spacing 0.05em)：简约站章节标题英文版、勿忘我 hotspot 卡片标题。
- **Body** (Source Han Sans SC 400 / Inter 400, 16px, line-height 1.7)：所有正文。**最大行宽 65–75ch**。
- **Label / Mono** (Bender / JetBrains Mono 500, 0.78rem, letter-spacing 0.08em)：元数据 (时间戳、阅读分钟、技术栈标签)。
- **Handwritten** (Caveat 500, 1.05rem)：便签关键词、Cosmos 愿望文本起首。

### Named Rules

**The Bilingual Equal Rule.** 中英对等不是字号相等——而是**文字密度感**相等。中文方块字密度高，所以 1rem 中文 ≈ 1rem 英文; 但中文 letter-spacing 应为 `-0.005em` (微紧)，英文为 `normal` 或 `0.01em` (微松)，让两版面对应行宽。**禁止英文做小一档 (0.85em) 来"塞进同样空间"——这就是把英文当二等公民**。

**The Brush-Marks-the-Welcome Rule.** 「晚樵庐」手写字标 (display-brush) 仅出现在三个位置：(a) 首页 hero 桌面左上、(b) 简约站头部、(c) 站点 favicon / og-image 微缩版。**禁止在内文段落、章节标题、按钮、链接里使用手写字标——它是签名，不是字体**。

**The Bender-Stays-Industrial Rule.** Bender 只用于元数据 (时间戳、技术栈、坐标轴、版本号)。**禁止用 Bender 写正文、章节标题或导航**——它在方舟原系统里是基建系统的工业残留字，本站继承这个分工。

**The Serif-Speaks-Mood-Sans-Speaks-Function Rule.** 勿忘我走衬线 (Source Han Serif + Cormorant Italic) 表达情绪/手账感；简约站走无衬 (Source Han Sans Heavy + Cinzel caps) 表达档案/速览感。**禁止在简约站内文用衬线、在勿忘我章节标题用 Heavy 黑体**——字怀分工与模式分工绑定。

**The Handwritten-Is-Personal-Only Rule.** Caveat 仅在 (a) 首页便签内手写关键词、(b) Cosmos 观星塔愿望文本、(c) 简约站第一屏的"今日感兴趣"标签内文 出现。**禁止在 navigation、按钮、长段正文里用 Caveat**——它太"私人"，泛用即廉价。

## 4. Elevation

整个站点**默认 flat-by-ink** — 不靠 box-shadow 表达层级，靠 ink 描边 + grain 纹 + opacity 分层 + 静态绘画里的明暗关系。

例外：Homepage Fork 的 lamp-glow 是 radial gradient 渲染的"绘画式光照"，而非 box-shadow；Cosmos Sub-zone 的星空深度是多层 z-depth 的星点 opacity 分层，也不用 box-shadow。

### Why Flat-By-Ink

box-shadow 是数字界面的产物，与"羊皮卷 / 春绿便签 / 桌游夜灯下"的物理材质语境冲突。一张羊皮卷不会"漂浮"在另一张羊皮卷上方——它们在桌面上是侧靠的、有褶皱的、互相压住一角的。这种关系用 ink 描边 + 纸边磨损纹理表达，不用 shadow。

### Depth Vocabulary（无 box-shadow）

- **Ink Outline** (`border: 1px solid {colors.ink-black}` 或 `0.5px solid {colors.map-burgundy}`)：勿忘我 / 简约站卡片边缘的描边。**禁止 ≥2px 的实线边框**——会失去手账感。
- **Grain Overlay** (`background-image: url('grain.png'); mix-blend-mode: multiply; opacity: 0.08–0.15`)：卡片底纹。给所有"纸面"添加触感。
- **Edge Wear** (SVG mask)：羊皮卷四角与卷起边缘的磨损 — 静态贴图，不动。
- **Lamp Halo** (radial gradient)：仅 Homepage Fork 使用。`background: radial-gradient(circle at 30% 30%, var(--lamp-glow) 0%, transparent 70%);`
- **Atmospheric Layering** (Cosmos)：星点分 3 层 (远 / 中 / 近)，opacity 0.4 / 0.7 / 1.0；不用 box-shadow，靠数量与大小变化表达深度。

### Named Rules

**The Flat-By-Ink Rule.** 全站禁用 `box-shadow`。任何看似"浮起"的元素必须改为 ink outline + grain overlay + 在绘画里画上明暗，**不用 CSS shadow**。例外：Homepage Fork 的 lamp-glow，但它是 radial gradient 不是 box-shadow。

**The Atmosphere-Not-Shadow Rule.** Cosmos 区域的"深空感"由星点 opacity 分层、银河带 blur、星座连线粗细变化共同构成——**禁止用 backdrop-filter blur 或 box-shadow 模拟空气感**。

**The No-Levitation Rule.** 卡片不上浮、不悬停抬升、不 transform: translateY(-2px) on hover。状态变化由颜色 + 描边粗细表达，不由"高度"表达。这是对"羊皮卷压在桌面上"这一物理事实的尊重。

## 5. Components

每个组件先一句性格描述，再列形状、色、状态、AI 资产提示词（如适用）。

### 晚樵庐 Hero Scene (站点主体首屏：书桌 + 卡片堆 + 彩蛋卷轴)

**Character:** 一张俯视角的暖灯下书桌——桌面中央摊着一堆春绿丝带束扎的卡片（5 张，分类内容入口），桌面左下/抽屉一角微微露出一卷羊皮（彩蛋触发器）。访客落地即在此——他们不需要做"选择"，而是直接坐在了这张桌子前。**卡片堆是显眼的主导航；卷轴是好奇心强的人才会发现的秘密。**

**Scene 视觉规格：**
- 背景静态层：S3 final.png（desk-walnut 木桌 + 灯光圈 + 远处书架剪影）
- 背景动态层（V1）：8 秒循环视频，painterly shimmer + 飘尘飘动，reduced-motion 下退化为 S3 静态图
- 灯光圈：lamp-glow radial gradient 覆盖中心 60% 视口，opacity 1 → 0（已包含在 S3 中）

**Card Stack (S5C 卡片堆，桌面中央，主导航)：**
- 资产：S5C final.png（含 5 张档案卡 + 春绿丝带 + 蝴蝶结）
- 占视口：约 35% width × 45% height，center-x 与 center-y 都居中
- 表面：cream paper 底 + 春绿丝带束扎 + 5 张卡片右上角 motif（山水 / 花草 / 星点 / 朱砂章 / 留白）
- 5 张卡片 = 5 个内容分类入口（技术 / 生活 / 兴趣 / 杂念 / 留白——映射详见 [`web/app/components/CardStack.vue`](web/app/components/CardStack.vue) 的 `cards` 常量）
- Hover 一张卡片（motion 启用）：该卡的 motif 角落出现 1px ink-black 描边 + 微亮（CSS filter brightness 1.08）；**禁止 translateY 抬升（The No-Levitation Rule）**
- Hover (reduced-motion)：仅描边，不变亮
- Focus (键盘)：8px ink-black 双环虚线（与 hotspot 标记一致）
- Click 一张卡片：进入对应分类页面（`/tech`、`/life`、`/interests`、`/thoughts`、`/blank`）

**Easter-Egg Scroll (S4 卷轴一角，桌面左下，彩蛋触发器)：**
- 资产：S4 final.png（半展开羊皮卷地图）
- 占视口：约 12% width × 8% height（**仅一角微露**，主体被裁切到画外）
- 位置：桌面左下角或抽屉一角，约视口左下 (5%, 75%) 处
- 默认态：仅露 5–10% 卷面，能隐约看到塔尖剪影或一两个金色 hotspot
- Hover (motion 启用)：V2 视频接管，5 秒内卷轴慢慢展开 → 露出更多地图内容；展开到约 70% 时显示 ink-black "进入" 文本（仅此处可有，是发现仪式）
- Hover (reduced-motion)：直接显示 S6 地图缩略图静态预览，无展开动画
- Click：触发 V3 过场（5 秒）→ 进入勿忘我地图全屏视图
- **绝对禁止**：在卷轴附近添加任何 CTA 文字、箭头指引、提示气泡、引导动画。卷轴自身的"微露"就是邀请。

**Footer Easter-Egg Link (页脚冗余路径)：**
- 位置：所有页面页脚右下
- 文案：「**还在某处游荡** / still wandering somewhere...」
- 字体：label-mono Bender 0.78rem，颜色 ink-black × 0.6 opacity
- Hover：颜色变为 seal-red × 0.8
- Click：跳转 `/map`

**URL Direct Path：**
- `/map` 与 `/勿忘我` 都直达勿忘我地图主面（直接播放 V3 入场动画，跳过卷轴展开过程）

**AI Prompt for the desk scene background (无两件物件)：**
```
A high-angle (overhead 75° tilt) view of an old wooden writing desk in a quiet evening study,
warm walnut wood grain (oklch 28% 0.04 55), partially lit by a single warm desk lamp from
upper-left casting a soft circular glow (oklch 82% 0.10 75) covering ~60% of the frame.
The lit area is centered on the desk surface; edges fall into deep walnut shadow
(oklch 20% 0.03 50). Floating dust motes (4–6 visible) catch the light. Empty desk surface —
NO papers, NO objects, NO text. Background: dim study room with bookshelf silhouettes
fading into darkness. Painterly digital illustration style, NOT photorealistic, NOT 3D rendered,
NOT photographed. Mood: late-night, calm, board-game-night warmth. Texture: visible brush strokes,
slight parchment-grain overlay across whole image. Composition: centered, with negative space
for two objects to be composited in (one left-center, one right-center).
Anti-references: NOT cyberpunk, NOT industrial, NOT modern minimalist, NOT photo-real,
NOT high-saturation. Reference inspiration: Studio Ghibli interior backgrounds, early
Trigger animation backgrounds, Delicious in Dungeon kitchen scenes.
Output: 16:9, 4K.
```

**AI Prompt for the parchment scroll (front view):**
```
A half-unrolled aged parchment scroll, lying flat, viewed from above. Paper color: warm
oklch 89% 0.04 80 with grain texture. Edges show wear, fold creases, slight darkening at curls.
Visible content on the unrolled portion: a corner of an isometric fantasy world map showing
a tower silhouette (top), a small stream (middle), and 3–4 glowing dot markers (oklch 72%
0.14 75 mustard gold). Style: hand-drawn, painterly, NOT digital map, NOT modern infographic.
Inspired by D&D campaign maps, Tolkien-era fantasy cartography, Delicious in Dungeon's
recipe-tome aesthetic. NO text, NO labels visible. NO 3D rendering, NO photorealism.
Output PNG with transparent background. 1024×768.
```

**Note：sticky note 已废弃。** 本架构 v2 把"右物件"从单张春绿便签升级为 S5C 春绿丝带束扎的档案卡片堆——见 [`assert-preparation/prompts/static/S5-quiet-object.md`](assert-preparation/prompts/static/S5-quiet-object.md) 与 [`generated/static/S5C/final.png`](assert-preparation/generated/static/S5C/final.png)。完整 prompt 在 [`generator/prompts.py`](assert-preparation/generator/prompts.py) 的 `S5C` 常量。

### Hotspot Marker (地图标记圆点)

**Character:** 一颗在羊皮地图上发出微光的金色小点——访客的眼睛会本能地被它吸引但不会被它打扰。

- 形状：圆 (rounded.pill)，size 20px (desktop) / 16px (mobile)
- 默认态：map-mustard-gold 实心圆 + 1px ink-black 描边
- Hover (motion 启用)：径向 8s 慢速呼吸 (scale 1 → 1.15 → 1)，外缘添加 lamp-glow 模糊 60% opacity
- Hover (reduced-motion)：仅外缘 lamp-glow 静态显示，不呼吸
- Focus (键盘)：8px ink-black 双环虚线
- 点击：触发 hotspot-peek-card 出现

### Hotspot Peek Card (hotspot 弹出卡)

**Character:** 像翻开手账上一页——羊皮纸右下角写着这个 hotspot 的故事。

- 形状：不规则矩形，右下角微卷 (paper-curl SVG mask)
- 大小：clamp(280px, 30vw, 420px) × auto
- 位置：从对应 hotspot 圆点向"羊皮卷外缘"飞出 (transform-origin: hotspot 坐标，scale 0.6 → 1, 320ms ease-out-quart)
- 表面：map-parchment + grain overlay
- 内容结构：
  - 标题 (Source Han Serif SC 600 / Cormorant Italic 400)
  - 1–2 段正文 (Source Han Sans SC 400)
  - 底部一行 Bender 元数据 (Coordinates / Visited Count / Last Update)
  - 右下角 4mm 印章红 signature-seal
- 关闭：ESC / 点击外部 / 点击右上角 ✕（手绘体）

### Quiet Tag Pill (简约站关键词标签)

**Character:** 一颗能从便签上抠下来贴到日记本里的轻便标签。

- 形状：rounded.pill，padding 6px 14px
- 默认态：quiet-paper 底 + quiet-ink-mountain 文字 + 1px quiet-mist 描边
- Hover：quiet-lime 底 + ink-black 文字 (200ms ease-out)
- Active / 已选：quiet-lime-deep 底 + paper-white 文字
- 字体：body-zh / body-en，0.875rem
- 内容：5–7 个并排，水平 wrap，间距 spacing.sm

### Quiet Archive Card (简约站博客 / 内容卡)

**Character:** 像一张干员档案卡，但内容是技术博客或生活记录——继承罗小黑联动 Operator Archive Card 形制。

- 形状：rounded.sticker (2px 微圆角，几乎方)
- 表面：quiet-paper 底 + grain overlay
- 边框：1px ink-black 描边（hover 时切换为 quiet-lime-deep）
- 内部布局：
  - 顶部 Bender 元数据条 (date / tags / read-time)
  - 主标题 (Source Han Sans SC 700 / Cinzel 600)
  - 副标题 / 摘录 (body, 2–3 行截断)
  - 底部右下角 4mm seal-red 小章 (signature-seal)
- Hover：边框换色，描边粗细仍 1px（不加粗，No-Levitation Rule）

### Cosmos Observation Card (观星塔 hotspot 内卡片)

**Character:** 一张深夜天文台的观测记录——访客点开"观星塔" hotspot 后，整个屏幕从羊皮卷过渡到星空。

- 全屏接管，背景 cosmos-deep-night + 星点 SVG 分 3 层
- 卡片：cosmos-deep-night × 0.85 opacity 上叠加 1px cosmos-pearl-blue 描边
- 标题：Source Han Serif SC 600 (中) / Cormorant Italic 400 (英)，cosmos-ice-white
- 正文：Source Han Sans SC 400 / Inter 400，cosmos-ice-white × 0.85
- 引用愿望句 (Caveat)：cosmos-tangerine，仅"我希望" / "I wish" 起首的句子用
- 关闭：星空慢速 fade out (1200ms) → 回到 map parchment

### Signature Seal (印章红方章)

**Character:** 整个站点的署名——像一枚樵夫盖在每件物品角落的小私章。

- 形状：4mm × 4mm 方形 (rounded.none)
- 颜色：seal-red 底 + paper-white 文字
- 文字：「桀」单字 (display-serif-zh) 或 「XFM」三字母 (Cinzel) — 两种版本，按区域选
- 位置：所有内容卡 / 章节末尾的右下角，距边缘 spacing.md
- 不可点击 / 不可 hover — 它是**静默的签名**，不是 UI 元素

**AI Prompt for the seal stamp asset:**
```
A small Chinese-style red ink seal/stamp print (4×4 ratio), traditional vermilion red
(oklch 48% 0.18 28), as if pressed onto cream paper. Slight edge unevenness, faint blur
at corners (typical of hand-pressed seals). Single character "桀" (or "XFM" Latin variant)
in seal script (篆书) inside, white reserved space. PNG with transparent background. 256×256.
Anti-references: NOT digital sticker, NOT vector-clean — preserve the imperfect hand-pressed
quality. Reference: traditional Chinese 印章 / 落款印.
```

### Brush Wordmark「晚樵庐」(站点字标)

**Character:** 整个站点身份的"手写签名"——继承星语共愿"主标保留笔触感"那招。

- 资产：自定义手写 SVG，三个字 + 拼音 "WǍN QIÁO LÚ"（小一档，下方）
- 笔触：可见起笔 / 收笔 / 飞白；不是字体输出
- 颜色：ink-black 描边 + 笔锋部分微微透出底色
- 出现位置：(a) 首页 hero 桌面左上方（压在台灯光圈外缘）、(b) 简约站头部、(c) favicon / og-image 微缩
- 大小：clamp(2.8rem, 8vw, 5rem)（Display Brush token 控制）

**AI Prompt for the brush wordmark:**
```
Three Chinese characters "晚樵庐" hand-brushed in ink calligraphy (行书 semi-cursive style),
arranged horizontally. Ink color: deep ink-black with cool blue undertone (oklch 22% 0.01 250).
Visible brush dynamics: starting strokes show ink loading, ending strokes show feathering
(飞白). Slight ink bleed at strokes that paused. Below the characters, much smaller, the
pinyin "WǍN QIÁO LÚ" in custom Latin calligraphy that visually rhymes with the brush style
(NOT a system font — also hand-drawn, with similar weight modulation). Background: transparent.
Anti-references: NOT a font output, NOT vector-clean, NOT laser-precise. Preserve every
imperfection of a single take. Reference: Wang Xizhi 行书, Japanese 書道 brushwork, Akira
Kurosawa film title cards. SVG output preferred (or PNG 2048×768 transparent).
```

### Language Toggle (语言切换)

**Character:** 一张桌面上的小标签——不是 dropdown，不是 select。

- 位置：所有页面右上角同位置 (top: spacing.lg, right: spacing.lg)
- 形状：两个并排的 rounded.sticker 微圆角小标签
- 默认态：paper-white 底 + ink-black 文字
- 活跃态：seal-red 底 + paper-white 文字（小印章语义）
- 字体：label-mono 0.78rem
- 文字：「中 / EN」
- 切换：保留当前 hotspot / 当前页面位置，不重新加载到 hero

### World Map (勿忘我底图)

**Character:** 整个勿忘我赖以存在的画——一张精绘等距异世界地图，访客在它上面慢慢行走。

- 渲染：单张 SVG / WebP 静态图，不是拼图
- 风格：等距 (isometric)，俯视 ~45°
- 主色板：map-parchment 底 + map-dungeon-olive (森林山林) + map-mustard-gold (高光) + map-burgundy (远处建筑)
- 包含 5 大区域 (与 PRODUCT.md 对应) + 8–10 个 hotspot 圆点：
  - 西部「鸢尾平原」(Iris Plains) — 生活 / 旅行
  - 北方「钢铁书库」(Ironbound Library) — 技术博客
  - 东方「烹饪窝棚」(Cooking Hut) — 迷宫饭 / 动漫 / 游戏
  - 山顶「观星塔」(Stargazer's Tower) — 天文宇宙 (该 hotspot 触发 Cosmos Sub-zone)
  - 地图边缘「旅人客栈」(Wayfarer's Inn) — About Me as a Person
  - 其它 3–5 个 hotspot 由内容增长决定，分散在五大区之间

**AI Prompt for the World Map:**
```
An isometric (45° overhead tilt) hand-illustrated fantasy world map painted on aged parchment
(base color oklch 89% 0.04 80). The map covers a small fictional landmass with five regions,
arranged across a 16:9 canvas:

  - WEST: "Iris Plains" — rolling hills covered in iris/lavender wildflowers, a single
    winding road, scattered with a few wayposts.
  - NORTH: "Ironbound Library" — a dark stone tower with iron-banded architecture, half-
    embedded into a low mountain. Books and scrolls visible through tower windows.
  - EAST: "Cooking Hut" — a small wooden cottage with a smoking chimney, surrounded by
    herbs and a vegetable garden. A pot is visible inside through the door.
  - PEAK (top center, on a high mountain): "Stargazer's Tower" — a slender tall observatory
    with a domed top, telescope visible through the dome opening. The mountaintop is
    slightly bluer/cooler in tone (hint of cosmos-pearl-blue oklch 72% 0.08 240).
  - SOUTH-EDGE / BORDER: "Wayfarer's Inn" — a humble traveler's inn with warm windows lit,
    sitting at the edge of where the map dissolves into mist.

Color palette: parchment base, dungeon-olive (oklch 42% 0.08 110) for forests/hills,
mustard-gold (oklch 72% 0.14 75) accents for paths and structures, burgundy (oklch 34%
0.12 25) for distant building outlines. Edges of the map show wear, fold creases, slight
darkening at corners.

Hand-drawn style, painterly, NOT digital map, NOT 3D, NOT photorealistic. Inspired by:
Tolkien's Middle-earth maps, D&D campaign cartography, Delicious in Dungeon recipe-tome
illustrations, Studio Ghibli world maps. Mountains painted with visible brushstrokes,
tree clusters as small painted dots not detailed individual trees.

Hotspot dot positions: leave 8–10 small clear circles (~24px each at full canvas) where
markers will be composited later — distribute approximately: 2 in Iris Plains, 1 at
Ironbound Library, 2 at Cooking Hut, 1 at Stargazer's Tower (this one slightly larger),
1 at Wayfarer's Inn, plus 2–3 floating between regions. Mark these positions with a
pencil-light cross — they'll be replaced by SVG markers in code.

Output: 4096×2304 (4K, 16:9), PNG, with the parchment grain texture intact.
```

### Cosmos Starfield (观星塔背景)

**Character:** 当访客点开观星塔 hotspot 时整个屏幕被这片星空接管——不是地图叠加，是世界切换。

- 渲染：3 层星点 SVG 分别 z-index：远 (opacity 0.4, size 1px) / 中 (opacity 0.7, size 2px) / 近 (opacity 1.0, size 3–5px + glow)
- 包含：散点星 + 1–2 条银河带 (cosmos-pearl-blue × 0.4 模糊带状) + 几个识别星座连线 (cosmos-pearl-blue × 0.6 1px 直线)
- 微动效：近层星点慢呼吸 (8s, scale 0.9 → 1)；reduced-motion 下完全静止
- 与地图过渡：opacity-blend 600ms (parchment opacity 1 → 0, starfield opacity 0 → 1)

**AI Prompt for Cosmos Starfield:**
```
A deep night sky background, base color oklch 15% 0.03 260 (deep night blue with slight
violet undertone, NOT pure black). Stars distributed naturally (NOT in grid):
  - ~200 distant tiny stars (1px equivalent), oklch 95% 0.01 240 (ice white), low brightness.
  - ~80 mid-distance stars (2px), oklch 95% 0.01 240, medium brightness.
  - ~30 close stars (3–5px), oklch 95% 0.01 240 with subtle radial glow halo
    (oklch 72% 0.08 240 pearl-blue), bright.
  - One faint Milky Way band crossing the canvas diagonally — soft cloudy band of
    oklch 72% 0.08 240 at ~30% opacity, blurred.
  - Two recognizable constellations marked with thin 1px connecting lines in
    oklch 72% 0.08 240 at 60% opacity (e.g. Orion's belt, Cassiopeia W shape).
NO text, NO planets, NO moons, NO nebulae with high color saturation. The whole image
should feel like a quiet observatory's view on a clear night, NOT a cosmic event.
Style: minimal painterly, slight grain overlay (very subtle, like film grain).
Anti-references: NOT space-opera neon, NOT high-saturation nebula clouds, NOT NASA
photograph realism. Reference: vintage star charts, Studio Ghibli night skies, observatory
posters. 4096×2304 PNG.
```

## 6. Do's and Don'ts

每条 Don't 都直接对应 PRODUCT.md 的 Anti-references 或本文件的 Named Rules — 视觉规范在执行战略立场。

### Do:

- **Do** 用 OKLCH 表达全部色 token；任何 hex 表示都仅出现在导出层而非源真值。
- **Do** 让每张 AI 生成图都通过本文件 §5 内的 prompt 模板生成；**禁止"看着办"或"GPT 自由发挥"提示词**。
- **Do** 在五个区域的色板**严格不混用**——同一帧不出现 quiet-lime + map-parchment 同框，除了晚樵庐 Hero Zone（卷轴一角微露这个彩蛋触发器允许 desk-walnut + 极小 map-parchment 共存，是叙事必要）。
- **Do** 保持晚樵庐任何卡片 / 章节内最大行宽 65–75ch，让访客能舒服地读。
- **Do** 把 seal-red 用作签名 — 出现在内容卡右下、章节末尾、语言切换活跃态。**仅这三类位置**。
- **Do** 中英对等输出——任何文本块都有 `data-lang-zh` / `data-lang-en` 双版本，字号比一致。
- **Do** 在 Cosmos Sub-zone 内**全屏接管**，其它任何 hotspot 仅在地图原位弹卡片。
- **Do** 在所有动效背后提供 `prefers-reduced-motion` 完整静态版本——不是降级，是平等替代。包括晚樵庐 V1 桌面循环、彩蛋卷轴 V2 hover 展开、勿忘我 V3 入场都要有静态等效。
- **Do** 让 hotspot Tab 顺序按"叙事推荐"而非地理坐标——第一个 Tab 应该是访客最适合作为入口的那一个。
- **Do** 写勿忘我地图羊皮卷时给四周保留至少 12vw scroll-margin 的纸面留白——卷轴的余地是它的呼吸。
- **Do** 让彩蛋触发器（卷轴一角）**键盘可达 + 屏阅器有 alt 文本**（比如 `alt="一卷未走完的旧地图，可点击进入"`）——视觉路径之外 URL 与页脚链接是无障碍兜底。

### Don't:

- **Don't** 在任何位置使用 `#000` 与 `#fff`——所有"黑白"都通过 chroma 0.005–0.015 微偏移。**The No-Pure-Black/White Rule**.
- **Don't** 使用 `box-shadow`——任何"浮起感"改用 ink outline + grain + 绘画明暗。**The Flat-By-Ink Rule**.
- **Don't** 把晚樵庐与勿忘我做成同等公民式的导航（旧 fork 模式已废弃）——勿忘我是彩蛋，不是另一半。**carry from PRODUCT.md Design Principle #1**.
- **Don't** 在彩蛋触发器附近放任何 CTA 文字、箭头指引、提示气泡、引导动画——卷轴一角的微露 + V2 慢慢展开本身就是邀请。**carry from PRODUCT.md anti-ref #9 + Design Principle #3**.
- **Don't** 在站内任何位置放 GitHub-contribution-grid / Wakatime 时长 / 编程语言占比饼图等"勤奋指标"。**carry from PRODUCT.md anti-ref #4**.
- **Don't** 写 30 秒人设介绍段落 ("Hi, I'm [name], a [role] passionate about [things]")。**carry from PRODUCT.md anti-ref #6 + Design Principle #2**.
- **Don't** 用 Linktree-style 按钮列做主信息载体。**carry from PRODUCT.md anti-ref #2**.
- **Don't** 在晚樵庐任何位置出现"找伴侣 / 我在找一个 [adjectives] 的人"信号——只有在勿忘我「旅人客栈」hotspot 内部才允许出现该话题，且仍要克制。**carry from PRODUCT.md Design Principle #7**.
- **Don't** 在勿忘我 hotspot 卡片上加米哈游式的发光圆形背板 / 渐变光晕。**carry from PRODUCT.md anti-ref #5**.
- **Don't** 让英文版本字号小于中文版本来"塞进同样空间"。**The Bilingual Equal Rule**.
- **Don't** 在晚樵庐章节标题用衬线，也别在勿忘我章节标题用 Heavy 黑体。**The Serif-Speaks-Mood-Sans-Speaks-Function Rule**.
- **Don't** 用 Bender 写正文或导航——它仅承担元数据 (时间戳、技术栈、坐标)。**The Bender-Stays-Industrial Rule**.
- **Don't** 用 Caveat 手写体写按钮 / 导航 / 长段正文——它仅出现在 S5C 卡片角落 motif、Cosmos 愿望、关键词标签三个位置。**The Handwritten-Is-Personal-Only Rule**.
- **Don't** 把站名手写字标 (display-brush) 用作章节标题或按钮——它只是 hero 的签名。**The Brush-Marks-the-Welcome Rule**.
- **Don't** 让 hotspot 圆点 hover 时 transform: translateY 上浮——状态变化用呼吸 / 光晕表达，不用"高度"。**The No-Levitation Rule**.
- **Don't** 在勿忘我地图做横向滑动 hero 或视差 (parallax) 欺骗——本站是**静态画 + 微动效**，不是 scrolltelling 站。
- **Don't** 在勿忘我地图的羊皮卷上加现代衬线 (Playfair / Lora / Merriweather)——所有英文衬线限定 Cormorant Garamond Italic / Cinzel；中文衬线限定 Source Han Serif。
- **Don't** 让语言切换按钮使用 dropdown / select native 控件——它是桌面上的小标签，不是表单元素。
- **Don't** 把整套印章红 (seal-red) 用作按钮主色 / 链接默认色 / 大标题色。**The Signature-Red-Reserved Rule**.
- **Don't** 让 Cosmos 区域的色 (cosmos-*) 出现在勿忘我地图主面或晚樵庐任何位置。**The Cosmos-Lockout Rule**.
