## 题目 (5.md)

例 4 设 ${A}_1,{B}_1,{C}_1$ 分别是 $\bigtriangleup  {ABC}$ 的边 ${BC},{CA},{AB}$ 上的点， $\bigtriangleup  A{B}_1{C}_1$ ， $\bigtriangleup {A}_{1}B{C}_1$ 和 $\bigtriangleup {A}_1{B}_{1}C$ 的外接圆分别与 $\bigtriangleup {ABC}$ 的外接圆交于另一点 ${A}_2,{B}_2$ , ${C}_2\left( {{A}_2 \neq  A,{B}_2 \neq  B,{C}_2 \neq  C}\right)$ ,点 ${A}_3,{B}_3$ 和 ${C}_3$ 分别是 ${A}_1,{B}_1,{C}_1$ 关于边 ${BC}$ , ${CA},{AB}$ 的中点的对称点. 证明: $\bigtriangleup {A}_2{B}_2{C}_2 \backsim  \bigtriangleup {A}_3{B}_3{C}_3$ .

![16_1145_1681_314_367_0.jpg](images/16_1145_1681_314_367_0.jpg)

图 2-4

证明 如图 2-4,设 $\bigtriangleup {ABC}$ 的外接圆圆心为 $O$ ,连接 ${A}_{2}A,{A}_2{B}_1,{A}_{2}C,{A}_{2}B,{A}_2{C}_1$ . 因为

$$
\angle {C}_1{A}_2{B}_1 = \angle {BAC} = \angle B{A}_{2}C,
$$

$$
\angle {A}_2{B}_1{C}_1 = \angle {A}_{2}A{C}_1 = \angle {A}_2{CB},
$$

所以 $\bigtriangleup {B}_1{A}_2{C}_1 \backsim  \bigtriangleup C{A}_{2}B$ ,于是,

$$
\frac{{B}_1{A}_2}{C{A}_2} = \frac{{A}_2{C}_1}{{A}_{2}B} = \frac{{B}_1{C}_1}{CB}.
$$

①

对四边形 $A{B}_1{C}_1{A}_2$ 和 ${ACB}{A}_2$ ,由托勒密定理,有

$$
A{A}_2 \cdot  {B}_1{C}_1 = {B}_1{A}_2 \cdot  A{C}_1 - {A}_2{C}_1 \cdot  A{B}_1;
$$

$$
A{A}_2 \cdot  {BC} = {A}_{2}C \cdot  {AB} - {A}_{2}B \cdot  {AC}.
$$

结合①，有

$$
\frac{{A}_{2}C}{{A}_{2}B} = \frac{{AC} - A{B}_1}{{AB} - A{C}_1} = \frac{C{B}_1}{B{C}_1} = \frac{A{B}_3}{A{C}_3}.
$$

又 $\angle C{A}_{2}B = \angle {BAC} = \angle {B}_{3}A{C}_3$ ,故 $\bigtriangleup B{A}_{2}C \backsim  \bigtriangleup {C}_{3}A{B}_3$ ,从而 $\angle {A}_2{CB} = \; \angle A{B}_3{C}_3$ . 同理有 $\angle {B}_2{CA} = \angle B{A}_3{C}_3$ .

注意到在圆 $O$ 中, $\angle {A}_{2}O{B}_2 = \angle {A}_2{OB} + \angle {B}_2{OA} - \angle {AOB}$ ,所以

$$
\angle {A}_2{C}_2{B}_2 = \frac{1}{2}\angle {A}_{2}O{B}_2
$$

$$
= \frac{1}{2}\left( {\angle {A}_2{OB} + \angle {B}_2{OA} - \angle {AOB}}\right)
$$

$$
= \angle {A}_2{CB} + \angle {B}_2{CA} - \angle {ACB}
$$

$$
= \angle A{B}_3{C}_3 + \angle B{A}_3{C}_3 + \left( {\angle {BAC} + \angle {ABC} - {180}^{ \circ  }}\right)
$$

$$
= {180}^{ \circ  } - \angle A{C}_3{B}_3 - \angle B{C}_3{A}_3
$$

$$
= \angle {A}_{3}{C}_{3}{B}_{3}\text{ . }
$$

同理有 $\angle {B}_2{A}_2{C}_2 = \angle {B}_3{A}_3{C}_3,\angle {C}_2{B}_2{A}_2 = \angle {C}_3{B}_3{A}_3$ ,所以 $\bigtriangleup {A}_2{B}_2{C}_2 \backsim \; \bigtriangleup {A}_3{B}_3{C}_3$ . 原问题得证.

