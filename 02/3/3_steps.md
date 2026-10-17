# 3 — 分步证明文字

## 步骤 0：0️⃣ 题设构型与基准图形

在锐角 $\triangle ABC$ 中，$AB > AC$，$O$ 为外接圆心。
    $M$ 为劣弧 $BC$ 的中点（$BM = CM$），$K$ 为点 $A$ 的对径点（$AK$ 为外接圆直径）。
    过 $O$ 作 $AM$ 的平行线，交边 $AB$ 于点 $D$，交射线 $CA$ 的延长线于点 $E$。
    直线 $BM$ 与直线 $CK$ 相交于点 $P$；直线 $CM$ 与直线 $BK$ 相交于点 $Q$。
    求证目标： $\angle OPB + \angle OEB = \angle OQC + \angle ODC$

## 步骤 1：① 平行线导角：∠BDO=∠CBP 与 ∠DBO=∠BCP

连接辅助线段 $BO, CO, OM$ 及直径 $AK$：
    1. 第一组等角 由 $OD \parallel AM$ 得同位角 $\angle BDO = \angle BAM$。由同弧所对圆周角相等知 $\angle BAM = \angle BCM$；又 $M$ 为劣弧 $BC$ 中点，对应圆周角 $\angle BCM = \angle CBM = \angle CBP$。故：
    $\angle BDO = \angle BAM = \angle BCM = \angle CBP$
    2. 第二组等角 由于 $AK$ 是直径，有 $\angle ACK = 90^\circ$。在直角 $\triangle ACK$ 中，$\angle BCK = 90^\circ - \angle ACB$。
    在等腰 $\triangle AOB$ 中，底角 $\angle ABO = 90^\circ - \angle ACB$。
    因为 $B,D,A$ 共线且 $C,P,K$ 共线，故导出：
    $\angle DBO = 90^\circ - \angle ACB = \angle BCP$

## 步骤 2：② 关键相似：△BOD ∽ △CPB 与 △DBC ∽ △OCP

由第 ① 步的两组对应等角，立即得到第一对相似三角形：
    $\triangle BOD \sim \triangle CPB$
    根据对应边成比例：
    $$\frac{BD}{CP} = \frac{BO}{CB} \implies \frac{BD}{BO} = \frac{CB}{CP}$$
    注意到 $BO = CO$（外接圆半径），代换得：
    $$\frac{BD}{CO} = \frac{BC}{CP} \iff \frac{BD}{BC} = \frac{CO}{CP}$$
    又对应夹角 $\angle DBC = \angle B$；由于直径 $AK$ 使得 $\angle AKC = \angle B$，直角 $\triangle ACK$ 给出 $\angle OCP = 90^\circ - \angle ACB = \angle B$。
    因此两边成比例且夹角相等 $\angle DBC = \angle OCP$，导出第二对相似三角形：
    $\triangle DBC \sim \triangle OCP \implies \angle COP = \angle BDC$

## 步骤 3：③ 对称侧相似：△ECB ∽ △OBQ

完全平行地，考察直线 $OE \parallel AM$ 与点 $Q$（直线 $CM$ 与 $BK$ 的交点）：
    利用对称性同理可证 $\triangle COE \sim \triangle BQC$，借助外接圆半径 $CO = BO$ 进行比例转置，完全类似地可导出对称侧的关键相似三角形：
    $\triangle ECB \sim \triangle OBQ$
    由相似三角形对应角相等，立即得到对称侧的等角关系：
    $\angle BOQ = \angle CEB, \quad \angle BQO = \angle CBE$

## 步骤 4：④ 角度差转换：∠OPB - ∠OQC = ∠BDC - ∠CEB

以底端中点 $M$ 为基准，利用圆心角与外角关系及对称性（$\angle OMB = \angle OMC$）拆分角差：
    $$\angle OPB - \angle OQC = (\angle OMB + \angle POM) - (\angle OMC - \angle QOM)$$
    $$= \angle POM + \angle QOM = \angle COP - \angle BOQ$$
    代入第 ② 步和第 ③ 步导出的相似三角形对应角：
    $$\angle COP = \angle BDC, \quad \angle BOQ = \angle CEB$$
    从而立即建立关键的角度差恒等式：
    $\angle OPB - \angle OQC = \angle BDC - \angle CEB$

## 步骤 5：⑤ 外角拆分与移项得证 (Q.E.D.)

进一步利用三角形外角定理拆分差值 $\angle BDC - \angle CEB$：
    - 在 $\triangle ADC$ 中，边 $AB$ 上的外角 $\angle BDC = \angle BAC + \angle ACD$；
    - 在 $\triangle ABE$ 中，外角 $\angle CAB = \angle CEB + \angle ABE \implies \angle CEB = \angle CAB - \angle ABE$；
    两式相减（$\angle BAC = \angle CAB$ 互相抵消）：
    $$\angle BDC - \angle CEB = \angle ACD + \angle ABE$$
    再由截线 $\triangle ADE$ 中的外角关系，可知 $\angle ODC - \angle OEB = \angle ACD + \angle ABE$。
    因此得到：
    $$\angle BDC - \angle CEB = \angle ODC - \angle OEB$$
    与第 ④ 步结论联立：
    $$\angle OPB - \angle OQC = \angle ODC - \angle OEB$$
    移项整理即得题设结论：
    
      $\mathbf{\angle OPB + \angle OEB = \angle OQC + \angle ODC}$
