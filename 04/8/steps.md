# 04/8 (例 7) 平面几何交互分步证明规划 (steps.md)

## 题目概要
**题目**：设 $\triangle ABC$ 和 $\triangle XYZ$ 的交点 $A_1, A_2, B_1, B_2, C_1, C_2$ 满足
$$\frac{A_1 A_2}{BC} = \frac{B_1 B_2}{AC} = \frac{C_1 C_2}{AB}$$
证明：
$$\frac{A_2 B_1}{XY} = \frac{B_2 C_1}{YZ} = \frac{C_2 A_1}{ZX}$$

**核心思想**：通过向量平移将分散在各边的等比截线 $B_2 B_1$ 平移至 $C_1 O$（构造平行四边形 $C_1 O B_1 B_2$），进而利用余弦定理/SAS 证明 $\triangle C_2 C_1 O \sim \triangle BAC$ 并获得第二个平行四边形 $C_2 O A_2 A_1$。此时核心三角形 $\triangle O A_2 B_1$ 的三边分别平行且等于目标截线与边长，由 AAA 相似判定 $\triangle O A_2 B_1 \sim \triangle ZXY$，代换等长线段即证得结论。

---

## 分步规划（共 6 步：Step 0 ~ Step 5）

### Step 0: 已知条件与图形结构
- **标题**：✦ 已知条件与图形结构
- **数学逻辑**：
  给定 $\triangle ABC$ 与 $\triangle XYZ$，两三角形交织在各边形成截点 $A_1, A_2$（在边 $BC$ 上）、$B_1, B_2$（在边 $AC$ 上）、$C_1, C_2$（在边 $AB$ 上）。
  已知截线段与边长成比例：
  $$\frac{A_1 A_2}{BC} = \frac{B_1 B_2}{AC} = \frac{C_1 C_2}{AB} = \lambda$$
  求证目标截线与 $\triangle XYZ$ 各边亦成比例：
  $$\frac{A_2 B_1}{XY} = \frac{B_2 C_1}{YZ} = \frac{C_2 A_1}{ZX}$$
- **新增图元**：
  - 静态底层：$\triangle ABC$（深色实线）、$\triangle XYZ$（深青色实线）；
  - 动态层：高亮 $\triangle ABC$ 三边截线 $A_1 A_2, B_1 B_2, C_1 C_2$（蓝色高亮），展示对应等比关系。
  - 点集：显示 $A, B, C, X, Y, Z, A_1, A_2, B_1, B_2, C_1, C_2$ 及其标签（暂不显示 $O$）。
- **擦除图元**：无（初始状态）。
- **色彩规划**：
  - $\triangle ABC$：底线 `#1e293b`
  - $\triangle XYZ$：底线 `#0f766e`
  - 截线 $A_1 A_2, B_1 B_2, C_1 C_2$：主蓝 `#2563eb`

---

### Step 1: 平移辅助线：构造平行四边形 $C_1 O B_1 B_2$
- **标题**：① 平移辅助线：构造平行四边形 $C_1 O B_1 B_2$
- **数学逻辑**：
  将边 $AC$ 上的线段 $B_2 B_1$ 平移至以 $C_1$ 为起点的向量 $C_1 O$，即令 $\vec{C_1 O} = \vec{B_2 B_1}$。
  此时四边形 $C_1 O B_1 B_2$ 对边平行且相等，构成平行四边形：
  $$C_1 O = B_1 B_2 = \lambda AC, \quad O B_1 \parallel C_1 B_2 \ (\text{即 } O B_1 \parallel YZ), \quad O B_1 = B_2 C_1$$
- **新增图元**：
  - 点 $O$ 及其标签（带白底防遮挡）；
  - 辅助虚线 $C_1 O$（红色虚线）、$O B_1$（紫色虚线）；
  - 半透明高亮填充平行四边形 $C_1 O B_1 B_2$（淡橙色 `#ea580c18`）；
  - 平行标记箭头（$O B_1$ 与边 $YZ$）。
- **擦除图元**：擦除 Step 0 的全线高亮，聚焦于平移四边形。
- **色彩规划**：
  - 平移线 $C_1 O$：赤红 `#dc2626`
  - 对应平行边 $O B_1$：紫罗兰 `#7c3aed`
  - 平行四边形填充：`rgba(234, 88, 12, 0.12)`

---

### Step 2: 余弦定理与相似：证明 $\triangle C_2 C_1 O \sim \triangle BAC$
- **标题**：② 余弦定理与相似：证明 $\triangle C_2 C_1 O \sim \triangle BAC$
- **数学逻辑**：
  在 $\triangle C_2 C_1 O$ 中：
  1. $C_1 C_2 = \lambda AB$；
  2. $C_1 O = B_1 B_2 = \lambda AC$；
  3. 因为 $C_1 C_2$ 位于边 $AB$ 上，且 $C_1 O \parallel AC$，同位角（或方向对应角）满足 $\angle C_2 C_1 O = \angle BAC$。
  由余弦定理：
  $$C_2 O^2 = C_1 C_2^2 + C_1 O^2 - 2 C_1 C_2 \cdot C_1 O \cos \angle C_2 C_1 O = \lambda^2 (AB^2 + AC^2 - 2 AB \cdot AC \cos A) = \lambda^2 BC^2 = A_1 A_2^2$$
  故 $C_2 O = A_1 A_2 = \lambda BC$，且由 SAS 判定得 $\triangle C_2 C_1 O \sim \triangle BAC$。
