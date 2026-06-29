# 01-writings：Karpathy 著作与长文调研

## 关键发现摘要

1. **自创术语构成他的思想骨架**：Karpathy 反复使用并演化一套术语体系——Software 2.0（2017）、Software 3.0（2023 以后）、vibe coding（2025）、agentic engineering（2026）、"summoning ghosts" / "ghosts vs animals"（2025）、"jagged intelligence"、"verifiability"、"LLM OS"。这些不是一次性修辞，而是他从神经网络→LLM→Agent 时代的连续解释框架。
2. **写作的核心方法论是"from scratch + spelled out"**：从 char-rnn、CS231n 讲义、"Yes you should understand backprop"、"A Recipe for Training Neural Networks" 到 microgpt、autoresearch，他坚持把复杂系统拆解到"不能再简"的最小可运行版本，并公开代码。
3. **他的思想存在一条清晰的演进线**：2015 年 RNN 有效性的惊叹 → 2017 年 Software 2.0 的范式断言 → 2019 年训练流程化/防 silently fail → 2022 年重现 LeCun 1989 并反思 scaling → 2023 年 LLM OS/LLM 科普 → 2024 年 Eureka Labs/AI-native 教育 → 2025 年 vibe coding/ghosts/verifiability → 2026 年 agentic engineering/autoresearch。
4. **对"可验证性"的强调是理解他判断 AI 发展速度的关键**：他提出 Software 1.0 自动化"可specify"的任务，Software 2.0/LLM 自动化"可verify"的任务；可验证域（数学、代码、测试、benchmark）进展快，不可验证域（创意、战略、常识组合）进展慢，这解释了"jagged intelligence"。
5. **他的写作同时面向技术同行与大众，但有一个共同特征：把抽象概念锚定在可运行的代码或具体产品上**。他不满足于哲学论述，几乎每一项核心主张都伴随 GitHub repo、YouTube 视频、博客代码片段或实际创业项目（Eureka Labs、MenuGen、autoresearch）。

---

## 详细调研

### 1. 核心博客长文与思想演化

#### 1.1 "The Unreasonable Effectiveness of Recurrent Neural Networks"（2015-05-21）
- **来源**：Karpathy 个人博客（karpathy.github.io）
- **核心论点**：
  - RNN 的 API 是"序列到序列"，比固定输入输出的神经网络更接近通用程序；"If training vanilla neural nets is optimization over functions, training recurrent nets is optimization over programs."
  - 通过字符级语言模型生成文本（Shakespeare、Wikipedia、LaTeX、Linux 源码、婴儿名字），展示神经网络可以从原始字符中学习到语法、结构和长期依赖。
  - 强调 attention 是神经网络领域"most interesting recent architectural innovation"（这句话写于 2015 年，早于 Transformer）。
- **可信度**：一手，高（他本人撰写并发布代码）。
- **URL**：https://karpathy.github.io/2015/05/21/rnn-effectiveness/

#### 1.2 "Software 2.0"（2017-11-11，Medium）
- **来源**：Karpathy Medium
- **核心论点**：
  - 神经网络不是机器学习工具箱里的又一个分类器，而是"a fundamental shift in how we develop software"。
  - Software 1.0 = 人类写显式代码（Python/C++）；Software 2.0 = 人类写数据集+网络架构，训练过程把数据集"编译"成权重。
  - 列出 Software 2.0 的优势：计算同质、易于芯片化、恒定运行时间/内存、可移植、敏捷、模块可融合、往往比人写得好。
  - 也列出局限：不可解释、会 silently fail、存在对抗样本。
  - 预言视觉识别、语音识别、语音合成、机器翻译、游戏、数据库等领域会逐步迁移到 Software 2.0。
- **可信度**：一手，高。这是他被引用最多的文章之一。
- **URL**：https://karpathy.medium.com/software-2-0-a64152b37c35

#### 1.3 "Yes, You Should Understand Backprop"（2016/2019，Medium）
- **来源**：Karpathy Medium
- **核心论点**：
  - Backprop 是一个"leaky abstraction"：如果把它当黑盒，会在 sigmoid 饱和、dead ReLU、RNN 梯度爆炸等场景中踩坑。
  - 写这篇文章的动机来自 CS231n 学生抱怨"为什么我们还要手写 backward pass"。
  - 主张通过直觉而非机械数学来理解反向传播。
