---
title: Learning Rust, Quietly
date: 2026-04-20
category: tech
lang: en
slug: learning-rust-quietly
summary: A few notes I've been making while re-reading *Programming Rust*. Not for publishing — for thinking clearly first.
tags:
  - rust
  - notes
---

I'm re-reading *Programming Rust*. The second pass feels completely different from the first — not because the book changed, but because I've stepped on more of the rakes it warns about.

## What the borrow checker actually taught me

Not ownership. **Naming things carefully.** When the borrow checker complains, it's usually pointing out that I was less clear than I thought about who owns this slice of data.

## What's next

- Rewrite a small Python tool of mine in Rust
- Not for performance — for practice
- I want to see whether `tokio`'s cancellation semantics are really as subtle as people say

No rush.
