# 例 3：四边形内对角线旋转相似与平行线角转换证明分步

## 题目回顾
在四边形 $ABCD$ 中，点 $K$ 在 $BD$ 上，点 $L$ 在 $CK$ 上且满足 $\angle BLK = \angle BDA$ ， $\angle BKL = \angle BAD$。作 $PK \parallel DL$ 与 $CD$ 的延长线交于点 $P$。证明：$\angle APK = \angle LBC$。

---

## 步骤规划

### Step 0: 已知条件与几何构型
- **标题**：✦ 已知条件与几何构型
- **正文**：
  在四边形 $ABCD$ 中，点 $K$ 位于对角线 $BD$ 上，点 $L$ 位于线段 $CK$ 上。<br>
  已知角相等关系：$\angle BLK = \angle BDA$，$\angle BKL = \angle BAD$。<br>
  过点 $K$ 作 $PK \parallel DL$ 交 $CD$ 的延长线于点 $P$。<br>
  <b>求证目标</b>：$\angle APK = \angle LBC$。
- **画面图元**：
  - 绘制四边形 $ABCD$ 及其对角线 $BD$、线段 $CK$。
  - 绘制线段 $DL$、延长线 $DP$ 及平行线 $PK$。
  - 标出各点 $A, B, C, D, K, L, P$。
  - 用橙色与绿色角弧分别标出已知相等的两组角 $\angle BLK = \angle BDA$ 与 $\angle BKL = \angle BAD$。
  - 用箭头标出平行关系 $PK \parallel DL$。

### Step 1: △BLK ∽ △BDA 与成对旋转相似 △ABK ∽ △DBL
- **标题**：① △BLK ∽ △BDA 与成对旋转相似 △ABK ∽ △DBL
- **正文**：
  由已知 $\angle BLK = \angle BDA$ 且 $\angle BKL = \angle BAD$，两角对应相等，可得：
  $$\triangle BLK \sim \triangle BDA$$
  从而对应边成比例且对应角相等：
  $$\frac{BL}{BK} = \frac{BD}{AB} \implies \frac{AB}{DB} = \frac{BK}{BL}, \quad \angle ABK = \angle DBL$$
  这构成绕点 $B$ 的<b>成对旋转相似</b>（Spiral Similarity），由此判定：
  $$\triangle ABK \sim \triangle DBL$$
  由相似对应边成比例，得核心比值关系式（①）：
  $$\frac{AK}{KB} = \frac{DL}{LB}$$
- **画面图元**：
  - 高亮 $\triangle ABK$（蓝色半透明填充）与 $\triangle DBL$（青色半透明填充）。
  - 用蓝色粗线加亮线段 $AK, KB$ 与 $DL, LB$。
  - 角弧标记顶角相等 $\angle ABK = \angle DBL$。

### Step 2: 作辅助平行线 KR // BL 建立比例链
- **标题**：② 作辅助平行线 KR // BL 建立比例链
- **正文**：
  过点 $K$ 作辅助线 $KR \parallel BL$，交 $CB$ 的延长线于点 $R$。<br>
  由平行线截线段成比例定理：
  - 在 $\triangle CPK$ 中，$DL \parallel PK \implies \frac{DL}{PK} = \frac{CL}{CK}$；
  - 在 $\triangle CRK$ 中，$BL \parallel RK \implies \frac{LB}{KR} = \frac{CL}{CK}$。<br>
  连结中间比 $\frac{CL}{CK}$，得到比例链（②）：
  $$\frac{DL}{PK} = \frac{LB}{KR} \implies \frac{DL}{LB} = \frac{PK}{KR}$$
  结合式① $\frac{AK}{KB} = \frac{DL}{LB}$，立即递推得到：
  $$\frac{AK}{KB} = \frac{PK}{KR} \quad \left(\text{即 } \frac{PK}{AK} = \frac{KR}{KB}\right)$$
- **画面图元**：
  - 显现辅助点 $R$ 及延长线 $CR$。
  - 用绿色虚线绘制辅助平行线 $KR$，并用双箭头标记 $KR \parallel BL$。
  - 保持紫色箭头标记 $PK \parallel DL$。
  - 绿色高亮线段 $PK, KR, AK, KB$ 呈现成比例线段对。

### Step 3: 平行与相似推得夹角相等 ∠RKB = ∠PKA
- **标题**：③ 平行与相似推得夹角相等 ∠RKB = ∠PKA
- **正文**：
  考察点 $K$ 处的射线方向与夹角关系：
  - 因为 $PK \parallel DL$ 且 $KR \parallel BL$，两组边方向分别平行，所以两角相等：
    $$\angle PKR = \angle DLB$$
  - 由 Step 1 的相似 $\triangle ABK \sim \triangle DBL$，对应角相等：
    $$\angle AKB = \angle DLB$$
  - 由此传递得：$\angle PKR = \angle AKB$。<br>
  两边同时减去公共角 $\angle AKR$（即从两全等大角中扣除公共部分）：
  $$\angle PKR - \angle AKR = \angle AKB - \angle AKR \implies \angle RKB = \angle PKA$$
- **画面图元**：
  - 用浅紫色弧线展示 $\angle PKR = \angle DLB = \angle AKB$。
  - 用醒目的橙色角弧高亮展示关键夹角 $\angle RKB$ 与 $\angle PKA$ 相等。
  - 连接线段 $AP$ 便于下一步观察。

### Step 4: SAS 判定 △RKB ∽ △PKA
- **标题**：④ SAS 判定 △RKB ∽ △PKA
- **正文**：
  综合 Step 2 的线段比与 Step 3 的夹角关系，考察 $\triangle RKB$ 与 $\triangle PKA$：
  1. <b>对应夹边成比例</b>：$\frac{AK}{KB} = \frac{PK}{KR} \implies \frac{PK}{AK} = \frac{KR}{KB}$；
  2. <b>夹角对应相等</b>：$\angle PKA = \angle RKB$。<br>
  根据两边成比例且夹角相等的判定定理（SAS），判定两三角形相似：
  $$\triangle RKB \sim \triangle PKA$$
- **画面图元**：
  - 橙色半透明高亮填充 $\triangle RKB$。
  - 珊瑚红色半透明高亮填充 $\triangle PKA$。
  - 加粗绘制边线 $PK, KA, AP$ 与 $KR, KB, BR$。

### Step 5: 对应角相等推得最终结论 ∠APK = ∠LBC
- **标题**：⑤ 得出最终结论 ∠APK = ∠LBC
- **正文**：
  由相似三角形 $\triangle RKB \sim \triangle PKA$ 对应角相等，得：
  $$\angle APK = \angle KRB$$
  又因为 $KR \parallel BL$，$R$ 位于 $CB$ 的延长线上（即 $C, B, R$ 共线），由平行线同位角性质得：
  $$\angle KRB = \angle LBC$$
  从而两步等量代换，严谨推得：
  $$\angle APK = \angle LBC$$
  <b>全题获证！</b>
- **画面图元**：
  - 红色加粗扇形与粗角弧突出显示目标角 $\angle APK$ 与 $\angle LBC$。
  - 用中间橙色弧标出桥梁角 $\angle KRB$，三角齐显展示等量代换链。
  - 整体图形各关键几何元素达到最完整和谐的收官呈现。
