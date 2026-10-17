## 题目 (5.md)

例 4 设 $D, E, F$ 分别是 $\bigtriangleup {ABC}$ 的边 ${BC},{CA},{AB}$ 上的点, $P, Q, R$ 分别是线段 ${EF},{FD},{DE}$ 上的点,且 ${DP},{EQ},{FR}$ 三线共点. 证明: ${AP},{BQ},{CR}$ 三线共点的充要条件是 ${AD},{BE},{CF}$ 三线共点.

![24_1066_1310_363_370_0.jpg](images/24_1066_1310_363_370_0.jpg)

图 3-4

证明 注意到

$$
\frac{EP}{PF} = \frac{EA}{AF} \cdot  \frac{\sin \angle {PAC}}{\sin \angle {BAP}},
$$

$$
\frac{FQ}{QD} = \frac{FB}{BD} \cdot  \frac{\sin \angle {QBA}}{\sin \angle {CBQ}},
$$

$$
\frac{DR}{RE} = \frac{DC}{CE} \cdot  \frac{\sin \angle {RCB}}{\sin \angle {ACR}}.
$$

三式相乘得

$$
\frac{EP}{PF} \cdot  \frac{FQ}{QD} \cdot  \frac{DR}{RE} \cdot  \frac{BD}{DC} \cdot  \frac{CE}{EA} \cdot  \frac{AF}{FB} \cdot  \frac{\sin \angle {BAP}}{\sin \angle {PAC}} \cdot  \frac{\sin \angle {CBQ}}{\sin \angle {QBA}} \cdot  \frac{\sin \angle {ACR}}{\sin \angle {RCB}} = 1.
$$

另一方面,因 ${DP},{EQ},{FR}$ 三线共点,由塞瓦定理,得

$$
\frac{EP}{PF} \cdot  \frac{FQ}{QD} \cdot  \frac{DR}{RE} = 1,
$$

因此

$$
\frac{BD}{DC} \cdot  \frac{CE}{EA} \cdot  \frac{AF}{FB} \cdot  \frac{\sin \angle {BAP}}{\sin \angle {PAC}} \cdot  \frac{\sin \angle {CBQ}}{\sin \angle {QBA}} \cdot  \frac{\sin \angle {ACR}}{\sin \angle {RCB}} = 1.
$$

于是,因 $D, E, F$ 分别是 $\bigtriangleup {ABC}$ 的边 ${BC},{CA},{AB}$ 上的点, ${AP},{BQ},{CR}$ 分别是过 $\bigtriangleup {ABC}$ 的三个顶点的三条直线,故由塞瓦定理,得

$$
{AP},{BQ},{CR}\text{ 三线共点 }
$$

$$
\Leftrightarrow  \frac{\sin \angle {BAP}}{\sin \angle {PAC}} \cdot  \frac{\sin \angle {CBQ}}{\sin \angle {QBA}} \cdot  \frac{\sin \angle {ACR}}{\sin \angle {RCB}} = 1
$$

$$
\Leftrightarrow  \frac{BD}{DC} \cdot  \frac{CE}{EA} \cdot  \frac{AF}{FB} = 1
$$

$$
\Leftrightarrow  {AD},{BE},{CF}\text{ 三线共点. }
$$

原问题得证.

注:本题只需用塞瓦定理将共点转化好即可.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

数学教材和竞赛解答中最让人头疼的两个字就是**“注意到”**——它把原本顺理成章的**“逆向分析（执果索因）”**擦掉了，只留下倒过来写的**“正向推导（由因导果）”**，让人感觉第一步像变魔术一样凭空冒出来。

如果还原解题者大脑里的真实探索过程，这个证明其实是按以下三步自然“逼”出来的：

---

### 第一步：先把三个“共点”翻译成代数式（为什么要用角元塞瓦？）

题目里一共有三组“三线共点”：一组已知，两组求证等价。看到三线共点，第一反应自然是**塞瓦定理（Ceva's Theorem）**。但怎么选塞瓦定理的形式，大有讲究：

1. **已知条件：$DP, EQ, FR$ 共点**
   因为 $P, Q, R$ 刚好在 $\triangle DEF$ 的三边上[cite: 1]，直接对 $\triangle DEF$ 用**线元塞瓦定理**：
   $$\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE} = 1 \quad \text{——【式 ①】}$$

2. **结论一：$AD, BE, CF$ 共点**
   因为 $D, E, F$ 刚好在 $\triangle ABC$ 的三边上[cite: 1]，直接对 $\triangle ABC$ 用**线元塞瓦定理**：
   $$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1 \quad \text{——【式 ②】}$$

3. **结论二：$AP, BQ, CR$ 共点（关键转折点！）**
   这里遇到了一个麻烦：$P, Q, R$ 是 $\triangle ABC$ 内部的点（在 $\triangle DEF$ 的边上），**并不在 $\triangle ABC$ 的三边上**[cite: 1]。
   * 如果你想硬用普通的“线元塞瓦定理”，就必须延长 $AP, BQ, CR$ 去交 $BC, CA, AB$ 于三个新点 $P', Q', R'$。这会凭空增加三个交点，图形瞬间变成一团乱麻。
   * 怎样在不延长线段、不引入新交点的情况下，直接刻画过顶点的三条射线 $AP, BQ, CR$ 共点？答案只有一个工具——**角元塞瓦定理**！
   
   直接对 $\triangle ABC$ 和射线 $AP, BQ, CR$ 写出角元塞瓦定理：
   $$\frac{\sin \angle BAP}{\sin \angle PAC} \cdot \frac{\sin \angle CBQ}{\sin \angle QBA} \cdot \frac{\sin \angle ACR}{\sin \angle RCB} = 1 \quad \text{——【式 ③】}$$

