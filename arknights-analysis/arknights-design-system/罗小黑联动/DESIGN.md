---
name: 明日方舟 × 罗小黑战记 / Arknights × The Legend of Luoxiaohei
description: 2022 年 9 月联动活动"好久不见"，春绿水墨 + 萌系贴纸的双面视觉系统
colors:
  spring-lime: "oklch(86% 0.16 125)"
  young-leaf: "oklch(74% 0.14 130)"
  paper-cream: "oklch(95% 0.012 90)"
  ink-mountain: "oklch(58% 0.02 150)"
  ink-black: "oklch(24% 0.012 250)"
  seal-red: "oklch(48% 0.18 28)"
  warm-tan: "oklch(82% 0.05 70)"
  shadow-green: "oklch(34% 0.06 145)"
typography:
  display:
    fontFamily: "Source Han Serif SC, FZQiTaJW, '方正启体', 'Noto Serif CJK SC', serif"
    fontSize: "clamp(2.5rem, 7vw, 5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.04em"
  display-poster:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.5rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.02em"
  display-latin:
    fontFamily: "Bungee, 'Alfa Slab One', 'Fjalla One', sans-serif"
    fontSize: "clamp(2rem, 4.5vw, 3rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "0"
  headline:
    fontFamily: "Source Han Serif SC, 'Noto Serif CJK SC', serif"
    fontSize: "clamp(1.5rem, 3.5vw, 2.25rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0"
  title:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Source Han Sans SC, 'Noto Sans CJK SC', sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0"
  label:
    fontFamily: "Cormorant Garamond, 'EB Garamond', serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.22em"
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
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.ink-black}"
    textColor: "{colors.paper-cream}"
    rounded: "{rounded.card}"
    padding: "12px 28px"
  button-primary-hover:
    backgroundColor: "{colors.shadow-green}"
    textColor: "{colors.spring-lime}"
  button-spring:
    backgroundColor: "{colors.spring-lime}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.card}"
    padding: "12px 28px"
  card-archive:
    backgroundColor: "{colors.paper-cream}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.none}"
    padding: "32px"
  banner-spring:
    backgroundColor: "{colors.spring-lime}"
    textColor: "{colors.ink-black}"
    rounded: "{rounded.card}"
    padding: "24px"
  seal-stamp:
    backgroundColor: "{colors.seal-red}"
    textColor: "{colors.paper-cream}"
    rounded: "{rounded.card}"
    size: "48px"
---

# Design System: 明日方舟 × 罗小黑战记 / Arknights × Luoxiaohei

## 1. Overview

**Creative North Star: "山道上递来的一封春日明信片" (A Spring Postcard Handed Over on a Mountain Trail)**

这套视觉系统的工作是**把两个差异巨大的 IP 缝合到同一帧画面里**——方舟带来"工业精确 + 档案式形制"的形 (form)，罗小黑带来"水墨山林 + 春绿气韵"的气 (air)。两者不混合，而是**叠合**：方舟的卡片骨架 + 罗小黑的水墨皮肤，方舟的字怀规范 + 罗小黑的色温情绪。

它显式拒绝的事：拒绝国内联动手游惯用的"两个 LOGO 拼一起 + 紫红渐变 + 巨大 CROSSOVER 字样"懒惰模板，拒绝米哈游式高饱和金属渐变光晕，也拒绝过度幼龄化的儿童海报色板。它同样拒绝把方舟的工业警戒色硬塞进来——那会让山林立刻发酸。

整套系统在《明日方舟》全局视觉规范 ([../README.md](../README.md)) 之上做的偏移是：
- 把工业警戒色 (alert orange) 整体替换为春绿 (spring lime)
- 把毛玻璃 acrylic material 弱化为水墨纸面噪点
- 保留方舟的"扁平卡片 + 档案式标签 (代号/种族/出身/专精)"骨架
- 把字型重心从 Source Han Sans 转向 Source Han Serif (思源宋体)

