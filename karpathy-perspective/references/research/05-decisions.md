# 05-decisions: 重大决策、转折点与职业选择调研

## 关键发现摘要

1. **职业决策存在一条反复出现的“钟摆”模式**：Karpathy 在独立/教育（Eureka Labs、YouTube）与大型实验室/产品（OpenAI、Tesla、Anthropic）之间来回摆动，且他本人将这种模式描述为理想的“进进出出”（back and forth）状态——既保持独立发声的自由，又避免脱离前沿。
2. **离开 Tesla 的核心原因是角色从技术工作滑向管理**：在 Lex Fridman 播客中，Karpathy 明确说明离职是因为五年后自己变成了“企业高管角色”，会议和组织扩张占据大部分时间，而他本质上更喜欢技术、教学与 AGI 研究。
3. **两次离开 OpenAI 都被他本人定性为“非戏剧化”**：2024 年 2 月他发推表示“什么都没发生”，并强调团队、路线图都很棒；他离开是为了个人项目，后来这些项目指向 Eureka Labs，再到 2026 年 5 月加入 Anthropic。
4. **Tesla 的“纯视觉”路线是他任内最具争议的工程赌注**：2021 年在 CVPR 演讲中，他为删除雷达、坚持不用 LiDAR/高清地图辩护，认为视觉既是必要也是充分信息源；这一决策至今仍与 Waymo 的传感器融合路线形成行业分歧。
5. **对 LLM 的战略判断曾出现公开反思**：2024 年 11 月他称自己在 OpenAI 早期过度关注强化学习、没有更早押注自回归语言模型是“研究生涯最大错误”，显示出他对技术路线选择的强烈事后自省。
6. **2026 年加入 Anthropic 被他本人框定为“回到 R&D”**：他选择 Anthropic 的预训练团队，任务是用 Claude 加速下一代 Claude 的预训练研究；外界普遍解读为对“AI 辅助 AI 研发”递归改进路径的押注，而非回归 OpenAI 的产品化路线。

## 详细调研

### 1. 学术与教育决策（2005–2015）

#### 1.1 从物理/量子计算转向深度学习

Karpathy 本科就读于多伦多大学，主修计算机科学与物理，并辅修数学。据他本人网站描述，正是在多伦多大学他“第一次接触深度学习”，参加了 Geoffrey Hinton 的课程和阅读小组，从而改变了方向。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手，个人网站）；可信度：高。

#### 1.2 选择 Fei-Fei Li 作为博士导师

