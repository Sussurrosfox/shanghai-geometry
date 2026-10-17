# 例 8 分步证明规划：直角三角形中的四点共圆

**题目**：在 $\triangle ABC$ 中，$\angle A = 90^\circ$，$D, E$ 分别为 $\triangle ABC$ 的内切圆与 $AB, AC$ 的切点，边 $BC$ 的中位线所在直线与 $\triangle ABC$ 的外接圆交于点 $P, Q$。证明：$D, E, P, Q$ 四点共圆。

---

## 步骤 0：已知条件与几何构型

- **标题**：✦ 已知条件与几何构型
- **数学逻辑**：
  在 $\text{Rt}\triangle ABC$ 中，$\angle A = 90^\circ$。外心 $O$ 为斜边 $BC$ 的中点，外接圆为 $\odot O$。
  内心为 $I$，内切圆 $\odot I$ 与直角边 $AB, AC$ 分别切于点 $D, E$。
  $M, N$ 分别为 $AB, AC$ 的中点，中位线所在直线 $MN$（平行于 $BC$）与外接圆 $\odot O$ 交于点 $P, Q$。
  求证：$D, E, P, Q$ 四点共圆。
- **画面设计**：
  - **保留图元（gBase）**：
    - 直角三角形 $\triangle ABC$（深色边框）
    - 直角顶点 $A$ 处的直角标记 $\angle A = 90^\circ$
    - 外接圆 $\odot O$（以 $O$ 为圆心，$BC$ 为直径的细蓝色实线圆）
    - 外心 $O$（$BC$ 中点）
    - 内切圆 $\odot I$（翠绿色细实线圆）及内心 $I$
    - 内切圆切线半径 $ID \perp AB, IE \perp AC$
    - 切点 $D, E$
    - 中位线所在直线 $PQ$（冷灰中性线穿过外接圆）
    - 基础顶点与交点：$A, B, C, O, I, D, E, P, Q$
- **擦除图元**：无（基础画面）。
- **色彩约定**：
  - $\triangle ABC$：`#1e293b`（石板黑）
  - 外接圆 $\odot O$：`#0284c7`（天蓝）
  - 内切圆 $\odot I$ 与切点 $D, E$：`#10b981`（翡翠绿）
  - 中位线 $PQ$：`#64748b`（冷灰中性）

---

## 步骤 1：构造对称轴 $AS, OS$ 并转化目标为 $SD = SP$

- **标题**：① 构造对称轴 $AS, OS$，目标转化为 $SD = SP$
- **数学逻辑**：
  - 连接角平分线 $AI$ 并延长，交外接圆 $\odot O$ 于点 $S$。
  - 由于 $\angle BAC = 90^\circ$，$AD = AE = r$，$AI$ 平分 $\angle BAC$，四边形 $ADIE$ 为正方形，因此切点 $D, E$ 关于直线 $AS$ 对称，得 $SD = SE$。
  - 又 $\angle BAS = \angle CAS = 45^\circ$，所对圆周角相等导致弧 $\widehat{BS} = \widehat{SC}$，故 $S$ 为劣弧 $BC$ 的中点。外心 $O$ 为直径 $BC$ 中点，由垂径定理知直径径线 $OS \perp BC$。
  - 中位线 $PQ \parallel BC$，故 $OS \perp PQ$，因此直径 $OS$ 垂直平分弦 $PQ$。点 $P, Q$ 关于直线 $OS$ 对称，得 $SP = SQ$。
  - 核心转化：若能证明 $SD = SP$，则有 $SD = SE = SP = SQ$，即 $D, E, P, Q$ 四点均在以 $S$ 为圆心的同一个圆上！
- **画面设计**：
  - **新增图元**：
    - 点 $S$（弧 $BC$ 中点）及外接圆半径 $OS$
    - 射线 $AS$（橙色角平分线）
    - 虚线段 $SD, SE$（橙色对称连线）
    - 垂足直角标记 $OS \perp BC$ 与 $OS \perp PQ$
    - 虚线段 $SP, SQ$（蓝色对称连线）
- **擦除图元**：无。
- **色彩约定**：
  - 直线 $AS$ 及 $SD, SE$：`#ea580c`（橙色 Orange）
  - 径线 $OS$ 及 $SP, SQ$：`#2563eb`（蓝色 Blue）

---

## 步骤 2：聚焦 $\triangle SID$，计算 $SD^2 = 2R^2 + r^2 + 2Rr$

- **标题**：② 聚焦 $\triangle SID$，余弦定理得 $SD^2 = 2R^2 + r^2 + 2Rr$
- **数学逻辑**：
  - 连接 $SI, ID, SD$。
  - 在 Rt$\triangle ABC$ 中，$BC = 2R$ 为直径，$S$ 为劣弧 $BC$ 中点，等腰直角 $\triangle OBC$ 得弦长 $SB = \sqrt{2}R$。
  - 由鸡爪定理（三叉戟定理），内心满足 $SI = SB = SC = \sqrt{2}R$。
  - 在正方形 $ADIE$ 中，$ID = r$，$\angle AID = 45^\circ$。因为 $A, I, S$ 共线，得 $\angle DIS = 180^\circ - 45^\circ = 135^\circ$。
  - 在 $\triangle SID$ 中应用余弦定理：
    $$SD^2 = SI^2 + ID^2 - 2 SI \cdot ID \cos 135^\circ$$
    $$= (\sqrt{2}R)^2 + r^2 - 2(\sqrt{2}R)r\left(-\frac{\sqrt{2}}{2}\right) = 2R^2 + r^2 + 2Rr$$
