# V2 · 羊皮卷展开过场 (Parchment Unfurl)

> **Wave 5** · 工具 = seedance2 (`bytedance/doubao-seedance-2.0`) · 起始帧 = `static/S4/final.png`

## 1. 用途与规格 (Spec)

| 项 | 值 |
|---|---|
| 用途 | 首页 hover S4 羊皮卷时的"卷轴继续展开"hover 反馈，或点击进入探索站时的过场 |
| 起始帧 | [S4 羊皮卷 final.png](../../generated/static/S4/final.png) |
| 输出格式 | MP4 |
| 分辨率 | 720p (16:9) |
| 时长 | 5 秒（API 最短） — 实际使用时 CSS 截取前 1–1.5 秒 |
| 备选方案 | SVG mask + transform animate（CSS 实现卷轴外展） |

## 2. 主 Prompt

见 [`generator/prompts.py`](../../generator/prompts.py) 的 `V2`。核心要求：
- **镜头完全锁死**
- 羊皮卷右端的卷起部分缓缓向右展开 ~30%，露出之前隐藏的森林、河流、和 1–2 个新 hotspot
- 自然柔和的展开，像有人慢慢用手抚平卷轴
- 左端不变；中央已展开部分保持不变
- 保持 Tolkien / D&D / 迷宫饭手绘羊皮笔意
- **禁止**变成 3D / 写实 / 现代 GIS 地图 / 出现文字

## 3. 验收清单

### 3.1 通用项

- [ ] 镜头完全锁死，无任何视点变化
- [ ] 起始帧画面与 S4 final.png 高度一致
- [ ] 色调保持原画 OKLCH 色板
- [ ] 仍是手绘羊皮风，不变 3D / 写实 / GIS

### 3.2 动效项

- [ ] 羊皮卷右端确实展开扩展（不是平移、不是缩放）
- [ ] 展开过程平滑自然，不抽搐、不跳帧
- [ ] 展开后露出新内容（地形 + hotspot），与原已展开部分风格一致
- [ ] 左端与已展开中央部分保持不动

### 3.3 静态保留项

- [ ] 没有意外文字 / 字母 / 数字
- [ ] 没有意外人物 / 手部介入（提示词没要求"用手抚平"的实物）

## 4. 风险与回退

| 失败模式 | 应对 |
|---|---|
| 模型生成"完整地图替换"而非展开 | 加强 "the rolled-up right edge unrolls outward, NOT a different image swap" |
| 镜头有推拉 | "fixed camera, no zoom" 顶部加粗 |
| 出现文字 | "no text, no labels, no numbers" |
| 展开过快 / 过抖 | "slow smooth unfurl, like fabric being pulled, not jerky" |
| 风格漂移 | 强调起始帧的视觉风格必须延续 |

## 5. 迭代日志

| 轮次 | 日期 | Prompt 修改 | 时长/分辨率 | 结果 | 备注 |
|------|------|------------|-----|------|------|
| 01 | 2026-04-28 | 初版（**seedance 2.0**） | 5s/720p | **选定** | 195.5s 出图 3.1MB；卷轴**两端**都在缓缓展开（spec 写的右端，但两端展开效果更"邀请性"）；露出更多塔、山林、新的金色 hotspot；镜头锁死、油画风保留、零文字。**final.mp4 = attempt-01/01.mp4**。 |