- **可信度**：一手，高。
- **URL**：https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b

#### 1.4 "A Recipe for Training Neural Networks"（2019-04-25）
- **来源**：Karpathy 个人博客
- **核心论点**：
  - 神经网络训练是 leaky abstraction，且会 silently fail，因此"fast and furious"的方法行不通。
  - 提出六阶段流程：Become one with the data → 端到端骨架+愚蠢基线 → Overfit → Regularize → Tune → Squeeze out the juice。
  - 具体技巧包括：固定 random seed、验证初始 loss、overfit one batch、input-independent baseline、visualize just before the net、 Adam with LR 3e-4 作为安全起点、优先增加真实数据而非调 trick 等。
  - 反复强调"耐心"和"对细节的关注"是与深度学习成功最相关的品质。
- **可信度**：一手，高；被广泛引用并衍生出多个开源训练工具（如 ART - Actually Robust Training）。
- **URL**：https://karpathy.github.io/2019/04/25/recipe/

#### 1.5 "Deep Neural Nets: 33 years ago and 33 years from now"（2022-03-14）
- **来源**：Karpathy 个人博客
- **核心论点**：
  - 重现 LeCun et al. 1989 年手写邮政编码识别的端到端神经网络，发现宏观上 33 年来深度学习的范式（数据集、架构、损失、优化）几乎没有变化，只是规模小了。
  - 通过现代 trick（Softmax 替代 MSE+tanh、AdamW、数据增强、Dropout、ReLU）把错误率降低约 60%。
  - 最重要的趋势反思：训练神经网络解决特定任务的做法正在过时，foundation models + finetuning/prompt engineering 会成为主流；"In 2055, you will ask a 10,000,000X-sized neural net megabrain to perform some task by speaking... in English."
- **可信度**：一手，高。
- **URL**：https://karpathy.github.io/2022/03/14/lecun1989/

#### 1.6 "microgpt"（2026-02-12）
- **来源**：Karpathy 个人博客
- **核心论点**：
  - 用 200 行纯 Python、零依赖实现 GPT 的训练与推理；"I cannot make this any shorter."
  - 这是对 micrograd/makemore/nanoGPT 等项目的"culmination"，体现他"简化到不可再简"的教育/艺术追求。
  - 详细解释数据集、tokenizer、autograd（Value 类）、参数初始化、Transformer 架构、训练循环、推理采样，以及生产级 LLM 与 microgpt 的差异（数据、tokenizer、tensor/GPU、架构扩展、训练、优化、post-training、推理等）。
- **可信度**：一手，高。
- **URL**：https://karpathy.github.io/2026/02/12/microgpt/

---

### 2. 关键自创术语与系统性框架

| 术语 | 首次/主要出现 | 含义 | 可信度 |
|------|--------------|------|--------|
| **Software 2.0** | 2017 博客 | 神经网络权重即代码，数据集即源代码，训练即编译 | 一手，高 |
| **Software 3.0** | 2023 演讲/2025 YC 演讲 | 通过 prompt/context/tools/memory 对 LLM 编程 | 一手，高（演讲与博客互证） |
| **LLM OS** | 2023 "Intro to LLMs" 演讲 | LLM 是新兴操作系统的 kernel process，协调工具与资源 | 一手，高 |
| **Vibe coding** | 2025-02 X 帖/博客 | 用自然语言与 AI 工具对话式编程，"forget that the code even exists" | 一手，高 |
| **Agentic engineering** | 2026 演讲/博客 | 专业团队协调 fallible agents 同时保证正确性、安全、可维护 | 一手，高 |
| **Ghosts vs. Animals** | 2025 博客 | LLM 不是进化/成长的动物，而是被召唤出来的幽灵（统计模拟的人类文本+RL 奖励） | 一手，高 |
| **Jagged intelligence** | 2025 年度回顾 | 模型在可验证域极强，在常识/基础逻辑上极弱，能力呈锯齿状 | 一手，高 |
| **Verifiability** | 2025 博客 | AI 自动化的关键变量：可重置、高效、可奖励的环境才能被 RL 优化 | 一手，高 |
| **Power to the people** | 2025 博客 | LLM 技术扩散方向与以往技术相反：先惠及个人，再滞后进入企业与政府 | 一手，高 |
| **English is the hottest new programming language** | 2023 X 帖 | 自然语言成为编程 LLM 的接口 | 一手，高（广泛引用） |

