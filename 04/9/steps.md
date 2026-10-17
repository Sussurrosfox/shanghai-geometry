# 例 8 分步证明交互演示规划 (04/9/steps.md)

## 一、题目解析与数学核心

### 1. 题目重述
在直角 $\triangle ABC$ 中，$\angle C = 90^\circ$，$CD$ 为斜边 $AB$ 上的高。记 $\triangle ACD$ 及 $\triangle BCD$ 的内心分别为 $I_1, I_2$，直线 $I_1 I_2$ 与直角边 $CA, CB$ 分别交于点 $M, N$。
证明：$S_{\triangle ABC} \geq 2 S_{\triangle CMN}$。

### 2. 核心数学推理链
1. **母子直角三角形相似**：Rt $\triangle DAC \sim$ Rt $\triangle DCB$（比值为 $\frac{CD}{BD} = \frac{AD}{CD} = \frac{AC}{BC}$），且以 $D$ 为旋转中心可看作绕点 $D$ 逆时针旋转 $90^\circ$ 叠加位似。
2. **内心三角形相似**：由于 $I_1, I_2$ 分别平分直角 $\angle ADC, \angle BDC$，故 $\angle CDI_1 = 45^\circ, \angle CDI_2 = 45^\circ \implies \angle I_1 D I_2 = 90^\circ = \angle BDC$。同时对应内心的距离比 $\frac{DI_1}{DI_2} = \frac{CD}{BD}$，从而 $\triangle D I_1 I_2 \sim \triangle D C B$。
3. **夹角旋转与等腰直角**：由上述相似，线段 $DC$ 旋转到 $DI_1$ 夹角为 $45^\circ$，说明 $\triangle D I_1 I_2$ 相对于 $\triangle D C B$ 逆时针旋转了 $45^\circ$。因此直线 $I_1 I_2$ 与直线 $CB$ 的夹角必等于旋转角 $45^\circ$，即 $\angle CNM = 45^\circ$。在 Rt $\triangle CMN$ 中（$\angle C = 90^\circ$），底角为 $45^\circ$，故 $\triangle CMN$ 为等腰直角三角形，即 $CM = CN$。
4. **全等三角形导出线段相等**：在 $\triangle I_2 C D$ 与 $\triangle I_2 C N$ 中，$CI_2$ 为公共边兼角平分线（$\angle I_2 C D = \angle I_2 C N$），且 $\angle C D I_2 = 45^\circ = \angle C N I_2$。由 AAS（角-角-边）判据知 $\triangle I_2 C D \cong \triangle I_2 C N$，故 $CD = CN$。结合前面结论知 $CM = CN = CD$。
5. **面积公式与斜边不等式**：
   $$S_{\triangle ABC} = \frac{1}{2} AB \cdot CD,\quad S_{\triangle CMN} = \frac{1}{2} CM \cdot CN = \frac{1}{2} CD^2$$
   面积比值：
   $$\frac{S_{\triangle ABC}}{S_{\triangle CMN}} = \frac{AB}{CD}$$
   在直角 $\triangle ABC$ 中，斜边中线 $CO = \frac{1}{2} AB$，而高线 $CD \leq CO = \frac{1}{2} AB$（垂线段不大于斜线段，或由均值不等式 $AB = AD + BD \geq 2\sqrt{AD \cdot BD} = 2CD$），故 $\frac{AB}{CD} \geq 2$。
   从而 $S_{\triangle ABC} \geq 2 S_{\triangle CMN}$，等号成立当且仅当 $AC = BC$。

---

## 二、几何坐标体系（精确解算）

