# 5 — 分步证明文字

## 步骤 0：题设条件与双层几何构形

在 $\triangle ABC$ 中，三边上分别有点 $D \in BC, E \in CA, F \in AB$，构成内层三角形 $\triangle DEF$。
           在内层 $\triangle DEF$ 的三边上分别有点 $P \in EF, Q \in FD, R \in DE$。
           
             已知条件：$DP, EQ, FR$ 三线共点于点 $Y$。
             求证目标：$AP, BQ, CR$ 三线共点 $\Longleftrightarrow$ $AD, BE, CF$ 三线共点。
           
           本题的核心在于利用正弦定理/面积比，建立内层分点与外层顶角正弦之间的桥梁。

## 步骤 1：① 顶角剖分与面积/正弦比分解

连接 $AP$。在 $\triangle AEF$ 中，线段 $AP$ 将其分割为 $\triangle AEP$ 与 $\triangle AFP$。
           两三角形共顶点 $A$ 且底边在同一直线 $EF$ 上，其面积比等于底边线段比：
           
             $$\frac{EP}{PF} = \frac{S_{\triangle AEP}}{S_{\triangle AFP}} = \frac{\frac{1}{2} AE \cdot AP \cdot \sin\angle PAE}{\frac{1}{2} AF \cdot AP \cdot \sin\angle PAF}$$
           
           由于 $E \in AC, F \in AB$，有 $\angle PAE = \angle PAC$ 且 $\angle PAF = \angle BAP$。
           约去公因式 $\frac{1}{2} AP$，即得核心分解式：
           $$\frac{EP}{PF} = \frac{EA}{AF} \cdot \frac{\sin\angle PAC}{\sin\angle BAP}$$

## 步骤 2：② 轮换对偶与三式联乘

同理，对顶点 $B$ 及 $\triangle BFD$ 中的截线 $BQ$、顶点 $C$ 及 $\triangle CDE$ 中的截线 $CR$ 应用完全相同的面积分解：
           
             $$\frac{FQ}{QD} = \frac{FB}{BD} \cdot \frac{\sin\angle QBA}{\sin\angle CBQ}, \quad \frac{DR}{RE} = \frac{DC}{CE} \cdot \frac{\sin\angle RCB}{\sin\angle ACR}$$
           
           将上述三个分比等式相乘，并移项整理各因子：
           
             $$\left(\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE}\right) \cdot \left(\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}\right) \cdot \left(\frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB}\right) = 1$$

## 步骤 3：③ 内层塞瓦定理：内层比消去

注意到题设已知强条件：在 $\triangle DEF$ 中，$DP, EQ, FR$ 三线共点于点 $Y$。
           根据塞瓦定理（Ceva's Theorem）边长比形式：
           
             $$\frac{EP}{PF} \cdot \frac{FQ}{QD} \cdot \frac{DR}{RE} = 1$$
           
           代入步骤 ② 的联乘式，第一项内层比值积恰好为 1，直接消去，得到惊艳的边元与角元守恒等式：
           
             $$\left(\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB}\right) \cdot \left(\frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB}\right) = 1$$

## 步骤 4：④ 边元塞瓦与角元塞瓦对偶解析

仔细观察守恒等式中的两个关键乘积因子：
           1. 边元乘积：由经典塞瓦定理，在 $\triangle ABC$ 中：
           
             $AD, BE, CF$ 三线共点于 $X$ $\Longleftrightarrow \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$
           
           2. 角元乘积：由角元塞瓦定理（Trigonometric Ceva），在 $\triangle ABC$ 中：
           
             $AP, BQ, CR$ 三线共点于 $Z$ $\Longleftrightarrow \frac{\sin\angle BAP}{\sin\angle PAC} \cdot \frac{\sin\angle CBQ}{\sin\angle QBA} \cdot \frac{\sin\angle ACR}{\sin\angle RCB} = 1$

## 步骤 5：⑤ 充要等价与结论达成

由于两项乘积之积恒等于 1（互为倒数）：
           
             $$M_{\text{边}} \cdot M_{\text{角}} = 1$$
           
           因此，乘积中一个等于 1 当且仅当另一个等于 1！
           
             $$AP, BQ, CR\text{ 三线共点 } \Longleftrightarrow AD, BE, CF\text{ 三线共点}$$
           
           原命题得证！图形中展示了三组三线共点的完美对应。
