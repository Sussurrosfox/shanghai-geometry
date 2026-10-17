# 例 3 几何证明可视化分步规划 (03/4/steps.md)

## 题目概述
已知直线上的三个定点依次为 $A, B, C$，$\Gamma$ 为过 $A, C$ 且圆心不在 $AC$ 上的圆。分别作过 $A, C$ 两点且与圆 $\Gamma$ 相切的直线交于点 $P$，线段 $PB$ 与圆 $\Gamma$ 交于点 $Q$。证明：$\angle AQC$ 的平分线与 $AC$ 的交点不依赖于圆 $\Gamma$ 的选取。

---

## 分步规划（共 6 步，Step 0 ~ Step 5）

### Step 0: 基础几何构型与切线交点 $P$
- **标题**：✦ 基础构型：定点 $A, B, C$ 与切线交点 $P$
- **核心推理**：
  在直线 $AC$ 上依次取定点 $A, B, C$。构造过 $A, C$ 的圆 $\Gamma$（圆心不在 $AC$ 上）。过 $A, C$ 作圆 $\Gamma$ 的切线，两切线交于点 $P$。连结线段 $PB$ 交圆 $\Gamma$ 于点 $Q$。连结弦 $QA, QC$。
- **画面图元**：
  - 底层图形：直线 $AC$（包含点 $A, B, C$），圆 $\Gamma$，切线段 $PA, PC$，割线段 $PB$ 及交点 $Q$，弦 $QA, QC$。
  - 颜色标识：圆 $\Gamma$ 为深灰色/蓝色细线；切线 $PA, PC$ 为深色实线；割线 $PB$ 贯穿图形；高亮标出三个定点 $A, B, C$ 与关键交点 $Q$。

### Step 1: 等腰 $\Delta PAC$ 与割线正弦比
- **标题**：① 等腰 $\Delta PAC$ 结合正弦定理
- **核心推理**：
  因为 $PA, PC$ 均切圆 $\Gamma$ 于 $A, C$，由切线长定理知 $PA = PC$，故 $\Delta PAC$ 是等腰三角形。
  在 $\Delta PAB$ 和 $\Delta PCB$ 中分别利用正弦定理：
  $$\frac{AB}{\sin\angle APB} = \frac{PA}{\sin\angle PBA}, \quad \frac{BC}{\sin\angle CPB} = \frac{PC}{\sin\angle PBC}$$
  由于 $A, B, C$ 共线，$\angle PBA + \angle PBC = 180^\circ$，其正弦值相等；且 $PA = PC$，两式相除立即得出：
  $$\frac{AB}{BC} = \frac{\sin\angle APB}{\sin\angle CPB}$$
- **画面图元**：
  - 高亮 $\Delta PAB$ 与 $\Delta PCB$。
  - 标记等长切线段 $PA = PC$（等长刻度线）。
  - 分别用不同颜色角弧标记共顶点角 $\angle APB$ 与 $\angle CPB$。
  - 强调底边线段 $AB$ 与 $BC$。

### Step 2: 角平分线 $QR$、圆周交点 $S$ 与等腰 $\Delta ASC$
- **标题**：② 角平分线 $QS$ 与等腰 $\Delta ASC$
- **核心推理**：
  设 $\angle AQC$ 的平分线交线段 $AC$ 于点 $R$，与圆 $\Gamma$ 再次交于异于 $Q$ 的一点 $S$。
  因为射线 $QS$ 平分 $\angle AQC$，所以圆周角 $\angle AQS = \angle CQS$。
  由同圆中等圆周角对等弧知，弧 $\wideparen{AS} = \wideparen{CS}$，从而弦长 $SA = SC$，$\Delta ASC$ 亦为等腰三角形（点 $S$ 为弧 $AC$ 的中点，且位于 $AC$ 的垂直平分线上）。
  在 $\Delta ASR$ 和 $\Delta CSR$ 中分别应用正弦定理，由 $\angle SRA + \angle SRC = 180^\circ$（正弦相等）及 $SA = SC$，同理可得：
  $$\frac{AR}{RC} = \frac{\sin\angle ASR}{\sin\angle CSR} = \frac{\sin\angle ASQ}{\sin\angle CSQ}$$
- **画面图元**：
  - 绘制角平分线 $QS$（贯穿 $R$ 和 $S$），标出点 $R \in AC$ 与圆周点 $S$。
  - 连结弦 $SA$ 与 $SC$，标出等长刻度线 $SA = SC$。
  - 标注 $\angle AQR = \angle CQR$ 等角弧。
  - 标注 $\angle ASQ$ 与 $\angle CSQ$ 角弧。
  - 高亮底边线段 $AR$ 与 $RC$。

