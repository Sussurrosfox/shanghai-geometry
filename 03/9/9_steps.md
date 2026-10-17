# 9 — 分步证明文字

## 步骤 0：已知条件与图形构型

设 $\triangle ABC$ 的外心为 $O$、内心为 $I$、重心为 $G$。
           过点 $B$ 作 $BP \bot OI$ 交 $AI$ 的延长线于点 $P$。
           过点 $P$ 作 $PM \parallel AC$ 交 $BC$ 于点 $M$。
           求证目标：证明 $I, G, M$ 三点共线。

## 步骤 1：梅涅劳斯定理：共线目标转化

连结 $AI$ 交 $BC$ 于点 $D$，$AG$ 延长线交 $BC$ 于中点 $E$。
           在 $\triangle ADE$ 中，待证三点 $I, G, M$ 分别位于三边所在的直线上：
           • $I$ 在边 $AD$ 上，内分比为 $\frac{AI}{ID}$；
           • $G$ 在边 $AE$ 上，内分比为 $\frac{EG}{GA}$；
           • $M$ 在边 $DE$ 延长线上，外分比为 $\frac{DM}{ME}$。
           由梅涅劳斯定理，要证 $I, G, M$ 共线，充要条件是：
           $\frac{AI}{ID} \cdot \frac{DM}{ME} \cdot \frac{EG}{GA} = 1$   ①

## 步骤 2：代数化简：目标归结为 FC = BC

由角平分线性质知 $\frac{AI}{ID} = \frac{AC}{CD}$ ②；
           由平行线 $PM \parallel AC$ 得 $\frac{AC}{CD} = \frac{PM}{MD}$ ③；
           由重心性质知 $\frac{EG}{GA} = \frac{1}{2}$ ④。
           将②、③、④代入①式化简，只需证明：$PM = 2ME$。
           延长 $PE$ 交 $AC$ 延长线于点 $F$。由于 $PM \parallel FC$，由相似三角形 $\triangle PME \sim \triangle FCE$ 得 $\frac{PM}{FC} = \frac{ME}{CE}$，故只需证明：
           $FC = 2CE = BC$

## 步骤 3：同一法构造：辅助点 P' 与外接圆中点 S

采用同一法证明：在射线 $CA$ 上截取点 $F$，使得 $CF = BC$。
           设 $FE$ 交角平分线 $AD$ 于点 $P'$。若能证明 $BP' \bot OI$，由垂线交点的唯一性，即得 $P' = P$！
           作外接圆 $\odot O$。连结 $CI$ 并延长交外接圆于点 $S$。
           因 $CI$ 平分 $\angle C$，$S$ 为弧 $AB$ 中点，故 $SO \bot AB$。
           由鸡爪定理（圆幂内心性质），弧中点到内心及两顶点等距：
           $SI = SA = SB$

## 步骤 4：等腰相似：导出 SO/SI = FC/FB

在等腰 $\triangle AOS$ 中，$OA = OS = R$，其顶角所对弧为弧 $AS = \frac{1}{2}\text{弧}AB$：
           $\angle SOA = \frac{1}{2}\angle BOA = \angle ACB$
           在等腰 $\triangle FCB$ 中，作法已知 $CF = CB$，顶角 $\angle FCB = \angle ACB$。
           两等腰三角形顶角相等，故两三角形相似：$\triangle AOS \sim \triangle FCB$。
           由对应边成比例：$\frac{SO}{SA} = \frac{FC}{FB}$，以 $SA = SI$ 替换底边得：
           $\frac{SO}{SI} = \frac{FC}{FB}$   ⑤

## 步骤 5：平行线 AT 与梅氏定理：导出 FC/FB = BA/AT

作 $AT \bot CI$ 交 $P'B$ 延长线于 $T$。
           因等腰 $\triangle FCB$ 顶角平分线 $CI \bot FB$，故 $AT \parallel FB$，且易得 $\angle OSI = \angle BAT$。
           延长 $BP'$ 交直线 $AC$ 于点 $X$。对 $\triangle XCB$ 及截线 $F-P'-E$ 应用梅涅劳斯定理：
           $\frac{XF}{FC} \cdot \frac{CE}{EB} \cdot \frac{BP'}{P'X} = 1$
           由 $CE = EB$ 及角平分线性质 $\frac{BP'}{P'X} = \frac{BA}{AX}$，结合平行线 $\frac{XF}{AX} = \frac{FB}{AT}$，整理得：
           $\frac{FC}{FB} = \frac{BA}{AT}$   ⑥

## 步骤 6：相似判定与垂直归宿：证明完成

综合⑤、⑥两式得：$\frac{SO}{SI} = \frac{BA}{AT}$。
           结合夹角相等 $\angle OSI = \angle BAT$，两边成比例且夹角相等：
           $\triangle OSI \sim \triangle BAT$
           由两三角形对应边位置垂直关系：$SO \bot BA, SI \bot AT$，则第三边必互相垂直：
           $OI \bot BT \implies BP' \bot OI$
           从而辅助点 $P'$ 与题目中的点 $P$ 必然重合！
           由此 $PM = 2ME$ 成立，逆推回①式，$I, G, M$ 严格三点共线，命题得证！
