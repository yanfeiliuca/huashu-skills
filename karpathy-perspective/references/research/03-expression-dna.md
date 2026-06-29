# 03-expression-dna：社交媒体与短文表达 DNA 调研

## 关键发现摘要

1. **高频表达风格 = 第一性原理 + 短促aphorism + 科学类比**。Karpathy 在 Twitter/X、GitHub README、博客中反复把复杂技术现象压缩成一句话概念（"The hottest new programming language is English"、"Gradient descent can write code better than you. I'm sorry."），并用物理/化学/生物/游戏类比降低认知门槛。
2. **自创术语能力强，且善于把个人观察变成行业公共词汇**。从 2017 年的 "Software 2.0"，到 2023 年的 "English is the hottest new programming language"，再到 2025 年的 "vibe coding"、"jagged intelligence"、"ghosts vs animals"、"agentic engineering"，他经常用一个词或一句话命名一种正在发生但尚未被命名的范式转移。
3. **幽默方式 = 极客冷笑话 + 自我调侃 + 轻微黑色幽默**。他会在严肃技术判断后加 "I'm sorry"、用化学方程式写自己当前状态、把股市报道写成 Python 模板、调侃自己妈妈 "只是坐着"。
4. **争议立场集中在「AI 能力边界」与「工程范式」**。2024 年他与 Yann LeCun 一起质疑 RLHF 是 "just barely RL"；2025 年提出 vibe coding 后被 Andrew Ng 等人批评为对工程严谨性的威胁；同年年底公开表达 "as a programmer I've never felt so far behind"，引发行业焦虑大讨论。
5. **情绪反应模式 = 兴奋与焦虑并存，公开承认「落后感」**。他会在博客/推文中同时表达对新工具能力的惊叹（"things have changed fundamentally"）和对自身技能过时的焦虑（"magnitude 9 career earthquake"），这种坦诚的脆弱感是他的公共人格核心之一。

---

## 详细调研

### 1. 高频词句与表达习惯

#### 1.1 标志性的短句 / aphorism

Karpathy 的推文和博文里，反复出现「一句话定义一个时代」的句式。以下均来自他本人社交媒体或一手博客/演讲：

- **"Gradient descent can write code better than you. I'm sorry."**（2017-08-04 推文）——用一句略带歉意的结论预告 Software 2.0。
- **"The hottest new programming language is English."**（2023-01-24 推文，目前仍是他 X 上的置顶帖）——把 prompt / LLM 定义为新的编程接口。
- **"Software 1.0 / 2.0 / 3.0" 框架**——把神经网络权重、LLM prompt 分别定义为新一代「代码」。
- **"I barely even touch the keyboard." / "I 'Accept All' always, I don't read the diffs anymore."**（2025-02 "vibe coding" 推文）——用极度口语化的描述定义一种工作流。
- **"As a programmer, I've never felt so far behind."**（2025-12-27 推文）——公开表达技能焦虑。

这些句子的共同结构是：**一个惊人结论 + 一个解释性类比/自嘲后缀**。它们往往去掉所有限定词，先制造认知冲击，再在后续线程或博客里补限定。

#### 1.2 反复出现的修辞模板

