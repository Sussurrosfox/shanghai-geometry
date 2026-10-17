# 08/8 步骤提取

## 步骤 0：已知构型与核心待求线段

设凸四边形 $ABCD$ 外切于圆 $O$，$OA=5, OB=6, OC=7, OD=8$。对角线 $AC, BD$ 的中点分别为 $M, N$。求 $\frac{OM}{ON}$ 的值。

## 步骤 1：① 建立以 $O$ 为中心、半径 $r$ 的反演变换

以 $O$ 为反演中心、圆 $O$ 为基圆（反演幂 $r^2$）作反演变换。各顶点反演像 $A', B', C', D'$ 落在射线 $OA, OB, OC, OD$ 上，满足 $OA \cdot OA' = OB \cdot OB' = OC \cdot OC' = OD \cdot OD' = r^2$。

## 步骤 2：② 证明 $A'B'C'D'$ 为切点中位线平行四边形

由切线直角射影性质，$A', B', C', D'$ 分别为切点弦的中点。由三角形中位线定理，$A'B' \parallel C'D'$ 且 $A'B' = C'D' = \frac{1}{2}HF$。因此 $A'B'C'D'$ 严格为一个平行四边形！其对角线互相平分于公共中点 $S$。

## 步骤 3：③ 相似三角形中线比：表达 $OM$

由反演性质知 $\bigtriangleup A'OC' \sim \bigtriangleup COA$（反向相似）。线段 $OS$ 与 $OM$ 分别是两相似三角形对应的中线，故对应中线比等于对应边长比：$\frac{OS}{OM} = \frac{OA'}{OC} = \frac{r^2}{OA \cdot OC}$，解得 $OM = \frac{OS \cdot OA \cdot OC}{r^2}$。

## 步骤 4：④ 相似三角形中线比：表达 $ON$

同理，在另一对对角线构成的三角形中，$\bigtriangleup B'OD' \sim \bigtriangleup DOB$。$OS$ 与 $ON$ 为对应中线，满足：$\frac{OS}{ON} = \frac{OB'}{OD} = \frac{r^2}{OB \cdot OD}$，解得 $ON = \frac{OS \cdot OB \cdot OD}{r^2}$。

## 步骤 5：⑤ 比值消元，得出最终精确值 $\frac{35}{48}$

将两式相除，公共未知量 $OS$ 与反演基圆幂 $r^2$ 完全对消：
$$\frac{OM}{ON} = \frac{\frac{OS \cdot OA \cdot OC}{r^2}}{\frac{OS \cdot OB \cdot OD}{r^2}} = \frac{OA \cdot OC}{OB \cdot OD} = \frac{5 \times 7}{6 \times 8} = \frac{35}{48}$$
最终得解：$\frac{OM}{ON} = \frac{35}{48}$！