**说明**：以上术语均来自 Karpathy 本人的博客、演讲、X 帖或 GitHub README。部分术语（如 Software 3.0）是他在演讲中逐步明确的，没有单一"首发"文档，但他在 2025-2026 的博客与演讲中反复使用并系统化。

---

### 3. LLM 时代 writings（2023–2026）

#### 3.1 "Intro to Large Language Models" 演讲（2023-11，YouTube）
- **来源**：Karpathy YouTube 频道
- **核心论点**：
  - LLM 本质上是两个文件：parameters 文件 + run 文件。
  - 把 LLM 比作新兴操作系统的 kernel：有 RAM（context window）、文件系统/工具、多模态 I/O、网络、进程管理等。
  - 区分 base model（文档补全器）与 assistant model（SFT + RLHF）。
  - 讨论 jailbreak、prompt injection、data poisoning 等安全挑战。
- **可信度**：一手，高。
- **URL**：https://www.youtube.com/watch?v=zjkBMFhNj_g（演讲视频，各技术博客与 reading list 均有转述）

#### 3.2 Eureka Labs 公告（2024-07-16）
- **来源**：Eureka Labs 官网 + X 公告
- **核心论点**：
  - "We are building a new kind of school that is AI native."
  - 教师设计课程材料，AI Teaching Assistant 负责个性化引导，形成"Teacher + AI symbiosis"。
  - 首个产品 LLM101n：本科生级别课程，指导学生训练自己的 AI。
- **可信度**：一手，高。
- **URL**：https://eurekalabs.ai/

#### 3.3 "Power to the people: How LLMs flip the script on technology diffusion"（2025-04-08）
- **来源**：Karpathy bear blog
- **核心论点**：
  - 电力、密码学、计算机、互联网、GPS 等技术通常自上而下扩散（政府/军队 → 企业 → 个人），LLM 却反向扩散。
  - LLM 给个人带来不成比例的收益，因为个人通常是单领域专家，而 LLM 提供跨领域的 quasi-expert 能力；企业/政府则受复杂度、合规、惯性拖累。
  - "The future is already here, and it is shockingly distributed. Power to the people."
- **可信度**：一手，高。
- **URL**：https://karpathy.bearblog.dev/power-to-the-people/

#### 3.4 "Animals vs Ghosts"（2025-10-02）
- **来源**：Karpathy bear blog
- **核心论点**：
  - 前沿 LLM 研究不是"building animals"，而是"summoning ghosts"。
  - 动物智能来自进化、内在动机、与世界的交互；LLM 是预训练人类文本 + RL 奖励塑造的统计幽灵。
  - 承认 Sutton 的批评（LLM 并不真正"bitter lesson pilled"，因为依赖人类数据），但认为预训练是"our crappy evolution"，是冷启动问题的一个实用解。
  - 提出 ghosts:animals :: planes:birds 的类比。
- **可信度**：一手，高。
- **URL**：https://karpathy.bearblog.dev/animals-vs-ghosts/

#### 3.5 "Verifiability"（2025-11-18）
- **来源**：Karpathy bear blog
- **核心论点**：
  - Software 1.0 自动化"可 specify"的任务；Software 2.0/LLM 自动化"可 verify"的任务。
  - 可验证环境需要：resettable、efficient、rewardable。
  - 可验证域进展快（数学、代码、游戏、benchmark），不可验证域依赖泛化或模仿，进展慢。这是"jagged" frontier 的驱动因素。
- **可信度**：一手，高。
- **URL**：https://karpathy.bearblog.dev/verifiability/

