---
name: 星语共愿 / Wishes from Stars
description: 《明日方舟》2025–2026 跨年周年纪念活动，珍珠星空 + 糖果生贺的双调式视觉系统
colors:
  pearl-blue: "oklch(78% 0.06 240)"
  ice-white: "oklch(96% 0.008 240)"
  starlight-platinum: "oklch(88% 0.015 240)"
  deep-night: "oklch(28% 0.05 250)"
  silver-mist: "oklch(72% 0.012 240)"
  candy-pink: "oklch(80% 0.10 20)"
  candy-blue: "oklch(70% 0.13 240)"
  buttercream: "oklch(94% 0.04 80)"
  ribbon-navy: "oklch(38% 0.10 250)"
typography:
  display:
    fontFamily: "FZShangKeS-EU, '方正尚酷宋', Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(2.75rem, 8vw, 6rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.06em"
  display-script:
    fontFamily: "Tangerine, 'Petit Formal Script', 'Pinyon Script', cursive"
    fontSize: "clamp(2rem, 5vw, 3.75rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0"
  headline:
    fontFamily: "Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(1.5rem, 3.5vw, 2.25rem)"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.02em"
  title:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  body:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0"
  label:
    fontFamily: "Cormorant Garamond, 'EB Garamond', serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.24em"
rounded:
  hairline: "1px"
  card: "8px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.deep-night}"
    textColor: "{colors.ice-white}"
    rounded: "{rounded.card}"
    padding: "12px 32px"
  button-primary-hover:
    backgroundColor: "{colors.ribbon-navy}"
    textColor: "{colors.starlight-platinum}"
  button-celebration:
    backgroundColor: "{colors.candy-pink}"
    textColor: "{colors.ice-white}"
    rounded: "{rounded.pill}"
    padding: "10px 24px"
  card-poster:
    backgroundColor: "{colors.ice-white}"
    textColor: "{colors.deep-night}"
    rounded: "{rounded.card}"
    padding: "32px"
  card-celebration:
    backgroundColor: "{colors.buttercream}"
    textColor: "{colors.ribbon-navy}"
    rounded: "{rounded.card}"
    padding: "24px"
---

# Design System: 星语共愿 / Wishes from Stars

## 1. Overview

**Creative North Star: "深夜天文台里的一封手写贺卡" (A Handwritten Card from the Midnight Observatory)**

这套视觉系统同时承担两件相关但不同的事：(1) 周年纪念的**正式情绪入口**——仰望、许愿、回望；(2) 博士生日玩法的**轻盈情感落点**——蛋糕、彩带、礼物。前者是 *Star Mode*，后者是 *Celebration Mode*，在同一活动伞下双调式 (dual-voice) 共存。

主调 *Star Mode* 把珍珠蓝、冰白、银白和深夜蓝堆成一种"高明度低对比"的天文台氛围，让光成为画面的主角而非反差成为画面的主角。它显式拒绝米哈游"星穹铁道"式的金属质感与玻璃粒子聚光灯——那是"璀璨"的修辞，不是"许愿"的修辞。它也拒绝国内手游周年常用的金红霓虹大字烟花套路。

副调 *Celebration Mode* 把糖果粉、糖果蓝、奶油黄堆成一种儿童绘本式的暖色场景，**只在"博士生日"这条具体支线**里被启用。它的存在是为了让玩家从主调的"被尊重"过渡到"被宠爱"——但绝不能反客为主。

整套系统在《明日方舟》全局视觉规范 ([../README.md](../README.md)) 之上做的偏移是：把全局工业警戒色完全换成珍珠蓝 + 糖果色，把毛玻璃 (acrylic material) 从"工业玻璃"重新解读为"凝结在玻璃罩上的水汽"，把卡片阴影从"扁平卡片漂浮"重新解读为"贺卡贴在木桌上"。

**Key Characteristics:**
- 双调式 (dual-voice)：Star Mode 主，Celebration Mode 副，副不能盖主
- 高明度低对比，靠柔光和留白而非反差表达层级
- 手写笔触作为品牌签名 (主标 + 副标 + 拉丁草书)
- 阴影偏向"贴纸式柔影"，与水墨克制 / 工业 acrylic 都不同
- 半透明层次承担"窥见过往" (透过冰晶看到去年的画面) 的隐喻

## 2. Colors

