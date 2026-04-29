# 美术资源准备方案 (Asset Preparation Plan)

> 关联文档：[PRODUCT.md](../PRODUCT.md) · [DESIGN.md](../DESIGN.md)
> 资源继承源（已归档）：[arknights-analysis/arknights-design-system/](../arknights-analysis/arknights-design-system/)

## 1. 目标 (Goal)

按 [DESIGN.md](../DESIGN.md) §5 的视觉规格，**用最少的迭代轮次**得到全部首发上线所需的美术资源。所有资源最终落到 `public/art/` 下供站点引用，准备阶段在本文件夹内完成提示词撰写、生成结果归档、验收复盘。

## 2. 工具栈 (Toolchain)

| 用途 | 工具 | 备注 |
|---|---|---|
| 静态图像 | **gpt-image-2** | 全部插画、贴图、字标、印章 |
| 动态视频 | **seedance2** | 过场转场 / 环境循环 (可选层) |
| 后处理 | remove.bg / Photoshop / Figma / Illustrator | 抠透明、SVG 描线、蒙版导出 |

**参考资料库** (`prompts-reference/`)：

| 仓库 | 服务工具 | 借鉴方向 |
|---|---|---|
| `awesome-gpt-image/` | gpt-image-2 | 中文场景描述提示词的句式与节奏 |
| `awesome-gpt-image-2-prompts/` | gpt-image-2 | 风格 / 视角 / 反例三段式结构 |
| `awesome-seedance/` | seedance2 | 时长 + 镜头分段的脚本式提示词 |
| `Seedance2-Storyboard-Generator/` | seedance2 | 角色—场景—道具编号制 (本项目仅借结构，不需要角色一致性) |

> **重要**：参考库提示词大多面向**电影 / 广告 / 网剧**等带人物的叙事视频。本项目几乎不出现人物——只生成"无人的物件 / 风景 / 字标"。借鉴它们的**句式与节奏**（如 gpt-image-2 喜欢"生成一张...，注意..."、seedance2 喜欢 `[00-05s] 镜头 1：` 时间轴），但**不**借鉴它们的"网红 / 写实人像 / 商业广告"语气。

## 3. 资源清单 (Inventory)

### 3.1 静态资源 (gpt-image-2，共 7 项 + 2 项工具件)

| # | 代号 | 用途 | 输出规格 | 透明背景 | 复用频率 |
|---|---|---|---|---|---|
| S1 | `wordmark-zh` | 站名「晚樵庐」手写字标 | 2048×768 PNG → 描 SVG | ✅ | 极高（hero / favicon / og-image） |
| S2 | `seal-jie` / `seal-xfm` | 印章红方章（两版） | 256×256 PNG ×2 | ✅ | 极高（每张内容卡角落） |
| S3 | `desk-scene` | 首页书桌场景（无物件） | 3840×2160 (16:9 4K) WebP | ✗ | 仅首页 hero |
| S4 | `parchment-scroll` | 首页左物件 半展开羊皮卷 | 1024×768 PNG | ✅ | 仅首页 hero |
| S5 | `sticky-note` | 首页右物件 春绿便签（空白） | 512×400 PNG | ✅ | 仅首页 hero |
| S6 | `world-map-base` | 探索站等距异世界地图 | 4096×2304 PNG | ✗ | 探索站底图 |
| S7 | `cosmos-starfield` | 观星塔 hotspot 背景 | 4096×2304 PNG | ✗ | Cosmos Sub-zone |
| T1 | `grain-paper` | 纸面颗粒贴图 | 512×512 平铺 PNG | ✅ | 全站叠加 |
| T2 | `edge-wear` / `paper-curl` | 卡片磨损 / 卷角蒙版 | SVG | ✅ | 探索站 / 简约站卡片 |

> **T1 和 T2 不走 AI**——T1 用 [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/) 或 Photoshop noise 生成；T2 用 Figma / Illustrator 手画几条不规则曲线导出。

### 3.2 动态资源 (seedance2，共 3 项可选)

按"是否真正不可被 CSS / SVG 替代"评估，**默认不上线，按需追加**。

