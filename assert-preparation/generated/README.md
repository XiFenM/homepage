# Generated Assets Archive

**这个文件夹存放每次生成的原始结果**，按资产代号 + 轮次组织。

## 目录结构

```
generated/
├── static/
│   └── S{n}/
│       ├── attempt-01/        ← 第 1 轮跑出来的全部候选（不挑选、不删）
│       │   ├── 01.png
│       │   ├── 02.png
│       │   ├── 03.png
│       │   └── 04.png
│       ├── attempt-02/        ← 第 2 轮（如果第 1 轮没通过）
│       └── final.{png|svg}    ← 选定的版本，从某一 attempt 拷贝过来
└── video/
    └── V{n}/
        ├── attempt-01/
        │   ├── 01.mp4
        │   └── prompt-used.txt
        └── final.mp4
```

## 规则

1. **每轮都留底**——通过验收的轮次也保留 attempt 目录，便于回看演化
2. **`final.{ext}` 永远只有一份**——重新选定时直接覆盖
3. **每个 attempt 目录可以放一份 `prompt-used.txt`**，记录这一轮实际用的 prompt（以防 prompt 文件后续又改了）
4. **拿去上线时**：从 `final.{ext}` 拷贝到 `public/art/{zone}/`，本目录保留作为产出档案

## 不要在这里 commit 大文件

> 如果接下来用 git 管理项目，建议给 `assert-preparation/generated/` 加 `.gitignore` 或用 git LFS。本文件夹的内容是**素材产出档案**，不是源码。
