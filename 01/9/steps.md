# 莫莱定理（Morley's Trisector Theorem）分步证明

**题目（例 8）**：设 $\bigtriangleup ABC$ 三内角的三等分线两两相交于 $D, E, F$。证明: $\bigtriangleup DEF$ 是正三角形。

---

## 步骤规划

### Step 0: 已知条件与逆向构造思路
- **标题**：已知条件与逆向构造思路
- **正文**：在 $\bigtriangleup ABC$ 中，三内角的三等分线两两相交于 $D, E, F$。直接正向证明 $\bigtriangleup DEF$ 是正三角形较为繁复。我们采用经典倒推构造法（逆向思维）：设 $\angle A=3\alpha, \angle B=3\beta, \angle C=3\gamma$（满足 $\alpha+\beta+\gamma=60^\circ$）。先由底角三等分线出发确定点 $D$ 与辅助点 $G$，逆向构造出正三角形 $\bigtriangleup DEF$，再证明 $A$ 处的两条射线恰为角 $A$ 的三等分线。
- **画面**：
  - 绘制基准三角形 $ABC$；
  - 绘制底角两条三等分线 $BD, CD$，交于点 $D$；
  - 显示点 $A, B, C, D$。

### Step 1: 辅助点 G 与内心性质
- **标题**：辅助点 G 与内心 D 的角平分线
- **正文**：设射线 $BG, BD$ 是 $\angle ABC$ 的三等分线（$\angle GBC=2\beta, \angle DBC=\beta$），$CG, CD$ 是 $\angle ACB$ 的三等分线（$\angle GCB=2\gamma, \angle DCB=\gamma$），两线交于 $G$。在 $\bigtriangleup BCG$ 中，$BD$ 平分 $\angle GBC$，$CD$ 平分 $\angle GCB$，故 **$D$ 恰为 $\bigtriangleup BCG$ 的内心**！因此 $GD$ 是 $\angle BGC$ 的平分线，且：
$$\angle BGC = 180^\circ - (2\beta+2\gamma) = 60^\circ + \frac{2}{3}\angle A$$
故 $\angle BGD = \angle CGD = 30^\circ + \frac{1}{3}\angle A$。
- **画面**：
  - 引出辅助射线 $GB, GC$ 相交于 $G$；
  - 连接对称轴/角平分线 $GD$（虚线）；
  - 高亮 $\bigtriangleup BCG$ 及其内心 $D$；
  - 显示点 $G$。

### Step 2: 逆向构造正三角形 DEF
- **标题**：对称构造正三角形 DEF
- **正文**：以 $GD$ 为对称轴，作 $\angle GDF = \angle GDE = 30^\circ$，射线分别与边 $GB, GC$ 交于点 $F, E$。顺次连接 $D, E, F$。由轴对称及全等 $\bigtriangleup GDF \cong \bigtriangleup GDE$ 可知 $DF = DE$；而顶角 $\angle EDF = \angle GDF + \angle GDE = 60^\circ$。顶角为 $60^\circ$ 的等腰三角形必为正三角形，故 **$\bigtriangleup DEF$ 为正三角形**（$DE = EF = FD$）。
- **画面**：
  - 绘制射线 $DF, DE$ 与线段 $EF$；
  - 填充并高亮正三角形 $\bigtriangleup DEF$；
  - 标注 $\angle GDF = \angle GDE = 30^\circ$ 的角弧；
  - 显示点 $E, F$。

### Step 3: 构造全等三角形转移等长
- **标题**：截取等长并证明两对三角形全等
- **正文**：在 $AB$ 上截取 $BH = BD$，在 $AC$ 上截取 $CK = CD$，连接 $HF, EK$。在 $\bigtriangleup BHF$ 与 $\bigtriangleup BDF$ 中：$BH=BD$，$BF$ 为公共边，夹角 $\angle HBF = \angle DBF = \beta$，由 SAS 判定得 **$\bigtriangleup BHF \cong \bigtriangleup BDF$**。同理，在 $\bigtriangleup CKE$ 与 $\bigtriangleup CDE$ 中由 SAS 得 **$\bigtriangleup CKE \cong \bigtriangleup CDE$**。由此得到关键等长链：
$$FH = FD = FE = DE = EK$$
- **画面**：
  - 在 $AB$ 上标出点 $H$，在 $AC$ 上标出点 $K$；
  - 绘制线段 $HF, EK$；
  - 高亮全等三角形对 $\bigtriangleup BHF \cong \bigtriangleup BDF$ 与 $\bigtriangleup CKE \cong \bigtriangleup CDE$；
  - 在 $FH, FD, FE, DE, EK$ 上显示等长刻度标记。

