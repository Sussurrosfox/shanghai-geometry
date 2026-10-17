# qchain self_study 攻击性研究报告

## 范围与结论

目标是评估 self_study 模式能否产出知识完整、逻辑连贯、问题驱动的学案，并重点检查选择题化填空。按用户最新要求，本次只研究并出具报告，不修改插件源码、配置、流水线状态或现有产物。

研究对象为已安装的 qchain 插件源码：`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain`。源码检查结合只读合成输入验证。当前 `self/` 只有模板文件 `sec_template.tex`，没有 `sec*.tex` 题链、映射表或 PDF；因此不能对真实已交付学案做端到端教学质量复核。本报告把可运行复现与源码推导的风险分开陈述。

**总评：** qchain 已有相当完整的结构、编号、选项格式、材料批准、渲染、审读与交付机制，不应笼统称为“没有门禁”。但最关键的自学语义承诺仍存在可实证绕过：知识卡/结论框只检测环境起始标记，不校验闭合、学生可见性、相对题目位置或章节末位置；知识依赖图和 coverage 也没有在现有被检查的核心脚本里形成全章逐项一致性门禁。选择题的“随机”机制是确定性哈希排序，能打散源码中答案首位的惯性，却不保证答案位置严格均衡，也不检查干扰项是否数学上可信或是否存在唯一正确答案。

## 高置信度发现

### F1. 教学语义门禁允许教师区内、错位和未闭合的知识框通过

**严重度：高。证据：只读合成复现，成功绕过。**

`check_pedagogy.check_pedagogy_slice` 在 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_pedagogy.py:60-75` 用正则 `findall` 搜索全文的 `\\begin{knowledgebox}` 与 `\\begin{microknowledge}`；只要找到开头标记就算存在。它未检查对应 `\\end`，也未检查学生可见性或知识卡是否出现在相关题目之前。题目与填空的教师区过滤是在之后另行做的，知识框存在性统计没有应用这个过滤。

攻击输入 A：把两个框都完整放在 `solution` 内，学生版不可见。攻击输入 B：在正文开头放一个 knowledgebox，再放一个未闭合的 microknowledge。两者调用 `check_pedagogy_slice` 均返回 `(1, 1)`，`problems=[]`，也就是门禁判定没有问题。复现结果与源码一致，不依赖真实学案。

此外，`check_numbering.py` 的知识框检测在 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_numbering.py:489-499` 也是全文子串存在性检查；环境栈配平覆盖普通 begin/end 事件，但不能将“至少出现过此环境”提升为“每节末结论框闭合且学生可见”。

**教学影响：** 门禁绿灯不代表学生实际看到前置定义，也不代表读完题链后看到总结。新符号可先被题目使用、定义放在后面，或总结藏在教师解答区；这直接破坏自学的局部自足与闭环。

**建议：** 以解析后的环境区间做检查：学生可见区、题目前置顺序、knowledgebox 位于节末、恰当的标题/内容、环境正确配平；并明确允许纯定理节不设 microknowledge 的规则与通用硬门禁规则如何统一。对多题节应检查每个新对象首次使用前的定义，而不只是“有一张卡”。

### F2. 选择题的结构合法不等于干扰项有效或答案唯一

**严重度：高（教学有效性），中（门禁缺口）。证据：源码检查。**

`check_numbering.check_fillin_options` 在 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_numbering.py:285-325` 可靠地检查答案存在、至少三个选项、答案属于选项、无空项、归一化后无重复。这些是有价值的结构约束。但它不检查选项数学语义、干扰项是否源于典型错误、选项是否互斥、题干是否给出充分条件、是否有多个选项都成立。

写作提示在 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\prompts\subagent_prompt.md:58-60` 要求干扰项来自初学者典型错误且不能明显荒谬；目前该要求在所检查的结构门禁中没有对应机器判定或逐题强制验收字段。故攻击性生成可用三个形式不同但都正确的表达式凑足选项，或给出两个正确选项；numbering gate 仍可能放行。此结论是基于检查器职责和代码覆盖范围的静态证据，不声称已运行一条完整的具体数学反例学案。

**教学影响：** 有效选择题必须把错误模型转化为可诊断选项，并能唯一地区分掌握状态。只验证格式会让“看似多选项、实际猜谜/多解”的题通过。

**建议：** 每空附结构化答案理由、干扰项对应错误类型、唯一性证明或边界条件；机器先验证代数等价/数值域等可计算部分，人工盲审处理开放数学语义。对近似、等价形式、符号域和定义条件明确规定判等策略。

### F3. 答案位置打散是确定性的，不是均衡保证

**严重度：中。证据：源码机制 + 只读模拟。**

`shuffle_options.py` 以 `SHA256(salt + identity + option)` 排序，身份为文件名加该文件内填空序号，详见 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\shuffle_options.py:190-203,217-270`。固定 salt 为 `qchain/shuffle-options/v1`（同文件第 62-64 行）。同一身份和选项集重跑次序完全相同；代码文档也明确其幂等性。这样可消除“答案永远第一个”的系统性偏差，且不会重复重排。但确定性伪随机不承诺整个章节的正确答案位置平衡。

只读模拟 1000 道四选项、固定正确项 A 的独立槽位，正确项落在 0/1/2/3 位的次数为 **270/245/246/239**，极差 31。对同一 identity 重复执行完全相同；1000 个 identity 中 24 种排列均出现。这个模拟不代表全部题型或某个具体章节分布，但说明机制没有严格配额约束。

**建议：** 发布前做章节级答案位置分布门禁，设置有统计依据的偏差阈值；如要严格均衡，按题目组生成约束排列并保留确定性 seed 与报告。给正式发布提供可审计的分布摘要，而非把“哈希排序”称作位置均匀。

### F4. coverage 与实际题目可通过顺序回退静默错配

**严重度：高（跨题链预算/覆盖一致性）。证据：源码追踪。**

`estimate_minutes.parse_coverage_map` 在 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\estimate_minutes.py:87-198` 解析 coverage 的题目身份。估算逐行先按 qid、再按 carrier_qid/node_id 匹配；若均未匹配且该节仍有 TeX 题目，则在 `:291-315` 按顺序取下一道题，而不是对身份不匹配报错。核心预算检查 `check_budget.py` 调用估算器，但现有此处未将 qid 无法精确对应作为硬失败（`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_budget.py:183-220`）。

