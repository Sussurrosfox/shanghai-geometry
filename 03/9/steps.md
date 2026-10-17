# 03/9.md（例 8）分步证明演示规划

## 命题信息
- **题面**：设 $\triangle ABC$ 的外心，内心，重心分别为 $O, I, G$。过点 $B$ 作 $BP \bot OI$ 交 $AI$ 的延长线于点 $P$。过点 $P$ 作 $PM \parallel AC$ 交 $BC$ 于点 $M$。证明：$I, G, M$ 三点共线。
- **核心思想**：
  1. 梅涅劳斯定理对共线条件的降维简化（化简为 $PM = 2ME$ 与 $FC = BC$）；
  2. 同一法辅助点构造（$CF = BC$ 连线交角平分线于 $P'$，证明 $BP' \bot OI$）；
  3. 鸡爪定理与外接圆弧中点性质；
  4. 两对相似三角形传递（$\triangle AOS \sim \triangle FCB$ 与 $\triangle OSI \sim \triangle BAT$）导出垂直。

---

## 颜色约定
- 基础三角形 $\triangle ABC$：深灰/藏青 `#1e293b`，点与边框清晰
- 外心 $O$、内心 $I$、重心 $G$：分别用蓝色 `#2563eb`、紫色 `#7c3aed`、橙色 `#ea580c` 标识
- 辅助线/割线/截线：
  - 角平分线 $AD$ 与中线 $AE$：细虚线/弱灰色 `#94a3b8`
  - 核心垂线 $BP \bot OI$：红色加粗线 `#dc2626`
  - 平行线对 $PM \parallel AC$ 与 $AT \parallel FB$：绿色 `#059669`
  - 最终共线 $I-G-M$：高亮荧光红/金橙渐变 `#dc2626` 贯穿线
  - 辅助圆（外接圆 $\odot O$）：轻柔天蓝 `#38bdf8` 虚线圆

---

## 步骤规划清单

### 步骤 0：已知条件与图形构型
- **标题**：已知条件与图形构型
- **正文**：
  设 $\triangle ABC$ 的外心为 $O$、内心为 $I$、重心为 $G$。<br>
  过点 $B$ 作 $BP \bot OI$ 交 $AI$ 的延长线于点 $P$。<br>
  过点 $P$ 作 $PM \parallel AC$ 交 $BC$ 于点 $M$。<br>
  <b>求证：</b>$I, G, M$ 三点共线。
- **画面**：
  - 显示基础三角形 $\triangle ABC$。
  - 标出外心 $O$、内心 $I$、重心 $G$ 及其对应连线 $OI$。
  - 连结 $AI$ 延长线至点 $P$，绘制垂直于 $OI$ 的垂线段 $BP$，并标出直角符号 $BP \bot OI$。
  - 绘制过 $P$ 平行于 $AC$ 的线段 $PM$ 交 $BC$ 于 $M$，并在 $PM$ 与 $AC$ 上标注平行箭头。
  - 点亮待证三点 $I, G, M$。

### 步骤 1：梅涅劳斯定理：共线目标转化
- **标题**：梅涅劳斯定理：共线目标转化
- **正文**：
  连结 $AI$ 与 $BC$ 交于点 $D$，$AG$ 与 $BC$ 交于点 $E$（中点）。<br>
  考虑 $\triangle ADE$ 及待证三点 $I, G, M$ 分别位于三边所在的直线上：<br>
  - 点 $I$ 在边 $AD$ 上，比值为 $\frac{AI}{ID}$；<br>
  - 点 $G$ 在边 $AE$ 上，比值为 $\frac{EG}{GA}$；<br>
  - 点 $M$ 在边 $DE$ 的延长线上，比值为 $\frac{DM}{ME}$。<br>
  由<b>梅涅劳斯定理</b>，要证 $I, G, M$ 三点共线，只需证明：<br>
  $$\frac{AI}{ID} \cdot \frac{DM}{ME} \cdot \frac{EG}{GA} = 1 \quad \text{①}$$
