# 例 5：直角四边形射影相似与角代换分步证明规划 (steps.md)

## 题目信息
- **题源**：`02/6.md`（例 5）
- **题面**：在凸四边形 $ABCD$ 中，$AB > AD$，$\angle ABC = \angle CDA = 90^\circ$。在 $AB$ 上取点 $M$ 使得 $AM = AD$，$DM$ 与 $CB$ 的延长线交于点 $N$。点 $D$ 在 $AC$ 上的投影为 $H$，$C$ 在 $AN$ 上的投影为点 $K$。证明：$\angle MHN = \angle MCK$。

---

## 分步规划与设计

### Step 0: 题设条件与几何构型
- **标题**：✦ 题设条件与几何构型
- **正文**：
  在凸四边形 $ABCD$ 中，$\angle ABC = \angle CDA = 90^\circ$，四边形共圆且以 $AC$ 为外接圆直径。已知 $AB > AD$。<br>
  在边 $AB$ 上截取点 $M$ 使得 $AM = AD$。连接 $DM$ 并延长，与 $CB$ 沿 $B$ 方向的延长线交于点 $N$。<br>
  作 $DH \perp AC$ 于 $H$，$CK \perp AN$ 于 $K$。设 $HN$ 与 $AB$ 交于点 $P$，$CK$ 与 $AB$ 交于点 $Q$。<br>
  <b>求证目标</b>：$\angle MHN = \angle MCK$。
- **画面**：
  - 基础图形：凸四边形 $ABCD$，对角线 $AC$。
  - 垂线段与延长线：$DM$ 延长至 $N$，$CB$ 延长至 $N$；垂线段 $DH$、$CK$；连线 $HN$、$CK$。
  - 直角标记：$\angle ABC = 90^\circ$, $\angle CDA = 90^\circ$, $\angle DHC = 90^\circ$, $\angle AKC = 90^\circ$。
  - 关键点：$A, B, C, D, M, N, H, K, P, Q$。

---

### Step 1: 等腰 △ADM 与角互余导出 CD = CN
- **标题**：① 等腰 △ADM 与直角互余 ⇒ CD = CN
- **正文**：
  因为 $AD = AM$，所以 $\triangle ADM$ 为等腰三角形，故：
  <div class="formula-box">$\angle ADM = \angle AMD = \angle BMN$ （对顶角相等）</div>
  因为 $\angle CDA = 90^\circ$，所以 $\angle ADM + \angle CDN = 90^\circ$；<br>
  又因为 $CB \perp AB$（即 $\angle CBN = 90^\circ$），在 $\text{Rt}\triangle BMN$ 中：
  <div class="formula-box">$\angle BMN + \angle CND = 90^\circ$</div>
  由等角之余角相等，立即得到：
  <div class="formula-box">$\angle CDN = \angle CND \implies CD = CN$</div>
  即 $\triangle CDN$ 也是以 $C$ 为顶点的等腰三角形。
- **画面**：
  - 高亮等腰 $\triangle ADM$（淡蓝色填充，虚线边框）。
  - 等长刻度标记：$AD = AM$（双刻度线），$CD = CN$（单刻度线）。
  - 高亮角弧：$\angle ADM, \angle AMD, \angle BMN$（绿色），$\angle CDN, \angle CND$（红色）。
  - 直角标记：$\angle CDA$ 与 $\angle MBN$。

---

### Step 2: 射影定理与等长代换导出 △CHN ∽ △CNA
- **标题**：② 射影定理与比例变换 ⇒ △CHN ∽ △CNA
- **正文**：
  在 $\text{Rt}\triangle ADC$ 中，由于 $DH \perp AC$，由射影定理可知：
  <div class="formula-box">$CD^2 = CH \cdot CA$</div>
  将 Step 1 证得的 $CD = CN$ 代入上式，得：
  <div class="formula-box">$CN^2 = CH \cdot CA \iff \frac{CH}{CN} = \frac{CN}{CA}$</div>
  注意到 $\triangle CHN$ 与 $\triangle CNA$ 拥有公共顶角：
  $$\angle NCH = \angle ACN$$
  两组对应边成比例且夹角相等（SAS 相似判据），因此：
  <div class="formula-box">$\triangle CHN \sim \triangle CNA \implies \angle CNH = \angle CAN$</div>
