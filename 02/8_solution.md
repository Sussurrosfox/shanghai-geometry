## 题目 (8.md)

例 7 在一个凸四边形 ${ABCD}$ 内部有一点 $M$ ,满足 ${MA} = {MC},\angle {AMB} = \; \angle {MAD} + \angle {MCD},\angle {CMD} = \angle {MCB} + \angle {MAB}$ . 证明:

$$
{AB} \cdot  {CM} = {BC} \cdot  {MD}.
$$

![19_1042_1630_395_482_0.jpg](images/19_1042_1630_395_482_0.jpg)

图 2-8

证明 如图 2-8,不妨设点 $M$ 在 $\bigtriangleup {ACD}$ 内. 由条件得

$$
\angle {CMD} = \angle {MCB} + \angle {MAB}
$$

$$
= {360}^{ \circ  } - \angle {AMC} - \angle {ABC}.
$$

所以

$$
\angle {ABC} = {360}^{ \circ  } - \angle {AMC} - \angle {CMD} = \angle {AMD}.
$$

同理有 $\angle {ADC} = \angle {BMC}$ .

在射线 ${MD}$ 上取点 ${D}^{\prime }$ ,使得 $\angle {MA}{D}^{\prime } = \angle {ACB}$ ,

结合 $\angle {AM}{D}^{\prime } = \angle {ABC}$ ,知 $\bigtriangleup {AM}{D}^{\prime } \backsim  \bigtriangleup {CBA}$ . 故

$$
\angle {D}^{\prime }{AC} = \angle {D}^{\prime }{AM} + \angle {MAC}
$$

$$
= \angle {ACB} + \angle {MCA}
$$

$$
= \angle {MCB}\text{ . }
$$

又

$$
\frac{{D}^{\prime }A}{AC} = \frac{AM}{CB} = \frac{CM}{CB},
$$

所以 $\bigtriangleup {D}^{\prime }{AC} \backsim  \bigtriangleup {MCB}$ . 于是

$$
\angle A{D}^{\prime }C = \angle {CMB} = \angle {ADC},
$$

即 $D$ 与 ${D}^{\prime }$ 重合,因此 $\bigtriangleup {AMD} \backsim  \bigtriangleup {CBA}$ ,则 $\frac{AM}{CB} = \frac{MD}{AB}$ . 又 ${AM} = {CM}$ . 所以 ${AB}$ . ${CM} = {BC} \cdot  {MD}$ . 原问题得证.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这是一道非常经典且富有启发性的竞赛几何题。表面上看，这个证明仿佛是从魔术师的帽子里凭空变出来的（例如极其巧妙地引入辅助点 $D'$，以及令人拍案叫绝的角度代换），但如果我们从**动机（Motivation）**、**几何变换**以及**复数/三角动机的视角**去剖析，就会发现它背后有一套非常自然的“寻路”逻辑。

下面我为你分步拆解这个证明是如何被“想出来”的：

---

### 第一阶段：目标导向与逆向分析（Goal & Target Analysis）

我们要证明的结论是：
$$AB \cdot CM = BC \cdot MD$$
将其改写成比例式：
$$\frac{AB}{BC} = \frac{MD}{CM} \quad \text{或} \quad \frac{AB}{MD} = \frac{BC}{CM} \quad \text{或交叉相乘：} \frac{AM}{CB} = \frac{MD}{AB} \quad (\text{因为 } MA = MC)$$

这个比例式在暗示我们什么？
1. 它把四边形的“对边”或“交错边”联系在了一起（$AB, BC$ 在 $\triangle ABC$ 中；$MD, MC$ 与点 $M$ 有关）。
2. 要证四条线段的积相等，最标准的几何工具是**相似三角形**。
3. 观察比例式 $\frac{AM}{CB} = \frac{MD}{AB}$，如果能证明 $\triangle AMD \sim \triangle CBA$，那么不仅能直接得到这个比例，还能顺带解决问题。但 $\triangle AMD$ 和 $\triangle CBA$ 一开始能直接相似吗？不一定，我们需要挖掘角度关系。

---

### 第二阶段：挖掘角度条件的几何本质

题目给出了两个看似古怪的角条件：
1. $\angle AMB = \angle MAD + \angle MCD$
2. $\angle CMD = \angle MCB + \angle MAB$

初看这些加法角，很难直观想象。但我们可以利用**三角形内角和**或**周角**将其转化。
在点 $M$ 处，围绕 $M$ 的三个角（或在四边形/三角形内）总和为 $360^\circ$ 或者利用 $\triangle MAB, \triangle MBC, \triangle MCD, \triangle MDA$ 的内角关系。

