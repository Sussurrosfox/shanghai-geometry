# 帕斯卡定理（Pascal's Theorem）交互可视化分步规划

## 题目背景与核心结论
**命题**：圆内接六边形的三组对边的交点共线。  
**已知**：六边形 $ABCDEF$ 内接于圆 $\odot O$。  
• 直线 $AB$ 与 $DE$ 交于点 $P$；  
• 直线 $BC$ 与 $EF$ 交于点 $Q$；  
• 直线 $CD$ 与 $FA$ 交于点 $R$。  
**求证**：$P, Q, R$ 三点共线（此线称为帕斯卡线，Pascal Line）。

---

## 几何坐标系参数设计
- 画布视口：`viewBox="0 0 760 640"`
- 圆心：$O(380, 320)$，外接圆半径：$R_0 = 200$
- 圆上 6 顶点分布（SVG 坐标系角度，顺时针）：
  - $E(283^\circ) = (424.99, 125.13)$
  - $C(344^\circ) = (572.25, 264.87)$
  - $F(30^\circ)  = (553.21, 420.00)$
  - $B(109^\circ) = (314.87, 509.11)$
  - $D(163^\circ) = (188.74, 378.47)$
  - $A(208^\circ) = (203.43, 226.15)$
- 对边相交点（严格解析解，三点共线）：
  - $P = AB \cap DE = (241.25, 322.16)$
  - $R = CD \cap FA = (377.45, 322.58)$
  - $Q = BC \cap EF = (511.02, 322.98)$
- 帕斯卡线斜率：$\Delta y / \Delta x \approx 0.003$（近乎水平穿过圆心区域，布局平衡开阔）。

---

## 步骤拆解（共 6 步，Step 0 ~ Step 5）

### Step 0：圆内接六边形 $ABCDEF$ 构型
- **标题**：圆内接六边形 $ABCDEF$ 构型
- **正文**：  
  已知六边形 $ABCDEF$ 内接于圆 $\odot O$。帕斯卡定理（Pascal's Hexagon Theorem）是射影几何与欧几里得几何中最著名的经典定理之一：圆内接六边形的三组对边延长线的交点必在同一直线上。<br>
  我们首先建立六边形的基础构型，观察六个顶点在圆周上的分布。
- **画面图元**：
  - **基础层（drawBase）**：外接圆 $\odot O$，圆心微标记，六边形顶点 $A, B, C, D, E, F$。
  - **动态层（renderStep 0）**：加粗高亮六边形六条边 $AB, BC, CD, DE, EF, FA$，展示完整的多边形骨架。
  - **点标签**：各顶点标签合理外扩偏移，避免与圆弧和边线交叉。

---

### Step 1：三组对边相交确定交点 $P, Q, R$
- **标题**：对边相交得交点 $P, Q, R$
- **正文**：  
  分别延长六边形的三组对边：<br>
  • 直线 $AB$ 与 $DE$ 相交于点 <b style="color:#2563eb;">$P$</b>；<br>
  • 直线 $CD$ 与 $FA$ 相交于点 <b style="color:#7c3aed;">$R$</b>；<br>
  • 直线 $BC$ 与 $EF$ 相交于点 <b style="color:#059669;">$Q$</b>。<br>
  本证明的核心目标，即证明这三个交点 <b style="color:#dc2626;">$P, Q, R$ 共线</b>。
- **画面图元**：
  - 绘制三组相交线段（延长虚线）：
    - 蓝色组：$AB$ 与 $DE$ 延伸交于 $P$
    - 紫色组：$CD$ 与 $FA$ 延伸交于 $R$
    - 绿色组：$BC$ 与 $EF$ 延伸交于 $Q$
  - 动态点亮三个交点 $P, R, Q$ 及其文字标签。

---

### Step 2：视点转换与圆周角等量代换
- **标题**：聚焦 $\triangle ADR$ 与同弧圆周角等量代换
- **正文**：  
  将视点转换至由边延长线交织而成的关键三角形 <b style="color:#2563eb;">$\triangle ADR$</b>，利用同弧所对圆周角相等与平角补角性质建立角量对应：<br>
  • 弧 $BD$ 所对圆周角：$\angle DCB = \angle DAB$；<br>
  • 弧 $BF$ 所对圆周角：$\angle BCF = \angle BAF$；<br>
  • 补角关系（$R$ 在直线 $FA$ 与 $CD$ 上）：$\angle FRP = 180^\circ - \angle ARP$，$\angle PRC = 180^\circ - \angle PRD$；<br>
  • 弧 $CE$ 与弧 $EA$ 所对圆周角：$\angle CFE = \angle RDE$，$\angle EFR = \angle EDA$。
