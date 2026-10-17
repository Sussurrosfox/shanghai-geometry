# 5 — 分步证明文字

## 步骤 0：已知条件与几何构型

已知 $AB$ 是圆 $O$ 的弦，$M$ 是弧 $\overset{\frown}{AB}$ 的中点。$C$ 是圆外任意一点，过 $C$ 作圆 $O$ 的切线 $CS, CT$（切点为 $S, T$）。
           连接 $MS, MT$ 分别交 $AB$ 于点 $E, F$；过 $E, F$ 作 $AB$ 的垂线分别交半径 $OS, OT$ 于点 $X, Y$。
           再过点 $C$ 作圆 $O$ 的割线交圆于 $P, Q$，连接 $MP$ 交 $AB$ 于 $R$。设 $Z$ 是 $\triangle PQR$ 的外心。
           求证：$X, Y, Z$ 三点共线。

## 步骤 1：① 弧中点引出的三角形相似：MR·MP = MA²

因为 $M$ 是弧 $\overset{\frown}{AB}$ 的中点，由同弧圆周角定理可知：
           $\angle MAB = \angle MPB = \angle MPA$。
           在 $\triangle MAR$ 与 $\triangle MPA$ 中，公共角 $\angle AMR = \angle PMA$，且 $\angle MAR = \angle MPA$，故：
           $\triangle MAR \sim \triangle MPA$。
           由对应边成比例得：$\dfrac{MA}{MP} = \dfrac{MR}{MA} \implies MR \cdot MP = MA^2$。
           又因为 $M$ 是弧中点，$MA = MB$，故 $MR \cdot MP = MA^2 = MB^2$。

## 步骤 2：② 切点弦角三角形相似：ME·MS = MA²

连接辅助线 $AS$。由同弧所对圆周角与弧中点性质：
           $\angle MSA$ 对应弧 $\overset{\frown}{MA}$，而 $\angle MAE = \angle MAB$ 对应弧 $\overset{\frown}{MB} = \overset{\frown}{MA}$，因此 $\angle MAE = \angle MSA$。
           结合公共角 $\angle AME = \angle SMA$，可知：
           $\triangle MAE \sim \triangle MSA$。
           同理得出对应边成比例：$\dfrac{MA}{MS} = \dfrac{ME}{MA} \implies ME \cdot MS = MA^2$。
           联立步骤 1，得到极其关键的恒等式：
           $MR \cdot MP = ME \cdot MS = MA^2$。

## 步骤 3：③ 构造圆 X：XS = XE 且点 M 在两圆根轴上

考察以 $X$ 为圆心、$XE$ 为半径的圆 $X$。因为 $EX \perp AB$ 且 $OM \perp AB$，所以 $EX \parallel OM$，内错角 $\angle XEM = \angle OME$。
           又因半径 $OS = OM = r_O$，等腰 $\triangle OMS$ 给出 $\angle OSM = \angle OMS$。
           由此推得 $\angle XSE = \angle OSM = \angle XEM = \angle XES$，故 $\triangle XSE$ 为等腰三角形，即 $XS = XE$！
           这说明：以 $X$ 为圆心、$XE$ 为半径的辅助圆 $X$ 恰好经过切点 $S$。
           因割线 $MES$ 交圆 $X$ 于 $E, S$，$ME \cdot MS$ 为点 $M$ 关于圆 $X$ 的幂；而割线 $MRP$ 交圆 $Z$ 于 $R, P$，$MR \cdot MP$ 为点 $M$ 关于圆 $Z$ 的幂。
           由 $MR \cdot MP = ME \cdot MS$ 可知：点 $M$ 必然位于圆 $Z$ 与圆 $X$ 的根轴上！

## 步骤 4：④ 切割线定理与公共根轴：CM ⊥ ZX

因为 $CS$ 是圆 $O$ 的切线，且圆心 $X$ 位于半径 $OS$ 上，故 $CS \perp OS \implies CS \perp XS$。因此 $CS$ 亦为圆 $X$ 在切点 $S$ 处的切线！
           因此点 $C$ 关于圆 $X$ 的幂等于切线长平方 $CS^2$。
           另一方面，割线 $CPQ$ 交圆 $O$ 于 $P, Q$，由于 $P, Q$ 亦在 $\triangle PQR$ 的外接圆 $Z$ 上，故点 $C$ 关于圆 $Z$ 的幂等于 $CP \cdot CQ$。
           由圆 $O$ 的切割线定理知：$CP \cdot CQ = CS^2$。
           这证明点 $C$ 关于圆 $Z$ 与圆 $X$ 的幂亦相等，故 点 $C$ 亦在圆 $Z$ 与圆 $X$ 的根轴上！
           两点确定一条直线，直线 $CM$ 必然是圆 $Z$ 与圆 $X$ 的公共根轴。
           由「两圆根轴垂直于连心线」定理，立得：$CM \perp ZX$！

## 步骤 5：⑤ 对称性 CM ⊥ ZY ⇒ X, Y, Z 三点共线

同理，考察以 $Y$ 为圆心、$YF$ 为半径的圆 $Y$。由完全对称的论证：
           $YF = YT$，圆 $Y$ 亦经过切点 $T$；$MF \cdot MT = MA^2 = MR \cdot MP$，且 $CT^2 = CP \cdot CQ$。
           因此直线 $CM$ 亦为圆 $Z$ 与圆 $Y$ 的公共根轴！由此立即得出：$CM \perp ZY$。
           因为经过平面上同一点 $Z$ 且垂直于已知直线 $CM$ 的垂线是唯一的，所以直线 $ZX$ 与直线 $ZY$ 必然完全重合！
           这严格证明了：$X, Y, Z$ 三点共线（且直线 $XYZ \perp CM$）。全题证毕！
