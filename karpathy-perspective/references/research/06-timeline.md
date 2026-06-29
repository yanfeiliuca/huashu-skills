# 06-timeline 调研：Andrej Karpathy 完整时间线

## 关键发现摘要

1. **职业路径呈现明显的“研究—工程—教育—再回研究”循环**：Karpathy 从斯坦福 multimodal 研究出发，先后进入 OpenAI（基础研究）、Tesla（大规模工程部署）、再回 OpenAI（GPT-4 / ChatGPT 应用优化），2024 年创办 Eureka Labs 转向 AI 教育，2026 年 5 月又加入 Anthropic 回归前沿预训练研究。这条轨迹反映了他对“从第一性原理理解机器”和“亲手实现”的持续追求。

2. **教育输出是其贯穿始终的副业，最终变成主业**：从 2019 年左右的 Rubik's cube 教程、斯坦福 CS231n（2015）、YouTube “Neural Networks: Zero to Hero” 系列（2022 起），到 Eureka Labs 的 LLM101n（2024）和 nanochat（2025），教育几乎从未离开他的时间线，并在 2024 年后成为全职事业。

3. **近期 12 个月（2025 年中—2026 年中）密集输出思想但角色剧烈转换**：他提出了 “vibe coding”（2025.02）、Software 3.0 / “Software Is Changing (Again)” 演讲（2025.06）、年度 “2025 LLM Year in Review”（2025.12）、Dwarkesh Podcast “AGI 仍需十年”（2025.10）、 nanochat 发布（2025.10），以及 2025 年末 “我从未像现在这样觉得跟不上程序员” 的反思帖；随后于 2026 年 5 月 19 日宣布加入 Anthropic 预训练团队。

4. **关键思想转折点与其职业节点高度重合**：2015 年 char-rnn 博客让他成为深度学习普及者；2017 年 “Software 2.0” 伴随他从 OpenAI 转向 Tesla Autopilot 的工程化验证；2023 年 “The hottest new programming language is English” 和 2025 年的 “vibe coding” / Software 3.0 与其离开 OpenAI、创办 Eureka Labs 后的教育/独立研究者身份一致。

5. **对 AGI 时间线持保守立场**：2025 年 10 月他在 Dwarkesh Podcast 中明确提出 AGI（按 OpenAI 定义）仍需约十年，原因是当前模型缺乏持续学习、可靠的多模态与计算机使用能力；这一立场与他 2026 年加入 Anthropic 做“用 Claude 加速 Claude 预训练”形成呼应。

---

## 详细调研

### 1. 出生、早期教育与移民背景

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 1986-10-23 | 出生于 Bratislava, Czechoslovakia（今 Slovakia） | 多个二手来源一致（Wikipedia、MIT Technology Review、TIME、FelloAI 等），他本人未公开强调此日期。可信度：高（二手交叉验证）。 |
| ~2001 | 15 岁随家人移居加拿大多伦多 | 多个来源一致（All American Speakers、Business Insider、FelloAI 等）。他本人未写回忆录式文章。可信度：高（二手交叉验证）。 |
| 2005–2009 | 多伦多大学本科，计算机科学与物理双主修，数学辅修 | 来自其个人网站 `karpathy.ai` 自我介绍，属一手来源。他提到在此期间首次接触深度学习，参加了 Geoffrey Hinton 的课程与 reading group。可信度：高（一手）。 |
| 2009–2011 | 不列颠哥伦比亚大学（UBC）硕士，师从 Michiel van de Panne | 来自其个人网站。研究方向为“ physically-simulated figures 的控制器学习”。可信度：高（一手）。 |

**备注**：关于童年与青少年时期的具体经历（家庭背景、移民原因、中学教育）目前未找到一手资料，二手报道高度同质化，基本复述同一简短生平。

