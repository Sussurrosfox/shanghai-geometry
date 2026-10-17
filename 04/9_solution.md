## 题目 (9.md)

例 8 直角 $\bigtriangleup {ABC}$ 中， $\angle C = {90}^{ \circ  }$ ， ${CD}$ 为 ${AB}$ 上的高，记 $\bigtriangleup  {ACD}$ 及 $\bigtriangleup {BCD}$ 的内心分别为 ${I}_1,{I}_2$ ，直线 ${I}_1{I}_2$ 与 ${CA},{CB}$ 分别交于点 $M, N$ .

证明: ${S}_{\bigtriangleup {ABC}} \geq  2{S}_{\bigtriangleup {CMN}}$ .

证明 如图 4-9，由 Rt $\bigtriangleup  {DAC} \backsim$ Rt $\bigtriangleup  {DCB}$ ， 知 $\bigtriangleup  {DAC}$ 可由 $\bigtriangleup  {DBC}$ 绕 $D$ 逆时针旋转 ${90}^{ \circ  }$ 再通过伸缩得到，即 $\frac{{I}_{2}D}{{I}_{1}D} = \frac{BD}{CD}$ . 又 $\angle {I}_{2}D{I}_1 = \angle {BDC} = \; {90}^{ \circ  }$ ，所以 $\bigtriangleup  {DCB} \backsim   \bigtriangleup  D{I}_1{I}_2$ ，于是 $\bigtriangleup  D{I}_1{I}_2$ 可由 $\bigtriangleup  {DCB}$ 绕 $D$ 逆时针旋转 ${45}^{ \circ  }$ 再伸缩得到，从而 ${CB}$ 与 ${I}_1{I}_2$ 之间的夹角为 ${45}^{ \circ  }$ ，故 ${CM} = {CN}$ . 而 $\angle {I}_2{CD} = \angle {I}_2{CN}$ ， $\angle {CD}{I}_2 = \; \angle {CN}{I}_2 = {45}^{ \circ  }$ ，因此 $\bigtriangleup {I}_2{CD} \cong  \bigtriangleup {I}_2{CN}$ ，于是 ${CD} = {CN}$ ，所以 ${CM} = {CN} = {CD}$ . 于是

$$
\frac{{S}_{\bigtriangleup {ABC}}}{{S}_{\bigtriangleup {CMN}}} = \frac{{AB} \cdot  {CD}}{{CM} \cdot  {CN}} = \frac{AB}{CD} \geq  2.
$$

![35_976_1610_440_256_0.jpg](images/35_976_1610_440_256_0.jpg)

图 4-9

注:在得到 ${CM} = {CN}$ 后，利用角平分线得到全等，推出 ${CM} = {CD} = {CN}$ ，再由面积公式推出结论.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这个证明看起来确实非常巧妙且具有跳跃性，但如果我们站在“逆向思维”和“启发式探索”的角度来看，它的思考路径其实是非常自然且环环相扣的。

我们可以把这个证明的“破案过程”拆解为以下几个关键步骤：

---

### 1. 终极目标的简化：把面积不等式转化为线段关系

拿到题目要求证 $S_{\triangle ABC} \ge 2S_{\triangle CMN}$ 时，直觉上我们需要找到这两个三角形面积之间的直接联系。
* $\triangle ABC$ 和 $\triangle CMN$ 都含有直角 $\angle C = 90^\circ$。
* 它们的面积比可以表示为：
  $$
  \frac{S_{\triangle ABC}}{S_{\triangle CMN}} = \frac{\frac{1}{2} CA \cdot CB}{\frac{1}{2} CM \cdot CN} = \frac{CA \cdot CB}{CM \cdot CN}
  $$
* 另一方面，利用直角三角形的高 $CD$，我们也有 $S_{\triangle ABC} = \frac{1}{2} AB \cdot CD$。题解中将其转化为：
  $$
  \frac{S_{\triangle ABC}}{S_{\triangle CMN}} = \frac{AB \cdot CD}{CM \cdot CN}
  $$