它有两种调式 (mode)，**层级关系是嵌套而非并列**：
- *Archive Mode* (档案模式)：用于干员介绍卡、剧情入口、活动公告。骨架是方舟，皮肤是水墨。
- *Banner Mode* (海报模式)：用于联动 PR 物料、活动入口 banner、社交分享卡。允许春绿铺面，允许 chibi sticker，但**必须有水墨 / 印章 / 山林等中式国漫底层元素同时在场**。

**Key Characteristics:**
- 两个 IP 字标必须同等级别共存，× 符号相连
- 春绿是关节高光，不是铺面底色
- Archive 卡走方舟形 + 水墨皮，Banner 走春绿铺面 + 中式根基
- 印章红 (seal-red) 沿用怀黍离的克制原则——只作落款
- 字型走宋体识别 + 黑体功能 + Bender 工业残留

## 2. Colors

整套色板锚定在"早春的山道"上——刚抽芽的叶子 (spring-lime)、晨雾浸透的山影 (ink-mountain)、被反复翻看的旧画册纸 (paper-cream)、罗小黑的剪影 (ink-black)、压在画册角上的私章 (seal-red)。

### Primary
- **Spring Lime** (`oklch(86% 0.16 125)`): 联动主导色——罗小黑战记 IP 的标志性春绿。承担 Banner Mode 主底色、关键 CTA、装饰高光。**不是普适绿色**，色相严格锁在 120–130 之间偏黄绿。
- **Paper Cream** (`oklch(95% 0.012 90)`): Archive Mode 主底色，承担 70% 以上画册纸感留白。比怀黍离的 paper-white 略微多一分黄气，模拟 1990s 国漫绘本纸色。
- **Ink Black** (`oklch(24% 0.012 250)`): 主笔墨色 + 罗小黑剪影色。承担书法字、文字、剪影、关键描边。

### Secondary
- **Young Leaf** (`oklch(74% 0.14 130)`): spring-lime 的暗版，承担文本与绿底间的对比层。
- **Ink Mountain** (`oklch(58% 0.02 150)`): 水墨远山色，承担背景山形、远景剪影、装饰水汽。**带极轻微的绿调**——这是它与怀黍离 ink-wash-gray 的关键区别。
- **Shadow Green** (`oklch(34% 0.06 145)`): 深绿，承担 hover 态与深色卡片底。

### Tertiary
- **Seal Red** (`oklch(48% 0.18 28)`): 印章红。沿用怀黍离的语义——**只作落款 / 章号 / 活动徽章**，不作主 CTA、不作装饰小红点。
- **Warm Tan** (`oklch(82% 0.05 70)`): 暖米色，承担木牌、皮质标签、葫芦水壶等山野道具的高光。

### Neutral
- 不引入纯灰；所有"灰"通过 ink-mountain (微绿调) 表达。

### Named Rules

**The Lime-As-Hinge Rule.** Spring lime 在任意单一画面中**最多承担 30% 视觉面积**——除非该画面是 Banner Mode 主 KV (例外允许铺到 60%)。Archive Mode 中 spring lime 只作"关节高光"：CTA 边缘、装饰角标、奖励标签底色。任何把春绿铺到背景过半的 Archive 卡都视为违规。

**The Two-IPs-Equal Rule.** 主 KV 与 PR 物料必须同时呈现「明日方舟」与「罗小黑战记」两个完整 IP 字标，并以一个细的 ×（cross 符号，1.5px stroke ink-mountain）相连。两个字标的高度比必须为 1:1，水平基线必须对齐。任何一方被缩小、模糊化或省略均视为违规。

**The Seal-as-Signature Rule.** 沿用怀黍离体系：seal-red 单帧最多两枚，仅作落款印 / 章回号 / 活动徽章。

## 3. Typography

