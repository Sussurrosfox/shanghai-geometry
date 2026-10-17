# 例 2：九点圆、外接圆与垂径定理分步证明规划 (steps.md)

## 题目回顾
锐角 $\triangle ABC$ 中，$H$ 为其垂心，圆 $\Omega$ 为其九点圆，圆 $\omega$ 为 $\triangle BHC$ 的外接圆（圆心为 $O'$），$X$ 为圆 $\omega$ 上弧 $BHC$ 上一点。延长 $AX$ 与圆 $\Omega$ 交于 $Y$，$P$ 在圆 $\Omega$ 上且 $PX = PY$。证明：$\angle O'PX = 90^\circ$。

---

## 颜色约定
- 基础三角形 $\triangle ABC$：深灰/石板蓝 `#334155`
- 九点圆 $\Omega$：经典蓝 `#2563eb`
- 圆 $\omega$（$\triangle BHC$ 外接圆）：翡翠绿 `#059669`
- 垂心 $H$ 与高线：深石板灰 `#475569`
- 点 $X$ 及射线 $AX$：绿色 `#10b981`
- 点 $Y$ 及位似对应点 $K$：深蓝/青蓝 `#0284c7`
- 点 $P$ 及位似对应点 $Q$：琥珀橙 `#f59e0b`
- 点 $Z$ 及线段 $XZ$：紫色/洋红 `#8b5cf6`
- 垂径 $O'P$ 及直角符号：深红 `#dc2626`

---

## 步骤规划清单

### Step 0: 已知构形与条件
- **标题**：已知构形与条件
- **讲解正文**：
  在锐角 $\triangle ABC$ 中，$H$ 为垂心，圆 $\Omega$ 为九点圆（圆心 $N$），圆 $\omega$ 为 $\triangle BHC$ 的外接圆（圆心 $O'$）。
  点 $X$ 是圆 $\omega$ 上弧 $BHC$ 上的一点。延长射线 $AX$ 与九点圆 $\Omega$ 交于点 $Y$。
  在九点圆 $\Omega$ 上取点 $P$，满足 $PX = PY$。
  <br><b>求证：</b>$\angle O'PX = 90^\circ$（即 $O'P \perp PX$）。
- **画面**：
  - 绘制 $\triangle ABC$ 实线，垂心 $H$ 及三条高线虚线。
  - 绘制九点圆 $\Omega$（蓝色实线）与圆 $\omega$（绿色实线），标注圆心 $N$ 和 $O'$。
  - 绘制射线 $AX$（穿过九点圆交于 $Y$，到达 $X$）。
  - 绘制等长线段 $PX, PY$（加双划等长标记）。
  - 显示所有已知点标签：$A, B, C, H, N, O', X, Y, P$。

### Step 1: 九点圆的中点性质与位似中心
- **标题**：九点圆的中点性质，A 为圆 Ω 与圆 ω 的外位似中心
- **讲解正文**：
  取线段 $AB, AC, AH$ 的中点分别为 $C', B', H'$。根据九点圆定理，$C', B', H'$ 均在九点圆 $\Omega$ 上。
  以点 $A$ 为位似中心，位似比为 $\frac{1}{2}$，显然有：
  $B \mapsto C',\quad C \mapsto B',\quad H \mapsto H'.$
  因此 $\triangle BCH$ 在以 $A$ 为中心、位似比 $\frac{1}{2}$ 的位似变换下映为 $\triangle C'B'H'$。
  因为 $\triangle C'B'H'$ 的外接圆即为九点圆 $\Omega$，而 $\triangle BCH$ 的外接圆为圆 $\omega$，所以：
  <br><b>点 $A$ 是九点圆 $\Omega$ 与圆 $\omega$ 的外位似中心，位似比为 $\frac{1}{2}$。</b>
- **画面**：
  - 标注三边及垂线中点 $C', B', H'$（紫色实心圆点），连成中位三角形 $\triangle C'B'H'$（紫色虚线）。
  - 绘制位似射线 $A \to H' \to H$、$A \to C' \to B$、$A \to B' \to C$（细点划线）。
  - 视觉呈现圆 $\Omega$ 为圆 $\omega$ 经位似比 $\frac{1}{2}$ 缩小后的像。

