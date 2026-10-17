# 题目 06/5（例 4）分步证明规划与图元清单

## 命题陈述
**题目**：设圆 $O$ 为 $\triangle ABC$ 的外接圆，点 $K$ 在边 $BC$ 上且不为 $BC$ 的中点，$D$ 为 $AK$ 延长线上一点，$AB$ 与 $CD$ 的延长线交于点 $E$，$AC$ 与 $BD$ 的延长线交于点 $F$，且 $OK \bot EF$。证明：$D$ 在圆 $O$ 上。

---

## 颜色约定规范
- **默认/基础底色**：
  - 外接圆 $O$：`#64748b`（石板灰，线宽 1.8）
  - 三角形 $ABC$ 及基本线段：`#1e293b`（深青灰，线宽 2）
  - 点标记：`#0f172a`（深色，白色描边，半径 4.5）
- **动态步骤主题色**：
  - **蓝色 (`#2563eb`)**：直线 $EF$、点 $E, F$、圆 $ABHF$、最终内接圆周
  - **绿色 (`#059669`)**：辅助圆 $OBHC$、弦 $OB, OC$ 等距标记
  - **红色 (`#dc2626`)**：垂直关系 $OK \bot EF$、垂足 $H$、直角标记、关键相等角弧
  - **紫色 (`#7c3aed`)**：完全四边形对角线、调和点列 $(G, K; B, C)$、圆 $AEHC$
  - **橙色 (`#ea580c`)**：密克点几何构型、辅助圆 $CDHF$
  - **青色 (`#0891b2`)**：辅助圆 $BDHE$、最终相等圆周角

---

## 分步规划表

### 步骤 0：已知条件与几何构型
- **标题**：已知条件与几何构型
- **数学逻辑**：
  - 给定 $\triangle ABC$ 及其外接圆 $O$；
  - $K$ 为边 $BC$ 上一点（非中点），$D$ 在射线 $AK$ 上；
  - 延长 $AB$ 与 $CD$ 相交于 $E$，延长 $AC$ 与 $BD$ 相交于 $F$；
  - 延长 $OK$ 与 $EF$ 交于点 $H$，$CB$ 与 $FE$ 延长线交于点 $G$；
  - 条件：$OK \bot EF$（垂足为 $H$）；
  - 求证：$D$ 落在圆 $O$ 上。
- **新增图元**：
  - 底层基准图形：外接圆 $O$、$\triangle ABC$、射线 $AD$ 及点 $D$；
  - 延长线：$BE$（虚线）、$DE$（虚线）、$CF$（虚线）、$DF$（虚线）；
  - 直线 $EF$ 及延长线 $EG$（实线）；
  - 射线 $OH$ 及垂线段 $KH$（红色粗线）；
  - 直角标记：$\angle OHF$（或 $\angle GHK = 90^\circ$）；
  - 标注关键点：$A, B, C, D, E, F, G, H, K, O$。
- **擦除图元**：无（初始构型）。

---

### 步骤 1：完全四边形调和分割 $\Longrightarrow$ $HK$ 平分 $\angle BHC$
- **标题**：完全四边形调和分割 $\Longrightarrow$ $HK$ 平分 $\angle BHC$
- **数学逻辑**：
  - 考察由四条直线构成的完全四边形 $ABEDCF$；
  - 其三条对角线为 $BC, AD, EF$；
  - 对角线 $BC$ 分别与另两条对角线 $AD, EF$ 交于点 $K$ 和点 $G$；
  - 由完全四边形调和性质，对角线 $BC$ 被对角线 $AD, EF$ 调和分割，即 $(G, K; B, C) = -1$，$G, B, K, C$ 为调和点列；
  - 又已知 $OK \bot EF \implies \angle GHK = 90^\circ$；
  - 根据阿波罗尼斯调和角平分线引理：当四点形成调和点列且视点张角为直角时，两射线分别平分两射线夹角及其外角；
  - 因此 $HK$ 平分 $\angle BHC$（即 $\angle BHO = \angle CHO$），$HG$ 平分 $\angle BHC$ 的外角。
- **新增图元**：
  - 紫色高亮直线 $BC$ 上的调和点列：点 $G, B, K, C$；
  - 连线 $HB$ 与 $HC$（橙黄色/紫色实线）；
  - 角弧标记：$\angle BHO$ 与 $\angle CHO$（带双弧/单弧标记，表示角相等）；
  - 直角标记：$\angle GHK = 90^\circ$。
- **擦除图元**：清空与本步调和分析无关的杂乱延伸线。

---

### 步骤 2：外心等距性质 $\Longrightarrow$ $O, B, H, C$ 四点共圆
- **标题**：外心等距性质 $\Longrightarrow$ $O, B, H, C$ 四点共圆
- **数学逻辑**：
  - 因为 $O$ 为 $\triangle ABC$ 的外接圆圆心，故 $OB = OC$；
  - 这意味着点 $O$ 落在底边 $BC$ 的垂直平分线上；
  - 由步骤 1 知，射线 $HO$ 平分顶角 $\angle BHC$；
  - 在 $\triangle BHC$ 中，顶角平分线 $HO$ 与底边垂直平分线交于 $\triangle BHC$ 外接圆对应弧 $BC$ 的中点；
  - 由于 $OB = OC$，点 $O$ 恰好是该交点，从而点 $O$ 必然位于 $\triangle BHC$ 的外接圆上；
  - 结论：$O, B, H, C$ 四点共圆！