### Step 4: 角度追索：计算底角 ∠FHE = ∠BAC / 3
- **标题**：角度追索：计算底角 ∠FHE = ∠BAC / 3
- **正文**：在 $\bigtriangleup GDF$ 中，外角 $\angle BFD = \angle FGD + \angle GDF = (30^\circ + \frac{1}{3}\angle A) + 30^\circ = 60^\circ + \frac{1}{3}\angle A$。由全等得 $\angle BFH = \angle BFD$。观察点 $F$ 处的周角：
$$\angle EFH = 360^\circ - 2\angle BFD - \angle DFE = 360^\circ - 2(60^\circ + \frac{1}{3}\angle A) - 60^\circ = 180^\circ - \frac{2}{3}\angle A$$
因为 $FH = FE$，在等腰三角形 $\bigtriangleup FEH$ 中，底角为：
$$\angle FHE = \frac{1}{2}(180^\circ - \angle EFH) = \frac{1}{3}\angle A$$
同理在等腰三角形 $\bigtriangleup EKF$ 中可得 $\angle FKE = \frac{1}{3}\angle A$。
- **画面**：
  - 连接辅助线 $HE$ 与 $FK$；
  - 高亮等腰三角形 $\bigtriangleup FEH$ 与 $\bigtriangleup EKF$；
  - 标出底角 $\angle FHE$ 与 $\angle FKE$ 的角弧（注明 $\frac{1}{3}\angle A$）。

### Step 5: 四点共圆与圆内接等腰梯形
- **标题**：HFEK 为圆内接等腰梯形
- **正文**：在四边形 $HFEK$ 中，$FH = EK$，且底角 $\angle FHE = \angle FKE = \frac{1}{3}\angle A$（点 $H, K$ 在 $FE$ 同侧且对 $FE$ 张角相等），故 **$H, F, E, K$ 四点共圆**，且 $HFEK$ 为**圆内接等腰梯形**。在该外接圆中，相等弦所对的圆周角相等，因此等弦 $HF, FE, EK$ 所对的圆周角均为 $\frac{1}{3}\angle A$。
- **画面**：
  - 绘制四边形 $HFEK$ 的外接圆（虚线圆）；
  - 高亮等腰梯形 $HFEK$；
  - 突出三段等弦 $HF, FE, EK$。

### Step 6: 顶点 A 落在外接圆上，莫莱定理得证
- **标题**：A 落在外接圆上，莫莱定理得证
- **正文**：连续三段等弦 $HF, FE, EK$ 张成的总圆周角为 $\frac{1}{3}\angle A \times 3 = \angle A$。而 $A$ 位于直线 $BH$ 与 $CK$ 的交点处，且 $\angle HAK = \angle BAC = \angle A$。根据圆周角性质，**顶点 $A$ 恰好位于该外接圆上**！由此引出的射线 $AF, AE$ 必然将圆周角三等分，即 $\angle HAF = \angle FAE = \angle EAK = \frac{1}{3}\angle A$。这证明 **$AF, AE$ 恰好是 $\angle BAC$ 的三等分线**！因此，三角形 $ABC$ 三内角三等分线两两相交所得的三个交点正是构造的正三角形的顶点 $D, E, F$。**莫莱定理获证：$\bigtriangleup DEF$ 必为正三角形**。
- **画面**：
  - 顶点 $A$ 与外接圆闭合交会；
  - 高亮角 $A$ 的两条三等分线 $AF, AE$；
  - 全图高亮显示三内角的三等分线交织网络及中心的正三角形 $\bigtriangleup DEF$。
