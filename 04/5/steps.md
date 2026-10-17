# 题目 04/5（例 4）分步证明与可视化规划

## 命题信息
- **题源**：例 4（第 4 章：垂心与正三角形）
- **题面**：在锐角 $\triangle ABC$ 中，$\angle A > 60^\circ$，$H$ 为 $\triangle ABC$ 的垂心，$M, N$ 分别在边 $AB, AC$ 上，且满足 $\angle HMB = \angle HNC = 60^\circ$。$O$ 为 $\triangle HMN$ 的外心，$D$ 使得 $\triangle DBC$ 为正三角形（且 $A, D$ 在 $BC$ 同侧）。证明：$H, O, D$ 三点共线。

---

## 几何坐标系设计
- **参数选择**：取 $BC = 10$，$\angle B = 66^\circ$，$\angle C = 49^\circ \implies \angle A = 65^\circ > 60^\circ$。
- **顶点坐标（笛卡尔系，原点 $B(0,0)$）**：
  - $B = (0.0000, 0.0000)$
  - $C = (10.0000, 0.0000)$
  - $A = (3.3870, 7.6074)$
  - $H = (3.3870, 2.9443)$（垂心）
  - $D = (5.0000, 8.6603)$（等边三角形顶点，在 $BC$ 同侧）
  - $M = (2.0997, 4.7161)$（在边 $AB$ 约 $62\%$ 处，$\angle HMB = 60^\circ$）
  - $N = (4.5371, 6.2844)$（在边 $AC$ 约 $83\%$ 处，$\angle HNC = 60^\circ$）
  - $O = (3.8675, 4.6469)$（$\triangle HMN$ 的外心，$R \approx 1.7691$）
  - $H' = (-0.7567, 7.1992)$（$H$ 绕 $D$ 顺时针旋转 $60^\circ$ 的象点）
- **三点共线验证**：
  - $\vec{HD} = (1.6130, 5.7160)$，模长 $\approx 5.9392$
  - $\vec{HO} = (0.4805, 1.7026)$，模长 $\approx 1.7691$
  - $\vec{HO} \times \vec{HD} = 0.4805 \times 5.7160 - 1.7026 \times 1.6130 = 0.0000$（严格共线，误差 $< 10^{-14}$）
  - 次序关系：$H - O - D$，其中 $O$ 恰好在外接圆上与 $H$ 的连线上，同时指向 $D$。

---

## 步骤规划清单（共 7 步，0 ~ 6）

### 第 0 步：已知条件与几何构型
- **标题**：已知条件与几何构型
- **数学逻辑**：给定锐角 $\triangle ABC$（$\angle A > 60^\circ$），垂心 $H$；边 $AB, AC$ 上有点 $M, N$ 满足 $\angle HMB = \angle HNC = 60^\circ$；$\triangle DBC$ 为正三角形；$O$ 为 $\triangle HMN$ 外心。目标是证明 $H, O, D$ 三点共线。
- **新增图元**：
  - 基础三角形 $ABC$（实线深色边框）
  - 垂心 $H$ 及高线脚印（轻色点划线）
  - 点 $M, N$ 及线段 $HM, HN$
  - 正三角形 $\triangle DBC$（琥珀色细线）
  - $\triangle HMN$ 外接圆 $\odot(HMN)$（半透明浅青色虚线圆）与圆心 $O$
  - 角弧标记：$\angle HMB = 60^\circ$、$\angle HNC = 60^\circ$
- **擦除图元**：无
- **色彩约定**：
  - $\triangle ABC$：基准深灰蓝 `#334155`
  - 正三角形 $\triangle DBC$：橙色 `#ea580c`
  - $M, N, H$ 及外接圆：青色 `#0891b2` 与天蓝 `#2563eb`