* **核心灵感**：如果我们能证明 **$CM = CN = CD$**，那么上式就会完美简化为：
  $$
  \frac{AB \cdot CD}{CD^2} = \frac{AB}{CD}
  $$
* 而在直角三角形中，斜边 $AB$ 和斜边上的高 $CD$ 永远满足 $AB \ge 2CD$（当且仅当 $\triangle ABC$ 为等腰直角三角形时取等号）。因此，只要证出 $CM = CN = CD$，不等式 $S_{\triangle ABC} \ge 2S_{\triangle CMN}$ 就**水到渠成了**。
* 于是，**寻找 $CM = CN = CD$** 成为了整个证明唯一的、最核心的进攻方向。

---

### 2. 寻找突破口：$I_1$ 和 $I_2$ 是什么角色？

既然目标转化为证明 $CM = CN = CD$，我们就必须研究由内心 $I_1, I_2$ 决定的直线 $I_1 I_2$。
* 题目中给出了 $\text{Rt}\triangle DAC \sim \text{Rt}\triangle DCB$。两个相似的直角三角形内部有各自的内心 $I_1$ 和 $I_2$。
* 在相似图形中，对应的特征点（如内心、外心等）也必然满足相同的相似比和旋转关系。
* **几何直觉**：$\triangle DAC$ 和 $\triangle DCB$ 是通过 **90°** 旋转和伸缩得到的，因此它们的内心 $I_1$ 和 $I_2$ 连线，必然也继承了这种几何变换的特征。

---

### 3. 确定直线 $I_1 I_2$ 的方向（发现 $CM = CN$）

通过分析 $I_1, I_2$ 在相似三角形中的位置关系，可以推导出：
* $\triangle D I_1 I_2$ 与 $\triangle DCB$ 之间存在 **45°** 的旋转伸缩关系（因为内角被平分了一半，原本 **90°** 的直角平分后产生了 **45°** 的夹角特征）。
* 由此推断出直线 $I_1 I_2$ 与 $CB$ 的夹角是 **45°**。
* 因为 $\angle C = 90^\circ$，直线 $I_1 I_2$ 与 $CA$、$CB$ 交于 $M$、$N$，在 $\triangle CMN$ 中，有一个角是 **90°**，且有一条边与底边成 **45°**，这说明 $\triangle CMN$ 是一个等腰直角三角形，从而直接得到了 **$CM = CN$**。

---

### 4. 建立最后一步桥梁：证明 $CM = CD$

现在我们有了 $CM = CN$，只差最后一步：证明它们等于高 $CD$。
* 观察图中的 $CD$ 和 $I_2$。由于 $I_2$ 是 $\triangle BCD$ 的内心，因此 $CI_2$ 是角平分线。
* 同时，结合前面得到的夹角关系（$\angle CN I_2 = 45^\circ$ 以及 $\angle CD I_2 = 45^\circ$），可以构造出全等三角形：$\triangle I_2 CD \cong \triangle I_2 CN$。
* 全等的直接推论就是对应边相等：**$CD = CN$**。

---

### 总结：作家的“倒推”视角

这个证明之所以让人觉得精妙，是因为它采用的是**目标导向的降维打击**：
1. **终点倒推**：先意识到若能证出 $CM = CN = CD$，结合斜边与高的基本不等式就能直接收网。
2. **性质调用**：利用内心的角平分线性质和相似三角形的旋转伸缩，锁定直线 $I_1 I_2$ 的走向（45°角），从而解出 $CM = CN$。
3. **构造全等**：利用直角和角平分线性质，通过全等三角形把 $CD$ 和 $CN$ 连结起来。

这就是为什么每一小步单独看都很容易验证，但整体串起来却像魔术一样——因为它的每一步都在为“收网证明 $CM = CN = CD$”这个隐藏的宏大目标服务。

\end{solution}