**Display Font (中文宋体):** Source Han Serif SC——承担"档案式标题"、活动主标"好久不见"等情感锚点。
**Display Font (中文黑体):** Source Han Sans SC Heavy——承担 Banner Mode 上的"罗小黑""明日方舟"大字标识。
**Display Latin:** Bungee / Alfa Slab One——承担 Banner Mode 上的 *Spring Praise* 等英文海报字 (粗胖 display 衬体，带轻微复古感)。
**Body Font:** Source Han Sans SC——长段功能性文字。
**Latin Label:** Cormorant Garamond——Archive Mode 中的英文小标 *NEW OPERATOR*、*GUARD · LORD*。
**Latin Mono:** Bender——继承自方舟基建系统的伪等距字，用于关卡代号、版本号等 metadata。

**Character:** 这是一组"档案 + 海报"的双面字型组合。Archive 走宋体识别 + 黑体功能 + Garamond 拉丁标签的中式画册风；Banner 走粗黑体大字 + Bungee 粗体海报字的二次元宣发风。两套在同一活动伞下并存，但通过模式 (Archive vs Banner) 严格分隔。

### Hierarchy
- **Display (Archive)** (Source Han Serif 700, 2.5–5rem clamp, line-height 1, letter-spacing 0.04em)：Archive 卡上的干员代号、章节名 (e.g. "罗小黑")。
- **Display (Banner / Poster)** (Source Han Sans 900, 2–3.5rem)：Banner Mode 上的 IP 字标与海报主标。允许大字 + 粗白边描边 (yellow-outlined display)。
- **Display Latin** (Bungee 700, 2–3rem)：Banner 上的英文海报标 *Spring Praise*。允许 1–3px 粗白边描边。
- **Headline** (Source Han Serif 600, 1.5–2.25rem)：副标题、活动副名。
- **Title** (Source Han Sans 700, 1.125rem)：UI 卡片标题、关卡名。
- **Body** (Source Han Sans 400, 0.9375rem, line-height 1.7)：正文、对话、奖励说明。行宽 ≤ 70ch。
- **Label** (Cormorant 500, 0.75rem, letter-spacing 0.22em)：英文小标 *NEW OPERATOR*、*MODEL*、*BRAND*。
- **Bender Mono** (Bender 500, 0.875rem, letter-spacing 0.06em)：关卡代号、版本号、metadata 类标签——承担方舟一贯的工业残留感。

### Named Rules

**The Mode-Locks-Type Rule.** Archive Mode 必须以 Source Han Serif (思源宋体) 作为主标识字怀；Banner Mode 必须以 Source Han Sans Heavy / 粗 display Latin 作为主标识字怀。**两种字怀禁止并置于同一画面**——它们属于两个模式，混用会让画面沦为"既不像档案也不像海报"的灰色地带。

**The Bender-Stays-Industrial Rule.** Bender 字体承担方舟的工业残留——只用于关卡代号 (e.g. *EX-1*)、metadata、版本号、UI 边缘小标。**禁止用 Bender 写中文转译或副本名**——它的工业感会立刻冲淡春绿的山林气。

## 4. Elevation

整套系统使用**纸面阴影 + 山影渐隐**两套手段，几乎不用毛玻璃。这是与全局规范 (Fluent Design 的 Acrylic Material) 之间的有意偏差——本活动里所有"窥见底层"的诉求都通过水墨晕染替代。

### Shadow Vocabulary

- **Paper Drop** (`box-shadow: 0 1px 0 rgba(28, 24, 18, 0.06), 0 6px 18px -10px rgba(28, 24, 18, 0.16)`)：画册纸面投影。用于 Archive 卡叠在画布上、奖励小卡叠在 banner 上的语义。
- **Sticker Outline** (`filter: drop-shadow(0 0 0 4px {colors.paper-cream}) drop-shadow(0 4px 8px rgba(0,0,0,0.18))`)：贴纸描边阴影。仅用于 Banner Mode 中的 chibi sticker 角色——4px 白边 + 投影模拟"剪下来的贴纸"。
- **Mountain Fade** (`background: linear-gradient(180deg, transparent 0%, {colors.ink-mountain} 100%)` 或同色相 mask)：山影渐隐——用于背景层级，**不是 box-shadow**——通过墨色渐隐表达远近。

