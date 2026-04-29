# Deployment · Cloudflare Pages

晚樵庐部署到 Cloudflare Pages，走静态生成（SSG）。

## 一次性准备

### 1. 把代码推到 Git 仓库

Cloudflare Pages 通过 git 连接自动 build。GitHub / GitLab / Bitbucket 任选。

```bash
cd /root/workspace/homepage    # 项目根（不是 web/ 子目录）
git init
git add .
git commit -m "Initial scaffold: 晚樵庐 + 勿忘我 + 美术资产"
git branch -M main
git remote add origin git@github.com:你的账号/homepage.git
git push -u origin main
```

> 注意：`assert-preparation/generated/` 共 ~380MB。建议加 `.gitignore` 排除（重生成的话 prompts.py 在）；或用 git-lfs。详见下方 [.gitignore 建议](#gitignore-建议)。

### 关于 Submodule（4 个 prompt 参考库）

[`assert-preparation/prompts-reference/`](../assert-preparation/prompts-reference/) 下的 4 个参考库通过 git submodule 引用，每个 `.gitmodules` 里设了 `shallow = true`。

- **本地 clone**：`git clone --recurse-submodules <url>` 一次到位（推荐）
- **二次同步 submodule**：`git submodule update --init --recursive --depth 1`
- **更新 submodule 到最新 main**：`git submodule update --remote`
- **Cloudflare Pages**：默认会自动 fetch submodule（约 +30 秒 build 时间）；submodules 仅供 prompt 参考，不参与 build，**可以忽略**

如果想让 Cloudflare Pages **完全跳过** submodule 提速 build，build 命令前加：

```bash
git -c submodule."assert-preparation/prompts-reference/*".update=none submodule update --init && cd web && bun install && bun run generate
```

但默认建议保留 submodule fetch——文档关联性强，build 时间影响微小。

### 2. Cloudflare Pages 控制台建项目

1. 登录 [https://dash.cloudflare.com/](https://dash.cloudflare.com/) → Workers & Pages → Create → Pages → Connect to Git
2. 选择刚才推的 GitHub repo
3. Build 配置：

   | 字段 | 值 |
   |---|---|
   | Production branch | `main` |
   | Framework preset | `Nuxt.js` |
   | Build command | `cd web && bun install && bun run generate` |
   | Build output directory | `web/.output/public` |
   | Root directory | （留空，使用仓库根） |
   | Environment variables | `NODE_VERSION=22`<br>`NPM_FLAGS=--version`（绕过自动 npm install）<br>**或者** 用 Bun 官方支持，下方说明 |

4. **如果 Cloudflare Pages 不识别 bun**：在 build command 里换为
   ```
   cd web && npm install -g bun && bun install && bun run generate
   ```

### 3. 自定义域名 xifengmu.net

1. 项目 → Custom domains → Set up a custom domain
2. 输入 `xifengmu.net`
3. Cloudflare 会引导你把域名 nameserver 转过来（如果你已经在 Cloudflare 管理域名，自动配 CNAME）
4. 自动签发 SSL（几分钟到几小时）

完成后访问 https://xifengmu.net 应直接看到 hero。

## 后续每次 deploy

```bash
git push origin main
```

Cloudflare Pages 每次 push 自动 build & deploy（~2–3 分钟）。Preview branch 也自动部署到子域名。

## 本地预览生产 build

```bash
bun run generate
bun run preview                  # 内置 nitro preview
# 或 npx serve .output/public    # 静态服务器，模拟 Cloudflare Pages
```

## .gitignore 建议

`assert-preparation/generated/` 体积大、可重生成（有 prompts.py 即可），建议 ignore：

```gitignore
# In root .gitignore
node_modules/
.output/
.nuxt/
.cache/
.DS_Store

# Asset generation outputs (regenerable from prompts.py)
assert-preparation/generated/
```

但 `web/public/art/` 必须**保留**（最终上线资产，58MB）。如果 GitHub 的 100MB 单文件限制成为问题，再考虑 git-lfs。

## 故障排查

| 问题 | 原因 | 解决 |
|---|---|---|
| `/勿忘我` 404 | `_redirects` 没生效 | 确认 `web/public/_redirects` 存在；Cloudflare Pages dashboard → Functions/Redirects 检查规则被识别 |
| `/random-bad-slug` 显示空白 | SPA fallback | 这是正常的——Nuxt 生成 200.html 作为 fallback |
| 视频播放失败 | 浏览器策略 | 确认所有 `<video>` 是 `muted` 才能 autoplay；H.264 编码兼容性 |
| 首次部署 build 失败 | bun 不可用 | 改用 `npm install -g bun && cd web && bun ...` 命令 |

## 当前部署目标

| 资产 | 大小 |
|---|---|
| HTML（10 个路由）| ~50 KB |
| JS chunks | ~280 KB（gzip 后 ~100 KB） |
| CSS | <50 KB |
| 美术资产 (`/art/*`) | ~58 MB |
| **总计** | **~59 MB** |

**首次访问关键路径**（不含视频）：~600 KB（HTML + JS + CSS + S3 desk-scene.png + S5C card-stack.png）。
**视频懒加载**：只在 hero 进入视口或 hover 触发时载入。