### 2. 斯坦福 PhD 与早期研究（2011–2015）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2011–2015 | 斯坦福大学计算机科学 PhD，导师 Fei-Fei Li | 来自其个人网站及博士论文致谢页（Stanford Digital Repository），属一手来源。论文委员会还包括 Percy Liang、Christopher Manning。可信度：高（一手）。 |
| 2011 | Google Brain（早期）实习 | 个人网站提到在“baby Google Brain”做无监督视频学习。可信度：高（一手）。 |
| 2013 | Google Research 实习 | 个人网站提到做 YouTube 视频的大规模监督学习。可信度：高（一手）。 |
| 2015 | DeepMind 实习 | 个人网站提到在 deep reinforcement learning 团队与 Koray Kavukcuoglu、Vlad Mnih 工作。可信度：高（一手）。 |
| 2014 | 论文 *Deep Fragment Embeddings for Bidirectional Image Sentence Mapping*（NeurIPS） | 其 Google Scholar / 个人网站列出。可信度：高（一手）。 |
| 2015 | 论文 *Deep Visual-Semantic Alignments for Generating Image Descriptions*（CVPR Oral） | 与 Fei-Fei Li 合作，被广泛引用。可信度：高（一手）。 |
| 2016-08 | 博士论文 *Connecting Images and Natural Language* 正式提交 | Stanford Digital Repository 记录。论文致谢中详细感谢 Fei-Fei Li、Chris Manning、Percy Liang 等。可信度：高（一手）。 |

**思想转折**：在斯坦福期间，他处于计算机视觉与自然语言处理的交叉点，这为其后来从 CV 转向 LLM、从感知转向“可编程智能”埋下伏笔。

### 3. CS231n 与教育影响力的起点（2015–2017）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2015 | 设计并主讲斯坦福第一门深度学习课程 CS231n: Convolutional Neural Networks for Visual Recognition | 个人网站自述。2015 年选课人数 150，2016 年 330，2017 年 750。可信度：高（一手）。 |
| 2015 起 | 与 Justin Johnson 共同维护 CS231n | 个人网站及课程官网。可信度：高（一手）。 |
| ~2015 | 个人博客发布 *The Unreasonable Effectiveness of Recurrent Neural Networks* | 该文让 char-rnn 与“训练 RNN 生成莎士比亚文本”的 demo 广为人知。Karpathy 在 2015-05-21 发布于 `karpathy.github.io`。可信度：高（一手，原始博客地址多次被学术论文引用）。 |
| ~2014–2015 | 开发 ConvNetJS / char-rnn 等开源项目 | 个人网站列出 ConvNetJS、REINFORCEjs、GANs in JS 等“pet projects”。可信度：高（一手）。 |

### 4. OpenAI 第一期：创始成员（2015–2017）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2015-12 | 加入 OpenAI 成为创始成员（founding member）/ research scientist | 个人网站、TechCrunch、路透社、The Information 等多家媒体报道。可信度：高（一手 + 二手交叉）。 |
| 2015–2017 | 研究聚焦深度学习、计算机视觉、生成模型、强化学习 | 二手报道；他本人对个人网站该时期描述较简短。可信度：中。 |
| 2017-11 | 在 Medium 发布 *Software 2.0* | 提出“神经网络不是另一种分类器，而是全新的编程范式；数据集是源码，训练是编译”。原始 URL `karpathy.medium.com/software-2-0-a64152b37c35`，被后续学术论文多次引用。可信度：高（一手）。 |

