# 例 1 分步证明规划与画面设计 (steps.md)

## 题目信息
- **题面**：已知 $O$ 为 $\triangle ABC$ 内一点，满足 $OD \perp BC, OE \perp AC$（点 $D, E$ 分别在边 $BC, AC$ 上），$F$ 为边 $AB$ 的中点。若 $DF = EF$，证明：$\angle OBD = \angle OAE$。
- **核心思想**：中点构造中位线与直角三角形斜边中线定理，通过构造辅助中点 $M, N$ 建立全等三角形 $\triangle FND \cong \triangle EMF$，再结合平行四边形 $FNOM$ 转换顶角，最终利用直角三角形斜边中线等腰外角性质推导出目标角相等。

---

## 步骤规划清单

### Step 0: 已知条件与图形构形
- **标题**：已知条件与图形构形
- **正文**：
  已知 $O$ 为 $\triangle ABC$ 内一点，满足 $OD \perp BC$ 于 $D$，$OE \perp AC$ 于 $E$。<br>
  $F$ 为边 $AB$ 的中点，且 $DF = EF$。<br>
  求证：<b>$\angle OBD = \angle OAE$</b>。
- **画面图元**：
  - 底层基准图形：$\triangle ABC$ 边线（深蓝灰实线）、点 $O$、线段 $OD, OE$。
  - 直角标记：$D$ 处 $OD \perp BC$，$E$ 处 $OE \perp AC$。
  - 中点标记：$F$ 处在中点，在 $AF$ 与 $FB$ 上标注单刻度线表示 $AF = FB$。
  - 已知等长线段：红色实线连接 $DF$ 与 $EF$，并在其上标注双等长刻度线表示 $DF = EF$。
  - 显示所有已知点及标签：$A, B, C, O, D, E, F$。

---

### Step 1: 作辅助线——取中点构造中位线与斜边中线
- **标题**：① 取 $AO, BO$ 中点构造中位线与斜边中线
- **正文**：
  分别取 $AO, BO$ 的中点 <b>$M$</b> 与 <b>$N$</b>。<br>
  连接 $AO, BO$（中点所在线段）。<br>
  连接 <b>$ME, MF, ND, NF$</b>。<br>
  提示：注意到 $F, M, N$ 分别为 $\triangle ABO$ 三边的中点，同时 $N, M$ 又是直角三角形 $\triangle ODB, \triangle OEA$ 斜边的中点！
- **画面图元**：
  - 新增点：$M$（$AO$ 中点）和 $N$（$BO$ 中点）及对应标签。
  - 辅助连线：虚线连接 $AO, BO$；实线/细虚线连接 $ME, MF, ND, NF$。
  - 保留已知条件中的 $DF, EF$（虚线显示）。

---

### Step 2: 第一组等长——中位线与斜边中线等于 $BO$ 的一半
- **标题**：② $FM$ 与 $ND$ 均等于 $\frac{1}{2}BO$
- **正文**：
  在 $\triangle ABO$ 中，$F, M$ 分别为 $AB, AO$ 的中点，故 $FM$ 为中位线，有 <b>$FM = \frac{1}{2}BO$</b>。<br>
  又在 $\text{Rt}\triangle ODB$ 中，$OD \perp BC$，$N$ 为斜边 $BO$ 的中点，由直角三角形斜边中线等于斜边一半可得 <b>$ND = \frac{1}{2}BO$</b>。<br>
  因此，得到第一组关键等长：<b>$FM = ND$</b>。
- **画面图元**：
  - 高亮基准线段：$BO$（蓝色加粗半透明光晕）。
  - 高亮等长线段：$FM$ 与 $ND$（蓝色实线，并标注等长刻度标记）。
  - 在 $\text{Rt}\triangle ODB$ 中标示出直角符号与斜边中线 $ND$。

---

### Step 3: 第二组等长——中位线与斜边中线等于 $AO$ 的一半
- **标题**：③ $FN$ 与 $ME$ 均等于 $\frac{1}{2}AO$
- **正文**：
  同理，在 $\triangle ABO$ 中，$F, N$ 分别为 $AB, BO$ 的中点，故 $FN$ 为中位线，有 <b>$FN = \frac{1}{2}AO$</b>。<br>
  在 $\text{Rt}\triangle OEA$ 中，$OE \perp AC$，$M$ 为斜边 $AO$ 的中点，由直角三角形斜边中线性质得 <b>$ME = \frac{1}{2}AO$</b>。<br>
  因此，得到第二组关键等长：<b>$ME = FN$</b>。
