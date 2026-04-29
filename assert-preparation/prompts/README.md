# Prompts Index

提示词主索引。**每个文件就是一份独立的提示词卡片**，包含主 prompt、生成参数、验收清单、迭代日志。

主流程见 [../PLAN.md](../PLAN.md)。视觉规格见 [../../DESIGN.md](../../DESIGN.md) §5。

## 静态资源 (`static/`，工具 = gpt-image-2)

| Wave | 代号 | 文件 | 状态 |
|------|------|------|------|
| 1 | S1 | [S1-wordmark-zh.md](static/S1-wordmark-zh.md) | **已定稿** |
| 1 | S2 | [S2-seal.md](static/S2-seal.md) | **已定稿** (A、B 版均完成) |
| 2 | S3 | [S3-desk-scene.md](static/S3-desk-scene.md) | **已定稿** |
| 2 | S4 | [S4-parchment-scroll.md](static/S4-parchment-scroll.md) | **已定稿** |
| 2 | S5C | [S5-quiet-object.md](static/S5-quiet-object.md) | **已定稿** (S5A/B 落选，S5C v2 选定) |
| 3 | S6 | [S6-world-map.md](static/S6-world-map.md) | **已定稿** |
| 3 | S7 | [S7-cosmos-starfield.md](static/S7-cosmos-starfield.md) | **已定稿** |

## 动态资源 (`video/`，工具 = seedance2，按需启动)

| Wave | 代号 | 文件 | 状态 |
|------|------|------|------|
| 5 | V1 | [V1-desk-ambient-loop.md](video/V1-desk-ambient-loop.md) | **已定稿**（seedance 2.0） |
| 5 | V2 | [V2-parchment-unfurl.md](video/V2-parchment-unfurl.md) | **已定稿**（seedance 2.0） |
| 5 | V3 | [V3-cosmos-transition.md](video/V3-cosmos-transition.md) | **已定稿**（seedance 2.0，一次通过） |

## 状态字段说明

- **待撰写**：还没写 prompt
- **待生成**：prompt 已写，等你跑生成
- **迭代中**：已生成至少一轮，未通过验收
- **已定稿**：`generated/{static|video}/{代号}/final.{ext}` 存在
- **待评估**：等静态版上线后再决定是否需要

## 工具件（已完成，不走 AI）

| 类型 | 输出 | 生成方式 |
|---|---|---|
| T1 纸感颗粒 | [`generated/textures/grain-paper.png`](../generated/textures/grain-paper.png) · `grain-parchment.png` · `grain-cosmos.png` | [`generator/tools/make_grain.py`](../generator/tools/make_grain.py) — numpy FFT 噪声 |
| T2 卷角蒙版 | [`generated/masks/paper-curl.svg`](../generated/masks/paper-curl.svg) + 3 个变体 | [`generator/tools/make_masks.py`](../generator/tools/make_masks.py) — 程序化 Bezier |
| T2 磨损蒙版 | [`generated/masks/edge-wear.svg`](../generated/masks/edge-wear.svg) + 3 个变体 | 同上 — 边缘随机抖动 |
