---
name: 怀黍离 / Here a People Sows
description: 《明日方舟》2024 Side Story 新春活动，水墨怀古调性的视觉系统
colors:
  ink-black: "oklch(22% 0.01 250)"
  ink-wash-gray: "oklch(62% 0.01 250)"
  paper-white: "oklch(97% 0.005 85)"
  paper-cream: "oklch(93% 0.012 85)"
  seal-red: "oklch(48% 0.18 28)"
  jade-blue: "oklch(56% 0.10 230)"
  wheat-gold: "oklch(74% 0.13 85)"
  violet-shadow: "oklch(38% 0.10 290)"
typography:
  display:
    fontFamily: "FZQuanTangShiS-EU, '方正全唐诗宋', Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(3rem, 9vw, 7rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "0.04em"
  headline:
    fontFamily: "Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(1.75rem, 4vw, 2.75rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "0"
  title:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0"
  label:
    fontFamily: "Trajan Pro, 'Cinzel', Source Han Serif SC, serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.18em"
  latin-display:
    fontFamily: "Trajan Pro, 'Cinzel', Cormorant Garamond, serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.32em"
rounded:
  none: "0"
  hairline: "1px"
  card: "2px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
  scroll: "120px"
components:
  button-primary:
    backgroundColor: "{colors.ink-black}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.card}"
    padding: "12px 28px"
  button-primary-hover:
    backgroundColor: "{colors.seal-red}"
    textColor: "{colors.paper-white}"
  button-ghost:
    backgroundColor: "{colors.paper-cream}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.none}"
    padding: "12px 28px"
  card-scroll:
    backgroundColor: "{colors.paper-cream}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.none}"
    padding: "32px"
  seal-stamp:
    backgroundColor: "{colors.seal-red}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.card}"
    size: "56px"
---

# Design System: 怀黍离 / Here a People Sows

## 1. Overview

**Creative North Star: "一卷未干的怀古素笺" (An Unfinished Scroll of Mourned Lands)**

这套视觉系统的核心是把宋元卷轴 (handscroll) 和水墨笔触 (sumi-e brushwork) 翻译成一个 2024 年的二游活动设计语言。它不是"中国风皮肤"，而是把卷轴本身——纸的肌理、墨的浓淡、章的位置、字的节奏——直接当作 UI 的底层语法。每一帧 KV 都应当看上去像一段被剪出来的卷轴片段，而不是一张被装饰过的海报。

它显式拒绝的事：拒绝春节默认的"红金 + 烟花 + 灯笼"模板，拒绝米哈游式的金粉仙侠华彩，也拒绝二游通行的"发光圆形背板 + 居中角色 + 渐变光晕"。任何让画面"热闹起来"的诱惑都要被识别并压回——这套系统的重点是让画面**安静，并因为安静而显得厚重**。

它在《明日方舟》全局视觉规范 ([../README.md](../README.md)) 之上做的偏移是：把全局常驻的工业警戒色 (industrial alert palette) 完全替换为水墨灰阶 + 单一主色相，把无衬线 Source Han Sans 的位置让渡给 Source Han Serif (思源宋体) 与衬线拉丁体，把卡片阴影和毛玻璃 (frosted glass / acrylic material) 弱化为纸面投影。

**Key Characteristics:**
- 水墨灰阶为主基调，单一主色相为情感锚点 (one ink hue per operator)
- 50%+ 留白预算，构图节奏向卷轴看齐
- 印章红只作落款，不作装饰
- 字型走古典衬线 (Song serif + Trajan)，不用现代圆体
- 阴影几乎为零，深度由墨色浓淡和构图远近承载

## 2. Colors: The Ink-Wash Palette

整套色板锚定在一张"被时光浸黄的素笺"上。它**不是黑白**——黑被压到 ink-black，白被偏暖成 paper-white，灰被冷化为 ink-wash-gray，让纸与墨之间留出一种宋画式的温度差。