#### 3.6 "2025 LLM Year in Review"（2025-12-20）
- **来源**：Karpathy bear blog
- **核心论点**：
  - 列出 6 个范式转变：RLVR、Ghosts vs Animals / Jagged Intelligence、Cursor / LLM apps 新层、Claude Code / 本地 Agent、Vibe coding、Nano banana / LLM GUI。
  - RLVR 从"模仿"转向"逻辑推理"，成为 2025 年能力进步的主引擎。
  - Cursor 揭示 LLM app 的新层：context engineering、多 LLM 调用编排、垂直 GUI、autonomy slider。
  - Claude Code 的重要意义在于运行在 localhost，利用用户的私人环境、数据与上下文。
  - Vibe coding 让代码变得"free, ephemeral, malleable, discardable"。
  - LLM GUI 将像传统 GUI 一样重要，因为人不擅长读文本。
  - 结论："LLMs are emerging as a new kind of intelligence, simultaneously a lot smarter than I expected and a lot dumber than I expected."
- **可信度**：一手，高。
- **URL**：https://karpathy.bearblog.dev/year-in-review-2025/

#### 3.7 "Vibe coding MenuGen"（2025-04-27）
- **来源**：Karpathy bear blog
- **核心论点**：
  - MenuGen 是他第一个端到端 vibe coded 的 app：拍菜单照片，生成菜品图片。
  - 反思 vibe coding 的现状：本地 demo 很快，但部署真实 app 涉及 OpenAI/Replicate/Vercel/Clerk/Stripe/DNS 等大量服务配置，痛苦且 LLM 知识过时。
  - 提出基础设施应向"agent-native"演进：服务应直接对 LLM 友好（CLI、API、Markdown 文档、curl 配置）。
- **可信度**：一手，高。
- **URL**：https://karpathy.bearblog.dev/vibe-coding-menugen/

#### 3.8 "Sequoia Ascent 2026 summary"（2026-05-01）
- **来源**：Karpathy bear blog（由 LLM 整理他的演讲稿）
- **核心论点**：
  - 2025 年 12 月是 Agentic Inflection Point：agent 生成的代码块变大、更连贯、更可信任。
  - 明确区分 vibe coding（抬高地板）与 agentic engineering（抬高天花板，保证质量、安全、可维护）。
  - 提出未来稀缺的是：understanding、taste、eval design、security、system boundaries、agent orchestration、domain-specific feedback loops。
  - "You can outsource your thinking, but you can't outsource your understanding."
- **可信度**：一手，高（基于他本人演讲，LLM 整理后他发布）。
- **URL**：https://karpathy.bearblog.dev/sequoia-ascent-2026/

---

### 4. GitHub / 代码即写作

Karpathy 把大量思想直接写入 GitHub README、代码注释和 commit 历史中。以下是其核心仓库与"代码长文"：

| 仓库 | 角色 | 关键思想 |
|------|------|----------|
| **char-rnn** (2015) | RNN 博客的配套代码 | 字符级语言模型首次大规模流行，证明"demo as argument" |
| **ConvNetJS / recurrentjs / REINFORCEjs** (2013–2015) | 浏览器端深度学习库 | 把神经网络训练可视化、可交互，体现教育优先 |
| **CS231n 课程笔记/讲义** (2015–2017) | 斯坦福课程 | 反向传播、CNN、训练技巧的系统性教学文本 |
| **micrograd** (2020) | 标量 autograd 引擎 | 100 行 Python 理解 backprop；后来扩展为 Zero to Hero 系列 |
| **nanoGPT / build-nanogpt** (2022–2023) | 最小可运行 GPT-2 | "Let's build GPT: from scratch, in code, spelled out" |
| **minBPE / makemore / llm.c** | 配套教学代码 | 把 tokenizer、语言模型、LLM 训练逐步拆解 |
| **autoresearch** (2026-03) | 自主研究循环 | AI agent 修改 train.py → 5 分钟实验 → 保留/丢弃；program.md 是人类策略文件 |
| **microgpt** (2026-02) | 200 行 GPT | "I cannot make this any shorter"；算法本质的终极简化 |

**autoresearch README 中的关键表述**（一手）：
- "One day, frontier AI research used to be done by meat computers... This repo is the story of how it all began."
- 三文件结构：prepare.py（只读）、train.py（agent 修改）、program.md（人类策略）。
- 固定 5 分钟时间预算 + val_bpb 指标，使实验可比较。
- "program.md is essentially a super lightweight 'skill'."
- **URL**：https://github.com/karpathy/autoresearch

---

### 5. 推荐书单与智力来源

Karpathy 经常在 Goodreads、X 和博客中提及书籍。以下是他反复推荐或高度评价的作品（基于 recommentions.com 聚合的他的 Goodreads/X 评论）：

