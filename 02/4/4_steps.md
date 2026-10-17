# 4 — 分步证明文字

## 步骤 0：已知条件与几何构型

在四边形 ABCD 中，点 K 位于对角线 BD 上，点 L 位于线段 CK 上。
已知角对应相等条件：
$\angle BLK = \angle BDA$，  $\angle BKL = \angle BAD$。
过点 K 作 $PK \parallel DL$ 与 CD 的延长线交于点 P。
【求证目标】：证明 $\angle APK = \angle LBC$。

## 步骤 1：成对旋转相似推出比例式 ①

由已知 $\angle BLK = \angle BDA$ 且 $\angle BKL = \angle BAD$，两角对应相等：
$\triangle BLK \sim \triangle BDA$
对应边成比例且对应顶角相等：
$\frac{BL}{BK} = \frac{BD}{AB} \iff \frac{AB}{DB} = \frac{BK}{BL}, \quad \angle ABK = \angle DBL$
两边成比例且夹角相等，构成绕点 B 的成对旋转相似：

  $\triangle ABK \sim \triangle DBL$

由此得出两对应边之比（式 ①）：

  ①   $\frac{AK}{KB} = \frac{DL}{LB}$

## 步骤 2：引入辅助平行线 KR 建立比例链

作辅助线 $KR \parallel BL$ 与 CB 的延长线交于点 R。
利用平行线分线段成比例定理：
• 在 $\triangle CPK$ 中，$DL \parallel PK \implies \frac{DL}{PK} = \frac{CL}{CK}$
• 在 $\triangle CRK$ 中，$BL \parallel RK \implies \frac{LB}{KR} = \frac{CL}{CK}$

  ②   $\frac{DL}{PK} = \frac{CL}{CK} = \frac{LB}{KR} \implies \frac{DL}{LB} = \frac{PK}{KR}$

结合式 ① $\frac{AK}{KB} = \frac{DL}{LB}$，立即递推得到：

  $\frac{AK}{KB} = \frac{PK}{KR} \iff \frac{PK}{AK} = \frac{KR}{KB}$

## 步骤 3：平行与相似推得夹角相等

考察绕点 K 的射线方向与夹角转换：
• 因 $PK \parallel DL$ 且 $KR \parallel BL$，两组边分别平行同向：
$\angle PKR = \angle DLB$
• 由 Step 1 的相似 $\triangle ABK \sim \triangle DBL$，对应角：
$\angle DLB = \angle AKB$
从而传递得到：$\angle PKR = \angle AKB$。
观察公共角与射线 $KB$：两相等大角减去公共部分：

  $\angle PKR - \angle AKR = \angle AKB - \angle AKR \implies \angle RKB = \angle PKA$

## 步骤 4：SAS 相似判定 △RKB ∽ △PKA

综合 Step 2 的线段比例与 Step 3 的夹角关系，观察 $\triangle RKB$ 与 $\triangle PKA$：
1. 对应夹边成比例：$\frac{PK}{AK} = \frac{KR}{KB}$ （由 Step 2 推得）；
2. 对应夹角相等：$\angle PKA = \angle RKB$ （由 Step 3 推得）。
根据两边成比例且夹角相等的三角形相似判定定理（SAS）：

  $\triangle RKB \sim \triangle PKA$

## 步骤 5：对应角相等得出最终结论

由相似三角形 $\triangle RKB \sim \triangle PKA$ 对应角相等，得：
$\angle APK = \angle KRB$
又因为 $KR \parallel BL$，$R$ 位于 $CB$ 的延长线上（$C, B, R$ 共线），由平行线同位角性质：
$\angle KRB = \angle LBC$
综上两步等量代换，严密推得：

  $\angle APK = \angle LBC$

全命题获证！