注:托勒密定理是指:圆内接四边形的两组对边的乘积之和等于两对角线的乘积.

![17_1135_1535_304_310_0.jpg](images/17_1135_1535_304_310_0.jpg)

图 2-5

事实上，如图 2-5，设四边形 ${ABCD}$ 内接于圆 $O$ ，在 ${BD}$ 上取点 $P$ ，使得 $\angle {PAB} = \angle {CAD}$ ，结合 $\angle {ABP} = \angle {ACD}$ ， 知 $\bigtriangleup {ABP} \backsim  \bigtriangleup {ACD}$ ，于是 $\frac{AB}{AC} = \frac{BP}{CD}$ ，即

$$
{AB} \cdot  {CD} = {AC} \cdot  {BP}.
$$

①

又 $\angle {BAC} = \angle {PAD},\angle {ADP} = \angle {ACB}$ ，因此， $\bigtriangleup  {ABC} \backsim \; \bigtriangleup {APD}$ ，于是 $\frac{BC}{AC} = \frac{PD}{AD}$ ，即

$$
{BC} \cdot  {AD} = {AC} \cdot  {PD}.
$$

②

将①、②两式相加，得

$$
{AB} \cdot  {CD} + {BC} \cdot  {AD} = {AC}\left( {{BP} + {PD}}\right)  = {AC} \cdot  {BD}.
$$

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这份证明之所以让人觉得“费解”，主要有两方面原因：
1. **叙述顺序是倒置的**：教材采用的是典型的“综合法”书写（从已知直接推到结论），隐藏了背后**从结论倒推（分析法）**的思维拆解过程。
2. **中间绕了一个大弯（强行使用托勒密定理）**：在证明核心比例式 $\frac{A_2C}{A_2B} = \frac{CB_1}{BC_1}$ 时[cite: 1]，作者为了契合章节主题（见文末专门介绍托勒密定理的“注”），强行用托勒密定理做代数消元，反而掩盖了极其简洁的**旋转位似（密克点）**几何本质。

下面我们把这套证明拆解还原，看看它是如何一步步被“倒推”出来的，以及如何用几何直观瞬间看穿它。

---

### 一、 逆向破局：如何把“全局相似”拆解为“局部相似”？

题目的目标是证明 $\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$[cite: 1]。
面对这个目标，第一反应会觉得棘手：$A_2, B_2, C_2$ 是由三个不同的圆分别生成的，直接去找这两个三角形的整体关系非常困难。因此，**核心策略是以 $\triangle ABC$ 为桥梁，将三个顶点的关系“解耦”（拆成单个顶点的独立问题）**。

#### 第 1 步：拆解圆周角 $\angle A_2C_2B_2$（对应证明的后半段）
要证相似，只需证内角相等，比如 $\angle A_2C_2B_2 = \angle A_3C_3B_3$[cite: 1]。
* **看左边（$\angle A_2C_2B_2$）**：$A_2, B_2, C_2$ 都在 $\triangle ABC$ 的外接圆 $O$ 上[cite: 1]。$\angle A_2C_2B_2$ 对的是弧 $\overset{\frown}{A_2B_2}$。怎样把动点 $A_2, B_2$ 的位置拆开？利用圆上的定点 $A, B, C$，把弧拆成：
  $$\overset{\frown}{A_2B_2} = \overset{\frown}{A_2B} + \overset{\frown}{AB_2} - \overset{\frown}{AB}$$
  转化为圆周角（以 $C$ 为顶点），立刻得到书中那步神来之笔[cite: 1]：
  $$\angle A_2C_2B_2 = \angle A_2CB + \angle B_2CA - \angle ACB$$
  注意看右边：$\angle A_2CB$ **只与 $A_2$ 有关**，$\angle B_2CA$ **只与 $B_2$ 有关**！两个动点被成功分离了。

* **看右边（$\angle A_3C_3B_3$）**：点 $C_3$ 在边 $AB$ 上[cite: 1]，利用平角 $180^\circ$ 和 $\triangle AC_3B_3$、$\triangle BC_3A_3$ 的内角和，同样把角度拆向两侧的 $\triangle AC_3B_3$ 和 $\triangle BC_3A_3$[cite: 1]：
  $$\begin{aligned} \angle A_3C_3B_3 &= 180^\circ - \angle AC_3B_3 - \angle BC_3A_3 \\ &= 180^\circ - (180^\circ - \angle A - \angle AB_3C_3) - (180^\circ - \angle B - \angle BA_3C_3) \\ &= \angle AB_3C_3 + \angle BA_3C_3 + (\angle A + \angle B - 180^\circ) \\ &= \angle AB_3C_3 + \angle BA_3C_3 - \angle ACB \end{aligned}$$