- **画面图元**：
  - 高亮显示 $\triangle ADR$（半透明填充背景）。
  - 绘制辅助虚线弦 $BD, BF, CE, EA$。
  - 用配对彩色角弧标记相等的圆周角对（如 $\angle DCB = \angle DAB$ 标记天蓝色角弧，$\angle CFE = \angle RDE$ 标记紫红色角弧）。

---

### Step 3：对 $\triangle ADR$ 与点 $P$ 应用角元塞瓦定理
- **标题**：$\triangle ADR$ 中三线共点于 $P$ 的正弦关系
- **正文**：  
  在 $\triangle ADR$ 中，连接点 $P$ 与各顶点：<br>
  射线 $PA$ 即直线 $AB$，射线 $PD$ 即直线 $DE$，射线 $PR$ 连结 $P, R$。<br>
  因直线 $PA, PD, PR$ 显然共点于 <b style="color:#2563eb;">$P$</b>，由<b>第一角元形式的塞瓦定理</b>（Trigonometric Ceva's Theorem）：<br>
  $$\frac{\sin \angle DAB}{\sin \angle BAF} \cdot \frac{\sin \angle ARP}{\sin \angle PRD} \cdot \frac{\sin \angle RDE}{\sin \angle EDA} = 1$$
- **画面图元**：
  - 聚焦 $\triangle ADR$，高亮三条塞瓦线 $PA, PD, PR$（加粗蓝色高亮），汇聚于点 $P$。
  - 标出顶点 $A$ 处的分割角 $\angle DAB, \angle BAF$；
  - 标出顶点 $R$ 处的分割角 $\angle ARP, \angle PRD$；
  - 标出顶点 $D$ 处的分割角 $\angle RDE, \angle EDA$。

---

### Step 4：正弦比等量代换转移至 $\triangle RCF$
- **标题**：正弦等比代换转移至 $\triangle RCF$
- **正文**：  
  利用 Step 2 中的同弧圆周角相等与平角补角正弦不变性：<br>
  $$\frac{\sin \angle DCB}{\sin \angle BCF} = \frac{\sin \angle DAB}{\sin \angle BAF},\quad \frac{\sin \angle FRP}{\sin \angle PRC} = \frac{\sin \angle ARP}{\sin \angle PRD},\quad \frac{\sin \angle CFE}{\sin \angle EFR} = \frac{\sin \angle RDE}{\sin \angle EDA}$$<br>
  将上述三组等式与 Step 3 的塞瓦恒等式结合，立即得到对 <b style="color:#ea580c;">$\triangle RCF$</b> 的正弦比乘积关系：<br>
  $$\frac{\sin \angle DCB}{\sin \angle BCF} \cdot \frac{\sin \angle FRP}{\sin \angle PRC} \cdot \frac{\sin \angle CFE}{\sin \angle EFR} = 1$$
- **画面图元**：
  - 视点切换：淡化 $\triangle ADR$，高亮显示目标三角形 $\triangle RCF$（半透明橙色填充）。
  - 显示从 $\triangle RCF$ 三个顶点引出的三条射线：$CB, FE, RP$。
  - 标出对应的六个分割角弧 $\angle DCB, \angle BCF, \angle FRP, \angle PRC, \angle CFE, \angle EFR$。

---

### Step 5：角元塞瓦逆定理导出三点共线
- **标题**：$BC, FE, RP$ 共点于 $Q \implies P, Q, R$ 三点共线
- **正文**：  
  在 $\triangle RCF$ 中，由正弦比乘积恒等于 $1$，根据<b>第一角元形式的塞瓦定理逆定理</b>：<br>
  从三个顶点 $C, F, R$ 分别引出的三条直线 $CB, FE, RP$ 必<b>共点</b>！<br>
  而根据已知，直线 $BC$ 与 $EF$ 本就相交于点 <b style="color:#059669;">$Q$</b>，因此直线 $RP$ 也必须经过点 $Q$！<br>
  这直接导出点 <b style="color:#059669;">$Q$</b> 落在直线 $RP$ 上，即：<br>
  <b style="color:#dc2626; font-size:15px;">$P, Q, R$ 三点共线！</b>（帕斯卡线，Pascal Line）。证毕。
- **画面图元**：
  - 高亮绘制贯穿 $P, R, Q$ 的整条<b>帕斯卡线</b>（大红色高光，加粗发光效果）。
  - 展现三线 $BC, FE, RP$ 精准交汇于点 $Q$。
  - 完整呈现交点 $P, R, Q$ 与共线关系，达成最终视觉闭环。