### 5. Tesla：从研究到大规模工程部署（2017–2022）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2017-06 | 加入 Tesla，任 Director of AI / Autopilot Vision | 个人网站、TechCrunch、路透社、CNBC 等。可信度：高（一手 + 二手交叉）。 |
| 2017–2022 | 领导 Autopilot 计算机视觉团队，负责数据标注、神经网络训练、定制推理芯片部署 | 个人网站自述，提到团队目标是实现 Full Self-Driving（FSD）规模化。可信度：高（一手）。 |
| 2021-08 | 在 Tesla AI Day 做技术 deep dive，讲解 Autopilot 视觉栈 | Tesla 官方 YouTube 视频及大量媒体转录（如 Elon Musk Interviews、CleanTechnica）。他提出“我们实际上是在从头构建一个合成动物”。可信度：高（一手视频 + 二手转录）。 |
| 2021-06 | CVPR 2021 WAD keynote，提出“meat computer vs. silicon computer” | CleanTechnica、NotATeslaApp 等报道。可信度：中（二手）。 |
| 2022-03 | 宣布休假约四个月 | 马斯克在 Twitter 上确认，Karpathy 称将“rest & travel”。可信度：高（本人/马斯克一手推文，二手报道）。 |
| 2022-07-13 | 宣布离开 Tesla | 本人推文："It's been a great pleasure to help Tesla towards its goals over the last 5 years..."；马斯克回复致谢。TechCrunch、CNBC、Mashable、Reuters 等均报道。可信度：高（一手推文 + 二手报道）。 |
| 2022-10 | Lex Fridman Podcast 访谈 | 他表示离职原因是角色变得过于管理化，想做更多技术工作；同时称不排除未来回归 Tesla 做 Optimus / AGI。可信度：中（二手摘要，一手视频存在）。 |

**思想转折**：Tesla 时期是其“Software 2.0”思想的工业级验证场。他在多次公开演讲中把自动驾驶描述为“用数据引擎替代手写规则”，这段经历后来成为他反复谈论的“long-tail edge cases”与“demo 到可靠产品鸿沟”的来源。

### 6. 独立研究者与教育内容创作者（2022–2023）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2022-08 | 启动个人 YouTube 频道，发布“Neural Networks: Zero to Hero”系列首支长视频 | TeslaNorth、个人推特等报道。首支视频约 2 小时 25 分钟，讲解 micrograd。可信度：高（一手视频 + 二手报道）。 |
| 2023-01-24 | X 发帖称 “The hottest new programming language is English” | 被广泛引用为他关于“提示即编程”的早期公开表达。可信度：高（一手 X 帖，二手广泛引用）。 |
| 2023 上半年 | 持续发布 YouTube 教程，包括 “Let's build GPT: from scratch, in code, spelled out” | 视频仍在 YouTube，是其最具传播力的教育内容之一。可信度：高（一手）。 |

### 7. OpenAI 第二期：回归与再次离开（2023–2024）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2023-02-09 | 宣布回归 OpenAI | 本人推文："I am joining OpenAI (again :))"，称受 ChatGPT 影响启发。可信度：高（一手）。 |
| 2023–2024 | 组建小团队，做 midtraining 与 synthetic data generation，改进 GPT-4 for ChatGPT | 个人网站 `karpathy.ai` 自述。可信度：高（一手）。 |
| 2024-02-13 | 宣布再次离开 OpenAI | 本人推文："nothing happened... not a result of any particular event, issue or drama"，称将投入个人项目。TechCrunch、The Information 报道。可信度：高（一手 + 二手）。 |

### 8. Eureka Labs：AI 原生学校（2024–2026）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2024-06-21 | 在 Delaware 注册 Eureka Labs LLC（据 VentureBeat） | 二手报道。可信度：中。 |
| 2024-07-16 | 在 X 宣布创办 Eureka Labs，定位“AI native school” | 本人推文。首课 LLM101n 被描述为“the world's obviously best AI course”，指导学生从零训练自己的 Storyteller LLM。可信度：高（一手）。 |
| 2024-07 起 | LLM101n 在 GitHub 公开开发 | GitHub 仓库 `EurekaLabsAI/llm101n`。2024 年 6 月 25 日 readme 更新称“课程需要一段时间构建，没有具体时间表”。可信度：高（一手仓库）。 |
| 2024-08-01 | 据部分报道，LLM101n 仓库被 archive 为只读 | StartupHub.ai 等报道；若属实，意味着从公开课程开发转向产品化开发。可信度：低—中（未见本人直接说明）。 |
| 2024-09 | 入选 TIME 100 Most Influential People in AI 2024 | TIME 官方名单。可信度：高（二手官方）。 |
| 2025 年初 | 据报道完成约 2000 万美元种子轮融资，投资方包括 Conviction（Sarah Guo）、Sam Altman 等 | Nextomoro、StartupHub.ai 等报道。可信度：中（未见官方融资公告）。 |
| 2025-06 | 在 Y Combinator AI Startup School 演讲 *Software Is Changing (Again)*，系统阐述 Software 3.0 | YC 官方视频与 Latent Space 笔记。可信度：高（一手视频 + 二手笔记）。 |
| 2025-10 | 发布 nanochat：一个可在 4 小时、约 100 美元成本内训练的极简 ChatGPT 式 pipeline | GitHub `karpathy/nanochat`。可信度：高（一手仓库 + 二手报道）。 |
| 2025-12 | 发布 *2025 LLM Year in Review* | 发布于其博客 `karpathy.bearblog.dev/year-in-review-2025/`，中文科技媒体大量转载。核心论点包括 RLVR、Ghosts vs. Animals / Jagged Intelligence、Vibe Coding、Claude Code、Nano banana / LLM GUI 等。可信度：高（一手博客）。 |
| 2025-12-26 | X 发帖："I've never felt this much behind as a programmer" | 引发广泛讨论。多家媒体（Stackademic、Dev.to、Scale Factory 等）引用。可信度：高（一手 X 帖，二手报道）。 |

