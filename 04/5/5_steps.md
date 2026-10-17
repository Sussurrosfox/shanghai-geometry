# 5 — 分步证明文字

## 步骤 0：已知条件与几何构型

在锐角 ΔABC 中，∠A > 60°，H 为垂心。
    点 M, N 分别在边 AB, AC 上，满足 ∠HMB = ∠HNC = 60°。
    O 为 ΔHMN 的外心。
    以 BC 为边在 A 同侧作正三角形 ΔDBC。
    目标：证明 H, O, D 三点共线。

## 步骤 1：① 垂心角与第一对相似 △MHB ∼ △NHC

因为 H 为 ΔABC 的垂心，所以高线与对边垂直：
    ∠ABH = ∠ACH = 90° - ∠A。
    又由题设已知：∠HMB = ∠HNC = 60°。
    两组对应角分别相等，故两三角形相似：
    ΔMHB ∼ ΔNHC &implies; MH / NH = BH / HC

## 步骤 2：② 绕点 D 旋转 60° 构造全等 △DBH' ≅ △DCH

将点 H 绕正三角形顶点 D 顺时针旋转 60° 得到点 H'。
    • 由旋转定义，ΔDH'H 为正三角形。
    • 由于 ΔDBC 是正三角形，边 DC 绕 D 顺时针旋转 60° 恰与边 DB 重合。
    因此整个三角形旋转对应：
    ΔDBH' ≅ ΔDCH &implies; H'B = HC 且 ∠DBH' = ∠DCH
    将 HC = H'B 代入前式比例，得到：
    MH / NH = BH / BH'   (式 ∞)

## 步骤 3：③ 角度外角分解与夹角相等 ∠MHN = ∠HBH'

在 ΔAHN 中利用外角定理展开：
    ∠AHN = ∠CNH - ∠CAH = 60° - (90° - ∠C) = ∠C - 30°。
    而在正三角形 ΔDBC 中：
    ∠DBH = ∠DBC - ∠CBH = 60° - (90° - ∠C) = ∠C - 30°。
    因此：∠AHN = ∠DBH。
    同理可证：∠AHM = ∠DCH = ∠DBH'。
    两式相加合成大角：
    ∠MHN = ∠AHM + ∠AHN = ∠DBH' + ∠DBH = ∠HBH'   (式 §)

## 步骤 4：④ 第二对相似 △H'BH ∼ △NHM

由式 ∞ 与式 §：
    对应边成比例：NH / MH = BH' / BH，且夹角相等：∠MHN = ∠HBH'。
    根据边角边判定定理，两三角形相似：
    ΔH'BH ∼ ΔNHM
    从而对应角相等：
    ∠MNH = ∠HH'B = ∠DH'B - ∠DH'H = ∠DHC - 60°

## 步骤 5：⑤ 外心 O 的圆心角-圆周角转化

因为 O 是 ΔHMN 的外心，故 OM = OH = ON。
    由圆周角与圆心角定理，顶角 ∠MOH = 2∠MNH。
    在等腰 ΔMOH 中，两底角相等：
    ∠MHO = (180° - ∠MOH) / 2 = 90° - ∠MNH
    代入前一步结论 ∠MNH = ∠DHC - 60°：
    ∠MHO = 90° - (∠DHC - 60°) = 150° - ∠DHC

## 步骤 6：⑥ 角度等量代换得出 H, O, D 三点共线

因为 AH ⊥ BC，而正三角形 ΔDBC 的对称轴为 BC 垂直平分线，故 AH 平行于中垂线。
    由角度关系推得：
    ∠AHD = 30° - ∠BDH &implies; ∠HDC = 30° + ∠AHD。
    在 ΔDHC 中：
    ∠DHC = 180° - ∠HDC - ∠DCH = 180° - (∠AHD + 30°) - ∠AHM
    ∠DHC = 150° - (∠AHD + ∠AHM) = 150° - ∠MHD
    整理得到：∠MHD = 150° - ∠DHC。
    与上一步 ∠MHO = 150° - ∠DHC 对比，立即得出：
    ∠MHO = ∠MHD
    由于射线 HO 与射线 HD 在 HM 同侧且夹角相等，射线重合，故 H, O, D 三点共线！
    ✓ 命题获证 (Q.E.D.)
