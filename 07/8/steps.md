# 07/8 几何证明步骤规划（例 7）

## 1. 题面阐释与核心结论

- **题目**：设锐角 $\triangle ABC$ 的外心为 $O$，垂心为 $H$，$\triangle ABC$ 内任一点 $P$ 关于 $BC, CA, AB$ 的对称点分别为 $D, E, F$。证明：
  $$\frac{S_{\triangle HDE}}{S_{\triangle HDF}} = \frac{S_{\triangle OAB}}{S_{\triangle OAC}}$$
- **核心数学机制**：
  1. **圆周角与平行线**：在等腰 $\triangle AEF$ 中顶角 $\angle EAF = 2A$，底角 $\angle AEF = 90^\circ - A$。垂心角 $\angle ACH = 90^\circ - A$。点 $E'$ 为射线 $AE$ 与 $\triangle AHC$ 外接圆的交点，同弧圆周角 $\angle AE'H = \angle ACH = 90^\circ - A$，从而同位角相等，导出平行线 $EF \parallel E'H$。
  2. **同底等高平行割补**：由 $EF \parallel E'H$，顶点在平行线上滑动保持面积守恒，从而 $S_{\triangle HEF} = S_{\triangle EE'F}$。
  3. **正弦定理与圆幂不变性**：$S_{\triangle EE'F} = \frac{1}{2} (AE \cdot EE') \sin 2A$。根据轴对称性，$E$ 和 $\odot(AHC)$ 分别是 $P$ 和外接圆 $\odot O$ 关于直线 $AC$ 的镜像对称图形，因此割线幂之积 $AE \cdot EE' = I_P = |R^2 - OP^2|$（点 $P$ 对外接圆 $\odot O$ 的圆幂绝对值）。
  4. **对称轮换与外心面积比**：由轮换对称性，$S_{\triangle HDE} = \frac{1}{2} I_P \sin 2C$，$S_{\triangle HDF} = \frac{1}{2} I_P \sin 2B$。而外心三角形面积分别为 $S_{\triangle OAB} = \frac{1}{2} R^2 \sin 2C$，$S_{\triangle OAC} = \frac{1}{2} R^2 \sin 2B$。两边相比，常数因子完美抵消，比值完全相等！

---

## 2. 严格代数几何坐标解算

### 2.1 参数设定与解析推导
- **画布参数**：`viewBox="140 10 570 530"`
- **外心与外接圆**：
  $$O = (360.00, 330.00), \quad R = 175.00$$
- **基准锐角三角形顶点**（极角分别取 $98^\circ, 212^\circ, 340^\circ$，内角分别为 $A = 66^\circ, B = 57^\circ, C = 57^\circ$ 的微调非等腰构型）：
  $$A = (335.64, 156.70)$$
  $$B = (211.59, 422.74)$$
  $$C = (524.45, 389.85)$$
- **垂心 $H$**（满足欧拉线向量关系 $\vec{OH} = \vec{OA} + \vec{OB} + \vec{OC}$）：
  $$H = (351.68, 309.29)$$
- **内部任意动点 $P$**（重心坐标 $(0.22, 0.48, 0.30)$）：
  $$P = (332.74, 354.34)$$
- **对称点 $D, E, F$**（由点到直线投影严格镜像解算）：
  - $P$ 关于 $BC$ 对称点：$D = (344.31, 464.45)$
  - $P$ 关于 $CA$ 对称点：$E = (529.57, 194.95)$
  - $P$ 关于 $AB$ 对称点：$F = (186.11, 285.97)$
- **辅助圆 $\odot(AHC)$**（$\odot O$ 关于边 $AC$ 的镜像圆）：
  - 圆心 $O_{AHC} = (500.09, 216.56)$，半径 $R = 175.00$
- **射线 $AE$ 与 $\odot(AHC)$ 的割线第二交点 $E'$**：
  - 严格代数二次方程割线交点解算：
  $$E' = (674.95, 223.63)$$

