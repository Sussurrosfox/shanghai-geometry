# 2 — 分步证明文字

## 步骤 0：已知条件与几何构型

设锐角 $\bigtriangleup ABC$ 的内切圆 $I$ 与三边 $BC, CA, AB$ 分别切于点 $D, E, F$；其外接圆记为 $\omega$。
取劣弧 $AC, AB$ 的中点分别为 $M, N$。
连结 $ME, NF$ 并延长相交于点 $P$。
从 $P$ 引割线 $PB, PC$ 分别与内切圆 $I$ 交于点 $X, Y$。
求证：$XY \parallel BC$。

## 步骤 1：引出弧中点 R 作外切三角形

设外接圆 $\omega$ 上劣弧 $BC$ 的中点为 $R$。
分别过点 $M, N, R$ 作外接圆 $\omega$ 的三条切线，两两相交依次构成 $\bigtriangleup A'B'C'$：
切点为 $N \in A'B'$, $R \in B'C'$, $M \in C'A'$。
显然，外接圆 $\omega$ 恰好为大三角形 $\bigtriangleup A'B'C'$ 的内切圆。

## 步骤 2：垂径定理导出三组对应边平行

记外接圆 $\omega$ 的圆心为 $O$。
因为 $A'B'$ 切圆 $\omega$ 于点 $N$，所以半径 $ON \bot A'B'$。
又因 $N$ 为弧 $AB$ 的中点，由垂径定理知直径所在直线 $ON \bot AB$。
故 $AB \parallel A'B'$。
同理可得：$BC \parallel B'C'$，$CA \parallel C'A'$。
三角形的三对边均保持平行！

## 步骤 3：确立两三角形的外位似映射

由三边对应平行且同向，必存在正位似变换 $\mathcal{H}$，将 $\bigtriangleup ABC$ 映射为 $\bigtriangleup A'B'C'$。
在该位似变换下：
1. $\bigtriangleup ABC$ 的内切圆 $I$ 必然映射为 $\bigtriangleup A'B'C'$ 的内切圆（即外接圆 $\omega$）；
2. 边 $AB$ 上的切点 $F$ 必映射为边 $A'B'$ 上的切点 $N$（$F \mapsto N$）；
3. 同理切点 $E \mapsto M$，切点 $D \mapsto R$。

## 步骤 4：交点 P 即为位似中心，三线共点

在位似变换下，任何一对对应点的连线必过位似中心。
由于 $F \mapsto N$ 且 $E \mapsto M$，故连线 $FN$ 与 $EM$ 必交于位似中心。
而已知 $ME \cap NF = P$，因此 $P$ 恰为位似中心！
对应顶点连线必过位似中心，立得：
$P, A, A'$ 共线；$P, B, B'$ 共线；$P, C, C'$ 共线。

## 步骤 5：位似映射导出 XY // BC（原命题得证）

位似变换 $\mathcal{H}$（中心为 $P$）将圆 $I$ 变换为圆 $\omega$：
由于点 $X$ 在圆 $I$ 上，且在射线 $PB$ 上，而 $B$ 为圆 $\omega$ 上的对应点，因此 $X$ 的位似对应点即为 $B$（$X \mapsto B$）。
同理，射线 $PC$ 上的圆 $I$ 点 $Y$ 的位似对应点即为 $C$（$Y \mapsto C$）。
因此，线段 $XY$ 在该位似变换下直接映射为线段 $BC$。
由位似变换保持直线方向平行的基本性质，直接得出：
$XY \parallel BC$。
原命题完全得证！
