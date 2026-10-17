## 题目 (3.md)

例 2 锐角 $\bigtriangleup  {ABC}$ 中， ${AB} > {AC}$ ， $M$ 为其外接圆 $O$ 上劣弧 ${BC}$ 的中点， $K$ 为 $A$ 的对径点. 过 $O$ 作 ${AM}$ 的平行线交 ${AB}$ 于 $D$ ，交 ${CA}$ 的延长线于 $E$ . 直线 ${BM}$ 交直线 ${CK}$ 于 $P$ ，直线 ${CM}$ 交直线 ${BK}$ 于 $Q$ . 证明: $\angle {OPB} + \angle {OEB} = \angle {OQC} + \; \angle {ODC}$ .

![15_1032_715_367_499_0.jpg](images/15_1032_715_367_499_0.jpg)

图 2-2

证明 如图 2-2，连接 ${AK},{BO},{CO},{OM}.$ 由 ${OD}//{AM}$ ，知 $\angle {BDO} = \angle {BAM} = \angle {BCM} = \angle {CBP}$ . 注意到 $\angle {DBO} = {90}^{ \circ  } - \angle {ACB} = \angle {BCP}$ ,故 $\bigtriangleup {BOD} \backsim \; \bigtriangleup {CPB}$ ,于是有 $\frac{BD}{CB} = \frac{BO}{CP} = \frac{CO}{CP}$ ,故 $\frac{BD}{CO} = \frac{BC}{CP}$ ,而 $\angle {DBC} = \angle {AKC} = \angle {OCP}$ ,所以 $\bigtriangleup {DBC} \backsim  \bigtriangleup {OCP}$ . 同理,有 $\bigtriangleup {ECB} \backsim  \bigtriangleup {OBQ}$ .

所以

$$
\angle {OPB} - \angle {OQC} = \angle {OMB} + \angle {POM} - \angle {OMC} + \angle {QOM}
$$

$$
= \angle {POM} + \angle {QOM}
$$

$$
= \angle {POM} + \angle {COM} - \angle {BOM} + \angle {QOM}
$$

$$
= \angle {COP} - \angle {BOQ}
$$

$$
= \angle {BDC} - \angle {CEB}
$$

$$
= \angle {BAC} + \angle {ACD} - \angle {CAB} + \angle {ABE}
$$

$$
= \angle {ACD} + \angle {ABE}
$$

$$
= \angle {ACD} + \angle {AED} - \angle {ADE} + \angle {ABE}
$$

$$
= \angle {ODC} - \angle {OEB}\text{ . }
$$

即 $\angle {OPB} + \angle {OEB} = \angle {OQC} + \angle {ODC}$ .

注:通过比例关系导出 $\bigtriangleup  {DBC} \backsim   \bigtriangleup  {OCP}$ 及 $\bigtriangleup  {ECB} \backsim   \bigtriangleup  {OBQ}$ 是本题的关键.

这是一个费解的证明。我能确认每一步的正确性，但我想知道这是怎么想出来的。请为我解释。

---

\begin{solution}

这份证明之所以让人觉得“费解”甚至“像变魔术”，主要有以下两个原因：
1. **前半部分的跳跃**：拿到题目后，为什么要去证 $\triangle DBC \sim \triangle OCP$[cite: 1]？通过半径 $BO = CO$ 把 $\triangle BOD \sim \triangle CPB$ 的比例进行“重组”是怎么想到的[cite: 1]？
2. **后半部分“无中生有”的代数变形**：在角度计算中，解答凭空加减了许多值为 $0$ 的项（如 $\angle OMB - \angle OMC$、$\angle COM - \angle BOM$、$\angle AED - \angle ADE$）[cite: 1]，让人看不出背后的几何动机。

实际上，如果剥开解答为了“写成紧凑的一行连等式”而特意包装的外壳，还原出探索这道题的**真实逆向思维过程**，你会发现每一步都有极其自然的几何动因。

---

### 一、 破题立意：利用“对称共轭性”重组结论

审题时首先观察图形的对称结构（即 $B$ 与 $C$ 互换时的对应关系）[cite: 1]：
* $M$ 是弧 $BC$ 中点，$K$ 是 $A$ 的对径点，这两点关于 $B, C$ 是对称的[cite: 1]。
* 当 $B \leftrightarrow C$ 互换时，点 $D(AB \cap OE)$ 与点 $E(AC \cap OD)$ 互换，点 $P(BM \cap CK)$ 与点 $Q(CM \cap BK)$ 互换[cite: 1]。

待证结论为 $\angle OPB + \angle OEB = \angle OQC + \angle ODC$[cite: 1]。面对这种高度对称的几何恒等式，最自然的想法是将**地位对等的角放在一起比较**：
$$\angle OPB - \angle OQC = \angle ODC - \angle OEB$$
移项后，等式左边 $\angle OPB - \angle OQC$ 完全属于圆下方的 $\{P, Q\}$ 系统，等式右边 $\angle ODC - \angle OEB$ 完全属于三角形上方的 $\{D, E\}$ 系统[cite: 1]。**整道题的核心任务，就变成了寻找连接“上方 $\{D, E\}$”与“下方 $\{P, Q\}$”的桥梁。**