| # | 代号 | 用途 | 时长 | 替代方案 | 优先级 |
|---|---|---|---|---|---|
| V1 | `desk-ambient-loop` | 首页环境循环（飘尘 + 灯光呼吸） | 6–8s 无缝循环 | CSS 颗粒 + radial-gradient 微动 | ⭐ 低（CSS 已够） |
| V2 | `parchment-unfurl` | 进入探索站时的卷轴展开过场 | 800–1500ms | SVG mask + transform animate | ⭐⭐ 中（视频更有质感） |
| V3 | `cosmos-transition` | 进入观星塔时的羊皮→星空过场 | 1000–1500ms | opacity blend (DESIGN.md §5 已规定 600ms) | ⭐⭐⭐ 高（增强"世界切换"感） |

> **建议**：先全 CSS 跑起来，**只在 V3 上线后给主观感受加一档**，再决定 V1 / V2 是否需要。视频文件大、加载慢、对 reduced-motion 不友好，能 CSS 解决的不上视频。

## 4. 文件组织 (Folder Layout)

```
assert-preparation/
├── PLAN.md                              ← 本文档（流程总纲）
│
├── prompts-reference/                   ← 已 clone（参考库，只读）
│   ├── awesome-gpt-image/
│   ├── awesome-gpt-image-2-prompts/
│   ├── awesome-seedance/
│   └── Seedance2-Storyboard-Generator/
│
├── prompts/                             ← 我们撰写的最终提示词
│   ├── README.md                        ← 提示词索引（按 wave 排序）
│   ├── static/                          ← gpt-image-2 提示词
│   │   ├── S1-wordmark-zh.md
│   │   ├── S2-seal.md
│   │   ├── S3-desk-scene.md
│   │   ├── S4-parchment-scroll.md
│   │   ├── S5-sticky-note.md
│   │   ├── S6-world-map.md
│   │   └── S7-cosmos-starfield.md
│   └── video/                           ← seedance2 提示词
│       ├── V1-desk-ambient-loop.md      (按需)
│       ├── V2-parchment-unfurl.md       (按需)
│       └── V3-cosmos-transition.md      (按需)
│
└── generated/                           ← 生成结果归档（每次跑都留底）
    ├── static/
    │   └── S{n}/
    │       ├── attempt-01/              ← 每轮 4 张候选图
    │       ├── attempt-02/
    │       └── final.png                ← 选定版本
    └── video/
        └── V{n}/
            ├── attempt-01/
            └── final.mp4
```

**生成结果命名约定**：
- 候选轮次 `attempt-NN/`，每轮存全部 raw 输出（不挑选、不删）
- 选定版本 `final.{png|svg|webp|mp4}` 放在资源代号根目录
- 每次新轮次开始前，更新对应 `prompts/{static|video}/{代号}.md` 末尾的「迭代日志」

**最终归档目标**（实现阶段从 `generated/` 拷贝到站点静态目录）：

```
public/art/
├── signatures/  wordmark-zh.svg, seal-jie.png, seal-xfm.png
├── homepage/    desk-scene.webp, parchment-scroll.png, sticky-note.png
├── map/         world-map-base.webp, world-map-base@2x.webp
├── cosmos/      starfield.webp
├── textures/    grain-paper.png
├── masks/       edge-wear.svg, paper-curl.svg
└── motion/      (按需) parchment-unfurl.mp4, cosmos-transition.mp4
```

## 5. 分批顺序与依赖 (Wave Ordering)

由小到大、由签名到场景。每个 wave 完成 + 验收后才进入下一个。

### Wave 1 — 签名层（先小后大、用来摸清工具脾气）
- **S1** 「晚樵庐」字标
- **S2** 印章红方章（两版）

> **理由**：体积小、迭代快、复用极广。落地后所有其它资源都可以挂上签名一并验收。同时 gpt-image-2 在中文行书 / 篆书上的成功率是个未知数，先用小图压力测试，必要时回退到"字魂手书 + 手描 SVG"路线。

### Wave 2 — 首页三件套（同会话同种子，保证调性统一）
- **S3** 书桌场景
- **S4** 羊皮卷
- **S5** 春绿便签

> **理由**：三件最终要合成在同一帧。最佳做法是同一个 gpt-image-2 会话内连续生成（必要时引用前一张作为风格参考），让笔触和色调一致。

### Wave 3 — 大图（最复杂、留到熟练后）
- **S6** 异世界地图
- **S7** 星空背景

