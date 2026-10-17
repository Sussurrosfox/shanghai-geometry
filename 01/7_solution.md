## 题目 (7.md)

例 6 在凸六边形 ${ABCDEF}$ 中， ${AB} = {CD} = {EF}$ ， ${BC} = {DE} = {FA}$ . 证明:若 $\angle {FAB} + \angle {ABC} = \angle {FAB} + \angle {EFA} = {240}^{ \circ  }$ ，则 $\angle {FAB} + \angle {CDE} = {240}^{ \circ  }$ .

![10_1026_1806_455_306_0.jpg](images/10_1026_1806_455_306_0.jpg)

图 1-6

证明 如图 1-6,连接 ${AC},{CE},{EA}$ .

由 $\angle {ABC} = \angle {EFA},{AB} = {EF},{BC} = {FA}$ ，知

$$
\bigtriangleup {ABC} \cong  \bigtriangleup {EFA}.
$$

于是

$$
{AC} = {AE},\angle {BAC} = \angle {FEA}.
$$

$$
\angle {EAC} = \angle {FAB} - \angle {FAE} - \angle {BAC}
$$

$$
= \angle {FAB} - \angle {FAE} - \angle {FEA}
$$

$$
= \angle {FAB} - \left( {{180}^{ \circ  } - \angle {EFA}}\right)
$$

$$
= {240}^{ \circ  } - {180}^{ \circ  }
$$

$$
= {60}^{ \circ  }\text{ . }
$$

结合 ${AC} = {AE}$ ,知 $\bigtriangleup {ACE}$ 是正三角形.

由 ${AB} = {CD},{BC} = {DE},{AC} = {CE}$ ,知 $\bigtriangleup {ABC} \cong  \bigtriangleup {CDE}$ ,所以 $\angle {ABC} = \; \angle {CDE}$ .

故

$$
\angle {FAB} + \angle {CDE} = \angle {FAB} + \angle {ABC} = {240}^{ \circ  }.
$$

所以，原问题得证.

注:由题中的边角关系，可通过三角形全等实现条件转化.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

教材上的证明采用了“综合法”（从已知直接推到结论），隐去了中间试探和逆向分析的过程，因此读起来会有“神来之笔”的突兀感。如果顺着**“翻译条件 $\rightarrow$ 寻找辅助线 $\rightarrow$ 逆向搭桥 $\rightarrow$ 还原出题背景”**的思路拆解，每一步其实都是顺理成章的必然选择。

---

### 第一步：剥离伪装，看清真正的条件与目标

题目给出了一个看似复杂的连等式和结论：
* **已知：** $\angle FAB + \angle ABC = 240^\circ$，且 $\angle FAB + \angle EFA = 240^\circ$
* **求证：** $\angle FAB + \angle CDE = 240^\circ$

把这三个式子放在一起对比，你会发现 $\angle FAB$ 像是一个“公共挂件”：
1. **从已知能直接推出什么？** 两个式子都含有 $\angle FAB$ 且和都为 $240^\circ$，两式相减，立刻得到 **$\angle ABC = \angle EFA$**（即 $\angle B = \angle F$）。
2. **要证的目标等价于什么？** 已知 $\angle FAB + \angle ABC = 240^\circ$，要证 $\angle FAB + \angle CDE = 240^\circ$，其实就是要证 **$\angle CDE = \angle ABC$**（即 $\angle D = \angle B$）。

> **思考转折点：** 既然如此，为什么题目不直接说“已知 $\angle B = \angle F$，求证 $\angle D = \angle B$”，非要把 $\angle A$（即 $\angle FAB$）和 $240^\circ$ 扯进来？
> 因为如果只给 $\angle B = \angle F$，六边形是可以变形的，$\angle D$ 未必等于 $\angle B$。这意味着：**$240^\circ$ 这个具体数值是用来“锁死”图形形状的关键条件**，后面一定会在算角度时用到它。

---

### 第二步：为什么必然要连 $AC, CE, EA$？

再看边长条件：$AB = CD = EF$（不妨记长度为 $a$），$BC = DE = FA$（不妨记长度为 $b$）。

观察六边形的六个顶点，你会发现边长是 **$a, b, a, b, a, b$ 交替排列**的[cite: 1]。再结合第一步整理出的三个角 $\angle B, \angle D, \angle F$：
* 顶点 $B$ 的两侧是边 $AB(a)$ 和 $BC(b)$，夹角是 $\angle B$[cite: 1]；
* 顶点 $D$ 的两侧是边 $CD(a)$ 和 $DE(b)$，夹角是 $\angle D$[cite: 1]；
* 顶点 $F$ 的两侧是边 $EF(a)$ 和 $FA(b)$，夹角是 $\angle F$[cite: 1]。