### 第 1 步：垂心角性质与第一对相似 $\triangle MHB \sim \triangle NHC$
- **标题**：① 垂心角性质与第一对相似 $\triangle MHB \sim \triangle NHC$
- **数学逻辑**：
  - $H$ 为垂心 $\implies BH \perp AC, CH \perp AB$
  - 从而 $\angle ABH = 90^\circ - \angle A = \angle ACH$
  - 结合已知 $\angle HMB = \angle HNC = 60^\circ$
  - 两角对应相等 $\implies \triangle MHB \sim \triangle NHC$
  - 导出比例式：$\frac{MH}{NH} = \frac{BH}{HC}$
- **新增图元**：
  - 高亮 $\triangle MHB$（蓝色半透明填充，轮廓加粗）
  - 高亮 $\triangle NHC$（绿色半透明填充，轮廓加粗）
  - 角弧：$\angle HMB$ 与 $\angle HNC$（$60^\circ$ 红色圆弧）
  - 角弧：$\angle ABH$ 与 $\angle ACH$（双弧高亮）
  - 对应边 $MH, NH$ 与 $BH, HC$ 高亮线段
- **擦除图元**：第 0 步的外接圆与 $D$ 点连线暂时淡化/隐藏，聚焦于下部两三角形。

### 第 2 步：绕点 $D$ 旋转构造全等 $\triangle DBH' \cong \triangle DCH$
- **标题**：② 绕点 $D$ 旋转构造全等 $\triangle DBH' \cong \triangle DCH$
- **数学逻辑**：
  - 将 $H$ 绕 $D$ 顺时针旋转 $60^\circ$ 得到 $H'$
  - 则 $\triangle DH'H$ 为正三角形（$DH' = DH, \angle H'DH = 60^\circ$）
  - 由于 $\triangle DBC$ 为正三角形，$DC$ 顺时针旋转 $60^\circ$ 与 $DB$ 重合
  - 故 $\triangle DCH$ 顺时针旋转 $60^\circ$ 变为 $\triangle DBH'$
  - 得 $\triangle DBH' \cong \triangle DCH \implies H'B = HC$ 且 $\angle DBH' = \angle DCH$
  - 将 $HC = H'B$ 代入比例式得：$\frac{MH}{NH} = \frac{BH}{B{H}'}$
- **新增图元**：
  - 点 $H'$、线段 $DH', BH', HH'$
  - 正三角形 $\triangle DH'H$（等边黄色虚线及等长短横线 mark）
  - 全等三角形 $\triangle DBH'$ 与 $\triangle DCH$（对比色半透明填充）
  - 顺时针旋转引导弧 $H \to H'$ 与 $C \to B$
- **擦除图元**：第 1 步的 $\triangle MHB, \triangle NHC$ 填充与角弧。

### 第 3 步：外角分解与夹角相等 $\angle MHN = \angle HBH'$
- **标题**：③ 角度外角分解与夹角相等 $\angle MHN = \angle HBH'$
- **数学逻辑**：
  - 在 $\triangle AHN$ 中外角：$\angle AHN = \angle CNH - \angle CAH = 60^\circ - (90^\circ - \angle C) = \angle C - 30^\circ$
  - 在正三角形 $\triangle DBC$ 中：$\angle DBH = \angle DBC - \angle CBH = 60^\circ - (90^\circ - \angle C) = \angle C - 30^\circ$
  - 从而 $\angle AHN = \angle DBH$
  - 同理 $\angle AHM = \angle DCH = \angle DBH'$
  - 相加得：$\angle MHN = \angle AHM + \angle AHN = \angle DBH' + \angle DBH = \angle HBH'$
- **新增图元**：
  - 高线射线 $AH$（垂直 $BC$）
  - 拆分角弧：$\angle AHN$ 与 $\angle DBH$（用青色双弧标出）
  - 拆分角弧：$\angle AHM$ 与 $\angle DBH'$（用紫红双弧标出）
  - 合成大角 $\angle MHN$ 与 $\angle HBH'$ 外框高亮
- **擦除图元**：第 2 步的全等三角形填充及旋转弧。