选取比例优美且易于观察的 $3-4-5$ 衍生构型：
- 取直角顶点 $D = (0, 0)$，高线 $CD$ 沿 $y$ 轴正方向；
- 斜边 $AB$ 沿 $x$ 轴，$A$ 在左侧，$B$ 在右侧；
- 取直角边比例 $AC : BC = 4 : 3$，斜边 $AB = 5$；
- 则高 $CD = h = 2.4$，$AD = 3.2$，$BD = 1.8$；
- 垂足 $D = (0, 0)$；
- 顶点 $A = (-3.2, 0)$，$B = (1.8, 0)$，$C = (0, 2.4)$；
- $\triangle ACD$ 内心 $I_1 = (-0.8, 0.8)$（内切圆半径 $r_1 = \frac{3.2 + 2.4 - 4.0}{2} = 0.8$）；
- $\triangle BCD$ 内心 $I_2 = (0.6, 0.6)$（内切圆半径 $r_2 = \frac{1.8 + 2.4 - 3.0}{2} = 0.6$）；
- 直线 $I_1 I_2$ 与 $CA$ 交点 $M = (-1.92, 0.96)$；
- 直线 $I_1 I_2$ 与 $CB$ 交点 $N = (1.44, 0.48)$；
- 校验：
  - $CM = \sqrt{(-1.92)^2 + (0.96 - 2.4)^2} = \sqrt{3.6864 + 2.0736} = \sqrt{5.76} = 2.4 = CD$；
  - $CN = \sqrt{1.44^2 + (0.48 - 2.4)^2} = \sqrt{2.0736 + 3.6864} = \sqrt{5.76} = 2.4 = CD$；
  - $CM = CN = CD = 2.4$ 绝对精准成立！

---

## 三、分步演示规划表

| 步序 | 步骤标题 | 数学推理要点 | 画面新增图元 | 画面擦除/保留 | 动态高亮与色彩规划 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | **已知条件与几何构型** | 给定 Rt $\triangle ABC$，$\angle C=90^\circ$，$CD \perp AB$。$I_1, I_2$ 为两直角子三角形内心，直线 $I_1 I_2$ 分别交 $CA, CB$ 于 $M, N$。目标：比较 $S_{\triangle ABC}$ 与 $S_{\triangle CMN}$。 | 底层直角三角形 $\triangle ABC$、高线 $CD$、直角标记 $\angle ACB, \angle ADC$、点 $I_1, I_2$、直线 $MN$（穿过 $I_1, I_2$）及交点 $M, N$。 | 全程保留基础骨架 | 主构型深色线段 `#1e293b`，高线高亮，直角标记红色 `#dc2626`，割线 $MN$ 紫色 `#7c3aed`。 |
| **1** | **母子直角三角形相似** | Rt $\triangle DAC \sim$ Rt $\triangle DCB$。<br>$\angle CAD = 90^\circ - \angle ACD = \angle BCD$。<br>比值 $\frac{AD}{CD} = \frac{CD}{BD} = \frac{AC}{BC}$。以 $D$ 为中心，逆时针旋转 $90^\circ$ 叠加位似变换即可使 $\triangle DCB$ 映射为 $\triangle DAC$。 | 高亮 $\triangle DAC$ 与 $\triangle DCB$ 对应区域；标出两互余锐角相等 $\angle CAD = \angle BCD$。 | 步骤 0 的基础骨架 | $\triangle DAC$ 浅蓝填充透明度 0.12，$\triangle DCB$ 浅橙填充透明度 0.12；对应等角弧度标记蓝色/橙色。 |
| **2** | **内心相似导出夹角** | $DI_1, DI_2$ 分别平分直角 $\angle ADC, \angle BDC$，故 $\angle CDI_1 = \angle CDI_2 = 45^\circ \implies \angle I_1 D I_2 = 90^\circ$。<br>对应边 $\frac{DI_1}{DI_2} = \frac{CD}{BD}$，故 $\triangle D I_1 I_2 \sim \triangle D C B$。<br>由旋转角为 $45^\circ$，导出直线 $I_1 I_2$ 与直线 $CB$ 夹角 $\angle CNM = 45^\circ$。 | 连接线段 $DI_1, DI_2$（虚线）；标注 $\angle CDI_1 = 45^\circ, \angle CDI_2 = 45^\circ$ 及夹角 $\angle CNM = 45^\circ$ 角弧。高亮 $\triangle D I_1 I_2$ 与 $\triangle D C B$。 | 擦除步 1 区域填充与角标记；保留 $MN$。 | $DI_1, DI_2$ 蓝色虚线，高亮线段，角弧标记绿色 `#059669`，角度文字标注 $45^\circ$。 |
| **3** | **确定 $\triangle CMN$ 为等腰直角** | 在 Rt $\triangle CMN$ 中，$\angle C = 90^\circ$。<br>由直线 $MN$ 与 $CB$ 的夹角 $\angle CNM = 45^\circ$，得 $\angle CMN = 90^\circ - 45^\circ = 45^\circ$。<br>因此 $\triangle CMN$ 两底角相等，为等腰直角三角形，故 $CM = CN$。 | 重点高亮 $\triangle CMN$ 区域与直角顶点 $C$；标出 $\angle CMN = 45^\circ, \angle CNM = 45^\circ$；在 $CM, CN$ 上标注等长刻度标记。 | 擦除步 2 的 $DI_1, DI_2$ 连线与复杂角弧，突出 $\triangle CMN$。 | $\triangle CMN$ 采用柔和翡翠绿填充（`#059669`，透明度 0.15）；等长刻度绿色双线。 |
| **4** | **全等三角形导出关键等长** | 考察 $\triangle I_2 C D$ 与 $\triangle I_2 C N$：<br>① $CI_2$ 为角平分线 $\implies \angle I_2 C D = \angle I_2 C N$；<br>② $C I_2$ 为公共边；<br>③ $\angle C D I_2 = 45^\circ = \angle C N I_2$。<br>由 AAS 判定定理得 $\triangle I_2 C D \cong \triangle I_2 C N$。<br>从而对应边 $CD = CN$。<br>结合步 3 知 $CM = CN = CD$！ | 连接辅助线 $CI_2$（虚线）；高亮全等三角形 $\triangle I_2 C D$ 与 $\triangle I_2 C N$ 区域；在 $CD, CN, CM$ 上均加上三重等长刻度标记。 | 擦除步 3 的 $45^\circ$ 刻度，聚焦于全等对应元素。 | $\triangle I_2 C D$ 浅紫填充，$\triangle I_2 C N$ 浅青填充；公共边 $CI_2$ 红色虚线高亮；等长标记洋红色 `#c026d3`。 |
| **5** | **面积之比与均值不等式** | $S_{\triangle ABC} = \frac{1}{2} AB \cdot CD$；<br>$S_{\triangle CMN} = \frac{1}{2} CM \cdot CN = \frac{1}{2} CD^2$。<br>比值 $\frac{S_{\triangle ABC}}{S_{\triangle CMN}} = \frac{AB}{CD}$。<br>作斜边中点 $O$（外心），中线 $CO = \frac{1}{2} AB$。<br>垂线段 $CD \leq CO = \frac{1}{2} AB \implies \frac{AB}{CD} \geq 2$。<br>故 $S_{\triangle ABC} \geq 2 S_{\triangle CMN}$（等号成立当且仅当 $AC = BC$）。证毕！ | 显现斜边中点 $O$，连接中线 $CO$（虚线），高亮大三角形 $\triangle ABC$ 与等腰直角 $\triangle CMN$ 进行面积对比，展示不等式结论框。 | 擦除步 4 的全等辅助线，还原纯净全局对比。 | $\triangle ABC$ 整体蓝色边框，$\triangle CMN$ 浅绿填充对比；中点 $O$ 及中线 $CO$ 橙色 `#ea580c` 虚线。 |

