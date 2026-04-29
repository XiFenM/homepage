# V1 · 首页书桌环境循环 (Desk Ambient Loop)

> **Wave 5** · 工具 = seedance2 · 起始帧 = `static/S3/final.png`

## 1. 用途与规格 (Spec)

| 项 | 值 |
|---|---|
| 用途 | 首页 hero 背景的环境动效（替代纯静态图 + CSS 颗粒） |
| 起始帧 | [S3 书桌场景 final.png](../../generated/static/S3/final.png) |
| 输出格式 | MP4 |
| 分辨率 | 720p (16:9) |
| 时长 | 8 秒（首尾可循环衔接） |
| 备选方案 | CSS `<div class="dust-mote">` × 4–6 + radial-gradient 微变化 |

## 2. 主 Prompt

见 [`generator/prompts.py`](../../generator/prompts.py) 的 `V1`。核心要求：
- **镜头完全锁死**（无平移/推拉/变焦/旋转）
- 4–6 颗尘埃在光圈内自然飘动
- 光圈亮度起伏 5%（呼吸感，4 秒周期）
- 桌面、构图不变
- 保持油画式数字插画笔触（吉卜力风），**禁止变成 3D / 写实 / 动画 CG**
- 8 秒首尾可循环

## 3. 验收清单

### 3.1 通用项

- [ ] 镜头完全锁定，无任何视点变化
- [ ] 起始帧画面与 S3 final.png 高度一致（暖胡桃木、灯光圈位置、夜屋氛围）
- [ ] 色调保持原画的 OKLCH 色板，不偏色
- [ ] 整体仍是油画手绘风，不变成 3D / 写实 / CG 动画

### 3.2 动效项

- [ ] 4–6 颗尘埃在光圈内可见，运动**自然**——不是机械循环、不是粒子特效
- [ ] 尘埃运动速度合理（像现实尘埃漂浮，每秒 5–10 像素级别）
- [ ] 灯光圈有微弱呼吸（约 5% 亮度起伏）
- [ ] 8 秒首尾可衔接（前 0.5 秒和最后 0.5 秒画面相近）

### 3.3 静态保留项

- [ ] 桌面木纹、构图、阴影**完全不动**
- [ ] 背景书架剪影**完全不动**
- [ ] 没有意外人物 / 物件 / 文字出现

## 4. 风险与回退

| 失败模式 | 应对 |
|---|---|
| 模型把油画风变成 3D 渲染 | prompt 加粗反例 + 试 Veo 3.1 备选 |
| 镜头有意外推拉 | "fixed camera, no zoom, no pan, no rotation" 顶部加粗 |
| 尘埃运动机械感 | "natural dust drift in still air, not VFX particles" |
| 8 秒不能循环 | 视频后期用 ffmpeg crossfade 0.3s 自循环；或丢弃，回退 CSS |
| 整体环境光变化大 | "ambient unchanged except for subtle 5% lamp glow breathing" |

## 5. 迭代日志

| 轮次 | 日期 | Prompt 修改 | 时长/分辨率 | 结果 | 备注 |
|------|------|------------|-----|------|------|
| 01 | 2026-04-28 | 初版（**Veo 3.1**） | 8s/720p | 落选 | 117s 出图 1.5MB；油画风保留极好；但 frame-diff 显示动效极微弱（仅左上零星亮点），整体过于静态。归档备查。 |
| 02 | 2026-04-28 | 同 prompt（切回 **seedance 2.0**，原模型名 vendor prefix 写错为 `volcengine/`，正确是 `bytedance/doubao-seedance-2.0`） | 8s/720p | **选定** | 266.7s 出图 2.2MB；油画风保留同样好；frame-diff 显示整张画面有 painterly shimmer 但放大 400×400 patch 看仍克制不刺眼——正是"几乎静止但仍有呼吸"的目标。**final.mp4 = attempt-02/01.mp4**。 |
