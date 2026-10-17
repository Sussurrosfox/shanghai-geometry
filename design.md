# Quarto Book 整理设计方案

## 1. 目标与边界

本方案把当前目录中的平面几何课程资料整理为一个可发布的 Quarto Book，并保留已有的分步几何动态演示。

目标输出：

- 可搜索、可交叉引用、适合电脑和手机阅读的 HTML 书籍；
- 可打印的中文 PDF；
- 每道题的题目、原书解答、解题分析、分步文字和动态演示入口；
- 统一的章节、题号、图号、公式和图片路径；
- 后续新增题目时，可以通过元数据和脚本增量生成。

本次只处理已有的 01、02、03、04、06、07、08 七章。05 章是有意缺失的章节：不创建占位页、不补编号、不在目录中显示。根目录中的 10、11、13 也不属于本次范围。

不在范围内：

- 不重新证明题目，不修改数学结论；
- 不重写已有动态演示的 SVG 绘图算法；
- 不把 Python 脚本、日志和临时报告放入正文；
- 不把所有原始文件直接批量改名为 QMD；
- 不要求 PDF 和 HTML 使用完全相同的页面布局。

## 2. 当前资料模型

当前七章约有 56 道题。每题通常由以下文件组成：

~~~text
01/2.md                 题目和原书解答
01/2_solution.md        解题思路分析
01/2/steps.md           分步证明规划稿
01/2/2_steps.md         分步证明文字
01/2/2.html             动态演示
01/images/*.jpg         题目和证明图片
01/raw.md               整章原始汇编
01/raw_split.md         拆分后的整章汇编
~~~

资料分为三层：

1. 源材料层：当前目录中的 raw.md、n.md、n_solution.md、图片和 HTML；
2. 规范化内容层：脚本清洗后得到的章节和题目 qmd 文件；
3. 发布层：Quarto 生成的 _site 和 PDF。

源材料层只读。所有清洗、拆分和路径转换都写入新的 quarto-book 目录。

## 3. 目标目录结构

在当前目录下新建独立的 quarto-book 项目：

~~~text
quarto-book/
├── _quarto.yml
├── index.qmd
├── assets/
│   ├── book.scss
│   ├── print.scss
│   ├── macros.tex
│   └── demo.css
├── data/
│   ├── chapters.yml
│   └── problems.yml
├── scripts/
│   ├── build_content.py
│   ├── validate_content.py
│   └── normalize_math.py
├── chapters/
│   ├── 01/
│   │   ├── index.qmd
│   │   ├── lesson.qmd
│   │   ├── problems/02.qmd
│   │   ├── images/
│   │   └── demos/02.html
│   ├── 02/
│   ├── 03/
│   ├── 04/
│   ├── 06/
│   ├── 07/
│   └── 08/
└── README.md
~~~

design.md 位于源目录，不进入书籍导航。quarto-book/README.md 记录构建命令和源文件映射。

图片和动态演示按章节复制，保持原文件名：

~~~text
源：01/images/7_957_1582_432_366_0.jpg
目标：quarto-book/chapters/01/images/7_957_1582_432_366_0.jpg

源：01/2/2.html
目标：quarto-book/chapters/01/demos/02.html
~~~

## 4. Quarto 配置

quarto-book/_quarto.yml 使用以下配置作为起点：

~~~yaml
project:
  type: book
  output-dir: _site
  resources:
    - chapters/**/images/**
    - chapters/**/demos/**
  execute:
    freeze: true
    echo: false

lang: zh-CN
mainfont: "Noto Serif CJK SC"
sansfont: "Noto Sans CJK SC"

book:
  title: "上海中学竞赛课程：平面几何"
  author: "上海中学竞赛课程"
  language: zh-CN
  search: true
  chapters:
    - index.qmd
    - chapters/01/index.qmd
    - chapters/02/index.qmd
    - chapters/03/index.qmd
    - chapters/04/index.qmd
    - chapters/06/index.qmd
    - chapters/07/index.qmd
    - chapters/08/index.qmd

format:
  html:
    theme:
      - cosmo
      - assets/book.scss
    toc: true
    toc-depth: 3
    html-math-method: katex
    smooth-scroll: true
  pdf:
    pdf-engine: xelatex
    documentclass: ctexbook
    classoption: [UTF8, oneside]
    geometry: [a4paper, margin=20mm]
    include-in-header: assets/macros.tex
    toc: true
~~~

正式构建前确认：

- 已安装 Quarto CLI，quarto check 通过；
- PDF 环境有 XeLaTeX 和中文字体；
- 离线 HTML 已本地化 KaTeX，或明确允许 CDN；
- 输出目录不在源材料目录中。

## 5. 章节页面

chapters/XX/index.qmd 只负责章节导航和概览，不直接塞入全部题目正文。

推荐结构：

~~~markdown
---
title: "第一讲 全等三角形"
number: 1
---

## 本讲内容

本讲介绍全等三角形的定义、判定和竞赛中的典型用法。

## 知识精讲

{{< include lesson.qmd >}}

## 典型例题

| 题号 | 主题 | 核心方法 | 动态演示 |
|---|---|---|---|
| [例 2](problems/02.qmd) | 中位线与角相等 | 中点构造、全等 | [打开演示](demos/02.html) |
~~~

lesson.qmd 从 raw_split.md 提取知识精讲部分。raw.md 保留为源材料，不直接作为书页，避免题目和生成提示语重复。

章节首页必须提供题目索引，链接使用相对路径。

## 6. 题目页面

每道题对应一个页面，例如 chapters/01/problems/02.qmd，固定包含：

~~~text
标题与元数据
题目和图形
原书解答
解题分析
分步证明文字
动态演示入口
相关定理与相关题目
~~~

front matter 示例：

~~~yaml
---
title: "例 2：直线 KL 过线段 AJ 的中点"
chapter: 1
problem: 2
source-chapter: "01"
source-file: "01/2.md"
id: "ch01-p02"
tags:
  - 全等三角形
  - 中点
  - 角平分线
difficulty: "竞赛"
image: "../images/8_981_790_477_383_0.jpg"
demo: "../demos/02.html"
---
~~~

正文模板：

~~~markdown
## 题目

<!-- 从 n.md 提取题目部分 -->

## 原书解答

<!-- 从 n.md 提取正式证明，删除末尾的分析请求 -->

## 解题分析

<!-- 插入 n_solution.md，保留其标题层级 -->

## 分步证明

<!-- 优先插入 n_steps.md；steps.md 只作为生成和审校依据 -->

## 动态演示

[在新窗口打开分步演示](../demos/02.html){.demo-link target="_blank" rel="noopener"}
~~~

题目标题统一为“例 N：简短主题”。没有可靠短标题时，先使用题目正文第一句生成临时标题，并在 problems.yml 中人工修订。

## 7. 源文件映射

对于题号 n，映射规则固定如下：

| 页面内容 | 首选来源 | 备用来源 | 处理 |
|---|---|---|---|
| 题目 | XX/n.md | 无 | 提取第一段和图片 |
| 原书解答 | XX/n.md | 无 | 提取正式证明 |
| 解题分析 | XX/n_solution.md | 无 | 删除重复题目标题和包围环境 |
| 分步文字 | XX/n/n_steps.md | XX/n/steps.md | 优先使用 n_steps.md |
| 动态演示 | XX/n/n.html | 无 | 复制到 demos/NN.html |
| 知识讲解 | XX/raw_split.md | XX/raw.md | 截取知识精讲 |
| 图片 | XX/images/* | 无 | 保留文件名复制 |

steps.md 是规划稿，主要用于人工审校；n_steps.md 是展示稿，存在时优先使用。二者差异很大时，生成报告列出该题。

## 8. 自动生成规则

不要用简单字符串替换批量生成页面。使用 Python pathlib 按 UTF-8 读取文件，并按 Markdown 标题、图片标记和数学块解析。

build_content.py 的处理顺序：

1. 读取 chapters.yml，只处理七个指定章节；
2. 遍历章节根目录下的数字文件 n.md；
3. 检查 n_solution.md、n/n_steps.md、n/steps.md、n/n.html；
4. 从 n.md 识别题目、正式证明和题末分析请求；
5. 将图片引用改为目标页面的相对路径；
6. 删除 n_solution.md 的重复题目标题；
7. 将 begin{solution} 和 end{solution} 转为普通 Markdown 区块；
8. 生成题目 qmd 和章节索引；
9. 复制图片和演示；
10. 输出缺失文件、未解析标题和公式警告。

解析器不能依赖中文句子。题号、路径和标题层级使用文件名和 Markdown 结构识别。所有读写显式指定 UTF-8。

题目末尾常有“这是一个费解的证明……”之类的分析请求。这是生成提示语，不属于原书解答，应从原书解答区块删除。无法可靠识别时，写入 needs_review.md，不能静默丢弃。

## 9. 数据清单

data/chapters.yml：

~~~yaml
- id: "01"
  number: 1
  title: "全等三角形"
  source: "../01"
- id: "02"
  number: 2
  title: "相似三角形"
  source: "../02"
- id: "03"
  number: 3
  title: "点共线与线共点"
  source: "../03"
- id: "04"
  number: 4
  title: "平移、对称和旋转变换"
  source: "../04"
- id: "06"
  number: 6
  title: "圆的基本性质"
  source: "../06"
- id: "07"
  number: 7
  title: "圆幂与根轴"
  source: "../07"
- id: "08"
  number: 8
  title: "反演与位似"
  source: "../08"
~~~

data/problems.yml 保存人工维护的信息：短标题、标签、难度、主图、核心定理和是否有演示。自动脚本负责文件路径，人工只修改教学元数据。

推荐字段：

~~~yaml
- id: "ch01-p02"
  chapter: "01"
  problem: 2
  title: "直线 KL 过线段 AJ 的中点"
  tags: [全等, 中点, 角平分线]
  difficulty: "提高"
  theorems: [中点定理, 三角形全等]
  demo: true
~~~

题目 ID 使用 ch01-p02 的形式，用于交叉引用、HTML 锚点和未来检索。不要使用中文文件名作为 ID。

## 10. 数学公式兼容

当前资料存在 bigtriangleup、parallel、ang 等历史宏和旧式花括号写法。

处理原则：

1. 保留公式语义，不做大规模人工重写；
2. HTML 和 PDF 分别提供宏定义；
3. KaTeX 不支持的宏由 normalize_math.py 转换；
4. 无法自动转换的公式输出文件和行号警告；
5. 公式不得放入代码块、HTML 属性或普通图片 alt 文本。

assets/macros.tex 至少定义：

~~~tex
\newcommand{\bigtriangleup}{\triangle}
\newcommand{\ang}{\angle}
\newcommand{\parallelogram}{\mathbin{/\!/}}
~~~

HTML 端提供相同的 KaTeX 宏。检查范围包括行内公式、行间公式、矩阵、分式、角度和几何符号。

## 11. 图片处理

规则：

- 保留原文件名；
- 每张图片有有意义的 alt 文本；
- 图注统一使用“图 1-2”格式；
- 页面图片使用相对路径和正斜杠；
- 题目主图通常设置为正文宽度的 78%；
- 动态演示中的 SVG 由 HTML 自己绘制，不另转 PNG；
- 脚本检查每个 Markdown 图片引用是否存在。

示例：

~~~markdown
![三角形中的辅助线构型](../images/8_981_790_477_383_0.jpg){#fig-ch01-p03 width=78%}

图 1-2
~~~

## 12. 动态 HTML 接入

现有演示是完整 HTML 文档，包含自己的 html、CSS、SVG 和 JavaScript。不要把完整 HTML 文档直接嵌套到 Quarto 页面中。

默认使用独立页面链接：

~~~markdown
[打开动态演示](../demos/02.html){.demo-link target="_blank" rel="noopener"}
~~~

确实需要内嵌时使用固定比例 iframe，并提供新窗口链接：

~~~html
<div class="demo-frame">
  <iframe src="../demos/02.html" title="例 2 分步证明演示" loading="lazy"></iframe>
</div>
<p><a href="../demos/02.html" target="_blank" rel="noopener">在新窗口打开</a></p>
~~~

桌面端 iframe 高度不小于 720px，移动端使用 aspect-ratio: 4 / 3。

现有 HTML 使用 KaTeX CDN。发布前二选一：

- 在线部署：保留 CDN，并在 README 说明需要网络；
- 离线部署：下载 KaTeX CSS、字体和脚本到 assets/vendor/katex/，批量替换 HTML 引用。

演示 URL 中不能出现当前机器的绝对路径。

## 13. HTML 样式

assets/book.scss 采用简洁教材风格，不复制演示页面的大面积渐变和卡片布局。

规范：

- 正文最大宽度 880px；
- 正文行高约 1.8；
- 中文正文优先使用 Noto Serif CJK SC，导航使用 Noto Sans CJK SC；
- 标题用深蓝灰，强调色使用青绿或橙色；
- 题目、证明、分析使用细边框 callout，不做多层嵌套卡片；
- 题目页顶部显示题号、章节、难度和标签；
- 章节侧栏显示章节和题目导航；
- 移动端侧栏折叠，图片和公式不得溢出；
- 交互演示按钮使用统一的 demo-link 样式；
- 链接和焦点状态需要足够的颜色对比度。

推荐区块：

~~~markdown
::: {.callout-note title="解题思路"}
这里放 n_solution.md 的分析内容。
:::

::: {.callout-tip title="关键观察"}
这里放辅助线、定理或构造动机的提炼。
:::
~~~

不要把整道题包成一个大卡片，也不要把证明放在深色背景上。

## 14. PDF 排版

PDF 是打印和归档版本，按题目、原书解答、解题分析、分步证明连续显示。HTML 标签页或折叠组件不能成为 PDF 中唯一的内容入口。

要求：

- ctexbook、XeLaTeX、A4、边距约 20mm；
- 章节从新页开始；
- 题目标题使用“例 N”，不重复文件名；
- 图片不超过正文宽度；
- 证明标题不能单独留在页底；
- 公式和图注不与上一段重叠；
- 脚本和动态 HTML不进入 PDF 正文，只保留演示链接；
- 黑白打印时不能只依赖颜色区分对象。

## 15. 验证脚本

validate_content.py 在构建前和构建后都运行。

构建前检查：

- 七个章节目录存在，05 不参与处理；
- 每题有 n.md；
- n_solution.md、n_steps.md 或 steps.md 的存在情况；
- 所有图片引用存在；
- 所有演示文件存在；
- 题目 ID 不重复；
- 图片路径使用正斜杠；
- 文件能以 UTF-8 解码。

构建后检查：

- quarto render 成功；
- 目录和搜索可用；
- 题目页面均能访问；
- 演示链接均指向本地文件；
- 页面没有 file:///、C:\ 或 D:\ 绝对路径；
- 没有未解析的 shortcode、div 标记或公式分隔符；
- 浏览器控制台没有阻塞性 JavaScript 错误；
- PDF 中中文、公式、图注和页码正常。

验证报告至少输出：

~~~text
chapters: 7
problems: 56
solution_files: 56
step_files: 112
demos: 56
missing_images: 0
missing_demos: 0
unresolved_math: 0
~~~

## 16. 实施阶段

### 阶段 A：最小样板

只处理 01/2，完成项目配置、章节首页、题目页、图片、公式和动态演示。先验证 HTML 和 PDF。

完成标准：正文完整、图片正确、演示可打开、中文和公式无乱码、移动端无横向滚动。

### 阶段 B：自动生成器

编写 build_content.py 和 validate_content.py，先生成 01 的全部题目，再扩展到其他章节。

完成标准：重复运行不产生重复内容；修改源文件可重新生成页面；缺失文件会报告，不生成静默空页。

### 阶段 C：批量导入七章

处理 01、02、03、04、06、07、08，复制图片和 HTML，生成章节索引和题目索引。

完成标准：56 道题全部进入导航；05 不出现在导航和输出目录；每道题 ID 唯一。

### 阶段 D：统一数学和排版

处理历史 LaTeX 宏、证明环境、图注、字体和 PDF 分页。不改变证明内容，只修正语法和展示层。

### 阶段 E：最终验收

检查桌面端、移动端、离线 HTML 和 PDF。发布时上传 quarto-book/_site 和 PDF，不上传临时报告或源材料，除非另有归档要求。

## 17. 验收标准

实现完成后必须满足：

1. quarto render 成功完成 HTML 构建；
2. XeLaTeX 生成中文 PDF，或明确记录 PDF 环境未安装；
3. 目录只包含七个已有章节；
4. 56 道题均有独立页面；
5. 每页包含题目、原书解答、解题分析和动态演示入口；
6. 现有动态 HTML 的几何逻辑未被改写；
7. 图片、公式和中文无明显乱码；
8. 没有失效的图片、题目或演示链接；
9. 页面在 375px 宽度下可阅读；
10. 项目中没有当前电脑绝对路径；
11. 生成报告列出所有跳过或需人工复核的文件；
12. 重新运行生成脚本不会修改源目录原始材料。

## 18. 常见问题

**终端中文乱码。** 先确认读取命令使用 UTF-8，不要因为 PowerShell 默认编码错误而修改源文件。

**公式不显示。** 记录文件和行号，再将历史宏转换为标准宏，不要直接删除公式。

**图片丢失。** 检查路径是否相对于生成后的 qmd，并确认使用正斜杠。

**iframe 尺寸异常。** 优先改为新窗口打开；必须内嵌时设置最小高度和 aspect-ratio。

**PDF callout 不理想。** 保留正文，改用普通标题和边框环境，不为复刻 HTML 视觉效果牺牲打印可读性。

**源文件重复题目。** n.md 是原书题目来源，n_solution.md 是分析来源，n_steps.md 是分步文字来源；raw.md 只用于知识讲解和人工比对。