整套色板锚定在"清晨四点的天文台 + 桌上一盒手作蛋糕"的双场景上。Star 与 Celebration 各占一半色板，且**互不混用**——一个画面要么 Star，要么 Celebration，不允许"半 Star 半 Celebration"。

### Primary (Star Mode)
- **Pearl Blue** (`oklch(78% 0.06 240)`): 主调主色。承担天空、PV 标题底色、KV 主纹理、光晕底色。
- **Ice White** (`oklch(96% 0.008 240)`): 主调底色，承担 70% 以上画面留白。**不是 #fff**——偏冷 5%，模拟雪天清晨。
- **Deep Night** (`oklch(28% 0.05 250)`): 主调反差锚点，承担文字、CTA、星点、关键描边。

### Secondary (Star Mode)
- **Starlight Platinum** (`oklch(88% 0.015 240)`): 银白星光，承担分隔线、玻璃罩、次级文字。
- **Silver Mist** (`oklch(72% 0.012 240)`): 雾灰，承担三级文字、远景剪影、装饰水汽。

### Tertiary (Celebration Mode)
- **Candy Pink** (`oklch(80% 0.10 20)`): 副调主色，承担蛋糕奶油、气球、彩带主体。
- **Candy Blue** (`oklch(70% 0.13 240)`): 副调副色，承担蛋糕底盘、丝带、礼盒装饰。
- **Buttercream** (`oklch(94% 0.04 80)`): 副调底色，替代 Star 的 ice-white 用于副调画面。
- **Ribbon Navy** (`oklch(38% 0.10 250)`): 副调反差锚点，承担副调画面里的文字与描边。比 Star 的 deep-night 更暖一些，与 buttercream 形成更亲和的反差。

### Neutral
- 主调下用 ice-white、starlight-platinum、silver-mist 三层叠合代替单一中性色——这是本系统的特点。**不引入纯灰** (any pure gray)，所有"灰"都偏一点点冷蓝。

### Named Rules

**The Two-Voices Rule.** 任意一个画面只能选 Star Mode 或 Celebration Mode 中的一种，不能并置。两种调式的过渡 (e.g. 玩家从主活动入口走到生贺玩法) 通过**场景切换**完成，而不是在同一画面里混色。混色会立刻让活动质感滑向"派对模板"。

**The No-Glitter Rule.** 任何"金属高光""光晕粒子""Lens flare 镜头光斑""3D 玻璃反射"都被禁止。表达"光"的合法手段是：(a) 大面积柔光渐变 (`radial-gradient` 半径 ≥40% 视口)、(b) 半透明白色叠层、(c) 极轻的星点 sticker (静态 SVG，**不闪**)。

**The High-Lightness-Low-Contrast Rule.** 主调画面的明度集中在 70%–96% 区间 (oklch L 值)，对比度通过明度差 ≤25% 表达。这是"清晨""星空许愿"该有的视觉湿度。任何超过 50% 明度差的局部都需要被压回，除非它是一段必须被读懂的功能性文字。

## 3. Typography

**Display Font (中文):** Source Han Serif SC (思源宋体) 或 FZShangKeS (方正尚酷宋) 风格变体——保留笔锋的现代宋体，主标"星语共愿"的字怀更接近"印刷的手写感"而非碑刻。
**Display Script (拉丁):** Tangerine / Petit Formal Script / Pinyon Script——草书衬线，承担副标 *WISHES FROM STARS* 与生贺 *Happy Birthdays* 等手写片段。
**Body Font:** Source Han Sans SC (思源黑体)——与方舟全局规范保持一致。
**Latin Label:** Cormorant Garamond — Old-Style 衬线，承担英文小标。

**Character:** 这是一组"清晨在贺卡上写字"的字型组合。中文宋体保留笔锋但不锐利，拉丁草书保留连笔但不潦草，黑体只在长段功能性文字里出现。三种字怀在画面里要呈现出"被同一支笔轻轻写下"的统一感。

