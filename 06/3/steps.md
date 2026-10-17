# 题目 06/3.md（例 2）分步证明规划与图元规范

## 题目概述
设直线 $l$ 与 $\triangle ABC$ 的边 $AB, AC$ 的延长线交于点 $D, E$。直线 $l$ 关于 $BC$ 的垂直平分线的对称直线 $l'$ 交 $AB, AC$ 的延长线于 $D', E'$。若 $BD + CE = DE$，证明：$BD' + CE' = D'E'$。

---

## 分步证明设计（共 7 步：Step 0 ~ Step 6）

### Step 0: 题设条件与几何构型
- **标题**：✦ 题设条件与几何构型
- **讲解正文**：
  给定 $\triangle ABC$ 以及经过延长线边 $AB, AC$ 的截线 $l$（交点分别为 $D, E$）。
  直线 $l$ 关于 $BC$ 垂直平分线的对称直线为 $l'$，分别与 $AB, AC$ 延长线交于点 $D', E'$。
  已知条件：$BD + CE = DE$。
  求证目标：$BD' + CE' = D'E'$。
- **新增图元**：
  - $\triangle ABC$ 基础三角形边 $AB, BC, CA$；
  - 延长线 $BD, CE$ 及 $BD', CE'$；
  - 截线 $l$（线段 $DE$）与对称截线 $l'$（线段 $D'E'$）；
  - 对称轴：$BC$ 的垂直平分线（中垂线虚线）；
  - 基础点 $A, B, C, D, E, D', E'$。
- **擦除图元**：无（初始全景）。
- **色彩规范**：
  - $\triangle ABC$：深灰蓝 `#1e293b`，宽度 2px；
  - 延长线：浅灰线 `#94a3b8`，虚线 1.5px；
  - 直线 $l(DE)$：主蓝 `BLUE (#2563eb)`，宽度 2.5px；
  - 对称直线 $l'(D'E')$：紫色 `PURPLE (#7c3aed)`，宽度 2.5px；
  - 对称轴：中灰虚线 `#64748b`。

---

### Step 1: 截长构造点 $R$ 与内心 $O$
- **标题**：① 截长构造点 $R$ 与内心 $O$
- **讲解正文**：
  在 $DE$ 上取点 $R$，使得 $DR = BD$。结合已知条件 $BD + CE = DE = DR + ER$，立得 $ER = CE$。<br>
  设 $\triangle RBC$ 的外心为 $O$（即 $OB = OR = OC$）。<br>
  在等腰 $\triangle DBR$ 中，$D$ 与 $O$ 均在线段 $BR$ 的垂直平分线上，故直线 $OD \perp BR$ 且平分顶角 $\angle ADE$；<br>
  同理在等腰 $\triangle CER$ 中，$OE \perp CR$ 且平分顶角 $\angle AED$。<br>
  两条内角平分线交于 $O$，因此 <b>$O$ 是 $\triangle ADE$ 的内心</b>！
- **新增图元**：
  - 点 $R$（在线段 $DE$ 上）与点 $O$；
  - 辅助连线 $BR, CR$（细青色实线）；
  - 垂直平分线/角平分线 $OD, OE$（红色实线）；
  - 等长刻度标记：$BD = DR$（单绿色刻度），$CE = ER$（双橙色刻度）；
  - 直角标记：$OD \perp BR$ 于中点，$OE \perp CR$ 于中点；
  - 外接圆半径 $OB, OR, OC$。
- **擦除图元**：无。
- **色彩规范**：
  - 等腰 $\triangle DBR$ 边与标记：绿色 `GREEN (#059669)`；
  - 等腰 $\triangle CER$ 边与标记：橙色 `ORANGE (#ea580c)`；
  - 角平分线 $OD, OE$ 与点 $O$：红色 `RED (#dc2626)`。

---

