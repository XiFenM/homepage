# 明日方舟活动设计系统文档

> 这不是《明日方舟》(Arknights) 的官方设计规范——而是基于公开活动美术资源 ([../arknights-art/](../arknights-art/)) 与两篇 UI/UX 分析文章 ([../arknights-pdf-article/article.md](../arknights-pdf-article/article.md)、[../arknights-ui-ux-article/article.md](../arknights-ui-ux-article/article.md))，按 [Anthropic impeccable](../.claude/skills/impeccable/) skill 的 PRODUCT.md / DESIGN.md schema 反推出的**研究型参考文档**。
>
> 它的目的是：当你要设计一个**风格上向《明日方舟》某个活动靠拢**的页面 / 物料 / 应用时，可以直接把对应活动的 `PRODUCT.md` + `DESIGN.md` 喂给 AI Agent 或人类设计师，作为 brand reference (品牌参考) 与 design tokens (设计令牌) 的来源。

## 全局：方舟视觉 DNA (Global Arknights Design DNA)

每个活动都不是独立设计的——它们都建立在方舟全局视觉规范这层"地基"之上，再各自做风格偏移。理解这层地基，再去看四个活动各自如何**继承 / 偏移**，比单独读任一活动文档都更有用。

### 全局规范的五个支柱

源自两篇 UI/UX 分析文章的核心结论。如果你只读一段全局介绍，请读这一段：

1. **高度统一的设计规范 (Highly Unified Design Standards)。** 干员代号一律 Source Han Sans (思源黑体) Heavy 字重 + 字间距 -100；档案信息 Normal 字重 + 字间距 -100；技能描述 Normal + 字间距 0。从 2019 年至今几乎无改动。统一性本身即是品牌识别——这是"舟味"的基础。
2. **Fluent Design 五要素 (Light / Depth / Material / Motion / Scale)。** 方舟在微软 2017 年提出的 Fluent Design 系统上做出二游版本演绎：扁平卡片 + 阴影构建层级 (Depth)、毛玻璃 / 亚克力材料模糊 (Material) 表达"窥见底层"、连接动画与协调动画 (Motion) 让"切换不离同一画布"、静态贴图代替即时光照 (Light)。
3. **画内界面 (Diegetic Interface)。** 主看板的 PRTS 全息投影 HUD 把"博士远程接入罗德岛"的世界观直接做进了 UI 里——电量、信号、时间随陀螺仪移动。这是方舟与同类二游最大的视觉区分点之一。
4. **字怀混编 (Mixed Typography)。** Source Han Sans (思源黑体) 主场 + 思源宋体衬线表达"古典骑士精神"、Trajan / Cormorant 等 Old-Style 衬线呼应碑刻铭文、Bender 伪等距体承担工业残留 (基建系统)。一中一西、一衬一无衬，靠**风格分工**而非互相替换。
5. **网点 / 条纹底图 + 局部失焦马赛克 (Grain Texture + Local Mosaic)。** 散点网点纸效果让所有素材看上去像"印刷在同一种纸上"，警戒条纹承担工业感。局部马赛克化是叙事性梗 ("失去同步")。两套底图处理在游戏内外**惊人统一**——这是 brand 渗透到每一个像素。

### 全局调色板 (Global Palette)

各活动的色板都是在**全局工业警戒色 (industrial alert palette)** 之上做的偏移。全局基准是：

- 工业灰阶 (Industrial Grayscale) — 暗钢灰、混凝土灰、白底
- 警戒亮色 (Alert Brights) — 警戒橙、毒物黄、危险红
- 工业蓝 / 罗德岛绿 — 主菜单与基建系统主导色

四个活动几乎都**显式压制了这套全局色**，理由是它们要表达的情绪（怀古、许愿、春日、烹饪）与"反乌托邦塔防"的主调不同。

## 四个活动的关系图谱

四个活动覆盖《明日方舟》四种典型的活动类型，形成一张光谱：

| 活动 | 类型 | 色彩策略 (Color Strategy) | 主导情绪 | 模式 |
|---|---|---|---|---|
| [怀黍离 / Here a People Sows](怀黍离/) | Side Story 新春 | Restrained — 水墨灰阶 + 单一主色相 | 怀古、克制、肃穆 | 单调式 |
| [星语共愿 / Wishes from Stars](星语共愿/) | 周年纪念 | Committed — 珍珠蓝主导 + 糖果副调 | 澄澈、温柔、许愿 | 双调式 (Star + Celebration) |
| [罗小黑联动 / × Luoxiaohei](罗小黑联动/) | IP 联动 | Restrained → Committed — 春绿关节高光 + 水墨纸感 | 春日、亲和、轻盈 | 双调式 (Archive + Banner) |
| [迷宫饭联动 / × Delicious in Dungeon](迷宫饭联动/) | IP 联动 | Full palette — 羊皮 + 酒红 + 暗墨绿 + 芥末金 | 桌游夜、烹饪手账 | 双调式 (Tome + Recipe) |

**色彩策略 (Color Strategy)** 的术语沿用 impeccable shared design laws 的四档分类：Restrained / Committed / Full palette / Drenched。

### 它们的共同立场 (Shared Stance)

四个活动彼此差异巨大——但它们对**同一些反例**保持一致拒绝。这是阅读单个活动文档时容易忽略、却最值得记住的一组共识：

1. **拒绝米哈游式高饱和金属 + 玻璃粒子聚光灯** (璀璨修辞)。
2. **拒绝国内手游联动惯用的"两 LOGO 拼一起 + 渐变 + 巨大 CROSSOVER 字"懒惰模板** (公关惰性)。
3. **拒绝二游通用 KV 模板：发光圆形背板 + 居中角色 + 渐变光晕** (训练数据反射)。
4. **拒绝把方舟工业警戒色硬塞进活动主调** (情绪与色板互斥)。
5. **拒绝纯黑 #000 与纯白 #fff** — 沿用 impeccable 的色彩共识，所有"黑白"都向品牌色相微微偏移。