### Primary
- **Ink Black** (`oklch(22% 0.01 250)`): 主笔墨色。承担书法字、剑刃、鳞片、关键文字。**不是 #000**——纯黑会让画面像 PPT，而不是卷轴。
- **Paper White** (`oklch(97% 0.005 85)`): 主底色，承担 80% 以上画面留白。**不是 #fff**——纯白会显得冷与新，paper-white 偏暖 5%，模拟陈纸的色温。

### Secondary
- **Seal Red** (`oklch(48% 0.18 28)`): 印章红 (vermilion ink stamp)。专用于落款印、章回号、活动标识图章。**任何其他"红色"用法都视作违规**——参见下方 The Seal Rule。
- **Ink-Wash Gray** (`oklch(62% 0.01 250)`): 中间墨色，承担二级文字、远景山形、衣袂阴影、装饰水纹。

### Tertiary (干员主色相 / one-per-operator)

每位限定干员只允许携带其中一种作为主导色相，禁止同一画面内并置两种以上 tertiary。

- **Jade Blue** (`oklch(56% 0.10 230)`): 干员"左乐"专属色——剑光、水龙、青墨。
- **Wheat Gold** (`oklch(74% 0.13 85)`): 干员"黍"专属色——麦穗、衣襟、印鉴底色。
- **Violet Shadow** (`oklch(38% 0.10 290)`): 干员"黍"辅助色——发色与暗部，用于和 wheat-gold 形成日落时的明暗张力。

### Neutral
- **Paper Cream** (`oklch(93% 0.012 85)`): 卡片底 / 弹窗底 / 卷轴本体。比 paper-white 暗约 4%，用于把"卡片"从"画布"上分离开。

### Named Rules

**The Seal Rule.** 印章红 (seal-red) 在任意单一画面中**最多出现两枚**，且只能用作落款印、章号、活动徽章。它的稀缺即是它的力量——一旦被用作 CTA 按钮主色、徽章背景或装饰小红点，整张画面立刻沦为节庆海报。CTA 默认走 ink-black；若需强调，hover 态可短暂切换到 seal-red，但持续状态严禁如此。

**The One-Hue-Per-Frame Rule.** 单帧画面只允许携带一种 tertiary 色相 (jade-blue 或 wheat-gold + violet-shadow 算一组)。这是水墨语言的根性——卷轴里同时画蓝龙和金麦是分裂的，不是丰富的。

## 3. Typography

**Display Font:** Source Han Serif SC (思源宋体) — 主标题"怀黍离"三字以更接近碑刻 / 印刷宋体的字怀承担识别。
**Body Font:** Source Han Sans SC (思源黑体) — 与方舟全局规范保持一致，承担长段文字与功能性 UI。
**Latin Display:** Trajan Pro / Cinzel — 用于 *HERE A PEOPLE SOWS*、*NEW OPERATOR* 等英文小标，走 Old-Style 衬线 (碑刻风) 而非 Modern 衬线 (时装风)。

**Character:** 这是一组"端庄但不僵硬"的字型组合。中文用宋体把笔画粗细差与古典刻字感拉到前景，拉丁文用 Trajan 系衬线呼应其碑刻共祖，一中一西在同一画面共存而不打架。

### Hierarchy
- **Display** (700, 3–7rem clamp, line-height 0.95, letter-spacing 0.04em)：主 KV 上的"怀黍离"等三到四字宋体大字。允许做笔画解构和留白处理 (e.g. 把"黍"字底部做断笔)。
- **Headline** (600, 1.75–2.75rem clamp, line-height 1.15)：章节名、KV 副标题、干员代号"左乐""黍"。仍走宋体，但不做解构变形。
- **Title** (Source Han Sans 700, 1.125rem)：UI 卡片标题、关卡名。**这一层切回黑体**——是设计上的"由古入今"过渡点。
- **Body** (Source Han Sans 400, 1rem, line-height 1.7)：正文、剧情对话、奖励说明。行宽控制在 36 个汉字 / 65–75ch 以内。
- **Label** (Trajan 500, 0.75rem, letter-spacing 0.18em)：英文小标 *NEW OPERATOR*、*HERE A PEOPLE SOWS*。大字距 + 大写 + Trajan 共同承担"碑刻铭文"的氛围。
- **Latin Display** (Trajan 500, 1.25rem, letter-spacing 0.32em)：拉丁活动副标 *HERE A PEOPLE SOWS*。**禁用 Didot、Bodoni 等 Modern 衬线**——它们的现代锐利感会把卷轴变成时尚海报。

