# 可信模型融合与协作 Awesome

研究范围为“广义可信模型融合与协作，联邦场景作为重点”。主线为 **Representation → Governance → Evolution**：先描述和组织模型，再在可信约束下决定如何协作，最后研究模型与环境变化后的更新和重新验证。

[英文文献目录](README.md) · [范围界定](docs/scope-and-definitions.md) · [分类框架](docs/taxonomy.md) · [综述比较](docs/prior-surveys.md) · [研究缺口](docs/research-gaps.md) · [Survey 提纲](docs/survey-outline.md)

唯一手工维护的文献源为 [data/papers.json](data/papers.json)。英文 README、CSV、BibTeX、详细文献页和综述数据视图由脚本生成。实际条目数量、核验状态和阅读深度见[文献报告](docs/literature-report.md)。

英文目录按研究类别分组，以表格列出年份、论文、发表 venue、CCF 等级、发表状态和论文／代码链接；[详细文献页](docs/papers.md)使用字段表保留每项工作的机制、假设、局限与证据定位。

两篇指定工作及相关补漏见[覆盖审计](docs/coverage-audit.md)。首页同时展示已核验条目和待核验表；书目核验与正文阅读深度独立记录，不因尚未读到正式全文而隐藏已确认的论文。

CCF 分类仅使用 **2026 年第七版正式目录**。未知等级保留为待核验，不等同于 None；Findings 和其他特殊轨道分别审查。对照原始文献时区分摘要核对、章节阅读和独立实验复现。

Survey 原稿、下载的全文、临时检索材料均保留在本地，不纳入 GitHub 发布。仓库中的研究报告属于文献分析，不能当作已经验证的新算法或已完成系统性检索的证明。

## 联邦场景的纳入边界

联邦学习仅是应用场景，不能作为纳入理由。此次移出 17 项一般联邦方法或融合相关性证据不足的工作，主库现有 120 项；[联邦模型融合专题表](docs/federated-literature.md)保留 42 项，每项明确列出融合对象和操作。见[范围纠正记录](docs/scope-correction.md)与[参考库逐项筛查](docs/federated-coverage-audit.md)。

模型对齐、参数／模块融合、多模型蒸馏，以及直接针对融合的可信机制可纳入；一般联邦优化、客户端调度、梯度防御或隐私／公平目标不单独构成纳入依据。用户指定的相关综述保留在综述比较区，不计入该方法专题表。