---

### 二、 核心桥梁：$\triangle DBC \sim \triangle OCP$ 是怎么想出来的？

这并非凭空猜测，而是“顺向导角”与“逆向目标分析”碰撞的结果：

1. **第一步：顺向翻译条件，自然撞见第一组相似**
   题目给出了两个极其明显的角度条件：“$OD \parallel AM$（角平分线）”和“$K$ 为对径点”[cite: 1]。只要把它们翻译成角度：
   * 由 $OD \parallel AM$ 及弧 $BC$ 中点 $M$，立刻得到 $\angle BDO = \angle BAM = \angle CBM = \angle CBP$[cite: 1]。
   * 由外心 $O$ 和直径 $AK$，立刻得到 $\angle DBO = 90^\circ - \angle ACB = \angle BCP$[cite: 1]。
   
   不需要任何技巧，顺手导角就会自动推导出 **$\triangle BOD \sim \triangle CPB$**[cite: 1]。

2. **第二步：发现缺口，利用“半径相等”重组相似（关键定式）**
   虽然拿到了 $\triangle BOD \sim \triangle CPB$，但观察我们的目标角 $\angle ODC$ 和 $\angle OPB$[cite: 1]：
   * $\angle ODC$ 是由线段 **$CD$** 构成的，而 $CD$ 不在 $\triangle BOD$ 中（它是 $\triangle DBC$ 的第三边）[cite: 1]；
   * $\angle OPB$ 是由线段 **$OP$** 构成的，而 $OP$ 也不在 $\triangle CPB$ 中（它是 $\triangle OCP$ 的第三边）[cite: 1]。
   
   **“已知相似的三角形里没有我想要的线段 $CD$ 和 $OP$，我需要把相似转移到包含 $CD$ 和 $OP$ 的 $\triangle DBC$ 和 $\triangle OCP$ 上去！”**
   
   在平面几何中，将一组相似转化为另一组相似的经典手法就是**利用等线段替换比例项**。注意到 $\triangle DBC$ 的两边是 $BD, BC$，而 $\triangle OCP$ 的两边是 $CO, CP$[cite: 1]。利用外接圆半径相等（**$BO = CO$**）作为跳板[cite: 1]：
   $$\triangle BOD \sim \triangle CPB \implies \frac{BD}{CB} = \frac{BO}{CP} \xrightarrow{BO = CO} \frac{BD}{CO} = \frac{BC}{CP}$$
   两边比例就位后，只需验证夹角 $\angle DBC$ 与 $\angle OCP$ 是否相等[cite: 1]。由于 $\triangle OCK$ 是等腰三角形（$OC=OK$），$\angle OCP = \angle OKC = \angle AKC = \angle DBC$[cite: 1]，于是 **$\triangle DBC \sim \triangle OCP$**（以及对称的 **$\triangle ECB \sim \triangle OBQ$**）便水到渠成[cite: 1]。

---

### 三、 拆解魔术：后半段的“长串角度加减”到底在算什么？

这是原证明最让人困惑的地方[cite: 1]。既然已经证出了 $\triangle OCP \sim \triangle DBC$ 和 $\triangle OBQ \sim \triangle ECB$，为什么不能直接得出结论[cite: 1]？

因为相似直接给我们的对应角是 **$\angle COP = \angle BDC$** 和 **$\angle BOQ = \angle CEB$**[cite: 1]，而不是题目要求的 $\angle OPB, \angle OQC$ 和 $\angle ODC, \angle OEB$[cite: 1]！
* 在 $\triangle OCP$ 中，内角是 $\angle OPC$（$OP$ 与 $CK$ 的夹角），但题目要的是 **$\angle OPB$（$OP$ 与 $BM$ 的夹角）**[cite: 1]。
* 在 $\triangle DBC$ 中，内角是 $\angle BDC$（$CD$ 与 $AB$ 的夹角），但题目要的是 **$\angle ODC$（$CD$ 与 $DE$ 的夹角）**[cite: 1]。

**原解答那串令人眼花缭乱的等式，本质上只是在做一件事：计算“目标角”与“相似对应角”之间的偏差（Offset），并利用对称性证明左右两边的偏差恰好抵消！**

我们把这串代数变形还原为直观的几何图像，你就能瞬间看懂：

#### 1. 下半部分：利用对称轴 $OM$ 消去偏差（对应原解答第 1～4 行）
我们要把 $\angle OPB - \angle OQC$ 转化为已知的 $\angle COP - \angle BOQ$[cite: 1]。
注意到 $M$ 是弧 $BC$ 中点，所以 **$OM$ 是整个圆下方的对称轴**，等腰 $\triangle OBM \cong \triangle OCM$，这给我们提供了两个天然相等的常量[cite: 1]：
$$\angle OMB = \angle OMC, \qquad \angle BOM = \angle COM$$