* **对比两端**：
  * $\angle A_2C_2B_2 = \color{blue}{\angle A_2CB} + \color{teal}{\angle B_2CA} - \angle ACB$[cite: 1]
  * $\angle A_3C_3B_3 = \color{blue}{\angle AB_3C_3} + \color{teal}{\angle BA_3C_3} - \angle ACB$[cite: 1]

  看到这里，破局点就彻底清晰了！只要能证明单独关于“$A$ 组点”的等式：
  $$\angle A_2CB = \angle AB_3C_3$$
  那么由轮换对称性，必然也有 $\angle B_2CA = \angle BA_3C_3$，两式一加，全局相似就证完了[cite: 1]！

---

#### 第 2 步：锁定过渡相似三角形 $\triangle BA_2C \sim \triangle C_3AB_3$
接下来，怎么证 $\angle A_2CB = \angle AB_3C_3$[cite: 1]？
观察这两个角所在的三角形：$\triangle BA_2C$ 和 $\triangle C_3AB_3$[cite: 1]。
因为 $A, B, C, A_2$ 四点共圆，我们手里**白送了一个等角**[cite: 1]：
$$\angle BA_2C = \angle BAC = \angle C_3AB_3$$
两个三角形已经有一组内角相等，如果还要让另一组内角 $\angle A_2CB = \angle AB_3C_3$ 相等，**唯一的可能就是这两个三角形相似**（$\triangle BA_2C \sim \triangle C_3AB_3$）[cite: 1]！

既然顶角 $\angle BA_2C = \angle C_3AB_3$ 已经相等，要证它们相似，只需证**夹边成比例**（SAS）[cite: 1]：
$$\frac{A_2C}{A_2B} = \frac{AB_3}{AC_3}$$
而根据题设，$B_3, C_3$ 分别是 $B_1, C_1$ 关于边 $AC, AB$ 中点的对称点，所以 $AB_3 = CB_1$，$AC_3 = BC_1$[cite: 1]。于是问题最终归结为证明[cite: 1]：
$$\frac{A_2C}{A_2B} = \frac{CB_1}{BC_1}$$

---

### 二、 局部攻坚：作者是如何想到用托勒密定理的？

现在只剩最后一个问题：已知圆 $(AB_1C_1)$ 与圆 $(ABC)$ 交于 $A, A_2$，如何证明 $\frac{A_2C}{A_2B} = \frac{CB_1}{BC_1}$[cite: 1]？

#### 1. 作者的思路（代数消元视角）
作者看到 $CB_1$ 和 $BC_1$，将它们看作了**线段的差**[cite: 1]：
$$CB_1 = AC - AB_1, \quad BC_1 = AB - AC_1$$
* 其中 $AC, AB$ 是大圆内接四边形 $ACBA_2$ 的边[cite: 1]；
* $AB_1, AC_1$ 是小圆内接四边形 $AB_1C_1A_2$ 的边[cite: 1]；
* 两个圆有一条公共弦 $AA_2$[cite: 1]。

为了把 $(AC, AB)$ 和 $(AB_1, AC_1)$ 联系起来并做差，作者先通过两组圆周角相等（$\angle C_1A_2B_1 = \angle BAC = \angle BA_2C$，$\angle A_2B_1C_1 = \angle A_2AC_1 = \angle A_2CB$）推出了基础相似 $\triangle B_1A_2C_1 \sim \triangle CA_2B$[cite: 1]，设其相似比为 $k$，即[cite: 1]：
$$\frac{B_1A_2}{CA_2} = \frac{A_2C_1}{A_2B} = \frac{B_1C_1}{CB} = k \quad \text{（即书中①式）}$$
接着，对两个内接四边形分别写托勒密定理（注意图 2-4 中 $A_2$ 在弧 $AB$ 上，对角线分别是 $B_1A_2, AC_1$ 和 $A_2C, AB$）[cite: 1]：
1. 小四边形：$AA_2 \cdot B_1C_1 = B_1A_2 \cdot AC_1 - A_2C_1 \cdot AB_1$[cite: 1]
2. 大四边形：$AA_2 \cdot BC = A_2C \cdot AB - A_2B \cdot AC$[cite: 1]