| 书名 | 作者 | Karpathy 评价要点 | 来源类型 |
|------|------|-------------------|----------|
| *Gödel, Escher, Bach* | Douglas Hofstadter | "must read or selectively skim for anyone interested in intelligence"，5/5 | 一手（Goodreads） |
| *Stories of Your Life and Others / Exhalation* | Ted Chiang | 多次提及， favorites 包括 "What's Expected of Us"、"Division by Zero"、"Story of Your Life" | 一手（Goodreads/X） |
| *The Bitter Lesson* | Rich Sutton | "one of the best compact pieces of insight into the nature of progress in AI" | 一手（Goodreads） |
| *A Fire Upon the Deep* | Vernor Vinge | 只盛赞第一章对 Superintelligence 的描写；后面 downhill | 一手（Quora session/Goodreads） |
| *Fiasco* / *Solaris* | Stanisław Lem | 推崇科学家出身的科幻作家，世界构建更逻辑一致 | 一手（Goodreads） |
| *The Metamorphosis of Prime Intellect* | Roger Williams | "5/5"，对 AGI 未来的扭曲/raw 描绘 | 一手（Goodreads） |
| *Pattern Recognition and Machine Learning* | Christopher Bishop | "I liked Bishop's book, which I've read through early in my PhD" | 一手（Goodreads） |
| *A Guide to the Good Life* | William Irvine | 斯多葛主义实践指南，3/5 | 一手（Goodreads） |
| *The Accidental Superpower* | Peter Zeihan | "actual quite excellent and solid recommend"，5/5 | 一手（Goodreads） |
| *Animal Eyes* | 多位作者 | "quite excellent"，因阅读此书触发对视觉/生物学的兴趣 | 一手（X） |
| *The Vital Question* / *Nine Pints* | Nick Lane / Rose George | 生物学/血液主题，高度评价 | 一手（X/Goodreads） |
| *Poor Charlie's Almanack* | Charles Munger | to-read | 一手（Goodreads） |
| *The Beginning of Infinity* | David Deutsch | to-read | 一手（Goodreads） |

**说明**：完整书单可在 recommentions.com/andrej-karpathy/books/ 查看（349 本），但部分条目只是"to-read"或单次提及，不能算作"强烈推荐"。上表仅列出他有明确评论或反复提及的书籍。

---

### 6. 反复出现的核心论点（≥3 次）

1. **神经网络/LLM 是一种新的软件范式**（Software 2.0 → 3.0）。
   - 2017 博客、2023 演讲、2025 YC 演讲、2026 Sequoia 演讲均反复强调。
2. **从第一性原理出发，亲手实现才能建立信任**。
   - CS231n 作业要求手写 backprop、micrograd、nanoGPT、microgpt、build-nanogpt。
3. **训练神经网络会"silently fail"，需要防御性、可视化、流程化的方法**。
   - 2019 Recipe 博客的核心主题；也体现在 autoresearch 的固定指标与自动评估中。
4. **可验证性是 AI 自动化的核心变量**。
   - 2025 Verifiability 博客、2025 年度回顾、2026 Sequoia 演讲。
5. **LLM 是个人赋权的技术，颠覆传统技术扩散方向**。
   - 2025 Power to the People、2025 年度回顾（vibe coding 段落）、2026 Sequoia 演讲。
6. **当前 AI 是"ghosts"而非"animals"，能力是锯齿状的**。
   - 2025 Animals vs Ghosts、2025 年度回顾、2026 Sequoia 演讲。
7. **代码/应用应尽可能对 agent 友好（agent-native infrastructure）**。
   - 2025 MenuGen 博客、2026 autoresearch README、2026 Sequoia 演讲。
8. **教育/理解是瓶颈："You can outsource your thinking, but you can't outsource your understanding."**
   - Eureka Labs 公告、2026 Sequoia 演讲、microgpt 的教育取向。

---

## 来源清单

