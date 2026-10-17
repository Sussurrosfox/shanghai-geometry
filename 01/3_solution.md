## 题目 (3.md)

例 2 在 $\bigtriangleup {ABC}$ 中， $\angle C < \angle A < {90}^{ \circ  }$ ， $D$ 为边 ${AC}$ 上一点，使得 ${BD} = {BA}$ . $\bigtriangleup  {ABC}$ 的内切圆分别与边 ${AB}$ ， ${AC}$ 切于点 $K$ ， $L$ . 设 $J$ 为 $\bigtriangleup  {BCD}$ 的内心. 证明:直线 ${KL}$ 过线段 ${AJ}$ 的中点.

![8_981_790_477_383_0.jpg](images/8_981_790_477_383_0.jpg)

图 1-2

证明 如图 1-2,过点 $B$ 作 ${BS} \bot  {AC}$ 于点 $S,{BS}$ 与 ${KL}$ 交于点 $H$ . 过 $J$ 作 ${JR} \bot  {AC}$ 于点 $R$ ,连接 ${DJ},{HJ},{LJ},{AH}$ ,则由 ${BD} = {BA}$ ,知

$$
{LR} = {AD} + {DR} - {AL}
$$

$$
= {AD} + \frac{{BD} + {CD} - {BC}}{2} - \frac{{AB} + {AC} - {BC}}{2}
$$

$$
= \frac{1}{2}{AD} = {AS} = {SD}.
$$

所以 ${AL} = {SR},{SL} = {DR}$ .

因为

$$
\angle {CDJ} = \frac{1}{2}\angle {CDB} = \frac{1}{2}\left( {\angle {DAB} + \angle {DBA}}\right)
$$

$$
= \frac{1}{2}\left( {\angle {DAB} + {180}^{ \circ  } - 2\angle {DAB}}\right)  = {90}^{ \circ  } - \frac{1}{2}\angle {DAB} = \angle {ALH},
$$

所以 $\bigtriangleup {LSH} \cong  \bigtriangleup {DRJ}$ ,故 ${SH} = {JR}$ ,结合 ${HS}//{JR}$ 知 ${HSRJ}$ 为矩形,故 ${HJ} = \; {SR} = {AL}$ ,于是四边形 ${ALJH}$ 为平行四边形,从而 ${HL}$ 与 ${AJ}$ 互相平分. 原问题得证.

注:通过条件中的角相等及要证的结论中直线 ${KL}$ 过线段 ${AJ}$ 的中点猜测图中有一个矩形结构，再通过内切圆相关边长表达式即可导出结论.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

教材和竞赛书在书写几何证明时，通常采用**“综合法”（由因导果）**的叙事顺序：一上来先把所有辅助线画好（“过 $B$ 作 $BS \perp AC$ 交 $KL$ 于 $H$”），然后一通计算和全等推导，最后突然变魔术般地得出平行四边形[cite: 1]。这种写法在逻辑上最简短，但完全掩盖了**“分析法”（执果索因）**的探索痕迹。

要看穿这个证明是怎么想出来的，我们可以从**逆向倒推（怎么锁定点 $H$ 的位置）**和**正向破题（条件特征如何自然触发构造）**两个维度，完整还原解题者的真实思考过程：

---

## 一、 逆向倒推：点 $H$ 和辅助线 $BS$ 是怎么被“算”出来的？

假设你刚拿到这道题，目标是证明：**直线 $KL$ 平分线段 $AJ$**[cite: 1]。

### 1. 转化目标：用“平行四边形”处理“中点”
在平面几何中，要证明一条已知直线（$KL$）平分一条线段（$AJ$），最经典的几何模型是什么？
注意到直线上已经有一个非常特殊且固定的点 $L$（内切圆切点，且在底边 $AC$ 上）[cite: 1]。如果直线 $KL$ 真的经过 $AJ$ 的中点 $M$，那么把点 $L$ 关于中点 $M$ 作中心对称，就会在直线 $KL$ 上得到一个对应点 $H$，使得**四边形 $ALJH$ 是一个平行四边形**[cite: 1]！

> **核心追问**：如果四边形 $ALJH$ 真的是平行四边形，那么直线 $KL$ 上的这个点 $H$ 究竟在哪里？它有什么几何特征？