### Named Rules

**The Song-Serif-Carries-Identity Rule.** 任何承担"怀黍离"品牌识别的标题位置都必须走宋体 / 思源宋体。任何用 Source Han Sans Heavy、几何无衬线、毛笔手写体替代主标题的做法均视为违规。次级 UI 文本可以走黑体，但识别位不行。

**The No-Modern-Serif Rule.** Latin display 严禁使用 Didot、Bodoni、Playfair 等 Modern 衬线。这类字怀的极锐利收笔与卷轴的钝头藏锋互相抵消。Trajan、Cinzel、Cormorant 这类 Old-Style / Transitional 是唯一选择。

## 4. Elevation

整套系统**几乎不使用 box-shadow**。这是与方舟全局规范 (强调 Fluent Design 的卡片阴影 + Acrylic Material 毛玻璃) 之间最大的有意偏差。

深度由两件事承载：
1. **墨色浓淡** — 远景用 ink-wash-gray + 高度透明度，近景用 ink-black + 实心。**远 = 淡，近 = 浓**，这是宋画的视差语法。
2. **纸面投影** — 仅当一个元素需要被识别为"贴在画布上的另一张纸"时 (e.g. 卷轴里的一张诗笺)，才允许极轻的纸面投影。

### Shadow Vocabulary

- **Paper Drop** (`box-shadow: 0 1px 0 rgba(34, 28, 22, 0.08), 0 8px 24px -16px rgba(34, 28, 22, 0.18)`)：纸面贴纸效果。仅用于"卷轴里嵌着一张签条"或"诗笺压在素笺之上"的情境。投影方向永远向下偏 1px，模拟纸张厚度。
- 没有第二档阴影。

### Named Rules

**The Flat-By-Ink Rule.** 默认零阴影。任何元素需要被强调时，先尝试 (a) 加深墨色浓度，(b) 增大相对画面的尺寸，(c) 移近留白中心。只有以上三招都用尽仍不够时，才允许加 paper-drop。

## 5. Components

每个组件先给一句调性，再写规格。

### Buttons
- **Shape:** 直角或近似直角 (`rounded.card = 2px`)，**禁止圆角胶囊**。
- **Primary:** ink-black 底 + paper-white 字，padding `12px 28px`。点击态 / hover 态切换为 seal-red 底 (短暂)。
- **Ghost:** paper-cream 底 + ink-black 字，1px ink-wash-gray 边框。用于次级动作。
- **Hover / Focus:** primary 走"墨变红"过渡 (180ms ease-out-quart)；ghost 走"纸面变浓" (背景从 paper-cream 加深 6%)。**禁止位移、禁止缩放、禁止发光**。

### Chips
- **Style:** paper-cream 底 + ink-black 字 + 1px ink-black 边框。**未选中 / 已选中以"反相"切换**：已选中变为 ink-black 底 + paper-white 字。
- **没有第二种 chip 风格**——任何想加圆角、加渐变、加图标的诉求都要被压回。

### Cards / Containers
- **Corner Style:** `rounded.none = 0` 直角。卷轴是直边的。
- **Background:** paper-cream，必要时叠加一层 ~6% 不透明度的水墨噪点纹理 (mimicking handmade paper grain)。
- **Shadow Strategy:** 默认无阴影；仅当卡片"嵌套在更大的卷轴 / 画布"上时使用 paper-drop。
- **Border:** 1px ink-wash-gray，仅在卡片需要从 paper-white 画布上分离时使用。
- **Internal Padding:** `lg = 32px`。卷轴里的字从来不贴边。