### Step 2: 延长 AP, AY 交圆 ω 于 Q, K，导出平行与比例
- **标题**：延长 AP, AY 交圆 ω 于 Q, K，导出 PY // QK 且 QK = 2PY
- **讲解正文**：
  延长射线 $AP, AY$ 与圆 $\omega$ 分别交于点 $Q, K$。
  由于 $A$ 是圆 $\Omega$ 到圆 $\omega$ 位似比为 $\frac{1}{2}$ 的外位似中心，圆 $\Omega$ 上的任意点经以 $A$ 为中心、放大 2 倍后，必落在圆 $\omega$ 上。
  因此，$Q$ 与 $K$ 即为 $P$ 与 $Y$ 在圆 $\omega$ 上的位似对应点，满足：
  $AQ = 2AP,\quad AK = 2AY.$
  在 $\triangle AQK$ 中，$P, Y$ 分别为 $AQ, AK$ 的中点，由三角形中位线定理立即得出：
  <br><b>$PY \parallel QK \quad \text{且} \quad QK = 2PY.$</b>
- **画面**：
  - 延长射线 $AP$ 到 $Q$（橙色实线加虚线延长），射线 $AY$ 到 $K$（青色实线加虚线延长），标注点 $Q, K$。
  - 高亮线段 $PY$ 与线段 $QK$（青色高亮），添加同向平行箭头。
  - 标注比例关系 $QK = 2PY$。

### Step 3: 延长 XP 交圆 ω 于 Z，由 PX = PY 导角证明
- **标题**：延长 XP 交圆 ω 于 Z，由等腰与平行导出 ∠ZKX = ∠QXY
- **讲解正文**：
  延长射线 $XP$ 与圆 $\omega$ 交于点 $Z$。
  由已知条件 $PX = PY$，$\triangle PXY$ 为等腰三角形，底角相等：
  $\angle PXY = \angle PYX.$
  又由 Step 2 可知 $PY \parallel QK$，且 $A, Y, X, K$ 四点共线（同在割线 $AX$ 上），截线 $XK$ 截平行线得同位角相等：
  $\angle PYX = \angle QKX.$
  结合 $X, P, Z$ 三点共线，角 $\angle PXY$ 也就是角 $\angle ZXY$（即 $\angle ZXK$），由此得到：
  <br><b>$\angle ZKX = \angle QXY \quad (\text{即 } \angle QXK).$</b>
- **画面**：
  - 绘制割线 $XPZ$（紫色加粗实线交圆 $\omega$ 于 $Z$），标注点 $Z$。
  - 绘制辅助虚线 $KX$ 与 $QX$。
  - 绘制角弧标记：$\angle PYX, \angle PXY, \angle QKX$（高亮双弧）。
  - 显示内接四边形导角相等 $\angle ZKX = \angle QXY$。

### Step 4: 等圆周角对等弦，得出 P 为 XZ 中点
- **标题**：等圆周角对等弦，得出 XZ = QK = 2PX，P 为 XZ 中点
- **讲解正文**：
  在圆 $\omega$ 中，圆周角 $\angle ZKX$ 所对的弦为 $XZ$，圆周角 $\angle QXY$（即 $\angle QXK$）所对的弦为 $QK$。
  由圆周角定理，同圆中相等的圆周角所对的弦相等：
  $\angle ZKX = \angle QXK \implies XZ = QK.$
  结合 Step 2 的位似中位线关系 $QK = 2PY$，以及已知条件 $PY = PX$，串联等式链：
  <br><b>$XZ = QK = 2PY = 2PX.$</b>
  因为点 $P$ 位于弦 $XZ$ 上，且全长 $XZ = 2PX$，这证明：
  <br><b>点 $P$ 恰好是弦 $XZ$ 的中点（$PX = PZ$）。</b>
- **画面**：
  - 高亮两条等长弦 $XZ$ 与 $QK$（洋红与青色对比高亮）。
  - 在线段 $XP$ 与 $PZ$ 上绘制单划等长标记，显式强调 $PX = PZ$。
  - 标注中点结论：$P$ 是弦 $XZ$ 的中点。

### Step 5: 由垂径定理得出 O'P ⊥ PX，即 ∠O'PX = 90°（证毕）
- **标题**：由垂径定理得出 O'P ⊥ PX，即 ∠O'PX = 90°（证毕）
- **讲解正文**：
  在圆 $\omega$ 中，$XZ$ 是一条弦，$O'$ 为圆心。
  由 Step 4 的结论，点 $P$ 是弦 $XZ$ 的中点。
  根据<b>垂径定理</b>：连接圆心与非直径弦的中点的线段，垂直于该弦！
  因此：
  <br><b>$O'P \perp XZ \implies O'P \perp PX.$</b>
  即：
  <br><b>$\angle O'PX = 90^\circ.$</b>
  原命题获证！
- **画面**：
  - 连接圆心 $O'$ 与弦中点 $P$，高亮深红线段 $O'P$。
  - 高亮弦 $XZ$（青色实线）。
  - 在点 $P$ 处绘制红色直角符号 $\llcorner$（严格与 $O'P$ 及 $PX$ 对齐）。
  - 弹出完满证明结论框：$\angle O'PX = 90^\circ$。
