# 9 — 分步证明文字

## 步骤 0：已知条件与几何构型

在 $\text{Rt}\triangle ABC$ 中，$\angle A = 90^\circ$。
           • $O$ 为斜边 $BC$ 的中点，外接圆为 $\odot O$（直径 $BC = 2R$）；
           • $I$ 为内心，内切圆 $\odot I$ 与直角边 $AB, AC$ 分别切于点 $D, E$；
           • 中位线所在直线 $PQ \parallel BC$，与外接圆 $\odot O$ 交于点 $P, Q$。
           求证：$D, E, P, Q$ 四点共圆。

## 步骤 1：构造对称轴，转化目标为 SD = SP

延长角平分线 $AI$ 交外接圆于点 $S$：
           1. $\angle BAC = 90^\circ$ 且 $AD=AE=r$，故切点 $D, E$ 关于直线 $AS$ 对称 $\implies \mathbf{SD = SE}$；
           2. $\angle BAS = 45^\circ$ 所对弧相等，故 $S$ 为劣弧 $BC$ 中点，径线 $OS \perp BC$；
           3. 中位线 $PQ \parallel BC \implies OS \perp PQ$，垂径定理得 $OS$ 垂直平分弦 $PQ$，故 $P, Q$ 关于 $OS$ 对称 $\implies \mathbf{SP = SQ}$；
           核心转化：若证明 SD = SP，则 $SD = SE = SP = SQ$，即四点全在以 $S$ 为圆心的圆上！

## 步骤 2：聚焦 △SID，余弦定理算 SD²

在 $\triangle SID$ 中计算线段 $SD$ 的长度：
           1. 在等腰直角 $\triangle OBC$ 中，$SB = \sqrt{2}R$。由鸡爪定理（内心-外心三叉戟定理），内心满足：
           $$SI = SB = \sqrt{2}R$$
           2. 四边形 $ADIE$ 为正方形，$ID = r$，$\angle AID = 45^\circ$。因 $A, I, S$ 共线：
           $$\angle DIS = 180^\circ - 45^\circ = 135^\circ$$
           3. 在 $\triangle SID$ 中由余弦定理：
           
             $$SD^2 = SI^2 + ID^2 - 2 SI \cdot ID \cos 135^\circ$$
             $$= (\sqrt{2}R)^2 + r^2 - 2(\sqrt{2}R)r\left(-\frac{\sqrt{2}}{2}\right) = \mathbf{2R^2 + r^2 + 2Rr}$$

## 步骤 3：设 OS ⊥ PQ 于 K，勾股定理算 SP²

设 $OS$ 与中位线 $PQ$ 相交于垂足 $K$：
           1. 设点 $A$ 到斜边 $BC$ 的高为 $h$。由于 $PQ$ 是中位线，$PQ$ 到 $BC$ 的距离为 $\frac{h}{2}$，且 $S$ 在 $BC$ 异侧：
           $$SK = SO + OK = R + \frac{h}{2}$$
           2. 在 $\text{Rt}\triangle OKP$ 中，半弦长平方为：
           $$KP^2 = OP^2 - OK^2 = R^2 - \left(\frac{h}{2}\right)^2$$
           3. 在 $\text{Rt}\triangle SKP$ 中应用勾股定理：
           
             $$SP^2 = SK^2 + KP^2 = \left(R + \frac{h}{2}\right)^2 + \left[R^2 - \left(\frac{h}{2}\right)^2\right] = \mathbf{2R^2 + Rh}$$

## 步骤 4：代数闭环：证明 r² + 2Rr = Rh

对比两式结果：$SD^2 = 2R^2 + (r^2 + 2Rr)$，$SP^2 = 2R^2 + Rh$。
           欲证 $SD = SP$，只需证明代数恒等式：$\mathbf{r^2 + 2Rr = Rh}$。
           严密证明：
           直角三角形周长为：
           $$2p = (AD+AE) + (BD+CE) + BC = 2r + 2BC = 2r + 4R$$
           得半周长 $p = r + 2R$。因此：
           
             $$r^2 + 2Rr = (r + 2R)r = pr = S_{\triangle ABC}$$
             又 $S_{\triangle ABC} = \frac{1}{2} BC \cdot h = \frac{1}{2}(2R)h = Rh$
           
           从而 $pr = Rh$ 严格成立！代数恒等式获证，故 $\mathbf{SD^2 = SP^2 \implies SD = SP}$。

## 步骤 5：得出结论：D, E, P, Q 四点共圆

终局总结：
           由前面各步推导：
           
             $$SD = SP \quad \text{且} \quad SD = SE, \; SP = SQ$$
             $$\implies \mathbf{SD = SE = SP = SQ}$$
           
           这表明：点 $D, E, P, Q$ 到点 $S$ 的距离全部相等！
           因此，以点 $S$ 为圆心、$SD$ 为半径的圆恰好同时经过 $D, E, P, Q$ 四点。
           原命题得证：$D, E, P, Q$ 四点共圆！
