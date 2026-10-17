# 6 — 分步证明文字

## 步骤 0：题设条件与几何构型

在凸四边形 $ABCD$ 中，$\angle ABC = \angle CDA = 90^\circ$，对角线 $AC$ 为外接圆直径。已知 $AB > AD$。
在边 $AB$ 上截取点 $M$ 使得 $AM = AD$。
连接 $DM$ 并延长，与 $CB$ 沿 $B$ 方向的延长线交于点 $N$。
作 $DH \perp AC$ 于 $H$，$CK \perp AN$ 于 $K$。设 $HN$ 与 $AB$ 交于 $P$，$CK$ 与 $AB$ 交于 $Q$。
求证目标：$\angle MHN = \angle MCK$

## 步骤 1：① 等腰 △ADM 与直角互余 ⇒ CD = CN

由 $AD = AM$，可知 $\triangle ADM$ 为等腰三角形，故：
$\angle ADM = \angle AMD = \angle BMN$ （对顶角相等）
由 $\angle CDA = 90^\circ$，知 $\angle ADM + \angle CDN = 90^\circ$；
又在 $\text{Rt}\triangle MBN$ 中，$\angle MBN = 90^\circ$，知：
$\angle BMN + \angle CND = 90^\circ$
由等角之余角相等，立得：
$\angle CDN = \angle CND \implies CD = CN$
即 $\triangle CDN$ 也是以 $C$ 为顶点的等腰三角形。

## 步骤 2：② 射影定理与比例变换 ⇒ △CHN ∽ △CNA

在 $\text{Rt}\triangle ADC$ 中，$DH \perp AC$，由直角三角形射影定理可知：
$CD^2 = CH \cdot CA$
结合上一步证得的 $CD = CN$，代换得：
$CN^2 = CH \cdot CA \iff \frac{CH}{CN} = \frac{CN}{CA}$
注意到 $\triangle CHN$ 与 $\triangle CNA$ 拥有公共顶角：
$$\angle NCH = \angle ACN$$
两组对应边成比例且夹角相等（SAS 相似），故：
$\triangle CHN \sim \triangle CNA \implies \angle CNH = \angle CAN$

## 步骤 3：③ 直角互余角转换 ⇒ ∠KCA = ∠BPN

因为 $CK \perp AN$（$\angle AKC = 90^\circ$），在 $\text{Rt}\triangle AKC$ 中：
$\angle KCA = 90^\circ - \angle KAC = 90^\circ - \angle CAN$
另一方面，在 $\text{Rt}\triangle PBN$ 中，$AB \perp CB$（$\angle PBN = 90^\circ$）：
$\angle BPN = 90^\circ - \angle BNP = 90^\circ - \angle CNH$
代入 Step 2 中已证的 $\angle CNH = \angle CAN$，由两锐角余角相等：
$\angle KCA = \angle BPN$
这一组角相等为后续的外角分解提供了关键桥梁。

## 步骤 4：④ 射影定理与公共角 ⇒ △AHM ∽ △AMC

再次在 $\text{Rt}\triangle ADC$ 中应用射影定理，以直角边 $AD$ 为基准：
$AD^2 = AH \cdot AC$
结合已知条件 $AD = AM$，代换得：
$AM^2 = AH \cdot AC \iff \frac{AM}{AH} = \frac{AC}{AM}$
注意到 $\triangle AHM$ 与 $\triangle AMC$ 拥有公共角：
$$\angle HAM = \angle CAM$$
两边对应成比例且夹角相等（SAS 相似），因此：
$\triangle AHM \sim \triangle AMC \implies \angle AMH = \angle ACM$

## 步骤 5：⑤ 外角代换消元 ⇒ 最终得出 ∠MHN = ∠MCK

在 $\triangle PMH$ 中，$A, P, M, B$ 共线，$\angle BPN$ 为顶点 $P$ 处的外角：
$\angle BPN = \angle AMH + \angle MHP = \angle AMH + \angle MHN$
又由 Step 3 知 $\angle BPN = \angle KCA$，而射线 $CM$ 将 $\angle KCA$ 拆分为：
$\angle KCA = \angle ACM + \angle MCK$
联立上述两式得到：
$$\angle AMH + \angle MHN = \angle ACM + \angle MCK$$
代入 Step 4 中已证的 $\angle AMH = \angle ACM$，消去两边等量，严谨推得：
$\angle MHN = \angle MCK$
原命题严密得证！
