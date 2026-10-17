# 4 — 分步证明文字

## 步骤 0：已知条件与几何构型

已知两圆 ⊙O 与 ⊙Γ 相交于 A, B 两点，点 O ∈ ⊙Γ 且在弦 AB 上的垂足投影为 S。直线 OS 与 ⊙Γ 交于点 P，因此线段 OP 恰为 ⊙Γ 的一条直径。∠ASP 的平分线与 ⊙O 交于点 L（A, L 在 OP 同侧）。点 K ∈ ⊙Γ 满足 PS = PK（A, K 在 OP 同侧）。求证：SL = KL。

## 步骤 1：① 延长割线相交，得出四点共圆 Q, K, S, O

设直线 PK 与 BA 的延长线交于点 Q。因为 OP 为圆 Γ 的直径，而点 K 在圆周上，所以直径所对圆周角 ∠OKP = 90°（即 OK ⊥ PQ）。又已知 OS ⊥ AB 于 S，故 ∠QSP = ∠QSO = 90°。由 ∠QSO = ∠QKO = 90° 知四边形 QSKO 拥有公共斜边直角，故 Q, K, S, O 四点共圆于 Γ'，且 OQ 为其直径。

## 步骤 2：② 利用直角三角比，导出等腰对称 PO = PQ

在直角 △PSQ 中（∠PSQ = 90°），由三角比：$$\cos\angle QPO = \frac{PS}{PQ}$$在直角 △PKO 中（∠PKO = 90°），同理有：$$\cos\angle QPO = \frac{PK}{PO}$$已知条件给定 PS = PK，分子相等则分母必相等：PO = PQ！这表明 △PQO 是以 P 为顶点的等腰三角形，两高线 QS 与 OK 呈对称结构。

## 步骤 3：③ 设内心 L'，证明 Q, K, L', S, O 五点共圆

设直角 △QSP 的内心为 L'。由内心经典角平分性质：$$\angle QL'S = 90° + \frac{1}{2}\angle QPS = 90° + \frac{1}{2}\angle QPO$$又在等腰 △PQO 中，底角 \angle QOP = 90° - \frac{1}{2}\angle QPO，从而：$$\angle QL'S = 180° - \angle QOP = 180° - \angle QOS$$因此四边形 QL'SO 对角互补，点 L' 必在过 Q, S, O 的外接圆上。综合前述，Q, K, L', S, O 五点共圆于 Γ'，且 OQ 为其直径。

## 步骤 4：④ 导角证明相似三角形 △QL'K ∽ △QPL'

在圆 Γ' 中，由同弧所对圆周角相等得 \angle QL'K = \angle QSK。显然 \angle QSK = 90° - \angle KSP。在等腰 △PSK（PS = PK）中，底角 \angle KSP = 90° - \frac{1}{2}\angle KPS，故 \angle QSK = \frac{1}{2}\angle KPS。而 PL' 是内心角平分线，\frac{1}{2}\angle KPS = \angle KPL'。于是得到 \angle QL'K = \angle QPL'。结合公共角 \angle L'QK，可得：△QL'K ∽ △QPL'，由此导出切割线式乘积：$$\frac{QL'}{QP} = \frac{QK}{QL'} \implies \mathbf{QL'^2 = QK \cdot QP}$$

## 步骤 5：⑤ 结合根轴圆幂与勾股定理，证明 L 与 L' 重合

因为直线 AB 是圆 O 与圆 Γ 的根轴，点 Q 在其延长线上，由割线圆幂定理：$$QK \cdot QP = QA \cdot QB = QO^2 - OA^2$$由前一步知 QL'^2 = QK \cdot QP，故 QL'^2 = QO^2 - OA^2。又因 OQ 是圆 Γ' 的直径且 L' ∈ Γ'，故 ∠QL'O = 90°。在直角 △QL'O 中由勾股定理：$$QO^2 = QL'^2 + OL'^2$$代入得：QL'^2 = (QL'^2 + OL'^2) - OA^2 \implies \mathbf{OL' = OA}！这说明内心 L' 落在圆 O 上。由于点 L' 在 ∠ASP 平分线上且在 OP 同侧，点 L' 与点 L 严格重合！

## 步骤 6：⑥ 等腰顶角平分线即中垂线，证得 SL = KL

既然点 L 就是 △QSP 的内心，射线 PL 即为 ∠KPS 的角平分线。在等腰三角形 △PSK 中（PS = PK），顶角平分线 PL 亦为底边 SK 的垂直平分线（三线合一）。因为点 L 落在底边 SK 的垂直平分线上，由中垂线性质直接得出：$$\mathbf{SL = KL}$$命题完整获证！∎
