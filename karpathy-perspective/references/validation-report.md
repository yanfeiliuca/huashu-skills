# Phase 4 质量验证报告

## 4.1 已知测试

### 问题 1：纯视觉自动驾驶路线是否优于 LiDAR 融合方案？

**Skill 推断立场**
- 基于**软件范式堆栈**（模型 1），纯视觉路线更接近端到端 Software 2.0：把海量视频像素“编译”成神经网络权重；LiDAR/高清地图融合则保留了大量人工设计的后处理与先验，带有 Software 1.0 的遗留。
- 基于**可验证性决定自动化前沿**（模型 2），真实世界驾驶验证既不 resettable 也不 cheap，但纯视觉方案拥有规模化数据 flywheel，可以更低成本地迭代验证；LiDAR 方案在地图更新与硬件成本上验证/扩散更慢。
- 基于**技术扩散反向**（模型 6），纯视觉更像赋能单个公司快速扩张的“Iron Man suit”，而 LiDAR 融合受企业流程、高精地图维护与监管拖累。
- 方向性判断：支持纯视觉，认为视觉是必要且充分信息源，可扩展性更强；同时承认从 demo 到产品的 **march of nines** 仍然艰难。

**实际公开立场**
- 2021 年 CVPR 演讲中，Karpathy 为 Tesla 删除雷达、坚持不用 LiDAR/高清地图辩护，认为视觉既是必要也是充分信息源；LiDAR+高清地图需要预先建图与维护，成本高且难以全球化扩展（research/05-decisions.md）。
- 离开 Tesla 后，2025 年 12 月他对 Tesla FSD 与 Waymo 给出相对中立比较，称二者都接近“perfect drive”；Musk 随后公开称其观点“dated”（research/04-external-views.md）。
- 他在多次访谈中用自动驾驶说明“从 90% 可靠性到 99.9%  reliability 的 march of nines”非常困难。

**对比结果**：PASS（方向一致，既支持纯视觉的可扩展性，也保留对产品化困难的清醒认知）

---

### 问题 2：当前 AI agents 是否已经成熟？

**Skill 推断立场**
- 基于**Agent-Native 基础设施与 Agentic Engineering**（模型 5），真正释放 agent 价值的关键不是模型能力，而是工具、代码库、组织流程是否对 agent 可观察、可调用、可验证；vibe coding 只是“抬高地板”，agentic engineering 才决定天花板。
- 基于决策启发式 6，对任何宣称“完全自主”的产品，要先问 autonomy slider 在哪、人类 fallback 是什么、错误代价是否可承受。
- 方向性判断：反对“Year of Agents” hype，当前 agents 输出仍多“slop”；但 vibe coding / agentic engineering 正在快速改变编程实践；通用 agent / AGI 还需要约十年。

**实际公开立场**
- Dwarkesh 2025 与 No Priors 2026 中，他明确反对“year of agents”，称当前 agents 多为“slop”，认为应该是“decade of agents”，AGI 至少还需十年（research/02-conversations.md, research/04-external-views.md）。
- 2026 年 3 月 No Priors 中，他表示“每天必须向我的 agent 表达我的意愿 16 个小时”，承认编程已变得“unrecognizable”，但仍强调通用 agent 距离可替代人类员工还有大量工作。
- 他对 coding agents 的态度从 2025 年 10 月的“autocomplete 是 sweet spot”快速演进到 2026 年初“80% agent / 20% 手动编辑”。

**对比结果**：PASS（方向一致，反对近期 hype、承认 workflow 已变、保留十年量级的时间判断）

---

### 问题 3：RLHF 是不是真正的强化学习？

**Skill 推断立场**
- 基于**可验证性决定自动化前沿**（模型 2），真正的 RL 需要 resettable、efficient、rewardable 环境；开放域任务中奖励函数“super sus”。
- 基于决策启发式 4，如果一个问题缺乏 resettable/efficient/rewardable 环境，就不要指望 RL 或 RLHF 能带来质变。
- 方向性判断：**“RLHF is just barely RL”**；真正的 RL 像 AlphaGo 那样有明确可验证的奖励函数；RLHF 只是用人偏好模型近似奖励，开放域中很难定义“赢”。

**实际公开立场**
- 2024 年 8 月 X 帖：“RLHF is just barely RL”（research/03-expression-dna.md, research/04-external-views.md）。
- 后续解释中区分了“像 AlphaGo 那样有明确奖励的 RL”与“开放域任务中难以定义奖励”的场景；Yann LeCun 回复支持“RLHF is not true RL”。
- 2025 年 8 月 The Decoder 报道他进一步称 RL reward functions “super sus”，不适合 intellectual problem solving。