---

## 四、视觉防遮挡与色彩体系约定

- **基础构架**：深蓝黑 `#1e293b`
- **动态步骤层高亮**：
  - 蓝色系 `BLUE = '#2563eb'`：母相似、大三角形
  - 绿色系 `GREEN = '#059669'`：$\triangle CMN$ 及其等长边
  - 红色系 `RED = '#dc2626'`：直角标记、全等关键线
  - 紫色系 `PURPLE = '#7c3aed'`：直线 $MN$ 及交点
  - 橙色系 `ORANGE = '#ea580c'`：斜边中线 $CO$ 及极值分析
- **标签排布防遮挡设计**：
  - $A$：向左下方偏移 `(-18, 16)`
  - $B$：向右下方偏移 `(18, 16)`
  - $C$：向正上方偏移 `(0, -18)`
  - $D$：向正下方略偏右 `(6, 18)`
  - $I_1$：向左上方偏移 `(-14, -14)`
  - $I_2$：向右上方偏移 `(14, -14)`
  - $M$：向左上方偏移 `(-16, -10)`
  - $N$：向右上方偏移 `(16, -10)`
  - $O$：向正下方偏移 `(0, 18)`
- 点全部采用白底双层描边（点半径 4.5px，标签自带白色轻微发光或背景无碰撞间距），确保在任何背景下文字清晰可辨。