- **新增图元**：
  - 辅助虚线 $C_2 O$；
  - 高亮三角形 $\triangle C_2 C_1 O$（浅红填充）与 $\triangle BAC$（浅蓝填充）；
  - 角弧标记：$\angle C_2 C_1 O$ 与 $\angle BAC$ 对比高亮。
- **擦除图元**：擦除 Step 1 中 $C_1 O B_1 B_2$ 的填充面与平行标记，保留 $O$ 与辅助线。
- **色彩规划**：
  - $\triangle C_2 C_1 O$：边 `#dc2626`，填充 `rgba(220, 38, 38, 0.15)`
  - $\angle C_2 C_1 O$ 与 $\angle A$ 角弧：`#dc2626`

---

### Step 3: 平行四边形传递：证明 $C_2 O A_2 A_1$ 为平行四边形
- **标题**：③ 平行四边形传递：证明 $C_2 O A_2 A_1$ 为平行四边形
- **数学逻辑**：
  由 $\triangle C_2 C_1 O \sim \triangle BAC$ 得对应角 $\angle C_1 C_2 O = \angle ABC$。
  因为 $C_1 C_2$ 位于直线 $AB$ 上，根据内错角/同位角关系，得 $C_2 O \parallel BC$（即 $C_2 O \parallel A_1 A_2$）。
  又已知 $C_2 O = A_1 A_2$，故一组对边平行且相等：
  四边形 $C_2 O A_2 A_1$ 为平行四边形！
  由此可推出另一组对边亦平行且相等：
  $$O A_2 \parallel C_2 A_1 \ (\text{即 } O A_2 \parallel ZX), \quad O A_2 = C_2 A_1$$
- **新增图元**：
  - 辅助虚线 $O A_2$（绿色虚线）；
  - 半透明高亮填充平行四边形 $C_2 O A_2 A_1$（淡绿 `#05966918`）；
  - 对边平行标记箭头（$O A_2$ 与边 $ZX$）。
- **擦除图元**：擦除 Step 2 的角弧与 $\triangle BAC$ 高亮，聚焦于平行四边形 $C_2 O A_2 A_1$。
- **色彩规划**：
  - $O A_2$：翠绿 `#059669`
  - 四边形 $C_2 O A_2 A_1$ 填充：`rgba(5, 150, 105, 0.14)`

---

### Step 4: 核心相似三角形：证明 $\triangle O A_2 B_1 \sim \triangle ZXY$
- **标题**：④ 核心相似三角形：证明 $\triangle O A_2 B_1 \sim \triangle ZXY$
- **数学逻辑**：
  考察中心小三角形 $\triangle O A_2 B_1$ 的三边：
  1. $O A_2 \parallel ZX$（由四边形 $C_2 O A_2 A_1$ 平行对边）；
  2. $O B_1 \parallel ZY$（由四边形 $C_1 O B_1 B_2$ 平行对边）；
  3. 底边 $A_2 B_1$ 本身就落在直线 $XY$ 上。
  两边分别平行于两直线，夹角必相等：
  $$\angle O A_2 B_1 = \angle ZXY, \quad \angle O B_1 A_2 = \angle ZYX$$
  由两角对应相等，判定：
  $$\triangle O A_2 B_1 \sim \triangle ZXY$$
- **新增图元**：
  - 高亮小三角形 $\triangle O A_2 B_1$（琥珀橙填充 `#ea580c`）；
  - 高亮外围大三角形 $\triangle ZXY$（青碧色描边与极浅底色）；
  - 对应角弧标记：$\angle O A_2 B_1 = \angle X$ 与 $\angle O B_1 A_2 = \angle Y$。
- **擦除图元**：擦除 Step 3 的平行四边形填充，让视野完全集中在两对相似三角形上。
- **色彩规划**：
  - $\triangle O A_2 B_1$：描边 `#ea580c`，填充 `rgba(234, 88, 12, 0.22)`
  - $\triangle ZXY$：高亮外框 `#0891b2`

---

### Step 5: 边长比代换：得出最终结论
- **标题**：⑤ 边长比代换：得出最终结论
- **数学逻辑**：
  由 $\triangle O A_2 B_1 \sim \triangle ZXY$ 的对应边成比例：
  $$\frac{O A_2}{ZX} = \frac{O B_1}{ZY} = \frac{A_2 B_1}{XY}$$
  代入之前证明的两组平移等长对边关系：
  1. $O A_2 = C_2 A_1$（来自平行四边形 $C_2 O A_2 A_1$）；
  2. $O B_1 = B_2 C_1$（来自平行四边形 $C_1 O B_1 B_2$）；
  即得：
  $$\frac{C_2 A_1}{ZX} = \frac{B_2 C_1}{YZ} = \frac{A_2 B_1}{XY}$$
  即 $\triangle XYZ$ 各边截线段与所在边长比例完全相等，命题得证！
- **新增图元**：
  - 综合辉映：高亮 $\triangle XYZ$ 上的三条截线 $A_2 B_1, B_2 C_1, C_2 A_1$（主蓝 `#2563eb` 加粗发光）；
  - 高亮全部对应边 $XY, YZ, ZX$；
  - 胜利徽章/结论完成标牌。
- **擦除图元**：擦除辅助角弧，保持主结论的清爽与庄严。
- **色彩规划**：
  - 目标三截线：主蓝 `#2563eb` 加粗，金色发光微晕
  - 整体完成提示：高对比度清爽展示
