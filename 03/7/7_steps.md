# 7 — 分步证明文字

## 步骤 0：初始构型与轴对称点定义

已知圆内接六边形 ABCDEF 满足 AB·CD·EF = BC·DE·AF。分别作点 B 关于直线 AC 的对称点 B₁、点 D 关于直线 CE 的对称点 D₁、点 F 关于直线 EA 的对称点 F₁。目标：证明新构成的三角形与原三角形相似，即 △B₁D₁F₁ ∽ △BDF。

## 步骤 1：角元塞瓦定理导出对角线共点于 P

在 △ACE 中考察三条主对角线 AD, BE, CF。由正弦定理与圆周角定理：sin∠ACF / sin∠ECF = AF / EF，sin∠BEC / sin∠BEA = BC / AB，sin∠EAD / sin∠CAD = DE / CD。三式相乘，代入题设条件 AB·CD·EF = BC·DE·AF：(AF/EF) · (BC/AB) · (DE/CD) = 1。由角元塞瓦定理逆定理，三对角线 AD, BE, CF 必交于一点 P！

## 步骤 2：轴对称与圆周角传递：∠PCD₁ = ∠F₁AP

由轴对称变换性质：• D₁ 关于 CE 对称于 D ⇒ D₁C = DC, ∠D₁CE = ∠DCE；• F₁ 关于 EA 对称于 F ⇒ F₁A = FA, ∠F₁AE = ∠FAE。根据同弧所对圆周角相等：∠ECD = ∠EAD，且 ∠FCE = ∠FAE = ∠F₁AE。计算顶角得：∠PCD₁ = ∠D₁CE - ∠PCE = ∠ECD - ∠FCE = ∠EAD - ∠F₁AE = ∠F₁AP！

## 步骤 3：相交弦比值导出 △D₁PC ∽ △F₁PA

在圆内接四边形中，相交弦 AD 与 CF 相交于 P。易知 △PCD ∽ △PFA，故对应边成比例：DC / CP = FA / AP。代入对称等长条件 D₁C = DC 和 F₁A = FA 得：D₁C / CP = F₁A / AP  ⟺  D₁C / F₁A = CP / AP。结合前一步已证夹角相等 ∠PCD₁ = ∠F₁AP，由两边成比例且夹角相等，判定 △D₁PC ∽ △F₁PA！

## 步骤 4：相似传递导出 △D₁PF₁ ∽ △DPF

由 △D₁PC ∽ △F₁PA，对应边成比例 D₁P / F₁P = PC / AP，且 ∠D₁PC = ∠F₁PA。考察夹角：∠D₁PF₁ = ∠D₁PC + ∠CPF₁ = ∠F₁PA + ∠CPF₁ = ∠CPA。由于对顶角相等，∠CPA = ∠DPF，故 ∠D₁PF₁ = ∠DPF！又相交弦有 △CPA ∽ △DPF ⇒ PC / AP = PD / PF，从而 D₁P / F₁P = PD / PF ⟺ D₁P / PD = F₁P / PF。结合夹角相等，证得 △D₁PF₁ ∽ △CPA ∽ △DPF！

## 步骤 5：轮换对称得出最终相似 △B₁D₁F₁ ∽ △BDF

同理，对点 B, B₁ 进行完全相同的轮换对称推导，得：• △B₁PF₁ ∽ △BPF ⇒ B₁F₁ / BF = B₁P / BP = F₁P / FP；• △B₁PD₁ ∽ △BPD ⇒ B₁D₁ / BD = B₁P / BP = D₁P / DP。综合各组对应比值，知三对对应边严格等比例：B₁D₁ / BD = D₁F₁ / DF = F₁B₁ / FB = λ。三边对应成比例，最终证得 △B₁D₁F₁ ∽ △BDF！命题得证。