### Hierarchy
- **Display** (Source Han Serif 600, 2.75–6rem clamp, line-height 1, letter-spacing 0.06em)：主 KV 上的"星语共愿"四字。允许在中宫做轻微开放和笔画断锋处理，但不做激进解构。
- **Display Script** (Tangerine 400, 2–3.75rem clamp)：副标 *WISHES FROM STARS* 与生贺 *Happy Birthdays*。允许略微倾斜 (≤6°) 与基线起伏。
- **Headline** (Source Han Serif 500, 1.5–2.25rem)：章节标题、PV 副标。
- **Title** (Source Han Sans 600, 1.125rem)：UI 卡片标题、关卡名。
- **Body** (Source Han Sans 400, 0.9375rem, line-height 1.7)：正文、剧情对话、奖励说明。行宽 ≤ 70ch。
- **Label** (Cormorant 500, 0.875rem, letter-spacing 0.24em)：英文小标。大字距 + 大写 + Garamond 共同承担"贺卡铭文"的氛围。

### Named Rules

**The Brushstroke-in-the-Mark Rule.** 主标"星语共愿"必须保留可见的笔触感——允许字怀边缘出现轻微的不规则"墨化"边或起笔的轻量飞白。**禁止使用 Source Han Sans Heavy / 几何无衬线**作为主标——这会立刻把"许愿"翻译成"宣告"。

**The Script-for-Wishes-Only Rule.** Display Script (草书) 仅用于副标位置的"愿望文本"——*WISHES FROM STARS*、*Happy Birthdays*、生贺贺卡正文等。**禁止用于功能性 UI** (奖励名、按钮、关卡名)——草书可读性低，混入功能位会立刻变成装饰滥用。

## 4. Elevation

整套系统使用**两档轻阴影** + **一档玻璃罩**。这是与全局规范 (Fluent Design 的卡片阴影 + Acrylic Material) 之间最和谐的偏差——保留了"卡片漂浮"的语义，但把材料从"工业 acrylic"换成了"水汽 + 贴纸"。

### Shadow Vocabulary

- **Sticker Drop** (`box-shadow: 0 1px 2px rgba(40, 60, 100, 0.10), 0 12px 24px -12px rgba(40, 60, 100, 0.18)`)：贴纸式柔影。用于 Celebration Mode 中的蛋糕组件、礼盒、生贺贴纸——让它们看起来像"贴在木桌上"的小物件。
- **Halo Glow** (`box-shadow: 0 0 80px 24px rgba(245, 248, 255, 0.45)`)：星辉柔光。用于 Star Mode 中的主标背后、关键奖励背后。**只能用 ice-white / starlight-platinum 着色**，禁止 candy 色 halo。
- **Frosted Pane** (CSS: `backdrop-filter: blur(20px); background: rgba(245, 248, 255, 0.55);`)：玻璃罩材质。用于浮窗、领奖弹窗、活动详情卡。模拟"凝结在玻璃罩上的水汽"，比工业 acrylic 更朦胧、更暖。

### Named Rules

**The Halo-Without-Beams Rule.** Halo Glow 是发散的，不带方向性。**禁止 lens flare 直线光斑、放射状光线、棱镜分色**——这些是"舞台聚光"的修辞，不是"星空"的修辞。

## 5. Components

### Buttons
- **Shape:** `rounded.card = 8px` 圆角。比怀黍离的直角宽容、比 candy 路线的胶囊克制。
- **Primary (Star Mode):** deep-night 底 + ice-white 字，padding `12px 32px`。Hover 切换为 ribbon-navy 底。
- **Celebration (Celebration Mode):** candy-pink 底 + ice-white 字，胶囊圆角 (`rounded.pill = 999px`)，padding `10px 24px`。**仅限生贺玩法内**——主活动 CTA 即便在 Celebration Mode 弹窗里仍走 Star Mode primary。
- **Hover / Focus:** 走 200ms ease-out-quart，背景色相位移 + 轻 1px 上浮。**禁止粒子飞溅、禁止礼花特效**。

### Chips
- **Style:** ice-white 底 + deep-night 字 + 1px starlight-platinum 边框，圆角 `rounded.card = 8px`。
- **Selected:** 切换为 deep-night 底 + ice-white 字，边框消失。
- **Celebration variant:** buttercream 底 + ribbon-navy 字 + 1px ribbon-navy 边框；selected 反相为 candy-pink 底。

### Cards / Containers
- **Corner Style:** `rounded.card = 8px`。
- **Background:** Star Mode 走 ice-white；Celebration Mode 走 buttercream。
- **Shadow Strategy:** Star Mode 默认走 Halo Glow (柔光晕)，Celebration Mode 默认走 Sticker Drop (贴纸柔影)。**两套阴影禁止并用于同一卡片**。
- **Border:** 默认无边框；如需分离，使用 1px starlight-platinum (Star) 或 1px buttercream-deep (Celebration，比 buttercream 暗 8%)。
- **Internal Padding:** `lg = 24px` (Celebration) / `xl = 48px` (Star 主 KV 内嵌卡)。