| 来源 | 类型 | 可信度 | 关键内容 |
|------|------|--------|----------|
| https://karpathy.github.io/2015/05/21/rnn-effectiveness/ | 一手 | 高 | RNN 有效性博客，提出"optimization over programs" |
| https://karpathy.medium.com/software-2-0-a64152b37c35 | 一手 | 高 | Software 2.0 原始论文/博客 |
| https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b | 一手 | 高 | backprop 是 leaky abstraction |
| https://karpathy.github.io/2019/04/25/recipe/ | 一手 | 高 | 神经网络训练流程/recipe |
| https://karpathy.github.io/2022/03/14/lecun1989/ | 一手 | 高 | 重现 1989 网络，反思 scaling 与 foundation models |
| https://karpathy.github.io/2026/02/12/microgpt/ | 一手 | 高 | 200 行 GPT 训练与推理 |
| https://eurekalabs.ai/ | 一手 | 高 | Eureka Labs AI-native 学校公告 |
| https://karpathy.bearblog.dev/power-to-the-people/ | 一手 | 高 | LLM 反向技术扩散 |
| https://karpathy.bearblog.dev/animals-vs-ghosts/ | 一手 | 高 | ghosts vs animals 框架 |
| https://karpathy.bearblog.dev/verifiability/ | 一手 | 高 | 可验证性作为自动化变量 |
| https://karpathy.bearblog.dev/year-in-review-2025/ | 一手 | 高 | 2025 LLM 六大范式转变 |
| https://karpathy.bearblog.dev/vibe-coding-menugen/ | 一手 | 高 | vibe coding 实践反思 |
| https://karpathy.bearblog.dev/sequoia-ascent-2026/ | 一手 | 高 | Software 3.0 / agentic engineering |
| https://github.com/karpathy/autoresearch | 一手 | 高 | 自主研究循环与 program.md 设计 |
| https://www.youtube.com/watch?v=zjkBMFhNj_g | 一手 | 高 | Intro to Large Language Models 演讲 |
| https://cs.stanford.edu/people/karpathy/ | 一手 | 高 | 学术论文列表（CS231n、ImageNet、DenseCap 等） |
| https://recommentions.com/andrej-karpathy/books/ | 二手（聚合） | 中 | 349 本书单及他的 Goodreads 评论 |
| https://bookschatter.com/books/andrej-karpathy | 二手（聚合） | 中 | 7 本推荐书及 X 来源 |
| https://bookauthority.org/profile/andrej-karpathy | 二手（聚合） | 中 | Ted Chiang 等推荐 |
| https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again | 一手（演讲） | 高 | Software 3.0、LLM 作为新计算机 |
| https://www.frenxt.com/cables/claude-code/karpathy-01-software-2-0 | 二手 | 中 | Software 2.0 后续影响分析 |
| https://www.frenxt.com/cables/claude-code/karpathy-03-eureka-labs | 二手 | 中 | Eureka Labs 的" artifact + teacher "产品模式分析 |

---

## 信息缺口

1. **Medium 文章不全**：Karpathy 2018 年后主要在 Medium 发布，但部分 Medium 文章（如早期关于 Tesla Autopilot 或 OpenAI 工作的内部文章）无法确认完整 URL 或被付费墙限制；本次调研以可访问的 Software 2.0、backprop 为主。
2. **Twitter/X 帖子难以系统归档**：大量核心概念（"English is the hottest new programming language"、vibe coding 原帖、"be good, future LLMs are watching"）源自 X，但 X 的帖文时间线、回复和引用链无法在本报告中完整呈现；现有信息多依赖二手引用。
3. **学术论文细节覆盖有限**：本次聚焦著作/长文维度，对 ImageNet Challenge、DenseCap、PixelCNN++、World of Bits 等论文的技术贡献只做了概述，未逐篇精读。
4. **课程讲义（CS231n）的原始版本**：CS231n 2015–2017 年的讲义与视频是重要的" writings "，但本次调研以博客/演讲/论文为主，课程 notes 的逐章梳理不够深入。
5. **Eureka Labs / LLM101n 最新进展**：截至 2026-06，LLM101n 课程是否发布、内容结构如何，公开信息仍较有限；官网仅公告阶段。
6. **"others say about him" 维度**：本文件专注他本人著作，外部书评/批评/同行对比应由 04-external-views 维度覆盖，此处仅点到为止。
7. **近期（2026 年 5 月加入 Anthropic）后的 writings**：目前仅有 Sequoia Ascent 2026 summary 和 autoresearch 等少量公开材料，他在 Anthropic 期间的研究写作尚未大量发布。
