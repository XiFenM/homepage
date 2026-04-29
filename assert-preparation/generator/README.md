# Asset Generator

通过 ZenMux 的 Vertex AI 协议调用 `openai/gpt-image-2`，按 `prompts.py` 里的清单批量生成 Wave 1+ 静态资源。

## 准备

```bash
export ZENMUX_API_KEY=sk-...   # 你的 ZenMux key
```

依赖已通过 `uv add` 写入 `pyproject.toml`，首次运行 `uv` 会自动建虚拟环境。

## 用法

```bash
# 单个资产
uv run python generate.py S1

# 多个连续跑
uv run python generate.py S2A S2B

# 全部
uv run python generate.py --all
```

## 输出位置

```
../generated/static/{code}/attempt-{NN}/
    01.png ~ 04.png        ← 候选图（每轮 4 张，由 prompts.py 的 n 控制）
    prompt-used.txt        ← 这一轮实际用的 prompt（snapshot，便于对比）
    meta.json              ← 参数 + 模型 + 用时
```

`attempt-NN` 自动递增，不会覆盖旧轮次。

## 编辑提示词

提示词的**机器执行版**在 [`prompts.py`](prompts.py)。**人类阅读版**在 [`../prompts/static/S{n}-*.md`](../prompts/static/)。修改时**两边都要改**，避免漂移。

每个 `AssetSpec` 字段：
- `code`：资产代号（S1, S2A, ...）
- `label`：人类可读简介
- `prompt`：模型实际收到的字符串
- `image_size`：`WxH`，必须 ÷16 整除、最长边 ≤3840、比例 ≤3:1、总像素 ≥655,360
- `n`：单次返回的候选数（默认 4）

## API 限制速记

来自 [`../../zenmux-image-generation.md`](../../zenmux-image-generation.md) 与 OpenAI 上游：

- `background` 透明背景参数 ❌ — 透明只能在 prompt 里说，必要时 remove.bg 后处理
- `quality` 仅 TypeScript SDK 支持 ❌ — Python 这边走默认质量
- `seed` 不在文档列出 ❌ — 同提示词二次跑结果会变，无法严格复现
- `n` 单次 1–10 张
- 自定义尺寸支持，但有上述像素/比例约束