### Step 3: 弦切角定理与等角链构建
- **标题**：③ 弦切角定理与圆周角相等转换
- **核心推理**：
  利用弦切角定理与同弧所对圆周角相等：
  1. 直线 $PA$ 切圆 $\Gamma$ 于 $A$，$AQ$ 为弦，故弦切角 $\angle PAQ = \angle QCA$；又弧 $\wideparen{AS} = \wideparen{CS}$，故圆周角 $\angle ASQ = \angle QCA$。得出等角链：
     $$\angle PAQ = \angle ASQ = \angle QCA$$
  2. 同理，直线 $PC$ 切圆 $\Gamma$ 于 $C$，$CQ$ 为弦，故弦切角 $\angle PCQ = \angle QAC$；又圆周角 $\angle CSQ = \angle QAC$。得出等角链：
     $$\angle PCQ = \angle CSQ = \angle QAC$$
- **画面图元**：
  - 第一组等角：$\angle PAQ$、$\angle ASQ$、$\angle QCA$ 用同色（紫色/蓝色）角弧高亮并连接视觉引导。
  - 第二组等角：$\angle PCQ$、$\angle CSQ$、$\angle QAC$ 用同色（绿色/橙色）角弧高亮。
  - 辅助连线强化弦切角与所夹弧所对圆周角的对应关系。

### Step 4: $\Delta PAC$ 中的角元塞瓦定理与正弦代换
- **标题**：④ 角元塞瓦定理与两式平方转换
- **核心推理**：
  在 $\Delta PAC$ 中，点 $Q$ 是三角形内的一点（三条射线 $PQ$ 即 $PB$、$AQ$、$CQ$ 共点于 $Q$）。
  对 $\Delta PAC$ 与点 $Q$ 应用角元形式的塞瓦定理（Trigonometric Ceva's Theorem）：
  $$\frac{\sin\angle APB}{\sin\angle CPB} \cdot \frac{\sin\angle QAC}{\sin\angle QAP} \cdot \frac{\sin\angle QCP}{\sin\angle QCA} = 1$$
  将角元塞瓦定理移项变形：
  $$\frac{\sin\angle APB}{\sin\angle CPB} = \frac{\sin\angle QAP}{\sin\angle QAC} \cdot \frac{\sin\angle QCA}{\sin\angle QCP}$$
  将 Step 3 得出的等角关系 $\angle PAQ = \angle ASQ = \angle QCA$ 与 $\angle PCQ = \angle CSQ = \angle QAC$ 代入：
  $$\frac{\sin\angle APB}{\sin\angle CPB} = \frac{\sin\angle ASQ}{\sin\angle CSQ} \cdot \frac{\sin\angle ASQ}{\sin\angle CSQ} = \frac{\sin^2\angle ASQ}{\sin^2\angle CSQ}$$
- **画面图元**：
  - 高亮 $\Delta PAC$ 及其内部塞瓦线段 $PQ, AQ, CQ$。
  - 高亮塞瓦定理中的 6 个角，并用色彩动画般映射到两对比值的平方乘积。

### Step 5: 最终结论：$AR/RC = \sqrt{AB/BC}$ 不依赖于圆 $\Gamma$
- **标题**：⑤ 最终结论：$R$ 为定比内分点，与圆无关
- **核心推理**：
  将 Step 1 的结果 $\frac{AB}{BC} = \frac{\sin\angle APB}{\sin\angle CPB}$ 与 Step 2 的结果 $\frac{AR}{RC} = \frac{\sin\angle ASQ}{\sin\angle CSQ}$ 代入 Step 4 的等式中：
  $$\frac{AB}{BC} = \frac{\sin^2\angle ASQ}{\sin^2\angle CSQ} = \left(\frac{AR}{RC}\right)^2$$
  两边开算术平方根，立即得出：
  $$\frac{AR}{RC} = \sqrt{\frac{AB}{BC}}$$
  因为 $A, B, C$ 是直线上的三个初始定点，线段长度 $AB$ 与 $BC$ 是完全不变的常数，比值 $\frac{AB}{BC}$ 为定值！
  因此，内分比 $\frac{AR}{RC} = \sqrt{\frac{AB}{BC}}$ 亦为唯一确定的常数，交点 $R$ 在线段 $AC$ 上的几何位置固定不变，**完全不依赖于圆 $\Gamma$ 的任何半径与圆心选取**！
  原命题得证。
- **画面图元**：
  - 黄金高亮线段 $AC$ 及分点 $R$，同时高亮定点 $A, B, C$。
  - 虚化褪色圆 $\Gamma$、点 $P$ 及相关弦切线，凸显“无论圆 $\Gamma$ 如何变化，比值与分点 $R$ 恒定不变”的几何本质。
