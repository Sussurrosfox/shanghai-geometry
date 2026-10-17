## 题目 (2.md)

例 1 已知圆 ${O}_1$ 和圆 ${O}_2$ 交于 $P, Q$ 两点,两圆的外公切线分别切圆 ${O}_1$ 和圆 ${O}_2$ 于点 $A, B$ . 点 $A, B$ 与 $Q$ 在点 $P$ 两侧. 过点 $A$ 作 ${AC} \bot  {BP}$ 交 ${O}_1{O}_2$ 于点 $C$ . 证明: $\angle {APC} = {90}^{ \circ  }$ .

![14_992_1387_487_334_0.jpg](images/14_992_1387_487_334_0.jpg)

图 2-1

证明 如图 2-1,连接 ${QP}$ 并延长交 ${AB}$ 于点 $D$ ,连接 ${O}_{1}Q,{AQ}$ ,则 $D{A}^2 = {DP} \cdot  {DQ} = \; D{B}^2$ ,即 $D$ 为线段 ${AB}$ 的中点.

连接 ${O}_{1}A$ ,则由 ${O}_{1}C \bot  {DP},{O}_{1}A \bot  {DB}$ , ${AC} \bot  {BP}$ ,知 $\bigtriangleup {DBP} \backsim  \bigtriangleup {O}_1{AC}$ ,故 $\frac{DP}{DB} = \frac{{O}_{1}C}{{O}_{1}A}$ . 所以

$$
\frac{{O}_{1}C}{{O}_{1}P} = \frac{{O}_{1}C}{{O}_{1}A} = \frac{DP}{DB} = \frac{DP}{DA} = \frac{AP}{AQ},
$$

结合 $\angle {PAQ} = \frac{1}{2}\angle P{O}_{1}Q = \angle P{O}_{1}C$ ,知 $\bigtriangleup P{O}_{1}C \backsim  \bigtriangleup {QAP}$ ,所以 $\angle {O}_1{PC} = \; \angle {AQP}$ ,故

$$
\angle {APC} = \angle {AP}{O}_1 + \angle {O}_1{PC} = \angle {O}_1{AP} + \angle {AQP}
$$

$$
= \angle {O}_1{AP} + \angle {PAD} = \angle {O}_1{AD} = {90}^{ \circ  }.
$$

所以，原问题得证.

注:利用相似联系线段长度和角度，是几何证明的常见手法.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这段证明之所以让人觉得“费解”、像变魔术一样，是因为教材采用了**正向综合法**来书写：它直接把 $\triangle DBP \sim \triangle O_1AC$ 和 $\triangle PO_1C \sim \triangle QAP$ 两个看似毫无征兆的相似三角形抛了出来[cite: 1]。

实际上，解题者在探索这道题时，并不是从头一路顺推到底的，而是采用了**“两头凑（双向奔赴）”**的策略——**从条件往前推一步，从结论往回退两步，最后在中间通过“切割线相似”实现合龙**。

下面我们把这个思维过程完整还原出来：

---

### 第一步：从条件顺推——如何把点 $C$ 的位置“算”出来？

题目中绝大多数条件都是固定的（两圆相交、外公切线），只有一个动点构造条件：**过 $A$ 作 $AC \perp BP$ 交 $O_1O_2$ 于点 $C$**[cite: 1]。解题的第一直觉是：**必须把点 $C$ 在 $O_1O_2$ 上的位置用线段比例刻画出来。**

