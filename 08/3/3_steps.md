# 3 — 分步证明文字

## 步骤 0：已知构形与条件

锐角 $\triangle ABC$ 中，$H$ 为垂心，圆 $\Omega$ 为九点圆（圆心 $N$），圆 $\omega$ 为 $\triangle BHC$ 的外接圆（圆心 $O'$）。
    $X$ 为圆 $\omega$ 上弧 $BHC$ 上一点。延长射线 $AX$ 与九点圆 $\Omega$ 交于点 $Y$。
    在九点圆 $\Omega$ 上取点 $P$，满足 $PX = PY$。
    求证：$\angle O'PX = 90^\circ$（即 $O'P \perp PX$）。

## 步骤 1：九点圆的中点性质与外位似中心 A

取线段 $AB, AC, AH$ 的中点分别为 $C', B', H'$。根据九点圆定理，$C', B', H'$ 均在九点圆 $\Omega$ 上。
    以点 $A$ 为位似中心，位似比为 $\frac{1}{2}$，显然有：
    $B \mapsto C',\quad C \mapsto B',\quad H \mapsto H'.$
    因此 $\triangle BCH$ 在以 $A$ 为中心、位似比 $\frac{1}{2}$ 的位似变换下映为 $\triangle C'B'H'$。
    因为 $\triangle C'B'H'$ 的外接圆即为九点圆 $\Omega$，而 $\triangle BCH$ 的外接圆为圆 $\omega$，所以：
    点 $A$ 是九点圆 $\Omega$ 与圆 $\omega$ 的外位似中心，位似比为 $\frac{1}{2}$。

## 步骤 2：延长 AP, AY 交圆 ω 于 Q, K，导出平行与比例

延长射线 $AP, AY$ 与圆 $\omega$ 分别交于点 $Q, K$。
    由于 $A$ 是圆 $\Omega$ 到圆 $\omega$ 位似比为 $\frac{1}{2}$ 的外位似中心，圆 $\Omega$ 上的任意点经以 $A$ 为中心放大 2 倍后，必落在圆 $\omega$ 上。
    因此，$Q$ 与 $K$ 即为 $P$ 与 $Y$ 在圆 $\omega$ 上的位似对应点，满足：
    $AQ = 2AP,\quad AK = 2AY.$
    在 $\triangle AQK$ 中，$P, Y$ 分别为 $AQ, AK$ 的中点，由三角形中位线定理立即得出：
    $PY \parallel QK \quad \text{且} \quad QK = 2PY.$

## 步骤 3：延长 XP 交圆 ω 于 Z，由 PX = PY 导角证明

延长射线 $XP$ 与圆 $\omega$ 交于点 $Z$。
    由已知条件 $PX = PY$，$\triangle PXY$ 为等腰三角形，底角相等：
    $\angle PXY = \angle PYX.$
    又由 Step 2 可知 $PY \parallel QK$，且 $A, Y, X, K$ 四点共线（同在割线 $AX$ 上），截线 $XK$ 截平行线得同位角相等：
    $\angle PYX = \angle QKX.$
    结合 $X, P, Z$ 三点共线，角 $\angle PXY$ 也就是角 $\angle ZXY$（即 $\angle ZXK$），由此得到：
    $\angle ZKX = \angle QXY \quad (\text{即 } \angle QXK).$

## 步骤 4：等圆周角对等弦，得出 P 为 XZ 中点

在圆 $\omega$ 中，圆周角 $\angle ZKX$ 所对的弦为 $XZ$，圆周角 $\angle QXY$（即 $\angle QXK$）所对的弦为 $QK$。
    由圆周角定理，同圆中相等的圆周角所对的弦相等：
    $\angle ZKX = \angle QXK \implies XZ = QK.$
    结合 Step 2 的中位线比例 $QK = 2PY$ 与已知条件 $PY = PX$，串联等式链：
    $XZ = QK = 2PY = 2PX.$
    因为点 $P$ 位于弦 $XZ$ 上，且全长 $XZ = 2PX$，这证明：
    点 $P$ 恰好是弦 $XZ$ 的中点（$PX = PZ$）。

## 步骤 5：由垂径定理得出 O'P ⊥ PX（证毕）

在圆 $\omega$ 中，$XZ$ 是一条弦，$O'$ 为圆心。
    由 Step 4 的结论，点 $P$ 是弦 $XZ$ 的中点。
    根据垂径定理：连接圆心与非直径弦的中点的线段，垂直于该弦！
    因此：
    $O'P \perp XZ \implies O'P \perp PX.$
    即：
    $\angle O'PX = 90^\circ.$
    命题获证！