### 2. 将平行四边形投影到底边 $AC$ 上
一旦假设 $ALJH$ 是平行四边形，它立刻需要满足两个条件：
* $HJ \parallel AL$（即 $HJ$ 平行于底边 $AC$）[cite: 1]；
* $HJ = AL$[cite: 1]。

在几何中，处理“平行于底边的线段 $HJ$”最自然的操作，就是**向底边 $AC$ 作垂线（正投影）**：
* 过点 $J$ 作 $JR \perp AC$ 于点 $R$[cite: 1]；
* 过我们假想的点 $H$ 作 $HS \perp AC$ 于点 $S$[cite: 1]。

因为 $HJ \parallel AC$，所以四边形 $HSRJ$ 必然是一个**矩形**[cite: 1]！既然是矩形，底边上的投影长度就必须满足：
$$SR = HJ = AL$$
两边同时减去公共部分 $SL$，立刻得到一个极其关键的定位等式：
$$AS = LR$$

### 3. 切线长公式揭晓点 $S$ 的真实身份
现在我们来算一算 $LR$ 到底有多长。
* $L$ 是 $\triangle ABC$ 内切圆在 $AC$ 上的切点[cite: 1]；
* $J$ 是 $\triangle BCD$ 的内心，而 $JR \perp AC$，说明 **$R$ 恰好就是 $\triangle BCD$ 内切圆在 $CD$ 上的切点**[cite: 1]！

利用烂熟于心的**内切圆切线长公式**，把 $AL$ 和 $DR$ 写出来：
$$AL = \frac{AB + AC - BC}{2}, \quad DR = \frac{BD + CD - BC}{2}$$
题目给出了条件 $BD = BA$[cite: 1]，把两式相减，烦人的 $AB, BD, BC$ 全部抵消了[cite: 1]：
$$AL - DR = \frac{AC - CD}{2} = \frac{AD}{2}$$
而从图上看，线段 $LR$ 的长度正是 $AD + DR - AL$[cite: 1]，代入上式立得：
$$LR = AD - (AL - DR) = AD - \frac{AD}{2} = \frac{1}{2}AD$$

结合刚才倒推出来的 $AS = LR$，我们震惊地发现：
$$AS = \frac{1}{2}AD$$
这说明什么？说明**点 $H$ 在底边 $AC$ 上的投影点 $S$，必然是线段 $AD$ 的中点**[cite: 1]！
而已知 $\triangle ABD$ 是等腰三角形（$BA = BD$）[cite: 1]，过底边 $AD$ 的中点 $S$ 作 $AC$ 的垂线，这条垂线不就是等腰 $\triangle ABD$ 底边上的高 $BS$ 吗[cite: 1]？！

**破案了！** 解题者根本不是灵机一动“过 $B$ 作 $BS \perp AC$ 交 $KL$ 于 $H$”，而是先在草稿纸上假定平行四边形 $ALJH$ 存在，把 $H$ 投影到 $AC$ 上算出了 $AS = \frac{1}{2}AD$，这才顺藤摸瓜发现点 $H$ 必定落在等腰 $\triangle ABD$ 的高线 $BS$ 上！

---

## 二、 正向破题：题目条件中的“两大巧合”是如何给出暗示的？

即便不先从平行四边形倒推，一个有经验的解题者在正向审题时，也会被题目中两个强烈的信号推着走完全程：

### 1. 信号一：等腰条件 $BD = BA$ 与两个内切圆的“代数消元”
题目中同时出现了 $\triangle ABC$ 的内切圆切点 $L$ 和 $\triangle BCD$ 的内心 $J$，且两者的底边都在同一条直线 $AC$ 上[cite: 1]。
* 看到内心 $J$，第一反应就是向底边作垂线 $JR \perp AC$ 找到切点 $R$[cite: 1]。
* 写出两个切线长 $AL = \frac{AB+AC-BC}{2}$ 和 $DR = \frac{BD+CD-BC}{2}$，看到条件 $BD = BA$，几乎会本能地将两式联立消元[cite: 1]。
* 一旦算出 $AL - DR = \frac{1}{2}AD$，而等腰 $\triangle ABD$ 的三线合一垂足 $S$ 恰好提供了 $\frac{1}{2}AD = AS = SD$，把 $AS$ 代进去立刻得到[cite: 1]：
  $$AL - AS = DR \implies SL = DR$$
  也就是说，在底边 $AC$ 上，天然存在着两条相等的短线段 $SL = DR$（以及两段相等的长线段 $AL = SR$）[cite: 1]。