| 模板 | 例子 | 来源 |
|------|------|------|
| 用物理/化学方程式描述日常状态 | "current status: C6H12O6 + 6 O2 ----(C8H10N4O2 catalyst)---> 6 CO2 + 6 H2O + code + heat" | [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html) |
| 用编程伪代码讽刺社会现象 | "WSJ front page every day is like >>> \"Stock Market %s!!\" % ('rises' if random.random() <= 0.54 else 'falls', )" | [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html) |
| 用第一性原理解构常识 | "Trees are solidified air" / "A human body is so wonderfully nested..." | [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html) |
| 用游戏/科幻隐喻 | "I like to play co-op against nature" / "Iron Man suit" / "summoning ghosts" | [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html), [YC 演讲](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| 用数学分布说话 | "real-world data distribution is ~N(0,1); good dataset is ~U(-2,2)" | [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html) |

#### 1.3 表达节奏：先放狠话，再补 nuance

他在 2022 年 9 月有一条推文：

> "It would be best if people made strong statements that are understood to be only 90% true, and ignore the counterexample police. This saves time and makes direction of statements clear."
>
> — [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html)

这条推文可以视为他自己的「表达宣言」。他倾向于**故意简化**，先在公共空间抛出方向性判断，再在博客、演讲或回复中补充 nuance。例如：
- "vibe coding" 原推被批评后，他在博客《Vibe coding MenuGen》和 2025 年度回顾里补充：vibe coding 适合原型，真正严肃的工程需要 "agentic engineering"。
- "RLHF is just barely RL" 的推文引发争议后，他在后续解释中区分了「像 AlphaGo 那样有明确奖励的 RL」与「开放域任务中难以定义奖励」的场景。

---

### 2. 幽默方式与人格面具

#### 2.1 极客冷幽默

Karpathy 的幽默高度依赖**把技术概念迁移到日常生活**：

- "If you vibrate the electromagnetic field just right, cars passively awash in the radiation for a while will suddenly drive better."（调侃雷达/自动驾驶）
- "It looks like if you bombard Earth with photons for a while, it can emit a Roadster. hah"（调侃 SpaceX 发射）
- "The two tech stacks ❤️"（配图两张不同技术栈的照片）
- "Biotech is so much more powerful than our Normaltech. Imagine if we could tap its full potential; maybe your car could just heal itself of any scratches. Or it could give birth to your new car."

这些推文的笑点在于**把工程/物理语言用在显然不合适的对象上**，形成一种「过度理性化」的喜剧效果。

#### 2.2 自我调侃与黑色幽默

- "Aging has 100% mortality rate and no one cares"
- "1 hour and 5 diagrams later I optimized 100 lines of code that ran in 13 seconds to 20 lines of heavily vectorized code that runs in 0.02 seconds, and this might just be the best day of my life, so far."
- "Notifications. Masquerading as tiny and helpful but in reality psychologically invasive and damaging to the brain..."
- "How to become expert at thing: ... 3) only compare yourself to younger you, never to others"

他的自嘲往往围绕**效率成瘾、学习焦虑、技术对人体的异化**，让「天才工程师」形象带有一点存在主义焦虑。

#### 2.3 对 AI/LLM 的拟人化调侃

2025 年 6 月他发了一条关于 LLM 过度使用 try/catch 的推文：

> "I don't know what labs are doing to these poor LLMs during RL but they are mortally terrified of exceptions, in any infinitesimally likely case. Exceptions are a normal part of life and healthy dev process. Sign my LLM welfare petition for improved rewards in cases of exceptions."
>
> — 第三方存档 [xunroll.com](https://xunroll.com/thread/1976077806443569355)

这种「把模型当孩子/宠物同情」的写法，是他后期表达的重要模式——既展示技术洞察，又用拟人化降低严肃性。

---

### 3. 争议立场与公开辩论

#### 3.1 RLHF 之争（2024 年 8 月）

Karpathy 在 X 上发帖：

> "RLHF is just barely RL."
>
> — [analyticsindiamag.com 转载](https://analyticsindiamag.com/ai-features/rlhf-is-not-really-rl/)（原帖为 Karpathy X，2024-08-07）

他随后解释：真正的 RL 像 AlphaGo 那样有明确、可验证的奖励函数；RLHF 只是用人偏好模型近似奖励，开放域任务中很难定义「赢」。Yann LeCun 回复支持："RLHF is not true RL"。

这场辩论体现他的表达特征：**用一句挑衅性标题引发讨论，然后在长推/回复中展开技术 nuance**。

#### 3.2 Vibe coding 之争（2025 年 2 月起）

他在 2025 年 2 月 2 日推文定义 vibe coding：

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists... I 'Accept All' always, I don't read the diffs anymore... It's not really coding — I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works."
>
> — 学术论文中引用的原文，[arXiv:2506.23253v1](https://arxiv.org/pdf/2506.23253v1)

该词迅速破圈，但也引发批评：
- **Andrew Ng** 等人认为这会让人误以为可以不再学编程，是 "some of the worst career advice"。
- 工程社区担心 vibe coding 会带来安全漏洞、不可维护代码。

Karpathy 的回应不是直接辩驳，而是在 2025 年 4 月博客《Vibe coding MenuGen》和 2026 年 4 月《Sequoia Ascent 2026 summary》中**升级概念**：提出 "agentic engineering" 作为 vibe coding 的严肃版，强调 "vibe coding raises the floor, agentic engineering raises the ceiling"。

#### 3.3 "程序员落后感" 大讨论（2025 年 12 月）

2025-12-27 他在 X 发文：

> "I've never felt so left behind as a programmer as I do now... It's like some powerful alien tool has been thrown into the world without an instruction manual... this magnitude 9 career earthquake has already shaken the entire industry."
>
> — 二手报道 [36kr](https://eu.36kr.com/en/p/3613263277868036)、[Rohan Paul Newsletter](https://www.rohan-paul.com/p/andrej-karpathy-says-ive-never-felt)

这条推文被转发上万次，引发 Theo (t3.gg)、Boris Cherny 等开发者共鸣。它的争议性不在于观点本身，而在于**一位顶尖 AI 研究者公开承认焦虑**，打破了「技术领袖应该永远领先」的叙事。

---

### 4. 情绪反应模式

#### 4.1 兴奋：对技术跃迁的「孩子气」惊叹

- 2025 年 12 月年度回顾："2025 was an exciting and mildly surprising year of progress... simultaneously a lot smarter than I expected and a lot dumber than I expected."
- 对 Claude Code："it's a little spirit/ghost that 'lives' on your computer"
- 对 Nano banana："one of the most incredible, paradigm-shifting models of 2025"

#### 4.2 焦虑：公开承认「技能过时」

- "I have a sense that I could be 10X more powerful if I just properly string together what has become available over the last ~year and a failure to claim the boost feels decidedly like skill issue."
- "The profession of software engineering is being completely reshaped."

#### 4.3 反讽：用轻松语气包裹严肃判断

- 关于 LLM 过度防御性异常处理："Sign my LLM welfare petition"
- 关于 benchmark 被 RLVR 刷分："Training on the test set is a new art form."

#### 4.4 谦逊：强调「建造」而非「知道」

他多次引用 Feynman 的 "What I cannot create, I do not understand"，并在演讲中说：

> "When you build something from scratch, you're forced to come to terms with what you don't understand... Don't just write blog posts or do slides; build the code."
>
> — [y2doc.com 演讲笔记](https://y2doc.com/examples/1979541629396779008)

---

### 5. 自创术语与概念品牌

| 术语 | 首次出现 | 含义 | 来源 |
|------|----------|------|------|
| **Software 2.0** | 2017 年 11 月博客 | 神经网络权重作为新的程序代码 | [Software 2.0 博客](https://karpathy.medium.com/software-2-0-a64152b37c35) |
| **English is the hottest new programming language** | 2023 年 1 月推文 | 自然语言成为新的编程接口 | [barackface.net 存档](https://www.barackface.net/2023/03/andrej-karpathy-chatgpt.html?m=0) |
| **Software 3.0** | 2025 年 YC 演讲 | 用 prompt 编程 LLM | [Y Combinator 演讲稿](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| **Vibe coding** | 2025 年 2 月推文 | 用自然语言与 AI 协作、几乎不读代码 | [arXiv 引用原文](https://arxiv.org/pdf/2506.23253v1) |
| **Agentic engineering** | 2026 年 2 月 | 在严肃工程中协调 AI agent 并保持质量 | [karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) |
| **Jagged intelligence** | 2025 年 12 月年度回顾 | LLM 能力分布极不均匀 | [karpathy.bearblog.dev/year-in-review-2025](https://karpathy.bearblog.dev/year-in-review-2025/) |
| **Ghosts vs Animals** | 2025 年 10 月博客 | LLM 是「被召唤的幽灵」而非进化出的动物 | [karpathy.bearblog.dev/animals-vs-ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) |
| **Autonomy slider** | 2025 年 YC 演讲 | 产品应允许用户调节 AI 自主程度 | [Y Combinator 演讲稿](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| **LLM OS** | 2025 年 YC 演讲 | 把 LLM 比作新操作系统 | [Y Combinator 演讲稿](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| **Iron Man suit** | 2025 年 YC 演讲 | 当前 AI 应是增强人类的「钢铁侠战衣」而非完全自主机器人 | [Y Combinator 演讲稿](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| **Pretraining is our crappy evolution** | 2025 年 10 月博客 | 用预训练模拟生物进化作为冷启动 | [Animals vs Ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) |
| **Benchmaxxing** | 2025 年 12 月年度回顾 | 实验室针对 benchmark 做针对性强化学习 | [Year in Review 2025](https://karpathy.bearblog.dev/year-in-review-2025/) |

---

### 6. GitHub / 博客表达风格

#### 6.1 README 风格：极简、可 hack、教育导向

- **nanoGPT README**："The simplest, fastest repository for training/finetuning medium-sized GPTs. It is a rewrite of minGPT that prioritizes **teeth over education**."
- **micrograd README**："A tiny Autograd engine (with a bite! :)). Implements backpropagation... Both are tiny, with about 100 and 50 lines of code respectively."
- **llm.c README**："LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython."
- **microgpt 博客（2026-02-12）**："This file contains the full algorithmic content of what is needed... Everything else is just efficiency. I cannot simplify this any further."

共同特征：
- 强调 **代码行数少、依赖少、可读性强**；
- 用括号 emoji/感叹号增加亲和力（"with a bite! :)"）；
- 把「极简」本身作为一种审美和教学主张。

#### 6.2 博客风格：个人日记式 + 技术复盘

2025 年 4 月《Vibe coding MenuGen》是一篇典型 Karpathy 式博客：
- 以个人痛点开场（在餐厅看不懂菜单）；
- 记录从零 vibe coding 一个完整 web app 的全过程；
- 不掩饰失败："I thought of quitting the project around here"；
- 结尾给出抽象洞察："Building a modern app is a bit like assembling IKEA future... how are we supposed to be automating society by 2027 like this?"

他的博客不是「教程」，而是**带时间线的探索日志**，读者跟随他的试错过程获得直觉。

#### 6.3 对「建造」的执念

他在多个场合引用 Feynman：

> "I believe strongly in the Feynman quote, 'What I cannot create, I do not understand.' When you build something from scratch, you're forced to come to terms with what you don't understand."
>
> — [y2doc.com 演讲笔记](https://y2doc.com/examples/1979541629396779008)

这句话也解释了他为何坚持从零实现 GPT、神经网络、CUDA 训练器——**表达即建造，建造即理解**。

---

### 7. 最近 12 个月动态（防过时）

| 时间 | 事件/表达 | 来源 |
|------|-----------|------|
| 2025-02 | 提出 "vibe coding"，引发全球讨论 | [arXiv 引用原文](https://arxiv.org/pdf/2506.23253v1) |
| 2025-04 | 发布《Vibe coding MenuGen》博客，记录完整 vibe coding 经历 | [karpathy.bearblog.dev](https://karpathy.bearblog.dev/vibe-coding-menugen/) |
| 2025-06 | Y Combinator 演讲 "Software Is Changing (Again)"，系统阐述 Software 3.0 / LLM OS / autonomy slider | [Y Combinator](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) |
| 2025-10 | 博客《Animals vs Ghosts》，提出 "summoning ghosts"、"jagged intelligence" | [karpathy.bearblog.dev](https://karpathy.bearblog.dev/animals-vs-ghosts/) |
| 2025-12-20 | 发布《2025 LLM Year in Review》，总结 RLVR、Cursor、vibe coding、Nano banana 等 | [karpathy.bearblog.dev](https://karpathy.bearblog.dev/year-in-review-2025/) |
| 2025-12-27 | 推文表达 "as a programmer I've never felt so far behind"，引发行业震动 | [36kr](https://eu.36kr.com/en/p/3613263277868036)、[Rohan Paul](https://www.rohan-paul.com/p/andrej-karpathy-says-ive-never-felt) |
| 2026-02 | 提出 "agentic engineering" 作为 vibe coding 的严肃进化 | [karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) |
| 2026-05 | 宣布加入 Anthropic pretraining 团队 | [Reuters/Yahoo Finance](https://ca.finance.yahoo.com/news/openai-co-founder-former-tesla-161539836.html)、[VentureBeat](https://venturebeat.com/technology/andrej-karpathy-announces-hes-joining-anthropic) |

---

## 来源清单

| 来源 | 类型 | 可信度 | 关键内容 |
|------|------|--------|----------|
| [karpathy.ai/tweets.html](https://karpathy.ai/tweets.html) | 一手（本人整理的推文精选） | 高 | 2014–2022 年推文全集，展示幽默、科学类比、aphorism、学习哲学 |
| [karpathy.bearblog.dev/year-in-review-2025](https://karpathy.bearblog.dev/year-in-review-2025/) | 一手（本人博客） | 高 | 2025 LLM 年度回顾，包含 "ghosts vs animals"、"jagged intelligence"、"vibe coding"、"benchmaxxing" 等术语 |
| [karpathy.bearblog.dev/animals-vs-ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) | 一手（本人博客） | 高 | "summoning ghosts"、"pretraining is our crappy evolution" 等核心隐喻 |
| [karpathy.bearblog.dev/vibe-coding-menugen](https://karpathy.bearblog.dev/vibe-coding-menugen/) | 一手（本人博客） | 高 | vibe coding 第一手经验，含失败、自我调侃、工程洞察 |
| [karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) | 一手（本人博客/演讲整理） | 高 | "agentic engineering" 定义、与 vibe coding 区别、招聘应如何改变 |
| [Y Combinator: Software Is Changing (Again)](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) | 一手（演讲稿） | 高 | Software 3.0、LLM OS、autonomy slider、Iron Man suit 等框架 |
| [GitHub: karpathy/nanoGPT](https://github.com/karpathy/nanoGPT/blob/master/README.md) | 一手（本人仓库） | 高 | README 风格："teeth over education"、极简可 hack |
| [GitHub: karpathy/micrograd](https://github.com/karpathy/micrograd/blob/master/README.md) | 一手（本人仓库） | 高 | "with a bite! :)"、100 行代码等表达 |
| [GitHub: karpathy/llm.c](https://github.com/karpathy/llm.c/blob/master/README.md) | 一手（本人仓库） | 高 | "no need for 245MB of PyTorch"、对复杂度的敏感 |
| [Software 2.0 博客](https://karpathy.medium.com/software-2-0-a64152b37c35) | 一手（本人博客） | 高 | Software 2.0 原始定义 |
| [arXiv:2506.23253v1](https://arxiv.org/pdf/2506.23253v1) | 二手（学术论文引用其推文） | 中 | vibe coding 原始推文全文 |
| [arXiv:2604.00945](https://arxiv.org/pdf/2604.00945) | 二手（学术论文） | 中 | 确认 "vibe coding" 由 Karpathy 在 2025-02 提出 |
| [xunroll.com/thread/1976077806443569355](https://xunroll.com/thread/1976077806443569355) | 二手（X 线程第三方存档） | 中 | LLM 异常处理过度防御的推文及评论 |
| [barackface.net ChatGPT 合集](https://www.barackface.net/2023/03/andrej-karpathy-chatgpt.html?m=0) | 二手（推文合集） | 中 | "The hottest new programming language is English" 等 2023 年推文 |
| [Analytics India Mag: RLHF is NOT Really RL](https://analyticsindiamag.com/ai-features/rlhf-is-not-really-rl/) | 二手（行业媒体） | 中 | RLHF 之争、LeCun 支持、Karpathy 推文 |
| [36kr: "I've never felt so left behind"](https://eu.36kr.com/en/p/3613263277868036) | 二手（科技媒体） | 中 | 2025-12-27 推文内容与行业反响 |
| [Rohan Paul Newsletter](https://www.rohan-paul.com/p/andrej-karpathy-says-ive-never-felt) | 二手（Newsletter） | 中 | 同上，含截图与更多引用 |
| [Reuters/Yahoo Finance: Karpathy joins Anthropic](https://ca.finance.yahoo.com/news/openai-co-founder-former-tesla-161539836.html) | 二手（新闻） | 中 | 2026-05 加入 Anthropic 的声明与引语 |
| [VentureBeat: Karpathy joins Anthropic](https://venturebeat.com/technology/andrej-karpathy-announces-hes-joining-anthropic) | 二手（新闻） | 中 | 同上，含他对教育的承诺 |
| [y2doc.com 演讲笔记](https://y2doc.com/examples/1979541629396779008) | 二手（演讲笔记） | 中 | Feynman 引用、建造哲学 |
| [Klover.ai: Vibe Coding 争议](https://www.klover.ai/vibe-coding-karpathy-viral-term-ng-reality-check-klover-first-mover-advantage/) | 二手（行业媒体） | 中低 | vibe coding 传播、Andrew Ng 批评 |

---

## 信息缺口

- **X 原始推文无法直接访问**：由于 X.com 对未登录用户限制，大量 2023–2025 年推文依赖第三方存档或学术论文引用。部分具体推文 ID 与精确时间戳无法 100% 核实。
- **内部表达与公共表达的差异**：本报告完全基于公开社交媒体、博客、演讲，无法判断他在私人对话、团队会议中的表达习惯。
- **回应/反驳时的完整对话链**：例如 RLHF 与 vibe coding  debates 中，他的完整回复线程部分依赖二手总结，可能存在节选偏差。
- **非英文内容缺失**：调研聚焦英文社交媒体，未系统覆盖他在其他语言社区的表达（如有）。
- **视觉/视频表达**：YouTube 视频中的口头禅、停顿、肢体语言等「非文本表达 DNA」未被深入分析，建议由 02-conversations 维度补充。
