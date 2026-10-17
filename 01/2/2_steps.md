# 2 — 分步证明文字

## 步骤 0：已知条件与图形构形

已知 $O$ 为 $\\triangle ABC$ 内一点，满足 $OD \\perp BC$ 于点 $D$，$OE \\perp AC$ 于点 $E$。

           $F$ 为边 $AB$ 的中点，且满足 $DF = EF$（画面红线标出）。

           求证：$\\angle OBD = \\angle OAE$。

## 步骤 1：① 取中点构造中位线与斜边中线

看到中点构造中位线，看到直角三角形斜边构造斜边中线。

           分别取 $AO, BO$ 的中点 $M$ 与 $N$。

           连接 $AO, BO$，并连接 $ME, MF, ND, NF$。

           此时 $F, M, N$ 构成中位线体系，而 $M, N$ 又是直角三角形斜边中点！

## 步骤 2：② $FM$ 与 $ND$ 均等于 $\\frac{1}{2}BO$

在 $\\triangle ABO$ 中，$F, M$ 分别为 $AB, AO$ 的中点，故 $FM$ 为中位线，有：

           $FM = \\frac{1}{2}BO$。

           在 $\\text{Rt}\\triangle ODB$ 中，$OD \\perp BC$，$N$ 为斜边 $BO$ 的中点，由直角三角形斜边中线定理得：

           $ND = \\frac{1}{2}BO$。

           因此得出第一组关键等长：$FM = ND$。

## 步骤 3：③ $FN$ 与 $ME$ 均等于 $\\frac{1}{2}AO$

同理，在 $\\triangle ABO$ 中，$F, N$ 分别为 $AB, BO$ 的中点，故 $FN$ 为中位线，有：

           $FN = \\frac{1}{2}AO$。

           在 $\\text{Rt}\\triangle OEA$ 中，$OE \\perp AC$，$M$ 为斜边 $AO$ 的中点，由直角三角形斜边中线定理得：

           $ME = \\frac{1}{2}AO$。

           因此得出第二组关键等长：$ME = FN$。

## 步骤 4：④ 构造 SSS 全等：$\\triangle FND \\cong \\triangle EMF$

在 $\\triangle FND$ 和 $\\triangle EMF$ 中对照三边：

           $\\begin{cases} FN = ME & (\\text{由步骤 ③}) \\\\ ND = FM & (\\text{由步骤 ②}) \\\\ DF = EF & (\\text{已知条件}) \\end{cases}$

           由 SSS 全等判定定理，得 $\\triangle FND \\cong \\triangle EMF$！

           对应角相等：$\\angle FND = \\angle FME$。

## 步骤 5：⑤ 平行四边形 $FNOM$ 转换顶角

因 $FM \\parallel BO$ 且 $FM = ON = \\frac{1}{2}BO$，故四边形 $FNOM$ 为平行四边形。

           平行四边形对角相等：$\\angle FNO = \\angle FMO$。

           两式作差：

           $\\angle OND = \\angle FND - \\angle FNO$

           $\\angle OME = \\angle FME - \\angle FMO$

           从而得出核心角相等关系：$\\angle OND = \\angle OME$。

## 步骤 6：⑥ 结论：等腰外角推得 $\\angle OBD = \\angle OAE$

在 $\\text{Rt}\\triangle ODB$ 中，$NB = ND = NO$，$\\triangle NOB$ 是等腰三角形，外角 $\\angle OND = 2\\angle OBD$，即 $\\angle OBD = \\frac{1}{2}\\angle OND$。

           同理在 $\\text{Rt}\\triangle OEA$ 中，$MA = ME = MO$，等腰 $\\triangle MOA$ 外角 $\\angle OME = 2\\angle OAE$，即 $\\angle OAE = \\frac{1}{2}\\angle OME$。

           因 $\\angle OND = \\angle OME$，立得：

           $\\angle OBD = \\angle OAE$。

           命题获证！

