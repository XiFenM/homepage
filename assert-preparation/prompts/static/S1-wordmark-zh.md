# S1 · 「晚樵庐」手写字标 (Brush Wordmark)

> **Wave 1** · 工具 = gpt-image-2 · 关联组件 [DESIGN.md §5 Brush Wordmark](../../../DESIGN.md)

## 1. 用途与规格 (Spec)

| 项 | 值 |
|---|---|
| 出现位置 | (a) 首页 hero 桌面左上 (b) 简约站头部 (c) favicon / og-image 微缩 |
| 渲染尺寸 | `clamp(2.8rem, 8vw, 5rem)` (Display Brush token) |
| **本次输出** | 2048×768 PNG，**透明背景** |
| 后处理 | Illustrator / Figma 描线 → SVG 入库 (`public/art/signatures/wordmark-zh.svg`) |
| Token 锚点 | `ink-black` = `oklch(22% 0.01 250)`（蓝偏移黑） |

## 2. 主 Prompt (中文主版)

```
生成一张水墨手写字标的扫描图：横排三个汉字「晚樵庐」，行书（半草书）笔法。
墨色为带冷蓝底调的浓黑（OKLCH 22% 0.01 250），起笔可见浓墨蓄力的湿润感，
收笔留有飞白与微微擦痕，像是用兼毫毛笔在生宣上一气呵成。三字结构精准、
间距匀称，「晚」字左收右放，「樵」字木字旁笔势直挺，「庐」字广字头开阔
而稳。墨迹有自然渗透形成的轻微毛边，但不渗透到失去笔锋的程度。

字下方居中放置一行小很多（高度约为汉字的 25%）的拉丁拼音「WǍN QIÁO LÚ」，
拼音也是手写笔触（不是印刷字体），笔形与上方汉字呼应——粗细变化、起收笔
方式同源，但更冷静收敛。元音 Ǎ 上的小帽 (caron) 也是手写。

整体留白考究：三字横向占画面 80% 宽度居中，上下各留 10% 透气空间。

风格参考：王羲之《兰亭序》行书、日本书道（書道）家井上有一的力道感、黑泽明
电影片头题字、龙瑛宗手书招牌。

反例：NOT 印刷字体输出，NOT 矢量光滑曲线，NOT 数字毛笔笔刷预设效果，
NOT 美术字标志设计感，NOT Photoshop 笔刷描边，NOT 油画质感，NOT 3D，
NOT 现代书法家网红字。

输出：透明背景 PNG，2048×768，无任何边框、印章、签名或装饰元素。
```

## 3. 主 Prompt (英文备版，仅当中文版连续 2 轮失败时启用)

```
A scanned ink calligraphy of three Chinese characters "晚樵庐" hand-brushed in
行书 (xíngshū, semi-cursive script), arranged horizontally, written in a single
continuous take with a traditional兼毫 brush on raw xuan paper. Ink color: deep
black with cool blue undertone (OKLCH 22% 0.01 250). Visible brush dynamics:
ink-loaded openings show wet density; closing strokes show feathering (飞白) and
fine drag marks. Each character: structurally accurate, evenly spaced. "晚" tight
on left, expansive on right; "樵" with vertical wood-radical strokes; "庐" with
open broad-roof radical sitting stably.

Below the three characters, centered, in much smaller scale (~25% of the
character height), the pinyin "WǍN QIÁO LÚ" — also hand-brushed (NOT a system
font), with stroke modulation and start/end behaviors that visually rhyme with
the Chinese characters above. The caron over Ǎ is also hand-drawn.

Composition: characters span ~80% width, centered, with 10% breathing room top
and bottom.

Style references: Wang Xizhi's《兰亭序》semi-cursive, Japanese 書道 brushwork
(井上有一's force), Akira Kurosawa film title cards, vintage hand-painted shop
signs.

Anti-references: NOT a font output, NOT vector-clean curves, NOT a Photoshop
brush preset effect, NOT modern logo-design calligraphy, NOT a calligraphy-app
generated stroke, NOT 3D, NOT oil-paint texture, NOT influencer-style brush
calligraphy.

Output: transparent PNG, 2048×768, no borders, no seals, no signatures, no
decorations.
```

## 4. 生成参数建议

| 项 | 值 | 备注 |
|---|---|---|
| 候选数量 | **4 张** | 每轮固定 4 张，便于横向比较 |
| 比例 | 16:6 (2048×768 ≈ 2.67:1) | 字标偏横长 |
| Seed | 首轮不锁；选定方向后**锁种子**用于后续微调 | |
| 中英版本 | **首轮中文** | 失败 2 轮后切英文版 |

## 5. 验收清单 (Acceptance Checklist)

### 5.1 通用项 (从 PLAN.md §8 继承)

- [ ] 墨色 OKLCH 抽 3 点落在 22%±5% L、0.01±0.02 C、250±10° H
- [ ] 无 anti-reference 触发（八条逐一过）
- [ ] 透明背景干净，无残留底色 / 无白边

### 5.2 字标特定项

- [ ] **三字结构正确**——「晚」「樵」「庐」三字均为字典正体，不出现错字、串字、缺笔
- [ ] **行书笔意**——非楷书（过端正）、非草书（过潦草），介于二者
- [ ] **可见飞白**——至少 2 个收笔处出现飞白扫纹，不是全篇湿润
- [ ] **可见浓墨起笔**——至少 1 处起笔有"蓄墨入纸"的湿重感
- [ ] **三字间距匀称**——不能某两字粘连或某字孤立
- [ ] **拼音笔形匹配**——「WǍN QIÁO LÚ」是手写，不是 Times / Cinzel 等系统字体
- [ ] **拼音不喧宾夺主**——拼音视觉重量明显小于汉字（约 25% 高度）
- [ ] **整体留白透气**——上下 10% 留白没有被笔触侵占
- [ ] **没有意外元素**——无印章、无签名、无装饰、无水印

## 6. 已知风险与回退

参见 [PLAN.md §9](../../PLAN.md#9-风险与回退-risks--fallbacks)：

> gpt-image-2 中文行书翻车概率中等。**连续 2 轮（共 8 张）均无任何一张通过 5.2 的"三字结构正确"项**，立刻切回退方案：
>
> 1. 用 [字魂 36 号-行楷体](https://izihun.com/) 或类似行书字体打出「晚樵庐」三字
> 2. Illustrator 中转为 outline，手工添加飞白笔触（用毛笔笔刷描）
> 3. 拼音区用同一字体的拉丁字符或 Cormorant Garamond Italic 描线
> 4. 导出 SVG 直接入库，跳过 AI 生成

## 7. 迭代日志

| 轮次 | 日期 | Prompt 修改 | 候选数 | 结果 | 备注 |
|------|------|------------|--------|------|------|
| 01 | 2026-04-27 | 初版 (本文件 §2 中文主版) | 4 | **2/4 通过 → 选定 01** | 01、04 通过；02「庐」字结构错；03 偏刻字、欠湿润。**final.png = attempt-01/01.png**。拼音「WǍN QIÁO LÚ」是模拟手写体的字体非真笔触，可接受。|

---

## 附：去掉拼音的极简变体（备用）

如果首页 hero 的字标"汉字+拼音"显得过满，可生成纯三字版本作为备选。**首轮不做这个变体——先把主版定下来再说**。

```
（与 §2 相同主体，但删除"字下方居中放置一行小很多..."整段，并把
"输出"段改为：透明背景 PNG，2048×512，仅三个汉字居中。）
```
