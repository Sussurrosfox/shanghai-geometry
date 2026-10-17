# 4 — 分步证明文字

## 步骤 0：已知条件与几何图形

在 $\bigtriangleup ABC$ 中，$AB < AC$。
           直线 $DE$ 为 $\angle BAC$ 的外角平分线。
           过点 $B$ 作 $BD \parallel AC$ 交外角平分线于 $D$；
           过点 $C$ 作 $CE \parallel AB$ 交外角平分线于 $E$。
           点 $F$ 是边 $AC$ 上一点，使得 $FC = AB$。
           求证：$DF = FE$。

## 步骤 1：① 延长 DB、EC 构造平行四边形 ABGC

延长 $DB$ 与 $EC$ 交于点 $G$，连接虚线 $GF$。
           由题设平行作法：
           $\because DG \parallel AC$（即 $BG \parallel AC$），$EG \parallel AB$（即 $CG \parallel AB$），
           $\therefore$ 四边形 $ABGC$ 为平行四边形。
           这一辅助平行四边形将分散的边长与平行条件统一串联起来。

## 步骤 2：② 外角平分线与平行线性质 ⇒ DG = GE

由 $EG \parallel AB$ 且直线 $DE$ 为截线，得内错角 $\angle DEG = \angle DAB$；
           同理由 $DG \parallel AC$，得内错角 $\angle ADG = \angle EAC$。
           又因为 $DE$ 是 $\angle BAC$ 的外角平分线，由平角两旁的对称性可知：
           $\angle DAB = \angle EAC = \frac{180^\circ - \angle BAC}{2}$。
           等量代换得：$\angle DEG = \angle ADG$。
           在 $\bigtriangleup DEG$ 中两底角相等，故 $\bigtriangleup DEG$ 为等腰三角形，即 $DG = GE$。

## 步骤 3：③ 利用平行四边形转化条件 ⇒ CG = CF

由平行四边形 $ABGC$ 对边相等，得 $CG = AB$。
           结合已知条件 $FC = AB$，立即得到：
           $CG = CF$。
           因此 $\bigtriangleup CGF$ 是以 $C$ 为顶点的等腰三角形，两底角相等：
           $\angle CGF = \angle CFG$。

## 步骤 4：④ 内错角转化得出 GF 平分 ∠DGE

由 $BG \parallel AC$，以 $GF$ 为截线，内错角相等：
           $\angle FGB = \angle CFG$。
           结合步骤 3 的等腰底角关系 $\angle CGF = \angle CFG$，推得：
           $\angle FGB = \angle CGF$。
           因为点 $B$ 在线段 $GD$ 上，点 $C$ 在线段 $GE$ 上，故：
           $\angle FGD = \angle FGB$，$\angle FGE = \angle CGF$。
           因此 $\angle FGD = \angle FGE$，即射线 $GF$ 为 $\angle DGE$ 的角平分线！

## 步骤 5：⑤ SAS 判定 △DFG ≌ △EFG ⇒ DF = FE

在 $\bigtriangleup DFG$ 与 $\bigtriangleup EFG$ 中：
           1. $DG = GE$（步骤 2 已证）；
           2. $\angle FGD = \angle FGE$（步骤 4 已证）；
           3. $FG = FG$（公共边）。
           由边角边（SAS）全等判定定理，可得：
           $\bigtriangleup DFG \cong \bigtriangleup EFG$。
           全等三角形对应边相等，故 $DF = FE$。命题得证！
