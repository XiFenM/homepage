# 晚樵庐 / The Late Woodcutter's Hut · Web

夕丰木的个人站前端。Nuxt 4 + Vue 3 + TypeScript。

> 战略文档：[../PRODUCT.md](../PRODUCT.md) · [../DESIGN.md](../DESIGN.md)
> 美术资产：[../assert-preparation/generated/](../assert-preparation/generated/)

## 架构

**主体 + 彩蛋 (one site, one secret)**：

- `/` 渲染**晚樵庐** Hero（书桌 + 卡片堆 + 角落卷轴）
- `/map`（也支持 `/勿忘我`）渲染 **勿忘我** 隐藏地图

无 fork 页。彩蛋触发三层冗余：
1. 视觉路径：[`<EasterEggScroll>`](app/components/EasterEggScroll.vue) 桌面一角微露
2. URL 路径：`/map` 与 `/勿忘我` 直达
3. 页脚路径：[`<FooterLink>`](app/components/FooterLink.vue) "还在某处游荡 →"

## 开发

```bash
bun install     # 已 init，二次 clone 时跑
bun dev         # http://localhost:3000
bun build       # SSR build
bun generate    # 静态站生成（部署用）
```

## 目录结构

```
web/
├── app/
│   ├── app.vue                      # 根组件（同步 html lang 与 i18n locale）
│   ├── pages/
│   │   ├── index.vue                # / — 晚樵庐 Hero
│   │   └── map.vue                  # /map + /勿忘我
│   ├── components/                  # 自动注册（Nuxt 默认）
│   │   ├── HeroScene.vue            # 桌面背景（V1 视频 / S3 静态备）
│   │   ├── CardStack.vue            # 5 卡片导航（占位）
│   │   ├── EasterEggScroll.vue      # 角落卷轴（彩蛋触发器）
│   │   ├── LanguageToggle.vue       # 语言切换 中 / EN
│   │   ├── FooterLink.vue           # 页脚冗余链接
│   │   └── MapView.vue              # 勿忘我地图
│   └── assets/
│       └── styles/
│           ├── tokens.css           # OKLCH 色板 + 字体 + 间距 token
│           └── global.css           # 全站重置 + 默认排印 + reduced-motion
├── i18n/
│   └── locales/
│       ├── zh.json                  # 中文（默认）
│       └── en.json                  # English
├── public/
│   └── art/                         # 见下方资产清单
├── content/                         # @nuxt/content 内容根（Markdown）
├── nuxt.config.ts                   # Nuxt 配置
└── package.json
```

## 资产清单

[`public/art/`](public/art/) 共 ~58MB（一次性从 `assert-preparation/generated/` 同步）：

| 路径 | 来源 | 用途 |
|---|---|---|
| `signatures/wordmark-zh.png` | S1 | 站名手写字标 |
| `signatures/seal-jie.png` | S2A | 印章「桀」 |
| `signatures/seal-xfm.png` | S2B | 印章「XFM」 |
| `homepage/desk-scene.png` | S3 | Hero 静态背景 |
| `homepage/parchment-scroll.png` | S4 | 彩蛋卷轴 |
| `homepage/card-stack.png` | S5C | 卡片堆 |
| `map/world-map.png` | S6 | 勿忘我地图 |
| `cosmos/starfield.png` | S7 | 观星塔星空 |
| `motion/desk-ambient.mp4` | V1 | Hero 环境循环 |
| `motion/parchment-unfurl.mp4` | V2 | 卷轴展开 hover |
| `motion/cosmos-transition.mp4` | V3 | 进观星塔过场 |
| `textures/grain-{paper,parchment,cosmos}.png` | T1 | 纹理叠加 |
| `masks/{paper-curl,edge-wear}*.svg` | T2 | 形状蒙版 |

## 关键约束（DESIGN.md doctrines 在代码层落地）

- **No Pure Black/White**：`global.css` 通过 token 强制；任何 `#000`/`#fff` 即违规
- **Flat By Ink**：`global.css` 全局 `box-shadow: none`；任何 shadow 即违规
- **Bilingual Equal**：中英 `font-family` 与 `letter-spacing` 在 `:root` 与 `html[lang="en"]` 双轨配置
- **No Easter-Egg CTA**：`<EasterEggScroll>` 与 `<FooterLink>` 无解释性文字（footer "→" 是文本标点而非 UI 装饰）
- **Reduced Motion**：`<HeroScene>` 与 `<EasterEggScroll>` 检测 `prefers-reduced-motion: reduce` 并降级到静态等效

## 接下来

按 PLAN.md：

- **A · `$impeccable shape homepage`** — 把 `<CardStack>` 拆成 5 张可点卡 / 卡片悬停状态 / 卷轴 hover→V2→ 跳转的精确时序
- **`$impeccable shape map`** — 在 [`MapView.vue`](app/components/MapView.vue) 上叠 9–10 个 hotspot SVG 标记 + 呼吸动画 + Tab 顺序
- 内容卡片（5 张 → 5 个分类页）— 用 `@nuxt/content` 写 Markdown