这可能使 coverage 中缺失/错误 qid 的目标被另一道题的结构耗时静默估算；从而预算账本仍可产出，但题目覆盖和负荷归属不可信。覆盖表解析允许通过 carrier_qid 让多个原文节点复用载体题，这是合理需求；然而需要显式区分合法多节点复用与错误 qid 的顺序兜底。目前源码路径把缺配归为估算 fallback，而不是暴露映射差异。

**建议：** 对 core/support 必须精确匹配 qid 或显式 carrier_qid；coverage 行与 TeX qid 集合做双向差集检查，唯一允许的多对一关系必须由 carrier_qid/复用组显式标注；顺序 fallback 限于无身份的旧格式并显式 warning，不能静默用于当前 schema。

## 设计层风险与较强保证

### R1. 全章知识依赖图作为教师契约，没有自动验证语义边

`overview-guide.md` 要求构建“没有前者就难以理解后者”的概念依赖图，并列出不可跳过定义、反例、完整证明和跨题关系：`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\self\overview-guide.md:53-78`。写作提示也要求在学生可见内容上检查依赖闭合：`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\prompts\subagent_prompt.md:51-55,75-79`。这些是良好的规划约束，但本次检查到的 `check_numbering`、`check_pedagogy`、`check_budget` 没有将图中每条边解析为全章可验证的先修约束。局部知识框存在性不能替代知识依赖图闭合。

### R2. self_study 的“三节规划”与“知识密度分节”需要解释为规划偏好而非硬限

self_study 映射提示将结构限定为概念引入、核心工具推导、度量与应用三节（必要时 sec3a/sec3b），并要求自学时长不设上限，见 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\workflow\nodes\mapping_nodes.py:75-89`。研究提示同样推荐三段精炼结构（`...\prompts\research_prompt.md:50-53`），但又允许按知识密度拆成子切片（`:45-49`）。若把“三节”提示理解为硬限制，可能与高密度内容必须拆分相冲突。代码侧主要硬约束是规划重试预算与 section 名称等，未在本次验证中找到直接强制恰好三节的结构门禁。建议在提示中声明“三类教学功能、节数按依赖图和认知负荷决定”，消除字面冲突。

### R3. 题链结构与选择题基础机制已有较好防线

以下能力经源码确认，报告不将其误报为漏洞：

- 题目 qid 缺失会警告、重复会失败；每题要求一个 solution 和 teacherNote；详见 `C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_numbering.py:355-389`。
- begin/end 环境采用栈式平衡检查，包含注释扫描、probchain/列表约束：`...\scripts\check_numbering.py:392-489`。
- 每个 fillin 的选项数、答案归属、去重、空项有硬门禁：`...\scripts\check_numbering.py:285-325`。
- 核心定理题认知台阶、数值例、常量答案比例、旁观者题干有教学门禁；但其语义检测主要靠关键词和启发式规则：`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\check_pedagogy.py:187-253`。
- 材料索引会校验 approved 状态、研究需求与 coverage 承接关系：`C:\Users\63254\AppData\Roaming\npm\node_modules\@deepseek-ai\dsh\node_modules\@local\qchain\scripts\evidence.py:495-558`。
- 选项重排提供只读 verify、逐槽记录和答案位置统计；交付管线要求接受审读覆盖全部 qid。项目自带回归测试包括 `test_runtime.py` 的材料链和部分 qid 审阅覆盖场景（`:392-424`）。

## 验证边界

- 已执行只读攻击：直接调用 `check_pedagogy_slice`，教师区内两个框与错位/未闭合框均未报错。
- 已执行只读选项统计：1000 个槽位、四选项固定正确答案的散列位置频数为 270/245/246/239；同一身份重复排列稳定。
- 未运行 `qchain_gate all` 或流水线，因为当前 self/ 没有真实学案输入，且部分流水线门禁会生成报告/状态文件；本任务要求不触碰流水线产物。
- 未证明任一真实学案存在数学错误或实际交付缺陷。关于干扰项有效性和题链语义闭合的判断，是从现有结构检查器不覆盖这些语义属性得出的风险，不等同于某个真实样本的失败报告。

## 修复优先级建议（供后续决策）

1. **P0：** 将知识卡/结论框检查改为学生可见的闭合环境区间校验，并检查相对题目位置、结论框位置及每个新概念的首次使用。
2. **P0：** 对 coverage-map 与 TeX qid 做双向精确集合核对；只允许显式声明的 carrier 复用，禁止静默顺序匹配掩盖身份错配。
3. **P1：** 建立选择题的唯一正确项/数学等价性与干扰项诊断依据审读协议；硬性可算题型先机械验证，其他题要求逐题证据。
4. **P1：** 汇总全章答案位置，增加可解释分布告警或严格平衡生成模式；保留当前确定性以支持可复现构建。
5. **P2：** 澄清 self_study 三类教学功能和实际切片数量的关系，并把“知识完整/逻辑连贯”拆成可审查的节点覆盖表、依赖边和学生侧证据。