### Named Rules

**The Sticker-Has-White-Border Rule.** Banner Mode 中的 chibi sticker 角色必须带 ≥3px paper-cream 描边 + 投影。无白边的 sticker 会立刻像"被错位贴上去的扣图"。

## 5. Components

### Buttons
- **Shape:** `rounded.card = 4px` 微圆角。比怀黍离 (2px) 略柔，比星语共愿 (8px) 略克制。
- **Primary (Archive):** ink-black 底 + paper-cream 字。Hover 切到 shadow-green 底 + spring-lime 字 (这是"春风掠过"的转场隐喻)。
- **Spring (Banner):** spring-lime 底 + ink-black 字。仅用于 Banner Mode 与社交分享按钮。
- **Hover / Focus:** 200ms ease-out-quart 色相位移；**禁止粒子飞溅、禁止落叶飘动**——动效用克制的色相位移即可。

### Chips
- **Style:** paper-cream 底 + ink-black 字 + 1px ink-mountain 边框，圆角 `rounded.card = 4px`。
- **Selected:** 反相为 ink-black 底 + paper-cream 字。
- **Spring variant:** 选中态切换为 spring-lime 底 + ink-black 字——用于 Banner Mode 内的标签。

### Cards / Containers (Archive)
- **Corner Style:** `rounded.none = 0` 直角。这是干员档案卡的传统形制。
- **Background:** paper-cream + ~6% 不透明度水墨噪点纹理。
- **Shadow Strategy:** Paper Drop。
- **Border:** 无 (paper-cream 与外部画布的色差自然分离)；如需强调，左右两侧细 hairline 描边走 ink-mountain。
- **Internal Padding:** `xl = 48px`。档案卡的字从来不贴边。
- **Header Strip:** 顶部一道 1px ink-black 横线 + 中文宋体大字干员代号 + 右侧 Bender 关卡代号 metadata。

### Cards / Containers (Banner)
- **Corner Style:** `rounded.card = 4px`。
- **Background:** spring-lime 主底 + paper-cream 内嵌卡 + warm-tan 装饰边。
- **Shadow Strategy:** Sticker Outline (用于 chibi 角色) + Paper Drop (用于内嵌卡)。
- **Border:** 顶部和底部装饰横向 chevron / 雪花纹边带，走 spring-lime 与 paper-cream 交错。
- **Internal Padding:** `lg = 24px`。

### Inputs / Fields
- **Style:** 4px 圆角矩形，paper-cream 底，1px ink-mountain 描边。
- **Focus:** 描边切换为 shadow-green (1.5px)。
- **Error:** 描边切换为 seal-red (这是 seal-red 唯一的功能性用法例外)。

### Navigation
- **Style:** 横向排版，Archive Mode 走宋体 + 大写 Latin label；Banner Mode 走黑体 Heavy + 大字。
- **Active state:** Archive 走 1px ink-black 下划线；Banner 走 spring-lime 胶囊背景。

### Signature Component: Operator Archive Card

干员介绍卡 (5_006QZng-Zgy1h640ujkc38j30rs15ogwk.jpg 的形制) 是 Archive Mode 的标志性组件：
- **Layout:** 横向 16:9，左 30% 档案信息 (代号 / 种族 / 出身 / 专精) 走"标签 - 内容"两列结构 + 五角星等级 + Bender 关卡代号、中 40% 角色全身水墨立绘穿过山影、右 30% 干员介绍文字 + 印章。
- **Header Strip:** 左上"明日方舟 × 罗小黑战记"双 IP 字标 + 中央"NEW OPERATOR"Cormorant 大字 + 五角星 + 右上职业图标。
- **Watermark:** 整张卡背景叠 ~8% 不透明度的 ink-mountain 山影 + 极轻水墨噪点。
- **Seal:** 右下角一枚 seal-red 印章——刻"小黑"或"罗"或干员代号。
- **Footer:** 干员台词 (灰底字小段 italic) + 技能编号 (Bender) + 版权字。