在平面几何中，当你手里有**“两条已知边及其夹角”**（$a, b$ 与夹角）时，最本能的操作就是**把这两条边的端点连起来，构造三角形（利用 $\text{SAS}$ 全等）**。
* 为了打包 $(AB, BC, \angle B)$，必须连接 $AC$，得到 $\triangle ABC$[cite: 1]；
* 为了打包 $(CD, DE, \angle D)$，必须连接 $CE$，得到 $\triangle CDE$[cite: 1]；
* 为了打包 $(EF, FA, \angle F)$，必须连接 $EA$，得到 $\triangle EFA$[cite: 1]。

这就是辅助线“连接 $AC, CE, EA$”的由来——它不是凭空猜出来的，而是为了把分散的边角条件装进三角形里，把六边形问题转化为三角形全等问题[cite: 1]。

---

### 第三步：正向推进与逆向倒推（“正三角形”是怎么想到的？）

辅助线画好后，图形变成了中间一个大三角形 $\triangle ACE$，外围贴着三个小三角形 $\triangle ABC, \triangle CDE, \triangle EFA$[cite: 1]。这时候我们采用**“两头凑”**的策略：

1. **从已知往前推（正向）：**
   在 $\triangle ABC$ 和 $\triangle EFA$ 中，两边分别为 $a, b$，且第一步已经推出了夹角 $\angle B = \angle F$。由 $\text{SAS}$ 立刻得到 $\triangle ABC \cong \triangle EFA$。
   全等能给中间的 $\triangle ACE$ 带来什么？带来两条边相等：**$AC = AE$**（即 $\triangle ACE$ 是等腰三角形）[cite: 1]。

2. **从结论往回推（逆向）：**
   我们的目标是证 $\angle D = \angle B$。放到 $\triangle CDE$ 和 $\triangle ABC$ 中看，它们已经有两条边对应相等了（都是 $a$ 和 $b$）。要让它们的夹角 $\angle D = \angle B$，只需要证明这两个三角形全等（$\text{SSS}$），也就是需要第三边相等：**$CE = AC$**[cite: 1]。

3. **在中间汇合：**
   * 正向推给了我们：$AC = AE$[cite: 1]；
   * 逆向推需要我们证：$AC = CE$[cite: 1]。
   合在一起，就是要证 **$AC = AE = CE$**，即**中间的 $\triangle ACE$ 是正三角形**[cite: 1]！

既然已经知道 $AC = AE$（等腰），要证它是正三角形，只需要证明它的顶角 **$\angle EAC = 60^\circ$**。

4. **用掉还没出场的 $240^\circ$：**
   怎么算 $\angle EAC$？看图可知，在顶点 $A$ 处，大角 $\angle FAB$ 被分成了三个小角[cite: 1]：
   $$\angle EAC = \angle FAB - (\angle FAE + \angle BAC)$$
   利用刚才的 $\triangle ABC \cong \triangle EFA$，把右侧的 $\angle BAC$ 偷梁换柱换成 $\angle FEA$，括号里就变成了 $(\angle FAE + \angle FEA)$——这正好是 $\triangle EFA$ 的两个底角之和[cite: 1]！
   由三角形内角和，$\angle FAE + \angle FEA = 180^\circ - \angle EFA$。代入上式：
   $$\angle EAC = \angle FAB - (180^\circ - \angle EFA) = (\angle FAB + \angle EFA) - 180^\circ$$
   此时，题干中一直没用上的 $\angle FAB + \angle EFA = 240^\circ$ 终于派上用场，算出 $\angle EAC = 240^\circ - 180^\circ = 60^\circ$，整个逻辑链条彻底合拢。

---

### 第四步：上帝视角——命题人是怎么编出这道题的？

如果反过来看命题人的出题过程，你会觉得这道题更加透明：

1. 命题人先在纸上画了一个**正三角形 $\triangle ACE$**（所以天然有 $AC = CE = EA$，且每个内角都是 $60^\circ$）[cite: 1]。
2. 接着，命题人拿来三个**完全全等的普通三角形** $\triangle ABC \cong \triangle CDE \cong \triangle EFA$，按顺时针方向依次贴在正三角形的三条边上，拼成了六边形 $ABCDEF$[cite: 1]。
3. 既然三个小三角形全等，自然有 $AB = CD = EF$，$BC = DE = FA$，以及 $\angle B = \angle D = \angle F$。
4. 这时命题人算了一下 $\angle FAB + \angle B$ 的度数：
   $$\angle FAB + \angle B = (\angle FAE + 60^\circ + \angle BAC) + \angle B$$
   因为 $\angle BAC = \angle FEA$，而 $\angle FAE + \angle FEA + \angle F = 180^\circ$（且 $\angle B = \angle F$），所以：
   $$\angle FAB + \angle B = 60^\circ + 180^\circ = 240^\circ$$
5. 最后，命题人擦掉中间的正三角形连线 $AC, CE, EA$，把其中两个 $240^\circ$ 当作已知条件，让你去证第三个也是 $240^\circ$。

看穿了“正三角形外贴三个全等三角形”的构造背景后，这道题的辅助线和倒角过程是不是就变得非常自然了？如果对其中某一步的转化还有疑问，我们可以继续探讨。

\end{solution}