### Step 2: 角度推导与 $A, B, O, C$ 四点共圆
- **标题**：② 角度推导与 $A, B, O, C$ 四点共圆
- **讲解正文**：
  由于 $O$ 为 $\triangle RBC$ 的外心，圆心角 $\angle BOC = 2\angle BRC$。<br>
  在点 $R$ 处由平角关系有：$\angle BRC = 180^\circ - \angle BRD - \angle CRE$。<br>
  而在等腰 $\triangle DBR$ 和 $\triangle CER$ 中，两底角之和分别为 $2\angle BRD = 180^\circ - \angle ADE$，$2\angle CRE = 180^\circ - \angle AED$。<br>
  因此：$2\angle BRC = \angle ADE + \angle AED$。<br>
  在 $\triangle ADE$ 中，$\angle A + \angle ADE + \angle AED = 180^\circ$。<br>
  故 $\angle A + \angle BOC = 180^\circ$！四边形 $ABOC$ 对角互补，<b>$A, B, O, C$ 四点共圆</b>！<br>
  又因 $OB = OC$，$O$ 恰好落在 $BC$ 的垂直平分线上。
- **新增图元**：
  - 外接圆 $\odot(ABOC)$（浅青色虚线圆）；
  - 角弧标记：$\angle A$ 与 $\angle BOC$（对角互补强调）；
  - 对称轴高亮：确认 $O$ 位于 $BC$ 中垂线上。
- **擦除图元**：
  - 擦除 Step 1 中暂态的 $BR, CR$ 辅助连线与垂足直角标记（保持画面聚焦）。
- **色彩规范**：
  - 外接圆：浅青色 `CYAN (#0891b2)`；
  - 互补角弧：红色 `RED (#dc2626)`。

---

### Step 3: 轴反射对称与 $\triangle AD'E'$ 的内心
- **标题**：③ 轴反射对称与 $\triangle AD'E'$ 的内心
- **讲解正文**：
  以 $BC$ 的垂直平分线为对称轴作轴反射。<br>
  由于 $OB = OC$，$O$ 位于中垂线上，故 $O$ 的对称点为其自身！<br>
  直线 $l$ 对称至 $l'$，点 $R$ 对称至 $R' \in l'$，因此 $OR' = OR = OB = OC$。<br>
  由对称性与共圆角关系，$\angle OR'D' = \angle ORE = 180^\circ - \angle OBD'$，故 $O, B, D', R'$ 四点共圆。<br>
  结合 $OB = OR = OR'$，可知直线 $OD'$ 平分 $\angle AD'E'$，同理 $OE'$ 平分 $\angle AE'D'$。<br>
  即 <b>$O$ 亦为 $\triangle AD'E'$ 的内心</b>！
- **新增图元**：
  - 对称点 $R'$（在线段 $D'E'$ 上）；
  - 对称反射指引虚线 $R \leftrightarrow R'$（垂直于中垂线）；
  - 角平分线 $OD', OE'$（红色细实线）；
  - 线段 $OR'$（紫色实线）；
  - 角平分标记：$\angle AD'E'$ 与 $\angle AE'D'$ 处的双角弧。
- **擦除图元**：
  - 擦除 Step 2 的外接圆 $\odot(ABOC)$ 与角弧。
- **色彩规范**：
  - 对称元素 $R', l'$：紫色 `PURPLE (#7c3aed)`；
  - 角平分线：红色 `RED (#dc2626)`。

---

### Step 4: 截长构造点 $K$ 与 $\triangle OBD' \cong \triangle OKD'$
- **标题**：④ 截长构造点 $K$ 与 $\triangle OBD' \cong \triangle OKD'$
- **讲解正文**：
  在 $D'E'$ 上截取点 $K$，使得 $KD' = BD'$。<br>
  考虑 $\triangle OBD'$ 与 $\triangle OKD'$：<br>
  ① $D'B = D'K$（截长构造）；<br>
  ② $\angle BD'O = \angle KD'O$（$OD'$ 为内角平分线）；<br>
  ③ $OD' = OD'$（公共边）。<br>
  由边角边（SAS）判定：<b>$\triangle OBD' \cong \triangle OKD'$</b>！<br>
  由此全等得对应边 $OK = OB = OC$，且对应角 $\angle BOD' = \angle KOD'$。