### 2.2 几何不变量与精度校验记录
- 平行度叉积：$\vec{EF} \times \vec{E'H} = -4.00178 \times 10^{-11} \approx 0$（严格共线平行）。
- 圆幂一致性：$AE \cdot EE' = 30043.2081 = |R^2 - OP^2| = I_P$（误差 $< 10^{-11}$）。
- 面积比检验：
  $$\frac{S_{\triangle HDE}}{S_{\triangle HDF}} = 1.03465423, \quad \frac{S_{\triangle OAB}}{S_{\triangle OAC}} = 1.03465423$$
  两比值差值为 $2.22 \times 10^{-16}$（达到浮点精度物理极限）。

---

## 3. 色彩系统与图元规范

- **基准图形层**：
  - $\triangle ABC$ 边框：`#64748b`，细线 1.8px
  - 顶点与外心垂心：顶点深灰 `#0f172a`，外心天蓝 `#0284c7`，垂心紫红 `#7c3aed`
- **动态高亮与强调层**：
  - 辅助圆 $\odot(AHC)$ 与外接圆 $\odot O$：虚线 1.8px，柔和淡彩透明填充
  - 平行线对 $EF$ 与 $E'H$：翡翠绿 `#059669` 与亮橙 `#ea580c`，2.5px 伴随平行指示
  - 面积对比色：
    - $\triangle HEF$ / $\triangle EE'F$：翡翠绿半透明 `rgba(16, 185, 129, 0.15)`
    - $\triangle HDE$ 与 $\triangle OAB$：天蓝半透明 `rgba(2, 132, 199, 0.18)`
    - $\triangle HDF$ 与 $\triangle OAC$：紫红半透明 `rgba(124, 58, 237, 0.18)`
- **顶层文字与标签（gPts）**：
  - 全局采用 `paint-order: stroke fill; stroke: #ffffff; stroke-width: 4px;` 保证任何图元穿过文字时文字绝对清晰可读，零重叠遮挡。

---

## 4. 分步演示规划（Step 0 ~ Step 6）

### Step 0：【已知构型与题设目标】
- **标题**：Step 0：题设条件与几何构型
- **正文**：
  在锐角 $\triangle ABC$ 中，外心为 $O$，垂心为 $H$。在 $\triangle ABC$ 内部任取一点 $P$，$P$ 关于三边 $BC, CA, AB$ 的对称点分别为 $D, E, F$。
  **求证目标**：$\frac{S_{\triangle HDE}}{S_{\triangle HDF}} = \frac{S_{\triangle OAB}}{S_{\triangle OAC}}$。
- **画面图元**：
  - 底层绘制 $\triangle ABC$。
  - 显现点 $P$ 以及三个对称垂足引线（虚线 $PD, PE, PF$）。
  - 显现对称点 $D, E, F$ 与外心 $O$、垂心 $H$。

### Step 1：【构造辅助圆 $\odot(AHC)$ 与点 $E'$】
- **标题**：Step 1：构造圆 $\odot(AHC)$ 与割线交点 $E'$
- **正文**：
  考虑过 $A, H, C$ 的圆 $\odot(AHC)$。根据垂心性质，垂心 $H$ 关于边 $AC$ 的对称点在外接圆 $\odot O$ 上，因此圆 $\odot(AHC)$ 恰为外接圆 $\odot O$ 关于边 $AC$ 的镜像圆（半径同样为 $R$）。
  延长射线 $AE$ 交圆 $\odot(AHC)$ 于点 $E'$。
- **画面图元**：
  - 绘制辅助圆 $\odot(AHC)$（优雅浅青紫虚线）。
  - 绘制射线 $A-E-E'$，标出交点 $E'$。
  - 虚线连接 $E'H$。

### Step 2：【等腰角平移与平行线证明：$EF \parallel E'H$】
- **标题**：Step 2：圆周角平移导出 $EF \parallel E'H$
- **正文**：
  由轴对称得 $AE = AP = AF$，且顶角 $\angle EAF = 2\angle BAC = 2A$。在等腰 $\triangle AEF$ 中，底角 $\angle AEF = 90^\circ - A$。
  在直角三角形中高线 $CH \perp AB$，故 $\angle ACH = 90^\circ - A$。
  在圆 $\odot(AHC)$ 中，弧 $AH$ 所对圆周角相等：$\angle AE'H = \angle ACH = 90^\circ - A$。
  从而同位角 $\angle AEF = \angle AE'H = 90^\circ - A$，由此得出：<b>$EF \parallel E'H$</b>！
- **画面图元**：
  - 高亮等腰三角形两腰 $AE, AF$（标等长刻度）。
  - 高亮两平行线段 $EF$ 与 $E'H$（带醒目平行箭头标记）。
  - 在 $\angle AEF$ 与 $\angle AE'H$ 处绘制等角弧线标记。

### Step 3：【同底等高平行割补：$S_{\triangle HEF} = S_{\triangle EE'F}$】
- **标题**：Step 3：同底等高平行割补面积转换
- **正文**：
  因为 $EF \parallel E'H$，点 $H$ 与点 $E'$ 到直线 $EF$ 的垂直距离严格相等（平行线间等高）。
  利用共底 $EF$ 的三角形平行变形定理，立即得到：
  $$S_{\triangle HEF} = S_{\triangle EE'F}$$
  我们将难以直接计算的垂心三角形 $\triangle HEF$ 成功转化到了射线割线 $AEE'$ 所在的三角形 $\triangle EE'F$！
- **画面图元**：
  - 绘制 $\triangle HEF$（彩色半透明填充）与 $\triangle EE'F$。
  - 高亮公共底边 $EF$ 与第三顶点所在的平行滑动轨 $E'H$。

### Step 4：【正弦定理与圆幂不变性】
- **标题**：Step 4：圆幂不变性求解 $S_{\triangle HEF}$
- **正文**：
  由正弦定理，$\triangle EE'F$ 的面积为：
  $$S_{\triangle EE'F} = \frac{1}{2} EF \cdot EE' \cdot \sin \angle FEA = \frac{1}{2} AF \cdot EE' \cdot \sin \angle EAF = \frac{1}{2} (AE \cdot EE') \sin 2A$$
  **核心几何洞察**：$E$ 与圆 $\odot(AHC)$ 分别是点 $P$ 与圆 $\odot O$ 关于直线 $AC$ 的镜像图形！
  因此过点 $E$ 的割线积 $AE \cdot EE'$ 严格守恒等于点 $P$ 对外接圆 $\odot O$ 的圆幂绝对值：
  $$AE \cdot EE' = I_P = |R^2 - OP^2| \implies S_{\triangle HEF} = \frac{1}{2} I_P \sin 2A$$
- **画面图元**：
  - 高亮共线割线段 $AE$ 与 $EE'$。
  - 显现点 $P$ 对外心 $O$ 的圆幂几何关系线段 $OP$ 与外接圆。

### Step 5：【对称轮换推演：$S_{\triangle HDE}$ 与 $S_{\triangle HDF}$】
- **标题**：Step 5：三边对称轮换导出面积闭式
- **正文**：
  完全同理，对关于边 $BC$（对角 $C$）与边 $AB$（对角 $B$）做完全对称的平行割补与圆幂映射，立即得到：
  $$S_{\triangle HDE} = \frac{1}{2} I_P \sin 2C$$
  $$S_{\triangle HDF} = \frac{1}{2} I_P \sin 2B$$
  两式相比，与动点 $P$ 位置相关的圆幂因子 $\frac{1}{2} I_P$ 完美抵消：
  $$\frac{S_{\triangle HDE}}{S_{\triangle HDF}} = \frac{\sin 2C}{\sin 2B}$$
- **画面图元**：
  - 高亮显现三角形 $\triangle HDE$（天蓝透明填充）与 $\triangle HDF$（紫红透明填充）。
  - 显示两三角形的面积比与角 $B, C$ 正弦值的对应关系。

### Step 6：【外心三角形面积与最终结论】
- **标题**：Step 6：外心三角形面积比与最终命题得证
- **正文**：
  考察外心 $O$ 与三顶点构成的三角形。在 $\odot O$ 中，$OA = OB = OC = R$。
  由同弧圆心角等于圆周角两倍知：$\angle AOB = 2C, \angle AOC = 2B$。
  故外心三角形面积分别为：
  $$S_{\triangle OAB} = \frac{1}{2} R^2 \sin 2C, \quad S_{\triangle OAC} = \frac{1}{2} R^2 \sin 2B$$
  两式相除，同样消去常数 $\frac{1}{2} R^2$：
  $$\frac{S_{\triangle OAB}}{S_{\triangle OAC}} = \frac{\sin 2C}{\sin 2B}$$
  与 Step 5 的面积比完全一致！因此：
  $$\frac{S_{\triangle HDE}}{S_{\triangle HDF}} = \frac{S_{\triangle OAB}}{S_{\triangle OAC}}$$
  **原命题完美得证！**
- **画面图元**：
  - 显现外接圆 $\odot O$ 以及外心连线 $OA, OB, OC$。
  - 高亮着色对比 $\triangle OAB$ 与 $\triangle OAC$。
  - 联动双侧面积比公式卡片，完成全闭环验证！