### Signature Component: Crossover Banner

联动公关 banner (1_006QZng-Zgy1h651bd86byj31hc0u07iu.jpg 的形制) 是 Banner Mode 的标志性组件：
- **Layout:** 横向 2.4:1，背景 spring-lime + 山影 + 散落树叶 sticker。
- **Top Strip:** 双 IP 字标居左居右对称 + 中央 × 符号。
- **Center:** chibi sticker 角色群像 (罗小黑、铃兰、风笛、空) 错落排布，每个都带 4px paper-cream 描边 + Sticker Outline 阴影。
- **Title Slot:** 居中或居左大字 display "好久不见" + 副标拉丁文 *Spring Praise* 或 *Long Time No See*。
- **Footer:** 活动时间、版权双 IP、Cormorant 小字署名。

## 6. Do's and Don'ts

### Do:
- **Do** 把 spring-lime 当作"关节高光"使用，单帧画面 ≤30% 占比 (Banner Mode KV 例外可达 60%)——参见 The Lime-As-Hinge Rule。
- **Do** 把"明日方舟"与"罗小黑战记"两个 IP 字标按 1:1 高度比同等呈现，× 符号相连——参见 The Two-IPs-Equal Rule。
- **Do** 在 Archive Mode 用宋体识别字怀；在 Banner Mode 用黑体 Heavy / Bungee——两个模式字怀严格分离 (The Mode-Locks-Type Rule)。
- **Do** 让 chibi sticker 永远带 ≥3px paper-cream 白边 + 投影——参见 The Sticker-Has-White-Border Rule。
- **Do** 让 seal-red 沿用怀黍离的克制原则，只作落款 / 章号 / 活动徽章——参见 The Seal-as-Signature Rule。
- **Do** 在 Archive 卡里保留方舟的工业残留 (Bender 关卡代号 + 标签 - 内容档案布局)，这是方舟的形。
- **Do** 把背景山影通过墨色渐隐 (Mountain Fade) 表达，而不是 box-shadow。

### Don't:
- **Don't** 用"两个 LOGO 拼一起 + 紫红渐变 + 巨大 CROSSOVER 字样"的国内联动懒惰模板——这是反例的核心。
- **Don't** 把方舟的工业警戒色 (alert orange、警戒条纹、工业网点) 带入本活动——它们与春日山林互斥。
- **Don't** 把 spring-lime 铺满 Archive 卡背景——绿色底色会立刻让档案沦为儿童海报。
- **Don't** 在 Banner Mode 出 chibi sticker 但不带水墨 / 印章 / 山林等中式根基元素——参见 Brand Personality 第 3 条 "可爱要有出处"。
- **Don't** 用米哈游式高饱和金属渐变光晕——它的"奢华联动"修辞会让山野气立刻变质。
- **Don't** 把 Bender 用于副本名 / 中文转译——Bender 只承担工业残留 (关卡代号、metadata)，参见 The Bender-Stays-Industrial Rule。
- **Don't** 把怀黍离的肃穆水墨调式 (低明度 + 大留白) 带入本活动——这是同 IP 内的另一种风格，会让"久别重逢"误读为"祭奠故人"。
- **Don't** 在 Archive 与 Banner 模式间混用字怀 (Source Han Serif 与 Source Han Sans Heavy 不能并置)。
- **Don't** 让任何一个 IP 字标被缩小 / 模糊化 / 省略——这是联动署名公平性的硬底线。
- **Don't** 用儿童化插画风、emoji 堆砌、糖果色系 (这是星语共愿 Celebration Mode 的领地，不属于本活动)。