书中写“结合①，有……”省略了一步关键的代数消元：将第 1 个式子中的 $B_1C_1, B_1A_2, A_2C_1$ 全部用 $k \cdot CB, k \cdot CA_2, k \cdot A_2B$ 替换：
$$AA_2 \cdot (k \cdot CB) = (k \cdot CA_2) \cdot AC_1 - (k \cdot A_2B) \cdot AB_1$$
两边约去 $k$，得到：
$$AA_2 \cdot BC = A_2C \cdot AC_1 - A_2B \cdot AB_1$$
把这个式子和第 2 个托勒密等式联立（消去左边的 $AA_2 \cdot BC$）：
$$A_2C \cdot AB - A_2B \cdot AC = A_2C \cdot AC_1 - A_2B \cdot AB_1$$
移项合并同类项：
$$A_2C(AB - AC_1) = A_2B(AC - AB_1) \implies \frac{A_2C}{A_2B} = \frac{AC - AB_1}{AB - AC_1} = \frac{CB_1}{BC_1}$$
这就是书中前半部分证明的完整来龙去脉[cite: 1]。

---

#### 2. 几何本质（降维打击）：其实完全不需要托勒密定理！
你觉得前半段证明别扭是非常敏锐的直觉——因为**这里用托勒密定理纯属“杀鸡用牛刀”**（很大可能是为了给托勒密定理凑例题[cite: 1]）。

从几何结构上看，直线 $AB, AC, BC, B_1C_1$ 构成一个完全四边形，点 $A_2$ 就是它的**密克点（Miquel Point，即旋转位似中心）**[cite: 1]。要证 $\frac{A_2C}{A_2B} = \frac{CB_1}{BC_1}$，只需**两行倒角**直接证 **$\triangle A_2BC_1 \sim \triangle A_2CB_1$** 即可：

1. 在大圆 $(ABC)$ 中，同弧 $\overset{\frown}{AA_2}$ 所对的圆周角相等[cite: 1]：
   $$\angle A_2BC_1 = \angle A_2BA = \angle A_2CA = \angle A_2CB_1$$
2. 在小圆 $(AB_1C_1)$ 中，同弧 $\overset{\frown}{AA_2}$ 所对的圆周角相等，故其补角也相等[cite: 1]：
   $$\angle A_2C_1B = 180^\circ - \angle A_2C_1A = 180^\circ - \angle A_2B_1A = \angle A_2B_1C$$

由 AA 相似立得 **$\triangle A_2BC_1 \sim \triangle A_2CB_1$**，直接写出对应边之比：
$$\frac{A_2C}{A_2B} = \frac{CB_1}{BC_1}$$
（注：哪怕从书中的 $\triangle B_1A_2C_1 \sim \triangle CA_2B$ 出发[cite: 1]，利用**旋转位似成对出现**的基本性质，将对应顶点交换位置，也能一步得出 $\triangle A_2BC_1 \sim \triangle A_2CB_1$。）

---

### 三、 思维脉络复盘图

把整道题的思维过程顺过来，其实就是一条非常自然的**分析法链条**：

$$\begin{array}{c}
\text{欲证 }\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3 \iff \angle A_2C_2B_2 = \angle A_3C_3B_3 \\
\Downarrow \text{（利用 }\triangle ABC\text{ 拆角解耦）} \\
\angle A_2CB + \angle B_2CA - \angle C = \angle AB_3C_3 + \angle BA_3C_3 - \angle C \\
\Downarrow \text{（化归为单侧等角）} \\
\text{欲证 }\angle A_2CB = \angle AB_3C_3 \xleftarrow{\text{已有 }\angle BA_2C = \angle C_3AB_3} \text{欲证 }\triangle BA_2C \sim \triangle C_3AB_3 \\
\Downarrow \text{（SAS 转化到夹边比 + 中点对称性质）} \\
\text{欲证 }\frac{A_2C}{A_2B} = \frac{AB_3}{AC_3} = \frac{CB_1}{BC_1} \\
\Downarrow \text{（密克点旋转位似 / 书中改用托勒密定理消元）} \\
\triangle A_2BC_1 \sim \triangle A_2CB_1
\end{array}$$

看清这条“**先拆角解耦 $\to$ 再锁定过渡相似 $\to$ 最后用密克点位似收尾**”的主线后，整道题的构造意图就彻底透明了。

\end{solution}