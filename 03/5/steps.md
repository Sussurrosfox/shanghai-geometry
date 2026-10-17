# 例 4：双层塞瓦共点定理的对偶转化 分步规划

## 题目描述
设 $D, E, F$ 分别是 $\triangle ABC$ 的边 $BC, CA, AB$ 上的点，$P, Q, R$ 分别是线段 $EF, FD, DE$ 上的点，且 $DP, EQ, FR$ 三线共点。
证明：$AP, BQ, CR$ 三线共点的充要条件是 $AD, BE, CF$ 三线共点。

---

## 分步演示规划（共 6 步）

### Step 0: 题设条件与双层几何构形
- **标题**：✦ 题设条件与几何构形
- **正文**：
  在 $\triangle ABC$ 中，三边上分别有点 $D \in BC, E \in CA, F \in AB$，连成内层三角形 $\triangle DEF$。<br>
  在 $\triangle DEF$ 的三边上分别有点 $P \in EF, Q \in FD, R \in DE$。<br>
  <b>已知条件</b>：内层塞瓦线 $DP, EQ, FR$ 三线共点于点 $Y$。<br>
  <b>求证目标</b>：$AP, BQ, CR$ 三线共点 $\iff AD, BE, CF$ 三线共点。
- **画面**：
  - 基础图形：$\triangle ABC$（深蓝细边，顶点 $A, B, C$）、内层 $\triangle DEF$（绿色细实线，顶点 $D, E, F$）。
  - 内层塞瓦线：$DP, EQ, FR$（绿色虚线/细线），标出交点 $Y$ 与分点 $P, Q, R$。

### Step 1: 顶角剖分与面积/正弦比转化
- **标题**：① 顶角剖分与面积/正弦比分解
- **正文**：
  连接 $AP$。在 $\triangle AEF$ 中，线段 $AP$ 将其分割为 $\triangle AEP$ 与 $\triangle AFP$。<br>
  两三角形共顶点 $A$ 且底边在同一直线 $EF$ 上，其面积比等于底边线段比：<br>
  $$\frac{EP}{PF} = \frac{S_{\triangle AEP}}{S_{\triangle AFP}} = \frac{\frac{1}{2} AE \cdot AP \cdot \sin\angle PAE}{\frac{1}{2} AF \cdot AP \cdot \sin\angle PAF}$$
  由于 $E \in AC, F \in AB$，故 $\angle PAE = \angle PAC$ 且 $\angle PAF = \angle BAP$。<br>
  约去公因式 $\frac{1}{2} AP$，即得：<br>
  <span style="color:#2563eb;font-weight:bold;">$\frac{EP}{PF} = \frac{EA}{AF} \cdot \frac{\sin\angle PAC}{\sin\angle BAP}$</span>
- **画面**：
  - 高亮顶点 $A$、线段 $AP$（蓝色粗实线）。
  - 绘制角弧 $\angle BAP$ 与 $\angle PAC$（分别标记）。
  - 强调底边分点 $P$ 分割线段 $EP$ 与 $PF$。

### Step 2: 轮换对偶与三式联乘
- **标题**：② 轮换对偶与三式联乘
- **正文**：
  同理，对顶点 $B$ 及 $\triangle BFD$ 中的截线 $BQ$、顶点 $C$ 及 $\triangle CDE$ 中的截线 $CR$ 作完全相同的面积比分解：<br>
  $$\frac{FQ}{QD} = \frac{FB}{BD} \cdot \frac{\sin\angle QBA}{\sin\angle CBQ}, \quad \frac{DR}{RE} = \frac{DC}{CE} \cdot \frac{\sin\angle RCB}{\sin\angle ACR}$$
  将这三个比值相乘，并移项整理因子：<br>
  <span style="color:#7c3aed;font-weight:bold;">$\left(\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE}\right) \cdot \left(\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}\right) \cdot \left(\frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB}\right) = 1$</span>
- **画面**：
  - 同时画出线段 $AP, BQ, CR$（紫色实线）。
  - 分别标出三组角弧：$\angle BAP$ 与 $\angle PAC$、$\angle CBQ$ 与 $\angle QBA$、$\angle ACR$ 与 $\angle RCB$。
  - 强调三边分比 $EP/PF, FQ/QD, DR/RE$。

### Step 3: 内层塞瓦定理：内层比消去
- **标题**：③ 内层塞瓦定理与内层比消去
- **正文**：
  回到题设已知条件：在内层 $\triangle DEF$ 中，$DP, EQ, FR$ 三线共点于点 $Y$。<br>
  由塞瓦定理（边比形式），分点比值之积恒为 1：<br>
  <span style="color:#059669;font-weight:bold;">$\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE} = 1$</span><br>
  将其代入联乘式，第一项内层分比直接消去为 1，立得核心守恒等式：<br>
  <span style="color:#dc2626;font-weight:bold;">$\left(\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}\right) \cdot \left(\frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB}\right) = 1$</span>
- **画面**：
  - 高亮内层三线 $DP, EQ, FR$ 与共点 $Y$（绿色高亮）。
  - 突出内层三角形 $\triangle DEF$ 上的塞瓦结构。

### Step 4: 边元塞瓦与角元塞瓦对偶
- **标题**：④ 边元塞瓦与角元塞瓦对偶解析
- **正文**：
  审视守恒等式中的两个关键乘积：<br>
  1. <b>边长比乘积</b>：由经典塞瓦定理，在 $\triangle ABC$ 中：<br>
     $AD, BE, CF$ 三线共点 $\iff \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$<br>
  2. <b>正弦比乘积</b>：由角元塞瓦定理，在 $\triangle ABC$ 中：<br>
     $AP, BQ, CR$ 三线共点 $\iff \frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB} = 1$
- **画面**：
  - 画出外层三线 $AD, BE, CF$（橙色虚线），与外层线 $AP, BQ, CR$（蓝色实线）形成对比。
  - 标出边比分点 $D, E, F$ 与角元分配线。

### Step 5: 充要等价与结论收官
- **标题**：⑤ 充要等价与结论达成
- **正文**：
  因为两因子乘积恒等于 1（互为倒数）：<br>
  $$\left(\prod \frac{BD}{DC}\right) \cdot \left(\prod \frac{\sin\angle BAP}{\sin\angle PAC}\right) = 1$$
  因此，其中一个因子等于 1 当且仅当另一个因子等于 1！<br>
  <b>由此严格证明</b>：<br>
  <span style="color:#2563eb;font-weight:bold;font-size:15px;">$AP, BQ, CR$ 三线共点 $\iff AD, BE, CF$ 三线共点。</span><br>
  图形中 $AD, BE, CF$ 共点于点 $X$，$AP, BQ, CR$ 共点于点 $Z$，$DP, EQ, FR$ 共点于点 $Y$。
- **画面**：
  - 完整呈现三组三线共点：
    - $DP, EQ, FR$ 交于点 $Y$（绿色）；
    - $AD, BE, CF$ 交于点 $X$（橙色）；
    - $AP, BQ, CR$ 交于点 $Z$（蓝色）。
  - 所有点、线关系优雅协调，一目了然。