### 9. 加入 Anthropic：回归前沿预训练研究（2026 至今）

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2026-05-19 | 在 X 宣布加入 Anthropic | 本人推文："Personal update: I've joined Anthropic. I think the next few years at the frontier of LLMs will be especially formative... I remain deeply passionate about education and plan to resume my work on it in time." 可信度：高（一手）。 |
| 2026-05-19 | TechCrunch 等报道：他将在 Nick Joseph 领导下加入 pre-training 团队，组建新团队研究“用 Claude 加速预训练研究” | TechCrunch、Bloomberg、The Decoder、ExplainX 等。可信度：高（二手主流媒体交叉验证）。 |
| 2026-05 | 报道指出 Eureka Labs 处于“暂停 / 未关闭”状态 | TechCrunch："It’s not clear if... will continue with the startup"；Karpathy 本人称仍热爱教育、计划日后回归。可信度：中（他本人表态 + 媒体报道）。 |

**注意**：由于当前日期为 2026-06-26，该事件发生在约五周前，属于“最近 12 个月动态”中最重大的变化。所有关于他在 Anthropic 的具体项目细节目前均来自入职报道，尚无长期成果或职位稳定性的一手更新。

### 10. 其他值得记录的时间线节点

| 时间 | 事件 | 说明与来源 |
|------|------|------------|
| 2020 | 入选 MIT Technology Review Innovators Under 35 | MIT Technology Review 官方。可信度：高（二手官方）。 |
| 2026-02 | 据 Observer 报道，他与 Fei-Fei Li 共同投资 Simile（斯坦福衍生、AI 模拟人类行为） | Observer 报道 Simile 融资 1 亿美元，Karpathy 与 Fei-Fei Li 等人为投资人。可信度：中（他本人未公开确认投资细节）。 |

---

## 来源清单

