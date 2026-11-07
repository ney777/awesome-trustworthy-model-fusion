# 可信模型融合与协作 Awesome

本库整理模型融合及直接相关的可信协作研究，重点关注联邦与分布式场景。按 **Representation → Governance → Evolution** 组织文献：模型如何描述与对齐，融合决策如何满足可信要求，以及模型或环境变化后如何更新和重新验证。

[英文文献目录](README.md) · [范围界定](docs/scope-and-definitions.md) · [分类框架](docs/taxonomy.md) · [综述比较](docs/prior-surveys.md) · [模型配置](docs/model-conditions.md) · [文献概览](docs/literature-report.md)

## 如何浏览

- [英文文献目录](README.md)：按研究类别浏览表格，查看年份、论文、发表 venue、CCF 等级、发表状态及论文／代码链接。
- [联邦模型融合专题表](docs/federated-literature.md)：查看联邦与分布式工作各自的融合对象、操作和可信问题。
- [详细文献页](docs/papers.md)：查阅机制、假设、局限及原文证据位置；[综述比较](docs/prior-surveys.md)帮助选择入门和专题阅读材料。
- [CSV](data/papers.csv)：下载后按年份、类别、标签或发表状态筛选；[BibTeX](data/references.bib)用于引用，[JSON](data/papers.json)提供完整结构化记录。

目录收录书目信息已确认、符合范围的工作。书目确认、正文阅读深度和实验复现分别记录；尚未阅读全文不等于论文身份未确认，也不能据此推断论文没有讨论某个问题。最新统计和阅读深度见[文献报告](docs/literature-report.md)。

CCF 分类仅使用 **2026 年第七版正式目录**，并区分 Findings、Industry 等具体发表轨道。**“—”表示未列出等级**，不代表确定不在目录中，也不推断为主会等级。缺少 CCF 等级不影响书目信息已确认的相关工作正常收录。

本库提供文献导航与分析，覆盖范围和证据规则见[检索说明](docs/search-protocol.md)。文献归纳不等于算法验证或实验复现。欢迎按[贡献指南](CONTRIBUTING.md)补充相关论文和更正信息。

## 联邦场景的纳入边界

联邦学习是重点场景，不能单独作为纳入理由。专题表中的方法必须明确涉及哪些模型或模块，以及如何对齐、组合或传递其知识。

模型对齐、参数／模块融合、多模型蒸馏，以及直接针对融合的可信机制可纳入；一般联邦优化、客户端调度、梯度防御或隐私／公平目标不单独构成纳入依据。相关综述单列比较，并与方法条目区分。