- **画面**：
  - 高亮 $\text{Rt}\triangle ADC$ 与高线 $DH$（射影定理基底）。
  - 高亮相似三角形：$\triangle CHN$（橙色半透明填充）与 $\triangle CNA$（蓝色半透明填充）。
  - 高亮公共顶角 $\angle ACN$ 以及对应相等的角 $\angle CNH$ 与 $\angle CAN$（醒目紫色角弧）。

---

### Step 3: 垂线互余转化导出 ∠KCA = ∠BPN
- **标题**：③ 直角互余角转换 ⇒ ∠KCA = ∠BPN
- **正文**：
  因为 $CK \perp AN$（即 $\angle AKC = 90^\circ$），在 $\text{Rt}\triangle AKC$ 中：
  <div class="formula-box">$\angle KCA = 90^\circ - \angle KAC = 90^\circ - \angle CAN$</div>
  另一方面，在 $\text{Rt}\triangle PBN$ 中，$AB \perp CB$（即 $\angle PBN = 90^\circ$）：
  <div class="formula-box">$\angle BPN = 90^\circ - \angle BNP = 90^\circ - \angle CNH$</div>
  结合 Step 2 已证的 $\angle CNH = \angle CAN$，两者余角必然相等：
  <div class="formula-box">$\angle KCA = \angle BPN$</div>
  这一对角为后续外角分解建立了关键桥梁。
- **画面**：
  - 高亮直角 $\angle AKC$ 与 $\angle PBN$。
  - 高亮角 $\angle CAN$ 与 $\angle CNH$ 的等角关联。
  - 高亮目标对偶角：$\angle KCA$（青色角弧）与 $\angle BPN$（青色角弧），显示二者均等于 $90^\circ - \angle CAN$。

---

### Step 4: 射影定理导出 △AHM ∽ △AMC
- **标题**：④ 射影定理与公共角 ⇒ △AHM ∽ △AMC
- **正文**：
  再次在 $\text{Rt}\triangle ADC$ 中应用射影定理，以直角边 $AD$ 为基准：
  <div class="formula-box">$AD^2 = AH \cdot AC$</div>
  结合题设已知条件 $AD = AM$，代换得：
  <div class="formula-box">$AM^2 = AH \cdot AC \iff \frac{AM}{AH} = \frac{AC}{AM}$</div>
  注意到 $\triangle AHM$ 与 $\triangle AMC$ 拥有公共角：
  $$\angle HAM = \angle CAM$$
  两组对应边成比例且夹角相等（SAS 相似判据），因此：
  <div class="formula-box">$\triangle AHM \sim \triangle AMC \implies \angle AMH = \angle ACM$</div>
- **画面**：
  - 高亮直角边 $AD$、射影 $AH$ 及斜边 $AC$。
  - 高亮相似三角形：$\triangle AHM$（绿色半透明）与 $\triangle AMC$（黄色半透明）。
  - 高亮对应角 $\angle AMH$ 与 $\angle ACM$（鲜明绿色角弧）。

---

### Step 5: 外角代换消元，严密得出 ∠MHN = ∠MCK
- **标题**：⑤ 外角代换消元 ⇒ 最终得出 ∠MHN = ∠MCK
- **正文**：
  在 $\triangle PMH$ 中，由于 $A, P, M, B$ 共线，$\angle BPN$ 为其顶点 $P$ 处的外角：
  <div class="formula-box">$\angle BPN = \angle AMH + \angle MHP = \angle AMH + \angle MHN$</div>
  结合 Step 3 结论 $\angle BPN = \angle KCA$，将 $\angle KCA$ 按射线 $CM$ 进行角拆分：
  <div class="formula-box">$\angle KCA = \angle ACM + \angle MCK$</div>
  将两式联立代换，得到：
  $$\angle AMH + \angle MHN = \angle ACM + \angle MCK$$
  代入 Step 4 已证结论 $\angle AMH = \angle ACM$，两边消去相同项，最终严格推得：
  <div class="formula-box" style="font-weight:700; color:#dc2626; font-size:15px;">$\angle MHN = \angle MCK$</div>
  全题严密得证！
- **画面**：
  - 高亮目标角 $\angle MHN$（红色角弧加粗，填充半透明扇区）与 $\angle MCK$（红色角弧加粗，填充半透明扇区）。
  - 高亮外角三角形 $\triangle PMH$。
  - 醒目标出等式各部分的对应关系，所有证明要素完美闭环。