### 2. 信号二：隐藏的等角 $90^\circ - \frac{1}{2}\angle A$
在底边 $AC$ 上有了相等线段 $SL = DR$ 后，我们自然会去观察从分点 $L$ 和 $D$ 出发的两条斜线——$LK$ 与 $DJ$ 与底边 $AC$ 的夹角：
* **在点 $L$ 处**：因为 $AK, AL$ 是内切圆切线，所以 $AK = AL$，等腰 $\triangle AKL$ 的底角为：
  $$\angle ALH = 90^\circ - \frac{1}{2}\angle A$$
* **在点 $D$ 处**：因为 $BA = BD$，在等腰 $\triangle ABD$ 中，$\angle ADB = 90^\circ - \frac{1}{2}\angle A$，从而其邻补角 $\angle BDC = 90^\circ + \frac{1}{2}\angle A$？不对，注意算式：
  $$\angle BDC = \angle A + \angle ABD = \angle A + (180^\circ - 2\angle A) = 180^\circ - \angle A$$
  因为 $J$ 是 $\triangle BCD$ 的内心，$DJ$ 平分 $\angle BDC$[cite: 1]，所以：
  $$\angle CDR \text{ 处的 }\angle JDR = \frac{1}{2}\angle BDC = 90^\circ - \frac{1}{2}\angle A$$

**奇迹出现了**：
1. 在点 $D$ 右侧，有一个直角三角形 $\text{Rt}\triangle DRJ$，它的水平直角边是 $DR$，斜边 $DJ$ 与底边夹角为 $90^\circ - \frac{1}{2}\angle A$[cite: 1]；
2. 在点 $L$ 左侧，有一段长度完全相等的水平线段 $SL$（$SL = DR$），且从 $L$ 出发的直线 $LH$ 与底边夹角**也是** $90^\circ - \frac{1}{2}\angle A$[cite: 1]！

既然底边相等（$SL = DR$）、夹角相等（$\angle SLH = \angle RDJ$），在 $R$ 点有一条垂线 $JR \perp AC$ 构成了 $\text{Rt}\triangle DRJ$，那么在 $S$ 点**依样画葫芦作一条垂线 $SH \perp AC$ 去截 $KL$ 于点 $H$**，构造出全等的 $\text{Rt}\triangle LSH \cong \text{Rt}\triangle DRJ$，就是极其顺理成章的对称操作了[cite: 1]。

---

## 三、 思维路径与教材书写的对比

把整个过程串联起来，就能看清“探索顺序”与“书写顺序”刚好是完全相反的：

| 阶段 | 解题者的真实探索顺序（分析法） | 教材呈现的证明顺序（综合法） |
| :--- | :--- | :--- |
| **第一步** | 要证 $KL$ 平分 $AJ$ $\implies$ 猜想在 $KL$ 上找点 $H$ 使 $ALJH$ 为平行四边形[cite: 1]。 | 直接作 $BS \perp AC$ 交 $KL$ 于 $H$，作 $JR \perp AC$ 于 $R$[cite: 1]。 |
| **第二步** | 将 $HJ \parallel AC, HJ = AL$ 投影到 $AC$ 上 $\implies$ 需要矩形 $HSRJ$，且 $AS = LR$[cite: 1]。 | 用切线长公式计算 $LR = \frac{1}{2}AD = AS = SD$，得出 $AL = SR, SL = DR$[cite: 1]。 |
| **第三步** | 用切线长公式算出 $LR = \frac{1}{2}AD$ $\implies$ 发现 $S$ 就是 $AD$ 中点（即 $BS \perp AC$ 的垂足）[cite: 1]。 | 导角证明 $\angle CDJ = 90^\circ - \frac{1}{2}\angle A = \angle ALH$[cite: 1]。 |
| **第四步** | 检验 $SH$ 是否等于 $JR$ $\implies$ 通过 $\angle ALH = \angle CDJ$ 发现 $\triangle LSH \cong \triangle DRJ$，逻辑闭环[cite: 1]！ | 证出 $\triangle LSH \cong \triangle DRJ \implies HSRJ$ 为矩形 $\implies ALJH$ 为平行四边形，得证[cite: 1]。 |

掌握了**“遇到切点算切线长消元”**和**“遇到平分线段构造平行四边形向底边投影”**这两个基本功，这类看似神来之笔的几何构造就会变成有迹可循的常规推演。

\end{solution}