---

### 第二步：把三个式子摆在一起，“按顶点归类”找桥梁

现在目标非常明确了：已知【式 ①】$=1$，要证【式 ②】$=1 \iff$【式 ③】$=1$。
只要能证明**这三个式子的左边乘起来恒等于 $1$**（或者其中一个等于另外两个的乘积/商），问题就瞬间解决了！

我们把【式 ①】、【式 ②】、【式 ③】里的元素拆开，**把靠近顶点 $A$ 的所有量收集到一起**看看有什么：
* 来自【式 ①】的线段比：$\frac{EP}{PF}$
* 来自【式 ②】的含 $A$ 线段（把分子分母中和 $A$ 有关的提出来）：$\frac{AF}{EA}$
* 来自【式 ③】的顶角 $A$ 的正弦比：$\frac{\sin \angle BAP}{\sin \angle PAC}$

现在看图 3-4 的最上方[cite: 1]：点 $A, E, F, P$ 构成了什么？
它们刚好构成了角落里的小三角形 **$\triangle AEF$**，而 $AP$ 刚好是从顶点 $A$ 引出的一条分角线（截线）[cite: 1]！

---

### 第三步：在角落三角形 $\triangle AEF$ 中写出“分角定理”（面积比）

既然 $\frac{EP}{PF}$、$\frac{EA}{AF}$ 和 $\frac{\sin \angle PAC}{\sin \angle BAP}$ 全都集中在 $\triangle AEF$ 里，它们之间有什么关系？

在 $\triangle AEF$ 中，点 $P$ 在底边 $EF$ 上[cite: 1]，利用最基础的**共高三角形面积比等于底之比**（或者正弦定理 / 张角、分角定理）：
$$\frac{EP}{PF} = \frac{S_{\triangle AEP}}{S_{\triangle AFP}} = \frac{\frac{1}{2} \cdot EA \cdot AP \cdot \sin \angle EAP}{\frac{1}{2} \cdot AF \cdot AP \cdot \sin \angle FAP}$$

消去公因式 $\frac{1}{2} AP$，再注意到点 $E$ 在 $AC$ 上、点 $F$ 在 $AB$ 上（所以 $\angle EAP = \angle PAC$，$\angle FAP = \angle BAP$）[cite: 1]，立刻得到：
$$\frac{EP}{PF} = \frac{EA}{AF} \cdot \frac{\sin \angle PAC}{\sin \angle BAP}$$

这就是解答开头那句看似神来之笔的“注意到”的真实来源！

---

### 宏观视角：这个证明的本质结构是什么？

如果把三个角落三角形 $\triangle AEF$、$\triangle BFD$、$\triangle CDE$ 的面积比公式乘起来，你会发现一个极其优美的恒等结构：

$$\underbrace{\left(\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE}\right)}_{\triangle DEF \text{ 的线元塞瓦乘积}} = \underbrace{\left(\frac{EA}{AF} \cdot \frac{FB}{BD} \cdot \frac{DC}{CE}\right)}_{\triangle ABC \text{ 线元塞瓦乘积的倒数}} \cdot \underbrace{\left(\frac{\sin \angle PAC}{\sin \angle BAP} \cdot \frac{\sin \angle QBA}{\sin \angle CBQ} \cdot \frac{\sin \angle RCB}{\sin \angle ACR}\right)}_{\triangle ABC \text{ 角元塞瓦乘积的倒数}}$$

换句话说，对于任意内接三角形 $\triangle DEF$ 及其边上的点 $P, Q, R$，永远有：
$$\text{【式 ①】} \times \text{【式 ②】} \times \text{【式 ③】} \equiv 1$$

* **几何本质**：线段比 $\frac{EP}{PF}$ 是在内接三角形 $\triangle DEF$ 的边上度量的；当我们从外部顶点 $A$ 发出射线 $AP$ 去观察点 $P$ 时，相当于做了一次**以 $A$ 为中心的中心投影**。中心投影把底边线段比 $\frac{EP}{PF}$ 转化为了张角正弦比 $\frac{\sin \angle PAC}{\sin \angle BAP}$，而比例的修正系数恰好就是两条斜边之比 $\frac{EA}{AF}$。
* **如果不用三角函数（纯面积法视角）**：若设 $AP$ 的延长线交 $BC$ 于 $P'$，那么：
  $$\frac{BP'}{P'C} = \frac{S_{\triangle ABP}}{S_{\triangle ACP}}$$
  而由点 $F$ 在 $AB$ 上、点 $E$ 在 $AC$ 上[cite: 1]，有 $\frac{S_{\triangle ABP}}{S_{\triangle AFP}} = \frac{AB}{AF}$ 以及 $\frac{S_{\triangle ACP}}{S_{\triangle AEP}} = \frac{AC}{AE}$。结合 $\frac{S_{\triangle AEP}}{S_{\triangle AFP}} = \frac{EP}{PF}$，同样能消去三角形面积，直接建立 $P'$ 分 $BC$ 的比与 $P$ 分 $EF$ 的比之间的转换关系。教材选用正弦比（角元塞瓦），只是为了省去设交点 $P', Q', R'$ 的步骤而已。

\end{solution}