| 来源 | 类型 | 可信度 | 关键内容 |
|------|------|--------|----------|
| https://karpathy.ai/ | 一手（个人官网/自我介绍） | 高 | 教育、工作经历、项目列表、CS231n 规模、实习经历 |
| https://purl.stanford.edu/wf528qt3314 | 一手（博士论文） | 高 | PhD 导师、委员会、致谢、论文题目 |
| http://karpathy.github.io/2015/05/21/rnn-effectiveness/ | 一手（博客） | 高 | *The Unreasonable Effectiveness of RNNs* 原文 |
| https://karpathy.medium.com/software-2-0-a64152b37c35 | 一手（博客） | 高 | *Software 2.0* 原文 |
| https://karpathy.bearblog.dev/year-in-review-2025/ | 一手（博客） | 高 | *2025 LLM Year in Review* |
| https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again | 一手（演讲视频） | 高 | YC AI Startup School 2025 演讲 “Software Is Changing (Again)” |
| https://twitter.com/karpathy / X 帖子 | 一手（社交媒体） | 高 | 入职/离职公告、vibe coding、程序员反思、加入 Anthropic 等 |
| https://github.com/karpathy / https://github.com/EurekaLabsAI | 一手（代码仓库） | 高 | micrograd、nanoGPT、llm101n、nanochat 等项目 |
| https://www.youtube.com/@AndrejKarpathy | 一手（视频） | 高 | Zero to Hero、Let's build GPT 等教育视频 |
| https://www.technologyreview.com/innovator/andrej-karpathy/ | 二手（官方媒体） | 高 | MIT Innovators Under 35 2020 |
| https://time.com/7012851/andrej-karpathy/ | 二手（官方媒体） | 高 | TIME 100 Most Influential People in AI 2024 |
| https://techcrunch.com/2024/02/13/andrej-karpathy-is-leaving-openai-again-but-he-says-there-was-no-drama/ | 二手（科技媒体） | 高 | 2024 年离开 OpenAI 的报道，含本人推文原文 |
| https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ | 二手（科技媒体） | 高 | 2026 年加入 Anthropic 报道，含本人推文原文 |
| https://www.reuters.com/technology/artificial-intelligence/former-openai-tesla-engineer-andrej-karpathy-starts-ai-education-platform-2024-07-16/ | 二手（通讯社） | 高 | Eureka Labs 创办报道 |
| https://www.cnbc.com/2022/07/13/tesla-ai-leader-andrej-karpathy-announces-hes-leaving-the-company.html | 二手（财经媒体） | 高 | 2022 年离开 Tesla |
| https://cleantechnica.com/2021/06/21/teslas-andrej-karpathy-gives-a-keynote-at-cvpo-2021-workshop-on-autonomous-driving/ | 二手（科技媒体） | 中 | CVPR 2021 演讲内容摘要 |
| https://elonmuskinterviews.wordpress.com/2021/08/31/tesla-ai-day-the-presentation-i/ | 二手（演讲转录） | 中 | Tesla AI Day 2021 转录，含 Karpathy 发言 |
| https://www.latent.space/p/s3 | 二手（会议笔记） | 中 | YC AI Startup School 2025 演讲笔记 |
| https://www.dwarkesh.com/p/andrej-karpathy | 二手（播客页面） | 中 | Dwarkesh Podcast 2025.10 访谈 |
| https://observer.com/2026/02/simile-100m-startup-backed-fei-fei-li-andrej-karpathy/ | 二手（商业媒体） | 中 | Simile 投资传闻 |
| https://www.nextomoro.com/eureka-labs/ | 二手（行业研究） | 中 | Eureka Labs 融资与状态 |
| Wikipedia / 各类传记页面 | 二手（综合） | 中—低 | 出生日期、教育背景、职业时间线（交叉验证用） |

---

## 信息缺口

1. **童年与家庭背景**：出生后的成长环境、父母职业、移民加拿大的具体原因与过程均无一手资料，二手报道内容同质化严重。

2. **2015 年前早期编程/创业经历**：除了个人网站列出的“pet projects”（Rubik's cube color extractor、Tetris AI 等），缺乏具体的时间、动机与影响评估。

3. **OpenAI 第一期具体贡献细节**：他作为 founding member 参与了哪些具体项目、论文或决策？公开资料多为概括性描述，未见详尽一手回顾。

4. **Tesla 内部决策与离职真实动因**：虽然他在 Lex Fridman Podcast 中提到“想做更多技术工作”，但关于 Autopilot 进度、FSD 争议、团队裁员与其离职之间的关联，外界多为推测。

5. **Eureka Labs 融资与运营状态**：投资金额、投资方名单、员工规模等多来自媒体报道，未见官方融资公告；LLM101n 仓库是否被 archive、课程是否已商业化，目前缺乏本人明确说明。

6. **Anthropic 入职后的具体研究方向与成果**：由于入职时间为 2026 年 5 月，目前仅知道“用 Claude 加速预训练研究”这一高层描述，具体项目、论文、团队规模均无公开信息。

7. **个人生活与非公开活动**：婚姻、子女、居住地、日常工作时间安排等未公开，不属于公开调研可覆盖范围。