### 它们的私有手法 (Per-Event Signature)

| 活动 | 标志性手法 |
|---|---|
| 怀黍离 | 一人一墨色 (one ink hue per operator) + 印章红只作落款 + 卷轴留白 ≥50% |
| 星语共愿 | 主标"星语共愿"保留笔触感 + 草书拉丁体只用在"愿望文本"位置 + 玻璃罩 (Frosted Pane) |
| 罗小黑联动 | 春绿是关节高光不是铺面 + Archive 走方舟形 + 罗小黑气 + 双 IP 字标 × 相连 |
| 迷宫饭联动 | 羊皮卷底层语言 + 食谱三段式 + 立绘穿越功能边界 (Mission Central 板) + Cormorant Italic 命名英雄 |

## 怎么用这套文档

### 场景 A：你要做一个"方舟某活动风格"的网页或物料

1. 选定活动 → 进对应子目录 → 把 `PRODUCT.md` 与 `DESIGN.md` 一起喂给 AI Agent (或者作为人工设计 brief)。
2. `PRODUCT.md` 告诉 Agent：受众、调性、反例、原则——这五件事决定"哪些诱惑要拒绝"。
3. `DESIGN.md` 告诉 Agent：色彩 OKLCH 值、字型族谱、组件规格、Do's & Don'ts——这些决定"具体怎么落地"。
4. 如果项目有自己的 `PRODUCT.md`，可以把这里的"反例""设计原则"作为补充——但**主品牌仍以项目自身的 PRODUCT.md 为准**。

### 场景 B：你想用这里的某个组件作为参考

各活动的 DESIGN.md 都列出了一个 **Signature Component (标志性组件)**，是该活动最值得搬到 web / 应用语境的那个形制：

- 怀黍离 — *Operator Scroll Card* (横向卷轴式干员介绍卡)
- 星语共愿 — *PV Reward Poster* (立式海报 + 奖励格)
- 罗小黑联动 — *Operator Archive Card* + *Crossover Banner*
- 迷宫饭联动 — **Mission Central / 任务中心面板** (立绘穿过功能区 + 任务按钮堆叠 — 对网页 hero / dashboard 参考价值最大)

### 场景 C：跨活动的"共性原则"

如果你要做一个**贯穿多活动的统一界面** (e.g. 一个介绍《明日方舟》各活动美学的网站)，建议遵循以下层级：

- 在外壳 (shell / 全局导航) 上沿用方舟全局规范 — 工业警戒色、Source Han Sans、Bender metadata
- 在每个活动专题页 (per-event detail page) 上切换到该活动自己的色板与字怀
- 切换的接缝 (transition) 沿用方舟的连接动画 (Connected Animation) 思路 — 不要硬切

## 文件清单

```
arknights-design-system/
├── README.md                      ← 本文件
├── 怀黍离/
│   ├── PRODUCT.md                 ← 战略 (受众 / 调性 / 反例 / 原则)
│   └── DESIGN.md                  ← 视觉 (色板 / 字型 / 组件 / Do's & Don'ts)
├── 星语共愿/
│   ├── PRODUCT.md
│   └── DESIGN.md
├── 罗小黑联动/
│   ├── PRODUCT.md
│   └── DESIGN.md
└── 迷宫饭联动/
    ├── PRODUCT.md
    └── DESIGN.md
```

每份 `DESIGN.md` 都遵循 [Google Stitch DESIGN.md format](https://stitch.withgoogle.com/docs/design-md/format/)：YAML frontmatter (机器可读 token) + 六节正文 (Overview / Colors / Typography / Elevation / Components / Do's and Don'ts)。Stitch 与 awesome-design-md 等工具可直接消费。

每份 `PRODUCT.md` 都遵循 impeccable PRODUCT.md schema：Register / Users / Product Purpose / Brand Personality / Anti-references / Design Principles / Accessibility & Inclusion。

## 一些诚实的限制

1. **本文档基于公开美术资源逆向推导**，不代表《明日方舟》开发团队的内部规范。具体的字间距、组件 padding、动效曲线等数值是从画面中**估读 + 借鉴 impeccable design laws** 得来的合理值，但不一定与游戏内实际值一致。
2. **OKLCH 色值是从 KV 缩略图采样推导**，色相与明度区间正确，但绝对值可能存在 ±3% 的偏差。生产前请用真实素材重新采样校准。
3. **每个活动的"双调式"** (e.g. Star Mode / Celebration Mode) 是基于美术资源观察到的两种风格分支，并非游戏团队的官方命名。
4. **本文档不覆盖**：游戏内战斗 UI / 基建系统主调 / 主菜单 PRTS HUD 等全局界面——如需研究这些，请直接读 [../arknights-pdf-article/article.md](../arknights-pdf-article/article.md) 与 [../arknights-ui-ux-article/article.md](../arknights-ui-ux-article/article.md)。

## 参考资料

- 《"舟味"从何而来？解析明日方舟设计美学（UI/UX 设计篇）》— 杰尼龟，2023 — [../arknights-pdf-article/article.md](../arknights-pdf-article/article.md)
- 《产品《明日方舟》UI/UX 分析——藏在「好看」背后的先进性》— AJ，腾讯互娱 — [../arknights-ui-ux-article/article.md](../arknights-ui-ux-article/article.md)
- 美术资源 — [../arknights-art/](../arknights-art/) (4 个活动共 66 张 KV / 干员卡 / UI 截图)
- impeccable skill — [../.claude/skills/impeccable/](../.claude/skills/impeccable/)