> **理由**：地图含 5 区 + 8–10 hotspot 位 + 等距视角 + 羊皮材质，极易翻车，预估 5–8 轮迭代。星空相对简单，但分辨率大、星点分布是另一个考验。

### Wave 4 — 工具件（不走 AI）
- **T1** grain-paper.png
- **T2** edge-wear.svg / paper-curl.svg

### Wave 5 — 动态资源（仅在静态版上线、能感受到"哪里少了一口气"时再做）
- **V3** cosmos-transition（最有价值）
- **V2** parchment-unfurl（次之）
- **V1** desk-ambient-loop（CSS 已够，最低）

## 6. 提示词写作规约 (Prompt Conventions)

### 6.1 来自 DESIGN.md 的硬约束（每条 prompt 都必须遵守）

每条 prompt 末尾必须显式列出：

- **色板锚点**：用 OKLCH 数值 + 对应 token 名（如 `oklch(89% 0.04 80) — map-parchment`），不写 hex
- **风格锚点 (positive)**：参考导演 / 工作室 / 媒介，1–3 个，对应 DESIGN.md §1 北极星
- **反例 (negative)**：硬抄 [PRODUCT.md anti-references](../PRODUCT.md) 与 DESIGN.md Named Rules，例如：
  - NOT photorealistic, NOT 3D rendered, NOT photograph
  - NOT cyberpunk, NOT hacker chic
  - NOT miHoYo-style glowing KV
  - NOT high-saturation neon
  - NOT modern infographic / SaaS clean illustration
- **构图与留白**：明确画面占比 / 留白方位 / 透明背景需求

### 6.2 借鉴自 `awesome-gpt-image*/` 的句式

gpt-image-2 中文 prompt 通用结构：

```
生成一张 [媒介]：[主体描述]，[环境与光线]，[材质与笔触]，[色调与情绪]。
[构图细节：视角、画面占比、留白]。
风格参考：[1–3 个具体作品 / 导演]。
反例：NOT [反例 1]，NOT [反例 2]，NOT [反例 3]。
[输出规格：分辨率、比例、透明背景、文件格式]。
```

### 6.3 借鉴自 `awesome-seedance/` 的脚本结构

seedance2 视频 prompt 通用结构：

```
风格：[镜头语言 / 媒介]。
时长：N 秒。

[00-0Xs] 镜头 1：[景别 / 主体动作 / 情绪]。
[场景细节、光线变化、运动节奏]。

[0X-0Ys] 镜头 2：…

[技术参数：景深、机位、运动模糊、降噪、声音处理（如适用）]。
```

> 本项目几乎所有视频都是**单镜头 + 微变化**，不需要 3 段切换。把脚本结构压成 1 段即可，但保留时间轴写法以便控制节奏。

### 6.4 不借鉴的部分（参考库里有但本项目禁用）

- **写实人像 / 网红脸 / 凡尔赛腔**：本站无人物
- **iPhone 抓拍 / RAW 质感**：与"羊皮卷 / 暖灯油画"的物理质感冲突
- **赛博朋克霓虹 / 高饱和**：违反 DESIGN.md §2 多区委托色板原则
- **直接抄 IP 名（《塞尔达》《GTA》《黑神话悟空》）**：反例 #1 & #5

## 7. 单资产工作流 (Per-Asset Loop)

每张资产走相同的四步循环：

```
[我]                           [你]                          [我]
撰写/微调 prompt  →  喂给 gpt-image-2 / seedance2  →  对照 DESIGN.md 验收
   ↑                       ↓ (4 张候选 / 1 段视频)        ↓
   └────不通过则改 prompt ←────────────────────────  挑选 + 后处理 + 归档
```

**单轮迭代 SOP**：