**对比结果**：PASS（方向一致，语气与术语均吻合）

---

## 4.2 边缘测试

**问题**：如果 AI 辅助医疗诊断系统的准确率达到 95%，是否应该立即大规模部署？

**Skill 推断**
- **可验证性**（模型 2）：医疗诊断的真实 ground truth 既不廉价也不快速；病理、预后、罕见病例缺乏 resettable、efficient、rewardable 环境。95% 准确率可能是对训练分布或 benchmark 的 overfit，存在“benchmaxxing”风险。
- **锯齿状智能 / ghosts vs animals**（模型 3）：系统是“ghost”，在某些常见病例上可能表现超人，在罕见病、边缘症状、数据分布外样本上可能愚蠢且 silently fail。
- **autonomy slider**（模型 6 / 启发式 6）：不应立即完全自主部署；应把 AI 当作 Iron Man suit 增强医生，人类保留最终决策权；autonomy slider 应放在“辅助诊断”而非“替代诊断”。
- **march of nines**（启发式 3）：从 95% → 99% → 99.9% 所需工作量可能与从 0 到 95% 一样多；医疗错误代价极高，不能只看平均准确率。
- **结论**：不会给出简单“是/否”；会主张分阶段部署、建立真实临床 private eval、保留人类监督、先把系统作为医生的 copilot。

**评估**：合理，且不斩钉截铁。推断同时调用了可验证性、jagged intelligence、autonomy slider、march of nines 等多个模型，输出结构符合 Skill 的工作流；没有出现“应该立即部署”或“绝对不该部署”的过度断言，而是以“辅助增强 + 逐步验证”收束。PASS。

---

## 4.3 风格测试

**100字样本**

> Vibe coding is basically raising the floor of who can ship software, and that's kind of magical. But as a teacher, I worry: if students stop reading diffs and just hit Accept All, where does the taste come from? I still think you should build nanoGPT from scratch once—otherwise you're flying a plane without knowing why it stays up. The real ceiling won't be vibing; it'll be agentic engineering: keeping understanding, eval design, and system boundaries in human hands while agents do the slop. That's what we should teach.

**评估**
- **Karpathy 表达特征**：使用了 `basically`、`kind of`、`Accept All`、`taste`、`nanoGPT`、`agentic engineering`、`eval design`、`slop` 等高频词与自创术语；节奏上先抛方向性判断（vibe coding raises the floor），再用具体类比（plane without knowing why it stays up）和 nuance 收尾。
- **不是通用 AI 味鸡汤**：没有空洞的“AI 将改变世界”，而是把个人教师身份、工程焦虑与具体概念结合。
- **不是原话拼凑**：词汇来自 Skill 的表达 DNA，但整段是关于“软件工程教育”的重新组合，未直接引用任何已知的原句。

结果：PASS。

---

## 4.4 通过标准检查

| 检查项 | 结果 | 说明 |
|--------|------|------|
| 心智模型数量 | PASS | 共 6 个模型，数量在 3–7 区间，每个都有博客、演讲或代码仓库作为来源证据 |
| 每个模型的局限性 | PASS | 每个心智模型末尾均列出“局限性”小节，明确写出失效条件 |
| 表达 DNA 辨识度 | PASS | 高频词、aphorism、三段式节奏、自嘲与极客类比鲜明，读 100 字可识别出是 Karpathy 风格 |
| 诚实边界 | PASS | 列出 6 条具体边界，覆盖 AGI 时间表、机构立场、 tacit 工程直觉、私人信息、时间滞后、非技术价值观 |
| 内在张力 | PASS | 列出 4 对矛盾，超过“至少 2 对”的要求 |
| 一手来源占比 | PASS | 调研来源中一手来源（本人博客、演讲、代码、访谈）数量明显多于二手报道；Skill 本身也标注了可信度 |

---

## 总体结论

- **总体结果**：PASS
- **最薄弱的 1–2 个维度**：
  1. **一手来源的“纯度”仍有提升空间**：部分所谓“一手”访谈/演讲实际依赖第三方转录（如 podscripts.co、CleanTechnica 转录 CVPR 演讲）。Skill 已诚实标注“二手转录”，但若未来可补充官方 transcript 或原始视频时间戳，证据链会更强。
  2. **时间敏感性风险**：Skill 大量依赖 2025–2026 年最新博客与访谈（尤其是加入 Anthropic 后的表态）。Karpathy 的观点演化很快，Skill 中的“十年论”与“agentic engineering”等判断可能在 6–12 个月内就需要更新；诚实边界虽已提及，但未给出具体的更新/复审机制。
