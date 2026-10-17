# 7 — 分步证明文字

## 步骤 0：✦ 已知条件与几何构形

给定 $\triangle ABC$ 的外心 $O$、内心 $I$ 与外接圆 $\odot(ABC)$。
点 $D, E, F$ 分别在边 $BC, CA, AB$ 上，满足：
条件 $BD + BF = CA = b,\quad CD + CE = AB = c$。
作 $\triangle BFD$ 与 $\triangle CDE$ 的外接圆，两圆交于点 $D$ 与第二交点 P。
求证 $OP = OI$。

## 步骤 1：① 对称点 $I'$ 投影，导出 $DD'=EE'=FF'$

作内心 $I$ 关于外心 $O$ 的中心对称点 I'（$O$ 为 $II'$ 中点）。
过 $I'$ 分别向三边 $BC, CA, AB$ 作垂线，垂足为 $D', E', F'$。
因外心 $O$ 到各边的垂足为各边中点，由投影线段关系可证：
$BD' = s - c,\quad BF' = s - a \implies BF' + BD' = CA = b$；
$CD' = s - b,\quad CE' = s - a \implies CD' + CE' = AB = c$。
与已知条件 $BD+BF=CA, CD+CE=AB$ 相较，立即得出线段等长：
$DD' = EE' = FF'$。

## 步骤 2：② 作 $I'A' \perp IA$，导出全等与共圆 $A,E,A',F$

连结角平分线 $IA$，过 $I'$ 作 $I'A' \bot IA$ 于点 A'。
因 $\angle I'A'A = \angle I'F'A = \angle I'E'A = 90^\circ$，故 $A, F', A', E'$ 四点共圆（以 $AI'$ 为直径）。
角平分线 $AA'$ 平分弧 $\overset{\frown}{F'E'}$，推得弦长 $A'F' = A'E'$。
由步骤 1 知 $FF' = EE'$，且夹角均为直角，故直角三角形全等：
全等 $\bigtriangleup A'F'F \cong \bigtriangleup A'E'E$。
对应角 $\angle A'FF' = \angle A'EE'$，即四边形对角互补，导出：
$A, E, A', F$ 四点共圆。

## 步骤 3：③ 作 $I'B' \perp IB$，同理导出共圆 $B,D,B',F$

连结角平分线 $IB$，过 $I'$ 作 $I'B' \bot IB$ 于点 B'。
同理，$\angle I'B'B = \angle I'F'B = \angle I'D'B = 90^\circ$，点 $B, F', B', D'$ 四点共圆（以 $BI'$ 为直径）。
由角平分线平分弦弧得 $B'F' = B'D'$。
结合直角边 $FF' = DD'$，再次得到直角三角形全等：
全等 $\bigtriangleup B'F'F \cong \bigtriangleup B'D'D$。
从而对应角 $\angle B'FF' = \angle B'DD'$，立即导出：
$B, D, B', F$ 四点共圆。

## 步骤 4：④ Miquel 点传递，导出 $A,F,A',P$ 与 $B,F,B',P$ 共圆

根据著名的 Miquel 定理，$\triangle BFD$、$\triangle CDE$ 的外接圆交点 P 亦必落在 $\triangle AEF$ 的外接圆 $\odot(AEF)$ 上。
且由圆周角性质，点 $P$ 满足经典等角关系：
$\angle PFA = \angle PDB = \angle PEC$。
由步骤 2 知 $A, E, A', F$ 四点共圆，故该圆正是 $\odot(AEF)$，因此：
$A, F, A', P$ 四点共圆；
同理，由步骤 3 知 $B, D, B', F$ 共圆与 $\odot(BFD)$ 重合，因此：
$B, F, B', P$ 四点共圆。

## 步骤 5：⑤ 顶角对角互补，导出 $P, B', I, A'$ 四点共圆

考查四边形 $PA'IB'$ 在顶点 $B'$ 与 $A'$ 处的角：
在圆 $\odot(BFB'P)$ 中同弧圆周角：$\angle PB'B = \angle PFB$；
在圆 $\odot(AFA'P)$ 中同弧圆周角：$\angle PA'A = \angle PFA$。
由于点 $A, F, B$ 在三角形边 $AB$ 上共线，两角互为邻补角：
$\angle PFB + \angle PFA = 180^\circ$。
因 $A'$ 在直线 $IA$ 上、$B'$ 在直线 $IB$ 上，故：
$\angle PB'I + \angle PA'I = \angle PB'B + \angle PA'A = 180^\circ$。
四边形对角互补，立即证明：$P, B', I, A'$ 四点共圆！

## 步骤 6：⑥ $II'$ 直径圆覆盖点 $P$，得出最终结论 $OP = OI$

回顾点 $A'$ 与 $B'$ 的垂线定义：
$I'A' \bot IA \implies \angle I'A'I = 90^\circ$；
$I'B' \bot IB \implies \angle I'B'I = 90^\circ$。
这表明：点 $A'$ 和 $B'$ 均在以线段 $II'$ 为直径的圆上！
由步骤 5 知点 $P, B', I, A'$ 四点共圆，该外接圆必是以 $II'$ 为直径的圆。
因此：点 P 落在以 II' 为直径的圆上！
该直径圆的圆心即为 $II'$ 的中点——外心 $O$，其半径为 $\frac{1}{2}II' = OI$。
既然 $P$ 在以 $O$ 为圆心、$OI$ 为半径的圆上，立即得出：

  $OP = OI$

全题得证！✦