### 第 4 步：第二对相似 $\triangle H'BH \sim \triangle NHM$
- **标题**：④ 第二对相似 $\triangle H'BH \sim \triangle NHM$
- **数学逻辑**：
  - 由 $\frac{MH}{NH} = \frac{BH}{BH'} \implies \frac{NH}{MH} = \frac{BH'}{BH}$
  - 且夹角 $\angle MHN = \angle HBH'$
  - 满足两边对应成比例且夹角相等判定定理
  - 得 $\triangle H'BH \sim \triangle NHM$
  - 对应角相等：$\angle MNH = \angle H{H}'B$
  - 又 $\angle H{H}'B = \angle D{H}'B - \angle D{H}'H = \angle DHC - 60^\circ$
- **新增图元**：
  - 高亮 $\triangle H'BH$（紫罗兰色填充）与 $\triangle NHM$（天蓝色填充）
  - 标记对应角 $\angle MNH$ 与 $\angle HH'B$（同色强调角弧）
  - 标识角差 $\angle DH'B - \angle DH'H$
- **擦除图元**：第 3 步的细分小角弧与高线射线。

### 第 5 步：外心性质与圆心角-圆周角转化
- **标题**：⑤ 外心 $O$ 的圆心角-圆周角转换
- **数学逻辑**：
  - $O$ 为 $\triangle HMN$ 外心 $\implies OM = OH = ON$
  - 由圆周角定理：顶角 $\angle MOH = 2\angle MNH$
  - 在等腰 $\triangle MOH$ 中两底角相等：
    $\angle MHO = \frac{180^\circ - \angle MOH}{2} = 90^\circ - \angle MNH$
  - 代入 $\angle MNH = \angle DHC - 60^\circ$：
    $\angle MHO = 90^\circ - (\angle DHC - 60^\circ) = 150^\circ - \angle DHC$
- **新增图元**：
  - 显现 $\triangle HMN$ 外接圆 $\odot(HMN)$ 与外心 $O$
  - 半径线段 $OM, OH$（细实线）
  - 圆心角 $\angle MOH$ 与圆周角 $\angle MNH$ 对比弧线
  - 底角 $\angle MHO$ 醒目高亮弧
- **擦除图元**：第 4 步中 $\triangle H'BH$ 的大色块填充，视线聚焦于外心 $O$。

### 第 6 步：垂直轴对称代换，得出 $H, O, D$ 三点共线
- **标题**：⑥ 角度等量代换得出 $H, O, D$ 三点共线
- **数学逻辑**：
  - $BC$ 中垂线为正三角形对称轴，平分 $\angle BDC = 60^\circ \implies$ 半角为 $30^\circ$
  - $AH \perp BC \implies AH$ 平行于中垂线
  - 算得 $\angle AHD = 30^\circ - \angle BDH$
  - 从而 $\angle HDC = 60^\circ - \angle BDH = 30^\circ + \angle AHD$
  - 在 $\triangle DHC$ 中内角和为 $180^\circ$：
    $\angle DHC = 180^\circ - (\angle AHD + 30^\circ) - \angle DCH = 150^\circ - (\angle AHD + \angle AHM) = 150^\circ - \angle MHD$
  - 变形得到：$\angle MHD = 150^\circ - \angle DHC$
  - 结合第 5 步：$\angle MHO = 150^\circ - \angle DHC$
  - 故 $\angle MHO = \angle MHD$！
  - 射线 $HO$ 与射线 $HD$ 在 $HM$ 同侧且夹角相等 $\implies H, O, D$ 三点共线！
- **新增图元**：
  - 贯穿金色高亮直线/线段 $H-O-D$（醒目光晕与主轴）
  - 角重合对比：$\angle MHO$ 与 $\angle MHD$ 弧线完美叠合
  - 完工胜利印章（Q.E.D. 徽标提示）
- **擦除图元**：擦除过程辅助线，只保留 $H-O-D$ 核心主轴与基础三角形构架，宏伟清晰。