- **画面图元**：
  - 高亮基准线段：$AO$（紫色加粗半透明光晕）。
  - 高亮等长线段：$FN$ 与 $ME$（紫色实线，并标注等长刻度标记）。
  - 在 $\text{Rt}\triangle OEA$ 中标示出直角符号与斜边中线 $ME$。

---

### Step 4: 构造 SSS 全等三角形
- **标题**：④ 构造 SSS 全等：$\triangle FND \cong \triangle EMF$
- **正文**：
  在 $\triangle FND$ 和 $\triangle EMF$ 中：<br>
  $\begin{cases} FN = ME & (\text{由步骤 ③}) \\ ND = FM & (\text{由步骤 ②}) \\ DF = EF & (\text{已知条件}) \end{cases}$<br>
  由 <b>SSS</b> 全等判定定理，得 <b>$\triangle FND \cong \triangle EMF$</b>！<br>
  从而对应角相等：<b>$\angle FND = \angle FME$</b>。
- **画面图元**：
  - 几何填充：$\triangle FND$（半透明浅蓝色填充）与 $\triangle EMF$（半透明浅橙色填充）。
  - 边线强化：三组对应等长边高亮对应颜色。
  - 对应角弧高亮：标出 $\angle FND$ 与 $\angle FME$ 的彩色角弧。

---

### Step 5: 平行四边形对角转换顶角
- **标题**：⑤ 平行四边形 $FNOM$ 转换顶角：$\angle OND = \angle OME$
- **正文**：
  因为 $FM \parallel BO$ 且 $FM = ON = \frac{1}{2}BO$（或 $FN \parallel AO$ 且 $FN = OM$），<br>
  所以四边形 <b>$FNOM$ 是平行四边形</b>。<br>
  由平行四边形对角相等，得 <b>$\angle FNO = \angle FMO$</b>。<br>
  两式相减（角作差）：<br>
  $\angle OND = \angle FND - \angle FNO$<br>
  $\angle OME = \angle FME - \angle FMO$<br>
  因此得出核心角相等关系：<b>$\angle OND = \angle OME$</b>。
- **画面图元**：
  - 勾勒平行四边形 $FNOM$ 边界（加粗青色边框并带有平行箭头标记）。
  - 标明内角 $\angle FNO$ 与 $\angle FMO$ 的角弧（黄色/青色）。
  - 标出作差后得到的顶角 $\angle OND$ 与 $\angle OME$（高亮红色角弧）。

---

### Step 6: 得出最终结论
- **标题**：⑥ 利用斜边中线等腰外角推得 $\angle OBD = \angle OAE$
- **正文**：
  在 $\text{Rt}\triangle ODB$ 中，$N$ 为斜边中点，所以 $NB = ND = NO$。<br>
  在等腰 $\triangle NOB$ 中，$NB = NO$，故其外角 $\angle OND = \angle NBO + \angle NOB = 2\angle OBD$，即 <b>$\angle OBD = \frac{1}{2}\angle OND$</b>。<br>
  同理在 $\text{Rt}\triangle OEA$ 中，$M$ 为斜边中点，$MA = ME = MO$，等腰 $\triangle MOA$ 外角 $\angle OME = 2\angle OAE$，即 <b>$\angle OAE = \frac{1}{2}\angle OME$</b>。<br>
  结合步骤 ⑤ 中已证的 $\angle OND = \angle OME$，立得：<br>
  <b style="color:#2563eb; font-size:15px;">$\angle OBD = \angle OAE$</b>。<br>
  证明完毕！
- **画面图元**：
  - 显示 $\triangle NOB$ 与 $\triangle MOA$ 的外角与内角关系（双倍角弧对比）。
  - 终局高亮：目标角 $\angle OBD$（在顶点 $B$ 处，加粗绿色角弧及标签）与 $\angle OAE$（在顶点 $A$ 处，加粗绿色角弧及标签）。
  - 线段 $BO$ 与 $AO$ 呈金色/主题色高亮，整幅图形和谐收官。