1. **生成前**：你确认提示词版本号（如 `S1-wordmark-zh.md @ rev3`），把生成参数（aspect ratio / seed / 候选数量）抄到 `prompts/static/S{n}.md` 的"本轮参数"段
2. **生成中**：你跑 4 张候选（视频跑 1–2 段），原始结果全部存到 `generated/static/S{n}/attempt-NN/`
3. **生成后**：我用 [验收清单](#8-验收清单-acceptance-checklist) 逐项打勾。三种结局：
   - **通过 ≥1 张** → 选定版本拷为 `final.{ext}`，记录哪轮哪张
   - **接近但有具体缺陷** → 我改 prompt 局部参数（不是重写），版本号 +1
   - **整体方向偏** → 我重写 prompt 主体（如换风格锚点 / 重排反例），版本号 +1

4. **归档**：每次都更新对应 prompt 文件末尾的「迭代日志」表（轮次 / 修改了什么 / 结果如何），便于回溯

## 8. 验收清单 (Acceptance Checklist)

每张候选图 / 视频按以下逐项打勾。**任何一项不通过即重生成**。

### 通用项（所有资产）

- [ ] **色值匹配**：用取色器抽 3 个代表点，OKLCH 落在对应 token ±5% L、±0.02 C、±10° H 内
- [ ] **无 anti-reference 触发**：列出 PRODUCT.md 八条 anti-ref，逐条核对
- [ ] **无现代/数字感污染**：不出现 SaaS 截图、UI 元素、3D 渲染、CG 高光、霓虹光晕、写实皮肤
- [ ] **构图与留白匹配规格**：画面占比、留白方位、空位区域大小都对得上 DESIGN.md §5
- [ ] **分辨率与格式正确**：分辨率不低于规格、保留所需透明背景

### 资产特定项（举例）

- **S1 字标**：三个字结构正确（不串字）、可见飞白、无系统字体的对齐感
- **S2 印章**：边缘不齐、像手按上去；篆书可识别；红色不带橘也不带紫
- **S3 书桌**：俯视约 75° 倾角、灯光集中在中央 60%、桌面明显空（无物件）
- **S6 地图**：5 区都能识别（鸢尾平原 / 钢铁书库 / 烹饪窝棚 / 观星塔 / 旅人客栈）；hotspot 位置已留白；等距视角；羊皮 grain 完整保留
- **S7 星空**：3 层星点深度可辨；银河带不刺眼；星座连线清晰；不出现高饱和星云

(每张资产的 prompt 文件 §3 会有完整版逐项清单)

## 9. 风险与回退 (Risks & Fallbacks)

| 风险 | 发生概率 | 回退方案 |
|---|---|---|
| gpt-image-2 中文行书翻车（S1） | 中 | 用 [字魂 36 号-行楷体](https://izihun.com/) 或类似手写字体输出 → Illustrator 描线 → SVG |
| 篆书印章「桀」字识别失败（S2） | 低 | 用现成的篆书字典字形（如《说文解字》数据库）→ 红色色块 + 文字图层手工合成 |
| 地图 5 区辨识度不足（S6） | 高 | 把 5 区拆成 5 张 1024 局部图分别生成 → Photoshop 拼接到等距底图上 |
| 等距视角偏移（S6） | 中 | 提示词里加"orthographic projection at 30° axonometric tilt"等更精确的几何术语 |
| 星空过于"NASA 写实"（S7） | 中 | 强化反例 + 加 "vintage astronomy chart, hand-illustrated, NOT photograph" |
| 视频边界卡顿（V*） | 中 | seedance2 输出后 ffmpeg crossfade 0.3s 自循环 |

## 10. 下一步 (Next Step)

**等你点头**，我立刻开始做：

1. **写 Wave 1 提示词卡片** — `prompts/static/S1-wordmark-zh.md` 与 `prompts/static/S2-seal.md`
2. 卡片包含：完整 gpt-image-2 中英文 prompt（中文主、英文备）、生成参数建议、验收清单、迭代日志模板
3. 你拿去跑 4 张候选 → 我做第一次验收 → 进入循环

**同时建议（不阻塞你点头）**：

- [ ] **更新 [DESIGN.md](../DESIGN.md) 第 168–172 行的归档路径**：把 `arknights-design-system/...` 改为 `arknights-analysis/arknights-design-system/...`。这是小修，要不要现在做？

---

## 附录：迭代日志模板（每个 prompt 文件末尾共用）

```markdown
## 迭代日志

| 轮次 | 日期 | Prompt 修改 | 候选数 | 结果 | 备注 |
|------|------|------------|--------|------|------|
| 01   | YYYY-MM-DD | 初版 | 4 | 0/4 通过 | 笔触太细，缺少飞白 |
| 02   | YYYY-MM-DD | 加 "visible ink loading and feathering" | 4 | 2/4 接近 | 但「樵」字结构错 |
| 03   | YYYY-MM-DD | 单字描述更精确 | 4 | 1/4 选定 | final.png 来自这轮第 3 张 |
```