1. **条件反射作根轴**：在“两圆相交＋外公切线”的经典构图中，延长公共弦 $QP$（根轴）交公切线 $AB$ 于点 $D$，由切割线定理得 $DA^2 = DP \cdot DQ = DB^2$，即 $D$ 平分 $AB$，这是处理该构图的标准起手式[cite: 1]。
2. **识别“三边分别垂直”模型（关键动机）**：点 $C$ 是直线 $O_1O_2$ 与 $AC$ 的交点，要确定 $O_1C$ 的长度，自然聚焦于含 $O_1C$ 的直角或斜三角形 $\triangle O_1AC$[cite: 1]。观察构成 $\triangle O_1AC$ 的三条直线，你会发现它们各自都带有一个垂直条件[cite: 1]：
   * 连心线垂直平分公共弦：$O_1C \perp DP$[cite: 1]；
   * 半径垂直于切线：$O_1A \perp DB$[cite: 1]；
   * 题设给定的构造条件：$AC \perp BP$[cite: 1]。
   
   **平面几何的核心直觉之一：如果一个三角形的三条边分别垂直于另一个三角形的三条边，那么这两个三角形必然相似（本质上是将其中一个旋转 $90^\circ$ 后再放缩）。**
   把 $DP, DB, BP$ 拼在一起，恰好就是 $\triangle DBP$！因此 $\triangle DBP \sim \triangle O_1AC$ 并不是凭空猜出来的，而是将“三个垂直”打包转化的必然结果[cite: 1]。
3. **化简比例定位点 $C$**：由 $\triangle DBP \sim \triangle O_1AC$ 得到 $\frac{O_1C}{O_1A} = \frac{DP}{DB}$[cite: 1]。利用中点性质 $DB = DA$ 以及同圆半径相等 $O_1A = O_1P$，点 $C$ 的位置被彻底锁定为一条极简比例式[cite: 1]：
   $$\frac{O_1C}{O_1P} = \frac{DP}{DA}$$

推到这里，正向推导就卡住了：我们手握 $\frac{O_1C}{O_1P} = \frac{DP}{DA}$，但不知道该怎么跟 $\angle APC = 90^\circ$ 扯上关系。这时就必须切换到**逆向分析（执果索因）**。

---

### 第二步：从结论倒推——怎样才能证出 $\angle APC = 90^\circ$？

现在我们从目标 $\angle APC = 90^\circ$ 往回退，看看它等价于什么[cite: 1]：

1. **利用半径对称性拆角**：
   注意 $A$ 和 $P$ 都在 $\odot O_1$ 上，且在点 $A$ 处本来就有现成的直角 $\angle O_1AD = 90^\circ$[cite: 1]！
   既然 $O_1A = O_1P$，就有等腰底角相等 $\angle O_1PA = \angle O_1AP$[cite: 1]。用半径 $O_1P$ 把待证的 $\angle APC$ 劈成两半[cite: 1]：
   * 已知点 $A$ 处：$\angle O_1AP + \angle PAD = \angle O_1AD = 90^\circ$[cite: 1]；
   * 待证点 $P$ 处：$\angle O_1PA + \angle O_1PC = \angle APC = 90^\circ$[cite: 1]。
   
   消去相等的底角 $\angle O_1PA = \angle O_1AP$，**待证结论 $\angle APC = 90^\circ$ 瞬间等价于一个纯粹的导角目标**[cite: 1]：
   $$\angle O_1PC = \angle PAD$$

2. **用“SAS相似”反推目标三角形**：
   我们要证 $\angle O_1PC = \angle PAD$，而点 $C$ 是通过比例关系 $\frac{O_1C}{O_1P} = \dots$ 定位在射线 $O_1O_2$ 上的[cite: 1]。在纯几何中，**唯一能把“线段比例（$\frac{O_1C}{O_1P}$）”转化为“角度相等（$\angle O_1PC$）”的工具，就是证明包含它们的 $\triangle PO_1C$ 与某个已知三角形 SAS 相似！**
   
   那么，$\triangle PO_1C$ 应该和谁相似？我们盘点一下 $\triangle PO_1C$ 里已经固定的元素[cite: 1]：
   * 已知夹角：$\angle PO_1C = \frac{1}{2}\angle PO_1Q$（垂径定理），而圆心角的一半等于圆周角 $\angle PAQ$[cite: 1]；
   * 待证目标角：$\angle O_1PC = \angle PAD$，由弦切角定理，恰好又有 $\angle PAD = \angle AQP$[cite: 1]！
   
   看！已知角 $\angle PAQ$ 和目标角 $\angle AQP$ 刚好都在同一个三角形 **$\triangle QAP$** 中[cite: 1]！
   这意味着：**要想证 $\angle O_1PC = \angle AQP$，只需证 $\triangle PO_1C \sim \triangle QAP$[cite: 1]；而由于夹角 $\angle PO_1C = \angle PAQ$ 已经相等，只需凑出夹边成比例（SAS）**[cite: 1]：
   $$\frac{O_1C}{O_1P} = \frac{AP}{AQ}$$