- **画面**：
  - 绘制线段 $AD$（角平分线）与中线 $AE$（连结 $A, G, E$）。
  - 轻色填充突出三角形 $\triangle ADE$。
  - 连结虚线 $I-G-M$ 表示截线。
  - 标出分比端点 $D, E$。

### 步骤 2：代数化简：目标归结为 $FC = BC$
- **标题**：代数化简：目标归结为 $FC = BC$
- **正文**：
  由三角形角平分线性质，在 $\triangle ADC$ 中由 $CI$ 平分 $\angle C$ 得：<br>
  $$\frac{AI}{ID} = \frac{AC}{CD} \quad \text{②}$$<br>
  由 $PM \parallel AC$ 截线定理，在 $\triangle ADC$ 中得：<br>
  $$\frac{AC}{CD} = \frac{PM}{MD} \quad \text{③}$$<br>
  由重心 $G$ 分中线比知：$\frac{EG}{GA} = \frac{1}{2}$ ④。<br>
  将②、③、④代入①式：$\frac{PM}{MD} \cdot \frac{DM}{ME} \cdot \frac{1}{2} = 1 \iff PM = 2ME$。<br>
  延长 $PE$ 交 $AC$ 的延长线于点 $F$。由于 $PM \parallel FC$，由对顶相似 $\triangle PME \sim \triangle FCE$ 得 $\frac{PM}{FC} = \frac{ME}{CE}$，故只需证明：<br>
  <b>$$FC = 2CE = BC$$</b>
- **画面**：
  - 延长线段 $PE$ 交 $AC$ 的延长线于点 $F$。
  - 高亮相似三角形对 $\triangle PME$ 与 $\triangle FCE$。
  - 高亮显示线段 $PM$ 与 $ME$（$PM = 2ME$）以及线段 $FC$ 与 $BC$。
  - 标注 $CE = EB$（$E$ 为中点）。

### 步骤 3：同一法构造：辅助点 $P'$ 与外接圆弧中点 $S$
- **标题**：同一法构造：辅助点 $P'$ 与外接圆中点 $S$
- **正文**：
  下面采用<b>同一法</b>证明：<br>
  在射线 $CA$ 上截取点 $F$，使得 <b>$CF = BC$</b>。<br>
  设直线 $FE$ 交角平分线 $AD$ 于点 $P'$。若能证明 <b>$BP' \bot OI$</b>，则因过点 $B$ 作 $OI$ 的垂线与 $AD$ 的交点唯一，必有 <b>$P'$ 与 $P$ 重合</b>！<br>
  作 $\triangle ABC$ 的外接圆 $\odot O$。连结内心射线 $CI$ 并延长交外接圆于点 $S$。<br>
  因 $CI$ 为角平分线，$S$ 为弧 $AB$ 的中点，必有 $SO \bot AB$。<br>
  由<b>鸡爪定理</b>（圆幂内心几何），弧中点到两顶点与内心等距：<br>
  $$SI = SA = SB$$
- **画面**：
  - 绘制外接圆 $\odot O$ 虚线圆。
  - 在边 $AC$ 延长线上画出点 $F$，并在 $CF$ 与 $BC$ 上标注等长刻度（tickMark）。
  - 连结 $FE$ 穿过 $AD$ 于点 $P'$（高亮此关键同一法交点）。
  - 连结射线 $CS$ 交圆周于点 $S$，连结 $SO$ 与 $SA$，标注 $SO \bot AB$ 直角记号。
  - 连结线段 $SI$，标出 $SI = SA$ 等长记号。

### 步骤 4：等腰相似：导出 $\frac{SO}{SI} = \frac{FC}{FB}$
- **标题**：等腰相似：导出 $\frac{SO}{SI} = \frac{FC}{FB}$
- **正文**：
  在等腰 $\triangle AOS$ 中，$OA = OS = R$（外接圆半径）。<br>
  由于 $S$ 为弧 $AB$ 中点，圆心角 $\angle SOA = \frac{1}{2}\angle BOA = \angle ACB$。<br>
  在等腰 $\triangle FCB$ 中，构造已知 $CF = CB$，顶角即为 $\angle FCB = \angle ACB$。<br>
  两等腰三角形顶角相等，故底角对应相等，从而 <b>$\triangle AOS \sim \triangle FCB$</b>！<br>
  由对应边成比例：<br>
  $$\frac{SO}{SA} = \frac{FC}{FB}$$<br>
  由鸡爪定理 $SA = SI$ 替换底边，即得关键比例式：<br>
  $$\frac{SO}{SI} = \frac{FC}{FB} \quad \text{⑤}$$