### Inputs / Fields
- **Style:** 直角矩形，paper-cream 底，1px ink-wash-gray 描边。
- **Focus:** 描边切换为 ink-black (1px → 1.5px)，**不加发光、不加 glow**。
- **Error:** 描边切换为 seal-red (这是 seal-red 唯一的功能性用法例外)。

### Navigation
- **Style:** 横向排版，字距宽松 (≥0.18em)，全部走宋体 + 大写拉丁标签。Active 态以一道 1px ink-black 下划线表示，**不用色块、不用胶囊**。
- **Mobile treatment:** 折叠为顶栏 + 抽屉式抽出层，抽屉底色 paper-cream，覆盖时画布走 4–6px ink-wash-gray 模糊 (模拟卷轴被半合上)。

### Signature Component: Operator Scroll Card

干员介绍卡是这套系统的标志性组件，直接借鉴卷轴形制：
- **Layout:** 横向 16:9，左 30% 留白 (含小字代号、星级、职业标签)、中 40% 角色全身立绘穿越于水墨水龙 / 麦浪之间、右 30% 副标拉丁文 *NEW OPERATOR* + 干员名拼音。
- **Watermark Glyph:** 单字宋体大字 (e.g. 「黍」「乐」) 以 ~12% 不透明度水印形式贴底，作为该干员的视觉签名。
- **Seal:** 右下角或左上角放一枚 seal-red 印章 (**只一枚**)，刻干员代号或活动短语。
- **Stars:** 五角星走"扁平 + 描边" (1px ink-black)，**禁止金色填充**——金色属于"黍"专属色，普适星级不能借用。

## 6. Do's and Don'ts

### Do:
- **Do** 在 50% 以上的画面留白上落款，留白本身就是构图。
- **Do** 把每位干员的主导色相严格限制在一种——左乐 = jade-blue，黍 = wheat-gold + violet-shadow。
- **Do** 把"怀黍离"主标题走宋体大字 + 笔画解构变形 (允许在 Display 层做断笔、错位、留白处理)。
- **Do** 把英文小标走 Trajan / Cinzel + 大写 + ≥0.18em 字距，呼应碑刻铭文。
- **Do** 让 ink-black 默认承担所有 CTA 主色；hover 态才允许短暂切到 seal-red。
- **Do** 用墨色浓淡和构图远近来表达深度，**而不是用阴影**。

### Don't:
- **Don't** 把 seal-red 用作主 CTA 持续色、装饰小红点、徽章批量底色——参见 The Seal Rule，违者立刻沦为节庆海报。
- **Don't** 在同一画面内并置两种以上 tertiary 色相——参见 The One-Hue-Per-Frame Rule。
- **Don't** 用 Didot / Bodoni / Playfair 等 Modern 衬线代替 Trajan 系——参见 The No-Modern-Serif Rule。
- **Don't** 用红金大字 + 烟花 + 灯笼这套国内手游新春默认模板，即使是新春活动。
- **Don't** 加发光、加胶囊圆角、加渐变填充——这些来自二游通用 KV 模板，会立刻冲淡水墨的克制。
- **Don't** 让"中国风"沦为贴几张龙纹 PNG / 铜钱图案的贴花式装饰，必须走真实笔法的水墨绘画。
- **Don't** 把卡片阴影做大到能投出空间深度，本系统的 elevation 是平的，深度走墨色。
- **Don't** 把星级填充为金色——金属于干员"黍"，普适星级走描边 ink-black。
- **Don't** 在 CTA 按钮 hover 时使用位移 / 缩放 / glow——本活动里所有交互动效都向"水墨晕开"靠拢，不向"塑料弹起"靠拢。