- **新增图元**：
  - 点 $K$（在线段 $D'E'$ 上）；
  - 辅助线段 $OK$ 与 $OB$；
  - 全等三角形填充：$\triangle OBD'$ 与 $\triangle OKD'$ 浅蓝色微透填充；
  - 等长刻度标记：$BD' = KD'$（单绿色刻度）；
  - 对应角弧：$\angle BOD'$ 与 $\angle KOD'$。
- **擦除图元**：
  - 擦除 Step 3 的反射连线 $R \leftrightarrow R'$ 与角平分标记。
- **色彩规范**：
  - 第一对全等：浅蓝色 `rgba(37, 99, 235, 0.15)`；
  - 等长边与点 $K$：蓝色 `BLUE (#2563eb)`。

---

### Step 5: 导角计算与 $\triangle OCE' \cong \triangle OKE'$
- **标题**：⑤ 导角计算与 $\triangle OCE' \cong \triangle OKE'$
- **讲解正文**：
  在 $\triangle AD'E'$ 中，$O$ 为内心，故 $\angle D'OE' = 90^\circ + \frac{1}{2}\angle A$。<br>
  由 $A, B, O, C$ 共圆，有 $\angle BOC = 180^\circ - \angle A$。<br>
  由此可得两翼角之和：$\angle BOD' + \angle COE' = 360^\circ - \angle BOC - \angle D'OE' = 90^\circ + \frac{1}{2}\angle A$。<br>
  结合 Step 4 已证的 $\angle BOD' = \angle KOD'$，代入得：<br>
  $\angle KOD' + \angle COE' = \angle D'OE' = \angle KOD' + \angle KOE'$，两边消去 $\angle KOD'$，即得 <b>$\angle COE' = \angle KOE'$</b>！<br>
  在 $\triangle OCE'$ 与 $\triangle OKE'$ 中：$OC = OK$，$OE'$ 为公共边，夹角 $\angle COE' = \angle KOE'$。<br>
  由 SAS 判定：<b>$\triangle OCE' \cong \triangle OKE'$</b>！
- **新增图元**：
  - 全等三角形填充：$\triangle OCE'$ 与 $\triangle OKE'$ 浅橙色微透填充；
  - 辅助线段 $OC$；
  - 相等角弧标记：$\angle COE'$ 与 $\angle KOE'$（橙色角弧）；
  - 对应等长边 $OC = OK$。
- **擦除图元**：
  - 擦除 Step 4 的 $\triangle OBD'$ 蓝色全等填充。
- **色彩规范**：
  - 第二对全等：浅橙色 `rgba(234, 88, 12, 0.18)`；
  - 对应角与边：橙色 `ORANGE (#ea580c)`。

---

### Step 6: 对应边相等，原命题得证
- **标题**：⑥ 对应边相等，原命题得证
- **讲解正文**：
  由 $\triangle OCE' \cong \triangle OKE'$ 全等，立得对应边相等：<b>$CE' = KE'$</b>。<br>
  结合 Step 4 截长构造的 <b>$BD' = KD'$</b>，将两式相加：<br>
  $$D'E' = KD' + KE' = BD' + CE'$$<br>
  即 <b>$BD' + CE' = D'E'$</b>。<br>
  原命题完全得证！
- **新增图元**：
  - 高亮线段 $BD'$ 与 $KD'$（纯蓝色加粗辉光）；
  - 高亮线段 $CE'$ 与 $KE'$（纯橙色加粗辉光）；
  - 完整线段 $D'E'$ 顶层高亮展示拼接；
  - 点 $K$ 处的等长分段对比展示。
- **擦除图元**：
  - 擦除全部内部三角形填充与辅助角弧，只保留轮廓线与各段等长线段，极度干净明了。
- **色彩规范**：
  - $BD', KD'$：蓝色 `BLUE (#2563eb)`；
  - $CE', KE'$：橙色 `ORANGE (#ea580c)`；
  - 总结论 $D'E'$：紫色 `PURPLE (#7c3aed)`。