- **画面设计**：
  - **新增图元**：
    - 高亮三角形 $\triangle SID$（浅红半透明填充）
    - 线段 $SI, ID, SD$（红色高亮边框）
    - 钝角弧 $\angle DIS = 135^\circ$
    - 标签说明 $SI = \sqrt{2}R$ 与 $ID = r$
  - **擦除图元**：擦除步骤 1 中关于 $P, Q$ 的多余连线与直角标记，视线集中在 $\triangle SID$。
- **色彩约定**：
  - 三角形 $\triangle SID$ 及各元素：`#dc2626`（红色 Red）

---

## 步骤 3：设 $OS \perp PQ$ 于 $K$，计算 $SP^2 = 2R^2 + Rh$

- **标题**：③ 设 $OS \perp PQ$ 于 $K$，勾股定理得 $SP^2 = 2R^2 + Rh$
- **数学逻辑**：
  - 设 $OS$ 与中位线 $PQ$ 相交于点 $K$（即垂足 $K$）。连接 $OP, SP$。
  - 设斜边 $BC$ 上的高为 $h$。由于 $PQ$ 是中位线，$PQ$ 到 $BC$ 的距离为 $\frac{h}{2}$，且 $PQ$ 在 $A$ 与 $BC$ 之间。$S$ 在 $BC$ 异侧，故 $SK = SO + OK = R + \frac{h}{2}$。
  - 在 Rt$\triangle OKP$ 中，半弦长 $KP^2 = OP^2 - OK^2 = R^2 - \left(\frac{h}{2}\right)^2$。
  - 在 Rt$\triangle SKP$ 中运用勾股定理：
    $$SP^2 = SK^2 + KP^2 = \left(R + \frac{h}{2}\right)^2 + \left[R^2 - \left(\frac{h}{2}\right)^2\right] = 2R^2 + Rh$$
- **画面设计**：
  - **新增图元**：
    - 点 $K$ 及直角标记 $\angle SKP = 90^\circ$
    - 线段 $SK$（加粗青色）、半径 $OP$（紫色虚线）、线段 $SP$（加粗蓝色）
    - 高亮直角三角形 Rt$\triangle SKP$ 与 Rt$\triangle OKP$（半透明淡青/淡蓝填充）
    - 标注 $OK = \frac{h}{2}, SK = R + \frac{h}{2}, OP = R$
  - **擦除图元**：擦除步骤 2 中 $\triangle SID$ 的红色彩块、连线与角弧。
- **色彩约定**：
  - 直角三角形与勾股图元：`#0891b2`（青色 Cyan）与 `#2563eb`（蓝色 Blue）

---

## 步骤 4：由周长与面积恒等式证明 $r^2 + 2Rr = Rh$

- **标题**：④ 面积与周长代数闭环，严密证明 $SD^2 = SP^2$
- **数学逻辑**：
  - 比较前两步计算结果：
    $$SD^2 = 2R^2 + (r^2 + 2Rr), \quad SP^2 = 2R^2 + Rh$$
  - 要证明 $SD = SP$，只需证明代数恒等式：
    $$r^2 + 2Rr = Rh$$
  - 证明：考虑直角三角形周长 $2p$：
    $$2p = (AD + AE) + (BD + CE) + BC = 2r + 2BC = 2r + 4R \implies p = r + 2R$$
  - 故左边恰为 $(r + 2R)r = pr = S_{\triangle ABC}$。
  - 又由底高面积公式：$S_{\triangle ABC} = \frac{1}{2} BC \cdot h = \frac{1}{2}(2R)h = Rh$。
  - 因此 $pr = Rh$ 严格成立，即 $r^2 + 2Rr = Rh$ 恒成立！
  - 从而 $SD^2 = SP^2 \implies SD = SP$。
- **画面设计**：
  - **新增图元**：
    - 点 $A$ 到 $BC$ 的高线 $AH$（虚线，垂足 $H$，直角标记）
    - 标注高 $h$
    - 高亮等长切线段 $AD, AE$（标注 $r$）
    - 高亮整个 $\triangle ABC$（淡绿色半透明填充，体现面积 $S = pr = Rh$ 的代数统一）
  - **擦除图元**：擦除步骤 3 中 $K, OP, KP$ 等局部勾股图元。
- **色彩约定**：
  - 高线与面积：`#059669`（翡翠绿 Green）

---

## 步骤 5：得出最终结论：$D, E, P, Q$ 四点共圆

- **标题**：⑤ $SD = SE = SP = SQ$，得出四点共圆结论
- **数学逻辑**：
  - 综合上述推理：
    由 $SD = SP$，结合轴对称性 $SD = SE$ 与 $SP = SQ$，
    得到 $SD = SE = SP = SQ$。
  - 这表明：以点 $S$ 为圆心、$SD$ 为半径的圆同时穿过 $D, E, P, Q$ 四点！
  - 故 $D, E, P, Q$ 四点共圆，且外接圆心正是外接圆弧的中点 $S$。命题获证。
- **画面设计**：
  - **新增图元**：
    - 以点 $S$ 为圆心、$SD$ 为半径的辅助共圆圆弧及整圆（醒目紫色）
    - 四点 $D, E, P, Q$ 放大并附带光晕外圈
    - 四条等长辐射线段 $SD, SE, SP, SQ$（高亮紫色细虚线，带等长标记）
    - 呈现四点共圆的终局对称之美
  - **擦除图元**：擦除高线 $AH$ 及一切中间过渡辅助线，突出四点共圆。
- **色彩约定**：
  - 终局共圆与半径：`#7c3aed`（紫色 Purple）与 `#e11d48`（玫瑰红 Rose）