### Inputs / Fields
- **Style:** 8px 圆角矩形，starlight-platinum 1px 描边。
- **Focus:** 描边切换为 deep-night (1px → 1.5px) + 极轻外发光 (`0 0 0 4px rgba(40, 60, 100, 0.08)`)——这是本系统**唯一允许使用 box-shadow glow** 的位置，因为它表达"被星光选中"的语义。
- **Error:** 描边切换为 candy-pink (副调红色替代，避免与 Star 主调违和)。

### Navigation
- **Style:** 横向排列，字距 ≥0.06em，主标走 Source Han Serif，次级走 Source Han Sans。
- **Active state:** 文字色变 deep-night + 下方一道 1px pearl-blue 半透明 (50%) 下划线。**不用胶囊色块**。
- **Mobile treatment:** 折叠为顶栏 + 下拉抽屉，抽屉底用 Frosted Pane (玻璃罩材质)。

### Signature Component: PV Reward Poster

PV 播放量解锁奖励页 (16_Snipaste 的形制) 是本系统的标志性组件：
- **Layout:** 左侧立式海报 (poster card) 占 30%，右侧奖励格 (reward grid) 占 70%。海报上承载主标"星语共愿"+ 副标 *WISHES FROM STARS* 草书 + KV 缩略。
- **Frame Treatment:** 海报四角加细线晶簇装饰 (1px starlight-platinum + 极轻发光)，模仿"老照片相框"。
- **Reward Cards:** 每张奖励卡有 Sticker Drop 阴影，底为 ice-white，四角圆 8px，内嵌奖励插画 + 数量。**奖励插画必须是手绘风**，禁止 3D 渲染图。
- **Locked State:** 未达成的奖励卡叠一层 60% 不透明度 starlight-platinum + 一枚锁形 sticker (deep-night 1px 描边)。

## 6. Do's and Don'ts

### Do:
- **Do** 严格区分 Star Mode 与 Celebration Mode，一个画面只能选一种调式——参见 The Two-Voices Rule。
- **Do** 用大面积柔光渐变和半透明叠层表达"光"，让明度差 ≤25%——参见 The High-Lightness-Low-Contrast Rule。
- **Do** 让主标"星语共愿"保留可见的笔触感与轻微不规则，**这就是品牌签名**。
- **Do** 把草书拉丁体只用在愿望文本位置 (副标、贺卡)，长段文字一律走黑体——参见 The Script-for-Wishes-Only Rule。
- **Do** 在生贺奖励 UI 中用 Sticker Drop 阴影把蛋糕、礼盒呈现为"贴在桌面上的小物件"——参见 Brand Personality 第 4 条 "奖励即记忆"。
- **Do** 让博士成为周年 KV 的情感重心，干员的姿态走"望向你"。

### Don't:
- **Don't** 在主活动入口、官方公告、PV 缩略图等情感锚点上使用 Celebration Mode——副不能盖主。
- **Don't** 加金属高光、Lens flare、3D 玻璃反射、闪烁粒子——参见 The No-Glitter Rule。
- **Don't** 用红金大字 + 烟花 + 周年大字这套国内手游周年默认模板。
- **Don't** 用 Source Han Sans Heavy 或几何无衬线做主标"星语共愿"，会立刻把"许愿"变成"宣告"——参见 The Brushstroke-in-the-Mark Rule。
- **Don't** 把草书 (Tangerine / Pinyon) 用在功能性 UI (奖励名、按钮、关卡名)——可读性损失立刻破坏体验。
- **Don't** 在同一画面同时使用 Halo Glow 与 Sticker Drop 阴影——它们属于两个调式。
- **Don't** 用 lens flare / 放射状光线 / 棱镜分色当作 Halo——参见 The Halo-Without-Beams Rule。
- **Don't** 用 candy-pink / candy-blue 给 halo 着色——halo 永远是 ice-white / starlight-platinum。
- **Don't** 用"永远""唯一一次""不再"等绝对化文案——周年活动的情感安全前提。
- **Don't** 把 3D 渲染图当作奖励插画，本系统的奖励插画走手绘 sticker 风。
