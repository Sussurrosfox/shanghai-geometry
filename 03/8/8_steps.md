# 8 — 分步证明文字

## 步骤 0：已知条件与几何构型

给定锐角 $\triangle ABC$，其外心为 $O$（外接圆半径为 $R$），垂心为 $H$（三条高线的交点）。
           求证：在边 $BC, CA, AB$ 上分别存在点 $D, E, F$，满足：
           1. 折线长恒等：$OD + DH = OE + EH = OF + FH$
           2. 连线共点：$AD, BE, CF$ 三线共点。

## 步骤 1：垂心对称点落在外接圆上

设垂心 $H$ 关于三边 $BC, CA, AB$ 的对称点分别为 $A', B', C'$。
           垂心经典性质：
           $\angle BHC = 180^\circ - \angle A$。
           因为 $A'$ 与 $H$ 关于 $BC$ 对称，所以 $\triangle B A' C \cong \triangle BHC$，从而：
           $\angle B A' C = \angle BHC = 180^\circ - \angle A$。
           由于四边形 $A B A' C$ 对角互补，$A'$ 必落在 $\triangle ABC$ 的外接圆 $\odot O$ 上！
           同理，$B', C'$ 亦均落在外接圆 $\odot O$ 上。

## 步骤 2：射线确定点 D, E, F 且折线长恒等于 R

连结圆心 $O$ 与外接圆上的对称点：
           设线段 $OA'$ 与 $BC$ 交于 $D$；$OB'$ 与 $CA$ 交于 $E$；$OC'$ 与 $AB$ 交于 $F$。
           由轴对称性知 $DH = DA'$，因此折线长可直接拉直：
           $OD + DH = OD + DA' = OA' = R$（外接圆半径）！
           同理有：
           $OE + EH = OB' = R$，$OF + FH = OC' = R$。
           第一组等式条件天然获证！

## 步骤 3：外心射线交点与全等对称关系

设直线 $AO, BO, CO$ 与三边分别交于 $D', E', F'$。
           在圆周角与圆心角关系中：
           $\angle BAO = 90^\circ - \angle ACB = \angle CAA'$，由此可得顶角：
           $\angle BOD' = \angle COD$。
           又在等腰 $\triangle OBC$ 中 $OB = OC$，底角 $\angle OBD' = \angle OCD = 90^\circ - \angle A$。
           由角边角 (ASA) 判定得全等：
           $\triangle OBD' \cong \triangle OCD$！
           由此得对应边等长：$BD' = CD$。
           同理可证：$CE' = AE$，$AF' = BF$。

## 步骤 4：塞瓦定理比值代换

因为直线 $AD', BE', CF'$ 共点于外心 $O$，对 $\triangle ABC$ 应用塞瓦定理：
           $$\frac{BD'}{D'C} \cdot \frac{CE'}{E'A} \cdot \frac{AF'}{F'B} = 1$$
           利用 Step 3 证得的等长关系：
           $BD' = CD$（故分母 $D'C = a - BD' = a - CD = DB$）；
           同理 $CE' = AE, E'A = EC$ 以及 $AF' = BF, F'B = FA$。
           将等长对应代换入塞瓦式，即得：
           $$\frac{CD}{DB} \cdot \frac{AE}{EC} \cdot \frac{BF}{FA} = 1$$

## 步骤 5：塞瓦定理逆定理得证三线共点

将比值等式整理为逆时针顺序：
           $$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$
           由塞瓦定理逆定理：
           直线 $AD, BE, CF$ 必三线共点于点 $K$！
           至此，点 $D, E, F$ 不仅满足折线长恒等于外接圆半径 $R$，且连线三线共点全部获证。