- **画面**：
  - 连结等腰三角形底边 $FB$。
  - 浅色半透明分别填充 $\triangle AOS$（蓝色调）与 $\triangle FCB$（紫粉色调）。
  - 分别在顶角 $\angle SOA$ 与 $\angle FCB$ 上标注等角弧线（angleArc）。
  - 高亮对应比值边 $SO, SI$ 与 $FC, FB$。

### 步骤 5：平行线 $AT$ 与梅氏定理：导出 $\frac{FC}{FB} = \frac{BA}{AT}$
- **标题**：平行线 $AT$ 与梅氏定理：导出 $\frac{FC}{FB} = \frac{BA}{AT}$
- **正文**：
  过点 $A$ 作 $AT \bot CI$ 交 $P'B$ 的延长线于点 $T$。<br>
  在等腰 $\triangle FCB$ 中，顶角平分线 $CI \bot FB$；因 $AT \bot CI$，故 <b>$AT \parallel FB$</b>。<br>
  又因 $SO \bot AB, SI \bot AT$，由垂线边夹角相等易得：$\angle OSI = \angle BAT$。<br>
  延长 $BP'$ 交直线 $AC$ 于点 $X$。对 $\triangle XCB$ 及截线 $F-P'-E$ 应用梅涅劳斯定理：<br>
  $$\frac{XF}{FC} \cdot \frac{CE}{EB} \cdot \frac{BP'}{P'X} = 1$$<br>
  因 $CE = EB$，且在 $\triangle ABX$ 中 $AP'$ 为角平分线，由角平分线性质 $\frac{BP'}{P'X} = \frac{BA}{AX}$。<br>
  结合平行线截割定理 $\frac{XF}{AX} = \frac{FB}{AT}$，整理即得：<br>
  $$\frac{FC}{FB} = \frac{BA}{AT} \quad \text{⑥}$$
- **画面**：
  - 连结辅助线 $AT$，标出 $AT \bot CI$ 直角符号。
  - 延长 $BP'$ 线段至点 $T$ 与交点 $X$。
  - 标注平行箭头 $AT \parallel FB$。
  - 突出显示 $\triangle XCB$ 及贯穿截线 $F-P'-E$。
  - 在 $\angle OSI$ 与 $\angle BAT$ 处标出等角标记。

### 步骤 6：相似判定与垂直归宿：证明完成
- **标题**：相似判定与垂直归宿：证明完成
- **正文**：
  综合⑤式 $\frac{SO}{SI} = \frac{FC}{FB}$ 与⑥式 $\frac{FC}{FB} = \frac{BA}{AT}$，得：<br>
  $$\frac{SO}{SI} = \frac{BA}{AT}$$<br>
  结合夹角相等 $\angle OSI = \angle BAT$，两边成比例且夹角相等：<br>
  <b>$$\triangle OSI \sim \triangle BAT$$</b><br>
  由两三角形对应边位置关系：$SO \bot BA$，$SI \bot AT$，则第三对对应边必相互垂直：<br>
  $$OI \bot BT \implies BP' \bot OI$$<br>
  因此辅助点 $P'$ 与题目中的点 $P$ 必然重合！<br>
  从而 $FC = BC = 2CE$ 成立，进而 $PM = 2ME$ 成立，逆推回①式梅涅劳斯定理成立，<b>$I, G, M$ 严格三点共线</b>，命题完全得证！
- **画面**：
  - 填充并高亮相似三角形 $\triangle OSI$ 与 $\triangle BAT$。
  - 突出显示垂直关系 $OI \bot BP$（直角标记）。
  - 用醒目的加粗贯穿线点亮三点共线 $I-G-M$。
  - 最终显示结论框与全要素标注，展现完整的几何对称之美。