- **新增图元**：
  - 绿色虚线圆 $\odot(OBHC)$，标明圆心与圆周；
  - 连线 $OB, OC$（绿色粗实线）；
  - 等长刻度线：$OB = OC$；
  - 保持射线 $HO$ 平分 $\angle BHC$ 的角弧高亮。
- **擦除图元**：擦除调和点列高亮，聚焦点 $O, B, H, C$ 共圆结构。

---

### 步骤 3：圆周角转移 $\Longrightarrow$ $A, B, H, F$ 与 $A, E, H, C$ 共圆
- **标题**：圆周角转移 $\Longrightarrow$ $A, B, H, F$ 与 $A, E, H, C$ 共圆
- **数学逻辑**：
  - 由 $O, B, H, C$ 四点共圆，同弧所对圆周角相等：$\angle BHO = \angle BCO$；
  - 因 $OK \bot EF$，有 $\angle EHO = 90^\circ$，因此：
    $$\angle EHB = 90^\circ - \angle BHO = 90^\circ - \angle BCO$$
  - 在外接圆 $\odot O$ 中，由 $OB = OC$ 及圆周角定理：$\angle BCO = 90^\circ - \angle BAC$；
  - 代入得：
    $$\angle EHB = 90^\circ - (90^\circ - \angle BAC) = \angle BAC = \angle EAF$$
  - 在四边形 $ABHF$ 中，外角 $\angle EHB$ 等于内对角 $\angle EAF$，判定 $A, B, H, F$ 四点共圆！
  - 同理完全对称可得：$A, E, H, C$ 四点共圆。
- **新增图元**：
  - 绘制辅助圆 $\odot(ABHF)$（浅蓝色虚线）和 $\odot(AEHC)$（浅紫色虚线）；
  - 红色高亮角弧：$\angle EHB$ 与 $\angle BAC$；
  - 连线 $AH, HF, HE$；
  - 直角标记 $\angle EHO = 90^\circ$。
- **擦除图元**：淡化 $\odot(OBHC)$，仅保留关键角弧与共圆结构。

---

### 步骤 4：密克点定理 $\Longrightarrow$ $C, D, H, F$ 与 $B, D, H, E$ 共圆
- **标题**：密克点定理 $\Longrightarrow$ $C, D, H, F$ 与 $B, D, H, E$ 共圆
- **数学逻辑**：
  - 考察由直线 $AB(E), AC(F), CD(E), BD(F)$ 构成的完全四边形，其围成的四个三角形为：
    $\triangle AEF, \triangle ABC, \triangle CDE, \triangle BDF$；
  - 根据完全四边形的密克定理（Miquel's Theorem）：四个三角形的外接圆共于一点（即密克点）；
  - 已证 $H$ 既在 $\odot(ABHF)$ 上，也在 $\odot(AEHC)$ 上，说明 $H$ 恰为该完全四边形的密克点；
  - 因此，其余两个三角形的外接圆也必经过点 $H$：
    - $C, D, H, F$ 四点共圆（即 $H \in \odot(CDF)$）；
    - $B, D, H, E$ 四点共圆（即 $H \in \odot(BDE)$）。
- **新增图元**：
  - 绘制圆 $\odot(CDHF)$（橙色虚线）与圆 $\odot(BDHE)$（青色虚线）；
  - 密克点 $H$ 显著高亮（作为四个外接圆的共同交点）；
  - 连线 $HD$（高亮实线）；
  - 展示关键等角角弧：$\angle ABD = \angle EHD = \angle DCF$。
- **擦除图元**：擦除之前的多余角弧，凸显圆 $CDHF$ 与 $BDHE$ 对点 $D$ 的控制。

---

### 步骤 5：同弧圆周角与外角相等 $\Longrightarrow$ $D$ 在圆 $O$ 上，命题得证
- **标题**：同弧圆周角与外角相等 $\Longrightarrow$ $D$ 在圆 $O$ 上，命题得证
- **数学逻辑**：
  - 在圆 $\odot(BDHE)$ 中，同弧 $DE$ 所对圆周角相等：$\angle ABD = \angle EHD$；
  - 在圆 $\odot(CDHF)$ 中，同弧 $DF$ 所对圆周角相等：$\angle EHD = \angle DCF$；
  - 于是：$\angle ABD = \angle EHD = \angle DCF$；
  - 因为点 $F$ 在 $AC$ 的延长线上，四边形 $ABDC$ 的外角 $\angle DCF$ 等于内对角 $\angle ABD$（即对角互补 $\angle ABD + \angle ACD = 180^\circ$），判定 $A, B, C, D$ 四点共圆！
  - 又因圆 $O$ 是 $\triangle ABC$ 的外接圆，平面上过不共线三点 $A, B, C$ 的圆唯一确定；
  - 因此点 $D$ 必落在圆 $O$ 上，原命题全部得证！
- **新增图元**：
  - 高亮外接圆 $\odot O$（鲜明蓝色实线加光晕）；
  - 高亮内接四边形 $ABDC$ 的边；
  - 红色角弧高亮关键外角与内对角：$\angle ABD$ 与 $\angle DCF$；
  - 闪耀点 $D$ 与圆周顶点 $A, B, C$；
  - 弹出结论信息徽章。
- **擦除图元**：擦除所有过程辅助圆与辅助线，画面回归极致清爽与焦点突出。