现在，以对称轴 $OM$ 为基准，用外角定理把点 $P, Q$ 处的角转化到圆心 $O$ 处[cite: 1]：
* **看点 $P$（$\triangle OPM$ 的外角）**：
  $$\angle OPB = \angle OMB + \angle POM$$
  而我们需要的相似角是 $\angle COP = \angle COM + \angle POM$[cite: 1]。两式都有 $\angle POM$！说明 $\angle OPB$ 与 $\angle COP$ 之间只差了一个固定常量 $(\angle OMB - \angle COM)$[cite: 1]。
* **看点 $Q$（$\triangle OQM$ 的外角）**：
  $$\angle OQC = \angle OMC - \angle QOM$$
  而我们需要的相似角是 $\angle BOQ = \angle BOM - \angle QOM$[cite: 1]。两式都有 $-\angle QOM$！说明 $\angle OQC$ 与 $\angle BOQ$ 之间也只差了一个固定常量 $(\angle OMC - \angle BOM)$[cite: 1]。

由于对称性，这两个固定常量完全相等[cite: 1]！因此两式相减时，$\angle POM$ 和 $\angle QOM$ 组合起来，刚好把常量偏差抵消掉[cite: 1]：
$$\angle OPB - \angle OQC = \angle COP - \angle BOQ$$
> **真相大白**：原解答的前四行并不是凭空凑出了 $-\angle OMC$ 和 $+\angle COM - \angle BOM$[cite: 1]，而是先用外角定理把 $\angle OPB, \angle OQC$ 拆成以 $OM$ 为基准的 $\angle POM + \angle QOM$，然后再把基准线从 $OM$ 换回 $OC$ 和 $OB$（即代入 $\angle POM = \angle COP - \angle COM$ 和 $\angle QOM = \angle BOM - \angle BOQ$）[cite: 1]。

---

#### 2. 上半部分：利用等腰 $\triangle ADE$ 消去偏差（对应原解答第 5～9 行）
接下来，通过相似代换，式子变成了 $\angle BDC - \angle CEB$，我们需要把它变成目标 $\angle ODC - \angle OEB$[cite: 1]。

**其实这里根本不需要像原解答那样绕一大圈！** 
因为 $DE \parallel AM$（$\angle BAC$ 的平分线），所以 $\triangle ADE$ 是一个等腰三角形，天然具有相等的底角[cite: 1]：
$$\angle ADE = \angle AED$$

直接观察图 2-2 中顶点 $D$ 和顶点 $E$ 处的角分拆[cite: 1]：
* **在顶点 $D$ 处**：射线 $DO$ 在 $\angle BDC$ 内部，且 $\angle BDO = \angle ADE$（对顶角）[cite: 1]，因此直接有：
  $$\angle BDC = \angle ODC + \angle BDO = \angle ODC + \angle ADE$$
* **在顶点 $E$ 处**：射线 $EO$（即 $ED$）在 $\angle CEB$ 内部[cite: 1]，因此直接有：
  $$\angle CEB = \angle OEB + \angle AED$$

因为 $\angle ADE = \angle AED$，将上面两式直接相减，**一步就能得出**：
$$\angle BDC - \angle CEB = (\angle ODC + \angle ADE) - (\angle OEB + \angle AED) = \angle ODC - \angle OEB$$

> **为什么原解答写得那么复杂？**
> 原解答的作者没有直接在顶点 $D, E$ 处做角的加减，而是先对 $\triangle ADC$ 和 $\triangle ABE$ 使用外角定理（将 $\angle BDC, \angle CEB$ 展开为 $\angle BAC + \angle ACD$ 等消去 $\angle BAC$），然后再对 $\triangle EDC$ 和 $\triangle EBD$ 逆用外角定理凑回 $\angle ODC$ 和 $\angle OEB$[cite: 1]。这种写法虽然避开了说明“射线 $DO$ 在 $\angle BDC$ 内部”的位置关系，但在视觉上造成了极大的阅读障碍。

---

### 总结：这道题的思维路线图

如果把整道题的思考过程画成一张路线图，它其实非常清晰：

$$\begin{array}{ccccc}
\text{目标：}\angle OPB - \angle OQC & \xleftarrow[\text{外角定理 + 对称性}]{\text{关于对称轴 } OM \text{ 换基准}} & \angle COP - \angle BOQ \\
& & \parallel \text{（核心相似桥梁）} \\
\text{目标：}\angle ODC - \angle OEB & \xleftarrow[\angle ADE = \angle AED]{\text{等腰 }\triangle ADE\text{ 抵消偏差}} & \angle BDC - \angle CEB
\end{array}$$

当你以后再遇到类似“一长串莫名其妙的加零减零”的几何角度证明时，不妨先找出图形中的**对称轴或等腰三角形**——那些看似突兀的代数项，往往只是为了把角度转换到对称基准线上而引入的“脚手架”。

\end{solution}