正如证明的第一步所做的那样：
$$\angle CMD = \angle MCB + \angle MAB$$
而在一个包含 $M$ 的构型中，$\angle AMC + \angle CMD + \dots$ 往往和圆周角或三角形外角有关。通过代数变换：
$$\angle ABC = 360^\circ - \angle AMC - \angle CMD$$
最终精妙地化简出：
$$\angle ABC = \angle AMD \quad \text{和} \quad \> \angle ADC = \angle BMC$$

**这一步的直觉：**
原来的条件给的是“散落”的单角和（如 $\angle MAD + \angle MCD$），通过整体周角的约束，它们转化为**三角形之间对应角的相等关系**。这说明 $\triangle AMD$ 和 $\triangle ABC$ 之间有某种潜在的对应角相等（$\angle AMD = \angle ABC$）。

---

### 第三阶段：核心瓶颈与“辅助点 $D'$”的破局思维

现在我们手头已知：
* $\angle AMD = \angle ABC$
* 我们想证 $\triangle AMD \sim \triangle CBA$

但还差一个条件。两个三角形相似，要么需要夹角边成比例，要么需要另一个对应角相等。目前我们只有一组对应角相等（$\angle AMD = \angle ABC$），还缺条件。

如果直接硬证 $\triangle AMD \sim \triangle CBA$ 卡壳了怎么办？
**数学家（或解题者）的常规套路是：既然目标是证明 $D$ 点使得某个相似成立，不妨“先入为主”地构造一个满足相似的辅助点。**

这就是引入点 $D'$ 的动机：
1. 在射线 $MD$ 上截取一点 $D'$，使得 $\triangle AM{D}' \sim \triangle CBA$ 强行成立。
2. 既然强行让 $\triangle AM{D}' \sim \triangle CBA$，那么我们立刻就能得到两件事：
   * 对应角相等：$\angle A{D}'M = \angle CAB$？或者从边长比例入手：$\frac{A{D}'}{AC} = \frac{AM}{CB}$。
   * 对应边成比例：$\frac{A{D}'}{AC} = \frac{AM}{CB}$。因为已知 $AM = MC$，所以它等于 $\frac{MC}{CB}$。

---

### 第四阶段：连点成线，闭环逻辑

当我们引入了 $D'$ 并利用了 $\triangle AM{D}' \sim \triangle CBA$ 之后，我们需要回过头来看看 $D'$ 和原本的图有什么联系。

1. **构造第二个相似三角形：**
   我们看 $\triangle {D}'AC$ 和 $\triangle MCB$：
   * 边长关系：上面得到了 $\frac{A{D}'}{AC} = \frac{MC}{CB}$，即 $\frac{A{D}'}{MC} = \frac{AC}{CB}$。
   * 夹角关系：通过巧妙的角度追溯：
     $$\angle {D}'AC = \angle {D}'AM + \angle MAC = \angle ACB + \angle MCA = \angle MCB$$
   * **两边成比例且夹角相等！** 这意味着 $\triangle {D}'AC \sim \triangle MCB$。

2. **收网（证明 $D'$ 与 $D$ 重合）：**
   既然 $\triangle {D}'AC \sim \triangle MCB$，那么它们的对应角必须相等：
   $$\angle A{D}'C = \angle CMB$$
   而我们在前面（第二阶段）通过角追溯已经知道 $\angle ADC = \angle CMB$。
   因此：
   $$\angle A{D}'C = \angle ADC$$
   这意味着点 $D'$ 和点 $D$ 必须在以 $AC$ 为弦、且圆周角相等的同一圆弧上（或者通过点的位置关系直接推出 $D'$ 与 $D$ 重合）。

既然 $D'$ 与 $D$ 重合，那么我们一开始为了推导而假设的“强行相似” $\triangle AM{D}' \sim \triangle CBA$ 就是**真实的** $\triangle AMD \sim \triangle CBA$！

由此，结论 $\frac{AM}{CB} = \frac{MD}{AB}$ 顺理成章，结合 $AM = MC$，原题证毕。

---

### 总结：这种证法是怎么“想出来的”？

回顾整个过程，这个证明的思维路径是：
1. **目标驱动**：看到结论是线段乘积相等，立刻锁定**相似三角形**。
2. **条件化简**：把复杂的角条件通过周角/内角和转化，发现 $\angle AMD = \angle ABC$，拿到了相似的“半张入场券”。
3. **动态构造（关键跃迁）**：发现还差一个条件凑不出相似时，采用**“先构造、再证明重合”**的策略（即点 $D'$ 的引入）。这是平面几何中处理“共线/点重合”与“相似”交织时的杀手锏。
4. **桥梁搭建**：利用中间桥梁（三角形 $MCB$ 和 $AC$）把辅助点 $D'$ 和原图中的 $D$ 锁死在同一个几何位置上。

\end{solution}