---

### 第三步：中间合龙——为什么非要绕道点 $Q$？

现在把第一步（顺推）的终点和第二步（倒推）的起点摆在一起：
* **顺推给我们的筹码**：$\frac{O_1C}{O_1P} = \frac{DP}{DA}$[cite: 1]
* **倒推需要的条件**：$\frac{O_1C}{O_1P} = \frac{AP}{AQ}$[cite: 1]

中间只差一步 $\frac{DP}{DA} = \frac{AP}{AQ}$[cite: 1]！而在切割线基本构图中，$\triangle DAP \sim \triangle DQA$（公共角 $\angle D$，弦切角 $\angle PAD = \angle AQP$）是现成的，天然就有 $\frac{DP}{DA} = \frac{AP}{AQ}$[cite: 1]。至此，整条思维链完美闭环：

$$\text{三边垂直} \implies \triangle DBP \sim \triangle O_1AC \implies \frac{O_1C}{O_1P} = \frac{DP}{DA} \xlongequal{\triangle DAP \sim \triangle DQA} \frac{AP}{AQ} \xlongequal{\angle PO_1C = \angle PAQ} \triangle PO_1C \sim \triangle QAP \implies \angle APC = 90^\circ$$

---

### 更深一层的几何本质：$\triangle QAP$ 其实是“几何版正弦定理”

你可能会追问一个更本质的问题：**既然顺推已经得到了 $\frac{O_1C}{O_1P} = \frac{DP}{DA}$，为什么不能直接让 $\triangle PO_1C$ 和 $\triangle DAP$ 相似，非要绕道点 $Q$ 构造 $\triangle QAP$ 呢？**

* 如果你对比 $\triangle PO_1C$ 和 $\triangle DAP$，虽然它们有两组边成比例 $\frac{O_1C}{O_1P} = \frac{DP}{DA}$，但它们的**夹角不相等**（$\angle PO_1C \neq \angle ADP$），无法直接相似[cite: 1]。
* 如果用**三角法（正弦定理）**，在 $\triangle DAP$ 中直接有 $\frac{DP}{DA} = \frac{\sin\angle PAD}{\sin\angle DPA}$，代入 $\triangle PO_1C$ 就能直接算出角度，根本不需要点 $Q$。
* 但在**纯几何（综合法）**中，我们不能直接写正弦定理。怎样在不用三角函数的情况下，把圆外 $\triangle DAP$ 的边长比 $\frac{DP}{DA}$ 转化成角度信息？答案就是利用子母相似 $\triangle DAP \sim \triangle DQA$，把圆外割线与切线之比 $\frac{DP}{DA}$，“投影”成 $\odot O_1$ 内部的两条弦之比 $\frac{AP}{AQ}$，从而借用圆周角 $\angle PAQ$ 完成角度匹配[cite: 1]。

也就是说，证明中神秘出现的 $\triangle QAP$，本质上是在纯几何语言下充当了**正弦定理的“转换器”**。

如果从三角计算（正弦定理）或者解析/射影的角度切入，这道题其实可以完全避开辅助线 $AQ$ 和二次相似，需要我为你展示一下这种更直接的“无巧思”解法吗？

\end{solution}