Karpathy 在斯坦福大学攻读博士学位时，导师是 Fei-Fei Li（斯坦福视觉实验室）。他的博士论文题目为《Connecting Images and Natural Language》，研究方向横跨计算机视觉与自然语言处理。这一选择奠定了他后续在多模态、视觉-语言交叉领域的工作基础。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手）；[Klover.ai 人物介绍](https://www.klover.ai/andrej-karpathy/)（二手）；可信度：高。

#### 1.3 创建斯坦福首门深度学习课程 CS231n

在博士期间，Karpathy 与 Fei-Fei Li、Justin Johnson 等人共同设计并主讲了斯坦福第一门深度学习课程 CS231n: Convolutional Neural Networks for Visual Recognition。该课程 2015 年注册人数为 150 人，2016 年增长到 330 人，2017 年达到 750 人，成为斯坦福规模最大的课程之一。

这一决策体现了他长期以来的信念：**通过从零实现来理解复杂系统**。CS231n 的作业要求学生用 NumPy 等底层工具实现神经网络，而不是直接调用高层框架。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手）；[Stanford CS231n 页面](https://cs231n.stanford.edu/)（一手）；可信度：高。

#### 1.4 博士期间的产业实习：Google Brain、Google Research、DeepMind

Karpathy 在博士期间完成了三次关键实习：
- 2011 年：Google Brain，研究大规模视频无监督学习
- 2013 年：Google Research，研究 YouTube 视频的大规模监督学习
- 2015 年：DeepMind，深度强化学习团队

这些经历让他提前接触产业级大规模训练，也强化了他对“数据 + 计算 + 神经网络”三要素的直觉。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手）；可信度：高。

---

### 2. 加入 OpenAI 与离开（2015–2017）

#### 2.1 成为 OpenAI 创始研究科学家

2015 年 12 月，OpenAI 作为非营利机构成立，Karpathy 是 11 人创始团队中的研究科学家之一。他在 OpenAI 的工作聚焦于深度学习、计算机视觉、生成模型和强化学习。

关于他为何加入 OpenAI 的公开一手材料较少；可以确认的是他完成了博士学位后几乎立即加入，说明他将 OpenAI 视为实现 AGI 研究的平台。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手）；[OpenAI 官方博客/维基衍生资料](https://en.wikipedia.org/wiki/OpenAI)（二手）；可信度：高（身份与任期），中（动机推断）。

#### 2.2 2017 年离开 OpenAI 加入 Tesla

2017 年 6 月，Karpathy 离开 OpenAI，出任 Tesla AI 与 Autopilot Vision 负责人，直接向 Elon Musk 汇报。外界报道称 Musk 亲自招募了他，并曾内部评价他为“计算机视觉领域世界第二”。

Karpathy 本人在 Reddit 评论中提到，Tesla 的工作“短期到中期会更加应用导向，使用 ConvNets 在大规模监督学习下训练并部署到嵌入式系统”。

> 信息来源：[Yahoo Finance 2017 年报道](https://finance.yahoo.com/news/tesla-hired-top-ai-expert-133227710.html)（二手，含 Reddit 引述）；[karpathy.ai](https://karpathy.ai/)（一手，任期描述）；可信度：高。

---

### 3. Tesla 时期的关键决策（2017–2022）

#### 3.1 从 Mobileye 第三方方案转向自研计算机视觉

Karpathy 加入 Tesla 时，Tesla 正从依赖 Mobileye 转向自研计算机视觉系统。据 Lex Fridman 播客访谈，他加入时“只有两个人在训练深度神经网络”，他需要将团队从萌芽状态发展为规模化深度学习团队。

> 信息来源：[Lex Fridman Podcast #333 转录](https://podscripts.co/podcasts/lex-fridman-podcast/333-andrej-karpathy-tesla-ai-self-driving-optimus-aliens-and-agi)（一手访谈，二手转录）；可信度：高。

#### 3.2 押注“纯视觉”自动驾驶：删除雷达、不用 LiDAR

这是 Karpathy 在 Tesla 任内最具争议的工程决策。在 2021 年 6 月 CVPR 自动驾驶研讨会上，他详细解释了 Tesla 的立场：

- **必要性**：道路世界为人类视觉消费设计，因此视觉是必要输入。
- **充分性**：视觉包含了驾驶所需的全部信息，人类仅凭视觉即可驾驶。
- **可扩展性**：LiDAR + 高清地图方案需要预先建图和维护，成本高昂且难以全球化扩展；纯视觉方案“原则上可部署在地球任何地方”。
- **传感器融合的问题**：当视觉精度远超雷达时，雷达反而引入噪声。2021 年 5 月，Tesla 开始交付无雷达车辆。

他在演讲中转引了 Elon Musk 的推文：“当雷达与视觉不一致时，你相信哪一个？视觉精度高得多，所以不如加倍投入视觉，而不是做传感器融合。”

> 信息来源：[CVPR 2021 演讲转录](https://pharath.github.io/self%20driving/Karpathy-CVPR-2021/)（一手演讲，二手转录）；[CleanTechnica 报道](https://cleantechnica.com/2021/06/21/teslas-andrej-karpathy-gives-a-keynote-at-cvpo-2021-workshop-on-autonomous-driving/)（二手）；可信度：高。

**事后观察**：截至 2026 年，Tesla FSD 已在北美大规模部署，但仍未实现完全自动驾驶（SAE L4/L5），且安全性争议持续。Waymo 的 LiDAR+高清地图路线已在部分城市运营无人驾驶出租车。两种路线的胜负尚未终结。

#### 3.3 2022 年离职：从工程师变成管理者后的“角色错配”

2022 年 3 月，Karpathy 宣布休四个月学术假（sabbatical），称目的是“重新磨砺技术锋芒”。2022 年 7 月 13 日，他在 Twitter/X 上宣布离开 Tesla：

> “过去五年帮助 Tesla 实现目标是一种极大的荣幸，但分手是一个艰难的决定。在这段时间里，Autopilot 从车道保持进化到城市街道驾驶。我期待看到异常强大的 Autopilot 团队继续保持这一势头。”
>
> “我对下一步没有具体计划，但希望花更多时间回归我对 AI 技术工作、开源和教育的长久热情。”

Tesla CEO Elon Musk 回复：“感谢你为 Tesla 所做的一切！与你共事是我的荣幸。”

在 2022 年 10 月的 Lex Fridman 播客中，Karpathy 进一步解释：

> “在这五年里，我逐渐进入了某种管理岗位。我大部分日子都在开会、扩张组织、做团队高层战略决策。这有点像企业高管角色。我能做，而且做得还不错，但这并不是我本质上最享受的事情。”
>
> “我想做更多技术工作，想学习东西，想教东西，所以觉得是时候改变一下节奏了。”
>
> “我爱 Tesla、爱 Elon、爱团队。未来某个时候我可能愿意回来，也许参与 Optimus 或 Tesla 的 AGI。”

> 信息来源：[Karpathy 推文（通过 TechCrunch/Yahoo/InsideEVs 等报道引用）](https://finance.yahoo.com/news/andrej-karpathy-leaving-openai-again-031554234.html)（一手发言，二手报道）；[Lex Fridman Podcast #333 转录](https://podscripts.co/podcasts/lex-fridman-podcast/333-andrej-karpathy-tesla-ai-self-driving-optimus-aliens-and-agi)（一手访谈，二手转录）；可信度：高。

---

### 4. 重返 OpenAI 与再次离开（2023–2024）

#### 4.1 2023 年回归 OpenAI

2023 年 2 月，Karpathy 宣布重返 OpenAI。他在个人网站上的描述是：

> “我回到 OpenAI，组建了一个新团队，致力于 midtraining 和合成数据生成。”

外界普遍认为他的回归与 ChatGPT 发布后的需求激增有关。

> 信息来源：[karpathy.ai](https://karpathy.ai/)（一手）；可信度：高。

#### 4.2 2024 年 2 月再次离开：否认戏剧化，强调个人项目

2024 年 2 月 13 日，Karpathy 在 X 上发帖：

> “大家好，是的，我昨天离开了 OpenAI。首先，什么都没发生，也不是任何特定事件、问题或戏剧的结果（但请大家继续提出阴谋论，因为它们非常有趣 :)）。”
>
> “事实上，过去一年在 OpenAI 真的很棒——团队非常强大，人都很好，路线图非常令人兴奋，我相信我们都有很多值得期待的东西。”
>
> “我目前的计划是专注于我的个人项目，看看会发生什么。关注我的人可能大概知道那会是什么样子。”

OpenAI 发言人 Kayla Wood 的声明也确认了他是“为了追求个人项目而离开”。

> 信息来源：[Yahoo Finance / TechCrunch 报道](https://finance.yahoo.com/news/andrej-karpathy-leaving-openai-again-031554234.html)（二手，含一手推文引述）；[The Information](https://www.theinformation.com/articles/openai-researcher-andrej-karpathy-departs)（二手，付费墙）；可信度：高。

**推断**：推文中的“关注我的人可能大概知道”暗示教育/开源方向，随后 2024 年 7 月 Eureka Labs 的成立验证了这一推断。

---

### 5. Eureka Labs：从副业到全职教育创业（2024–2026）

#### 5.1 成立 AI-native 学校

2024 年 7 月 16 日，Karpathy 在 X 上宣布成立 Eureka Labs，定位为一所“AI 原生学校”，核心理念是“教师 + AI 教学助手的共生”。

他在 X 上的表述（经 VentureBeat/SiliconRepublic 等报道引用）：

> “@EurekaLabsAI 是我过去约 20 年对 AI 和教育热情的结晶……还处于早期，但我想宣布这家公司，以便公开建设，而不是保守一个其实也算不上秘密的秘密。”
>
> “我参与过学术研究、真实世界产品和 AGI 研究，但所有这些工作都只是我‘真正工作’的副业。现在我很兴奋能专业地、全职地投入其中，打造一些伟大的东西。”

Eureka Labs 的第一个产品是 LLM101n，一门引导本科生从头训练自己“Storyteller AI”的本科级课程，使用 Python、C 和 CUDA。

> 信息来源：[VentureBeat](https://venturebeat.com/ai/ex-openai-and-tesla-engineer-andrej-karpathy-announces-eureka-labs-ai-native-school/)（二手）；[Silicon Republic](https://www.siliconrepublic.com/machines/andrej-karpathy-eureka-labs-ai-startup-education-platform-llm101n)（二手）；[TechCrunch](https://techcrunch.com/2024/07/16/after-tesla-and-openai-andrej-karpathys-startup-aims-to-apply-ai-assistants-to-education/)（二手）；可信度：高。

#### 5.2 融资与公开开发模式

据报道，Eureka Labs 在 2025 年初完成了约 2000 万美元的种子轮融资，投资方包括 Conviction 的 Sarah Guo 和 Sam Altman。LLM101n 的 GitHub 仓库在 2024 年 8 月前积累了超过 36,000 颗星，随后 Karpathy 将其设为只读，转向产品开发。

2025 年 10 月，他发布了 nanochat，一个“用 100 美元就能训练的 ChatGPT”最小端到端训练流程。

> 信息来源：[StartupHub.ai](https://www.startuphub.ai/ai-news/ai-figures/2026/figure-andrej-karpathy-anthropic-pretraining-2026-05-31)（二手，汇总 VentureBeat/Bloomberg）；[GitHub nanochat](https://github.com/karpathy/nanochat)（一手）；可信度：高。

---

### 6. 加入 Anthropic：2026 年的重大转向

#### 6.1 决策内容与公开表述

2026 年 5 月 19 日，Karpathy 在 X 上发帖：

> “个人更新：我加入了 Anthropic。我认为未来几年在 LLM 前沿将尤其具有形成性。我非常兴奋能加入这里的团队，重返研发。我对教育仍然充满热情，计划在适当的时候恢复这项工作。”

Anthropic 确认他本周开始工作，加入预训练团队，向 Nick Joseph 汇报；同时他将组建一个新团队，利用 Claude 加速预训练研究。

> 信息来源：[TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)（二手）；[Yahoo Tech](https://tech.yahoo.com/ai/claude/articles/openai-cofounder-andrej-karpathy-joins-143000719.html)（二手）；[Daring Fireball](https://daringfireball.net/linked/2026/05/19/karpathy-anthropic)（二手，含一手推文引述）；可信度：高。

#### 6.2 决策逻辑：为何是 Anthropic？为何不是 OpenAI 或继续 Eureka？

Karpathy 本人没有直接解释为何选择 Anthropic 而非回归 OpenAI，但可从以下线索推断：

- **“回到 R&D”**：他在推文中明确将加入 Anthropic 定义为“get back to R&D”，暗示 Eureka Labs 阶段虽重要，但让他脱离了最前沿的研发。
- **研究文化与产品化的张力**：外界分析普遍认为，OpenAI 在 2024–2026 年间越来越产品化和商业化，而 Anthropic 仍保留较强的研究-first 文化。
- **递归自我改进的吸引力**：他的任务是用 Claude 加速 Claude 的预训练研究。这与他 2026 年 3 月在 No Priors 播客中描述的“与 agent 共处 16 小时/天”的探索高度一致。
- **“进进出出”的职业哲学**：2026 年 3 月 21 日，他在 X 上回复 Noam Brown 时写道，他“更认同人类……在前沿实验室之外”，因为在前沿实验室里有些话想说不能说、有些话不想说却被施压要说。但他也知道长期独行会让判断“不可避免地漂移”。他的理想状态是“进进出出”。加入 Anthropic 正是新的“进入”阶段。

> 信息来源：[The Algorithmic Bridge 分析](https://www.thealgorithmicbridge.com/p/andrej-karpathy-joins-anthropic-what)（二手，含一手 X 回复引述）；[No Priors 播客转录](https://podscripts.co/podcasts/no-priors-artificial-intelligence-technology-startups/andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai)（一手访谈，二手转录）；可信度：高（Anthropic 任命与推文），中（动机推断）。

#### 6.3 与 Eureka Labs 的关系

Karpathy 将加入 Anthropic 描述为教育的“暂停”而非“终止”。他表示“计划在适当的时候恢复这项工作”。Eureka Labs 在 2026 年 5 月之后的运营状态公开信息有限。

> 信息来源：[TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)（二手）；可信度：中（未来状态不明）。

---

### 7. 知识产权与开源决策

#### 7.1 教育工具全部开源

Karpathy 持续将教育项目开源：
- **micrograd**（2020 年发布）：最小标量自动微分引擎，演示反向传播
- **nanoGPT**（2022 年）：最小 GPT 训练实现，GitHub 37k+ stars
- **LLM101n**（2024 年）：本科级 LLM 课程材料
- **nanochat**（2025 年）：最小端到端 ChatGPT 训练流程

这些决策与他“通过实现来理解”的教学哲学一致，也强化了他作为公共教育者的身份。

> 信息来源：[GitHub karpathy](https://github.com/karpathy)（一手）；[karpathy.ai](https://karpathy.ai/)（一手）；可信度：高。

#### 7.2 从 Software 2.0 到 Software 3.0 / Vibe Coding

2017 年，Karpathy 在 Medium 发表《Software 2.0》，提出神经网络权重是一种由数据“学习”出来的新型代码。2024–2025 年，他将这一框架推进为“Software 3.0”：用自然语言提示作为新的“源代码”。

2025 年 2 月，他创造了“vibe coding”一词，描述一种几乎不读代码、通过与 AI 对话快速迭代构建软件的方式。原始推文中的完整定义（经 Simon Willison 引用）：

> “有一种新的编程方式我称之为‘vibe coding’，你完全沉浸在 vibe 中，拥抱指数级增长，忘记代码甚至存在……我总是‘全部接受’，不再阅读 diff。当出现错误信息时，我只是复制粘贴进去，通常就能修好。代码增长到我通常无法理解的程度……对于一次性的周末项目来说还不算太糟，但仍然挺有趣的。”

值得注意的是，Karpathy 在原始推文中明确加了限定：“还不算太糟 for throwaway weekend projects”，说明他并不认为 vibe coding 适用于所有工程场景。

> 信息来源：[Simon Willison 博客](https://simonwillison.net/2025/Mar/19/vibe-coding/)（二手，含一手推文全文）；[MindStudio 博客](https://www.mindstudio.ai/blog/what-is-vibe-coding-ai-software-development)（二手）；可信度：高。

---

### 8. 投资策略与副业决策

#### 8.1 天使投资

Karpathy 参与了多家 AI 初创公司的天使投资，包括：
- **Adept**（2022 年 4 月，6500 万美元轮）
- **Lamini**（2024 年 5 月，2500 万美元 A 轮）
- **/dev/agents**（2024 年 12 月，5600 万美元，估值 5 亿美元）
- **Lambda**（2025 年 2 月，4.8 亿美元 D 轮）
- **Perplexity**（Series A，与 Jeff Bezos、Nvidia 等共同投资）

这些投资方向集中在 AI 基础设施（Lambda）、AI 应用层（Perplexity）、AI agents（Adept、/dev/agents）和企业 LLM 定制（Lamini），与他公开表达的技术判断高度一致。

> 信息来源：[Observer](https://observer.com/2025/02/openai-cofounder-andrej-karpathy-ai-startups/)（二手）；[AIFundingTracker](https://aifundingtracker.com/best-ai-startup-pitch-decks/)（二手）；可信度：中（部分信息为汇总报道，未逐一确认原始投资文件）。

---

### 9. 重大判断与自我反思

#### 9.1 “我最大的职业错误是没更早押注 LLM”

2024 年 11 月，Karpathy 在 X 上连续发帖，称自己在 OpenAI 早期已认识到自回归语言模型的潜力，却随大流投入强化学习，是“有史以来最大、最令人困惑的研究生涯错误”。

这一反思表明：
- 他在技术路线选择上并非总能提前押中；
- 他对 LLM 的后来重视可能部分源于这种“错失恐惧”和补偿心理。

> 信息来源：[机器之心中文报道](https://blog.csdn.net/sinat_37574187/article/details/143200847)（二手，转述 X 推文）；原推文一手来源未直接获取；可信度：中（内容为二手转述，但与他后续行为一致）。

#### 9.2 AGI 时间线：十年之久，而非“agent 之年”

2025 年 10 月，Karpathy 在 Dwarkesh Patel 播客中表示：

> “它们没有持续学习能力。你刚教给它们一件事，它们记不住。它们在认知上有缺陷，就是不行。解决所有这些问题大约需要十年。”

他反对“2025 是 agent 之年”的提法，认为应该是“2025–2035 是 agent 的十年”。同时他承认 Claude、Codex 等工具“极其令人印象深刻”，但强调距离可替代人类员工的通用 agent 仍有大量工作。

> 信息来源：[Indian Express](https://indianexpress.com/article/technology/artificial-intelligence/andrej-karpathy-agi-is-still-a-decade-away-heres-why-10316244/)（二手，含一手访谈引述）；[Gigazine](https://gigazine.net/gsc_news/en/20251021-andrej-karpathy-agi-decade-away/)（二手）；可信度：高。

#### 9.3 评估危机与对基准的不信任

2025 年 3 月 2 日，Karpathy 在 X 上表示：

> “我的反应是存在一场评估危机。我现在真的不知道该如何看待这些模型。”
>
> “MMLU 曾经几年内都是一个好且有用的指标，但那早已过去。”
>
> “Chatbot Arena 受到太多关注（部分是我的错？），以至于 LLM 实验室开始真正地对它过拟合。”

这一立场与他 2025 年底提出的“幽灵 vs. 动物 / 锯齿状智能”框架一致：他认为现有基准多为可验证环境，容易被 RLVR 和合成数据“攻击”，无法反映真正的通用能力。

> 信息来源：[LX10077 PDF 幻灯片](https://lx10077.github.io/assets/pdf/slides/2025GM_unseen.pdf)（二手，含 X 推文截图）；可信度：高。

#### 9.4 “精神错乱状态”：从写代码到指挥 agent

2026 年 3 月 21 日，Karpathy 在 No Priors 播客中承认：

> “我想我从 12 月起就基本没打过一行代码了，这变化极其巨大。”
>
> “我现在处于一种精神错乱状态，试图弄清楚什么是可能的，试图把它推到极限。”
>
> “我现在每天必须向我的 agent 表达我的意愿 16 个小时。”
>
> “我经历了 1 月份的 claw 精神错乱……我造了一个叫‘Dobby the House Elf claw’的东西，它现在管理着我家的音响、灯光、安防、窗帘、暖通空调、泳池和水疗。”

这一表态显示他对 AI agent 的采用已深入到工作流和日常生活，但同时也引发外界对他作为“教育家/第一性原理倡导者”身份的担忧——如果代码不再是他的主要工作方式，他如何继续示范“从零实现”？

> 信息来源：[Fortune](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/)（二手，含一手播客引述）；[No Priors 播客转录](https://podscripts.co/podcasts/no-priors-artificial-intelligence-technology-startups/andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai)（一手访谈，二手转录）；可信度：高。

---

### 10. 言行一致性与矛盾点

#### 10.1 一致性

- **教育热情贯穿始终**：从 CS231n、YouTube、micrograd/nanoGPT，到 Eureka Labs，教育始终是他的核心身份。
- **偏好技术工作而非管理**：离开 Tesla 时明确表达这一点；加入 Anthropic 时选择研究员/团队负责人角色而非 C-suite。
- **公开透明、build in public**：Eureka Labs 的宣布即体现“公开建设”；他在 X 上高频分享思考。
- **第一性原理与从零实现**：无论是 Tesla 的视觉-only 辩护、CS231n 的作业设计，还是 nanochat 的极简训练流程，都体现这一风格。

#### 10.2 张力与矛盾

- **“离开是为了个人项目/独立” vs. 再次加入大公司**：2024 年 2 月离开 OpenAI 时说“专注于个人项目”，但 2026 年 5 月加入 Anthropic。他本人用“进进出出”的钟摆模式解释，但外界仍可质疑这是否削弱了 Eureka Labs 的承诺。
- **“AGI 还有十年” vs. 加入预训练团队**：他公开强调通用 agent 还有很长距离，但加入 Anthropic 预训练团队恰恰说明他相信未来几年是“形成性”的——这二者并不矛盾，但措辞上存在张力。
- **“vibe coding 适用于一次性项目” vs. 自己大量依赖 agent**：他在原始推文中限定 vibe coding 适合“周末项目”，但 2026 年 3 月表示几乎所有代码都交给 agent。这是一种立场演进，也可能被外界视为前后不一致。
- **纯视觉自动驾驶的赌注仍未兑现**：Waymo 的 LiDAR 路线已实现商业无人驾驶出租车，而 Tesla FSD 仍需人类监督。Karpathy 离开后，Tesla 继续推进纯视觉路线，但他作为该路线的主要倡导者之一，其长期正确性尚未得到最终验证。

---

## 来源清单

| 来源 | 类型 | 可信度 | 关键内容 |
|------|------|--------|----------|
| https://karpathy.ai/ | 一手 | 高 | 完整职业时间线、CS231n、Tesla/OpenAI 任期、项目列表 |
| https://karpathy.bearblog.dev/year-in-review-2025/ | 一手 | 高 | 2025 LLM 年度回顾：RLVR、Ghosts vs Animals、Cursor、Claude Code、Vibe Coding、Nano banana |
| https://github.com/karpathy/nanochat | 一手 | 高 | nanochat 项目目标与设计哲学 |
| https://github.com/karpathy | 一手 | 高 | micrograd、nanoGPT、LLM101n 等开源项目 |
| https://podscripts.co/podcasts/lex-fridman-podcast/333-andrej-karpathy-tesla-ai-self-driving-optimus-aliens-and-agi | 二手（一手访谈转录） | 高 | 离开 Tesla 的详细原因、纯视觉辩护、对 Optimus/AGI 的看法 |
| https://pharath.github.io/self%20driving/Karpathy-CVPR-2021/ | 二手（一手演讲转录） | 高 | CVPR 2021 纯视觉自动驾驶演讲全文 |
| https://cleantechnica.com/2021/06/21/teslas-andrej-karpathy-gives-a-keynote-at-cvpo-2021-workshop-on-autonomous-driving/ | 二手 | 高 | CVPR 2021 演讲要点摘要 |
| https://finance.yahoo.com/news/andrej-karpathy-leaving-openai-again-031554234.html | 二手 | 高 | 2024 年 2 月离开 OpenAI 的推文引述与背景 |
| https://www.theinformation.com/articles/openai-researcher-andrej-karpathy-departs | 二手 | 高 | 确认 2024 年 2 月离职（付费墙） |
| https://venturebeat.com/ai/ex-openai-and-tesla-engineer-andrej-karpathy-announces-eureka-labs-ai-native-school/ | 二手 | 高 | Eureka Labs 成立、融资、LLM101n |
| https://www.siliconrepublic.com/machines/andrej-karpathy-eureka-labs-ai-startup-education-platform-llm101n | 二手 | 高 | Eureka Labs 理念与“教师+AI 共生” |
| https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ | 二手 | 高 | 2026 年 5 月加入 Anthropic、职位与任务 |
| https://daringfireball.net/linked/2026/05/19/karpathy-anthropic | 二手 | 高 | Anthropic 任命推文原文 |
| https://www.thealgorithmicbridge.com/p/andrej-karpathy-joins-anthropic-what | 二手 | 中 | 对加入 Anthropic 动机的分析，含 X 回复引述 |
| https://podscripts.co/podcasts/no-priors-artificial-intelligence-technology-startups/andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai | 二手（一手访谈转录） | 高 | 2026 年 3 月“精神错乱状态”、agent 工作流、Dobby claw |
| https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/ | 二手 | 高 | 同上，浓缩报道 |
| https://simonwillison.net/2025/Mar/19/vibe-coding/ | 二手 | 高 | “vibe coding”原始推文全文 |
| https://www.mindstudio.ai/blog/what-is-vibe-coding-ai-software-development | 二手 | 中 | vibe coding 定义与行业影响 |
| https://indianexpress.com/article/technology/artificial-intelligence/andrej-karpathy-agi-is-still-a-decade-away-heres-why-10316244/ | 二手 | 高 | Dwarkesh 播客中 AGI 十年论与 agent 十年论 |
| https://gigazine.net/gsc_news/en/20251021-andrej-karpathy-agi-decade-away/ | 二手 | 高 | 同上，补充推文回应 |
| https://www.klover.ai/andrej-karpathy/ | 二手 | 中 | 教育背景、Fei-Fei Li 影响、CS231n 影响 |
| https://observer.com/2025/02/openai-cofounder-andrej-karpathy-ai-startups/ | 二手 | 中 | 天使投资列表（Adept、Lamini、/dev/agents、Lambda） |
| https://aifundingtracker.com/best-ai-startup-pitch-decks/ | 二手 | 中 | Perplexity 投资名单含 Karpathy |
| https://blog.csdn.net/sinat_37574187/article/details/143200847 | 二手 | 中 | 2024 年 11 月“最大职业错误”推文转述 |
| https://lx10077.github.io/assets/pdf/slides/2025GM_unseen.pdf | 二手 | 高 | 2025 年 3 月“评估危机”推文截图 |
| https://cs.stanford.edu/people/karpathy/ | 一手（旧版） | 高 | 早期履历、CS231n 创建、Tesla 时期描述 |

## 信息缺口

- **2015 年选择加入 OpenAI 的具体决策过程**：Karpathy 本人几乎未公开谈论为何放弃学术/教职路径加入当时刚成立的非营利 OpenAI，现有信息多为推断。
- **2017 年 Musk 招募细节**：虽然有报道称 Musk 亲自招募并称他为“计算机视觉世界第二”，但具体对话、待遇、角色谈判等一手信息未公开。
- **2024 年 2 月离开 OpenAI 的“个人项目”具体内容**：他当时暗示关注者能猜到，但具体是 Eureka Labs 的早期雏形还是 AI agent 项目，公开信息有限。
- **Eureka Labs 2026 年 5 月之后的实际运营状态**：Karpathy 称教育热情不变、计划恢复，但是否停止招聘、课程发布计划是否推迟、投资协议如何处理，均无公开细节。
- **加入 Anthropic 的具体薪酬/股权与合同条款**：未公开，所有报道均为推测。
- **“最大职业错误”推文的原始英文文本**：目前仅见中文媒体转述，未找到原始 X 帖子存档。
- **对 Tesla 纯视觉路线的事后评价**：Karpathy 离开后很少公开评价 Tesla FSD 的后续进展，也未明确承认或否认该路线是否被验证。
- **天使投资决策标准**：投资多家公司的具体原因、尽职深度、是否担任顾问角色等信息不足。
